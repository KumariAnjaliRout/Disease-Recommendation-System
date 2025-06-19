import streamlit as st
import pandas as pd
import pickle

# Load model and data
model = pickle.load(open("model.pkl", "rb"))
symptom_list = pickle.load(open("symptom_list.pkl", "rb"))
desc_df = pd.read_csv("symptom_Description.csv")
prec_df = pd.read_csv("symptom_precaution.csv")

# Helper to fetch description and precautions
def get_disease_info(disease):
    disease = disease.lower().strip()
    description = desc_df[desc_df["Disease"].str.lower() == disease]["Description"].values
    precautions = prec_df[prec_df["Disease"].str.lower() == disease].values

    description = description[0] if len(description) > 0 else "No description available."
    if len(precautions) > 0:
        precautions_list = list(precautions[0][1:])
        precautions_list = [p for p in precautions_list if str(p).strip() != '']
    else:
        precautions_list = ["No precautions available."]
    
    return description, precautions_list

# Streamlit UI
st.set_page_config(page_title="Disease Recommendation System", layout="centered")
st.title("Disease Recommendation System")
st.write("Enter your symptoms below to get possible disease predictions.")

# Symptom selection
selected_symptoms = st.multiselect("Select your symptoms:", symptom_list)

if st.button(" Predict Disease"):
    if selected_symptoms:
        input_vector = [1 if symptom in selected_symptoms else 0 for symptom in symptom_list]
        prediction = model.predict([input_vector])[0]
        description, precautions = get_disease_info(prediction)

        st.success(f"**Predicted Disease:** {prediction}")
        st.markdown(f" **Description:** {description}")

        st.markdown(" **Precautions:**")
        for i, p in enumerate(precautions, 1):
            st.markdown(f"{i}. {p}")
    else:
        st.warning(" Please select at least one symptom.")

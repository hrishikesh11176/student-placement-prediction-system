import streamlit as st
import pandas as pd
import pickle

# Load dataset and model
df = pd.read_csv("final_data.csv")
model = pickle.load(open("model.pkl", "rb"))

st.title("Student Placement Prediction System")

# User Inputs
cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0, value=7.5)
internships = st.number_input("Number of Internships", min_value=0, value=1)
projects = st.number_input("Number of Projects", min_value=0, value=2)
workshops = st.number_input("Workshops/Certifications", min_value=0, value=2)
aptitude = st.number_input("Aptitude Test Score", min_value=0, max_value=100, value=70)
softskills = st.number_input("Soft Skills Rating", min_value=0.0, max_value=5.0, value=4.0)

extra = st.selectbox(
    "Extracurricular Activities",
    sorted(df['ExtracurricularActivities'].unique())
)

training = st.selectbox(
    "Placement Training",
    sorted(df['PlacementTraining'].unique())
)

ssc = st.number_input("SSC Marks", min_value=0, max_value=100, value=80)
hsc = st.number_input("HSC Marks", min_value=0, max_value=100, value=75)

if st.button("Predict Placement"):

    input_df = pd.DataFrame({
        'CGPA':[cgpa],
        'Internships':[internships],
        'Projects':[projects],
        'Workshops/Certifications':[workshops],
        'AptitudeTestScore':[aptitude],
        'SoftSkillsRating':[softskills],
        'ExtracurricularActivities':[extra],
        'PlacementTraining':[training],
        'SSC_Marks':[ssc],
        'HSC_Marks':[hsc]
    })

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success(" Prediction : 🎉Congratulations! You Are Placed")
    else:
        st.error(" Prediction : 😔Sorry! Not Placed, Better Luck Next time")

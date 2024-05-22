import streamlit as st
import pickle
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(
    page_title="Heart Failure Prediction",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="auto",
)
st.write("Created by Brave")

# Define function to take user inputs
def user_input():
    st.header("Patient Data Input")
    st.write("Please enter the following patient information:")

    # Split into columns for a better layout
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider('Age', 40, 100, 65, help="Age of the patient")
        anaemia = st.selectbox('Anaemia', ('No', 'Yes'), help="Does the patient have anaemia?")
        creatinine_phosphokinase = st.number_input('Creatinine Phosphokinase', min_value=20, max_value=10000, value=200, help="Level of the enzyme creatinine phosphokinase in the blood")
        diabetes = st.selectbox('Diabetes', ('No', 'Yes'), help="Does the patient have diabetes?")
        ejection_fraction = st.slider('Ejection Fraction (%)', 10, 80, 40, help="Percentage of blood leaving the heart at each contraction")

    with col2:
        high_blood_pressure = st.selectbox('High Blood Pressure', ('No', 'Yes'), help="Does the patient have high blood pressure?")
        platelets = st.number_input('Platelets', min_value=0, max_value=1000000, value=250000, help="Platelet count in the blood")
        serum_creatinine = st.number_input('Serum Creatinine (mg/dL)', min_value=0.0, max_value=10.0, value=1.0, help="Level of creatinine in the blood")
        serum_sodium = st.slider('Serum Sodium (mEq/L)', 100, 150, 135, help="Level of sodium in the blood")
        sex = st.selectbox('Sex', ('Female', 'Male'), help="Gender of the patient")
        smoking = st.selectbox('Smoking', ('No', 'Yes'), help="Does the patient smoke?")
        time = st.slider('Follow-up Period (days)', 0, 300, 150, help="Follow-up period in days")

    # Encode categorical variables
    anaemia = 1 if anaemia == 'Yes' else 0
    diabetes = 1 if diabetes == 'Yes' else 0
    high_blood_pressure = 1 if high_blood_pressure == 'Yes' else 0
    sex = 1 if sex == 'Male' else 0
    smoking = 1 if smoking == 'Yes' else 0

    # Create a dictionary with the user inputs
    user_data = {
        'age': age,
        'anaemia': anaemia,
        'creatinine_phosphokinase': creatinine_phosphokinase,
        'diabetes': diabetes,
        'ejection_fraction': ejection_fraction,
        'high_blood_pressure': high_blood_pressure,
        'platelets': platelets,
        'serum_creatinine': serum_creatinine,
        'serum_sodium': serum_sodium,
        'sex': sex,
        'smoking': smoking,
        'time': time
    }
    
    return user_data

# Main function to run the app
def main():
    st.title("Heart Failure Prediction")
    st.write("""
        This application predicts the likelihood of heart failure based on various health metrics.
        Please provide the patient's information below and click on 'Predict' to see the results.
    """)

    # Get user input
    user_data = user_input()

    # Convert user data to dataframe
    input_df = pd.DataFrame([user_data])

    # Load the model
    with open('heart_failure_model.pkl', 'rb') as pickle_in:
        model = pickle.load(pickle_in)
    
    # Display the user input
    st.subheader('User Input Summary')
    st.write(input_df)

    # Make predictions with the model
    if st.button('Predict'):
        prediction = model.predict(input_df)
        prediction_output = 'Yes' if prediction[0] == 1 else 'No'
        
        st.subheader('Prediction Result')
        if prediction_output == 'Yes':
            st.markdown(f"<h3 style='color: red;'>Prediction: {prediction_output} - High Risk of Heart Failure</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='color: green;'>Prediction: {prediction_output} - Low Risk of Heart Failure</h3>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()

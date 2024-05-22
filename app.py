import streamlit as st
import pickle
st.set_page_config(layout="wide")
pickle_in = open('heart_failure_model.pkl', 'rb')
model = pickle.load(pickle_in)

# Define a dictionary to map categorical features to their possible values
categorical_features = {
    'anaemia': ['No', 'Yes'],
    'diabetes': ['No', 'Yes'],
    'high_blood_pressure': ['No', 'Yes'],
    'sex': ['Male', 'Female'],
    'smoking': ['No', 'Yes'],
}

# Define a function to perform one-hot encoding for categorical features
def encode_categorical(data):
  encoded_data = {}
  for feature, options in categorical_features.items():
    encoded_data[feature] = [0] * len(options)
    encoded_data[feature][options.index(data[feature])] = 1
  return encoded_data

# Create the Streamlit app
st.title("Heart Disease Prediction")

# Create input fields for numerical features
age = st.number_input("Age", min_value=0)
creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase")
ejection_fraction = st.number_input("Ejection Fraction")
platelets = st.number_input("Platelets")
serum_creatinine = st.number_input("Serum Creatinine")
serum_sodium = st.number_input("Serum Sodium")
time = st.number_input("Time")

# Create combo boxes for categorical features
anaemia_selected = st.selectbox("Anaemia", categorical_features['anaemia'])
diabetes_selected = st.selectbox("Diabetes", categorical_features['diabetes'])
high_blood_pressure_selected = st.selectbox("High Blood Pressure", categorical_features['high_blood_pressure'])
sex_selected = st.selectbox("Sex", categorical_features['sex'])
smoking_selected = st.selectbox("Smoking", categorical_features['smoking'])

# Combine user inputs
user_data = {
    'age': age,
    'anaemia': anaemia_selected,
    'creatinine_phosphokinase': creatinine_phosphokinase,
    'diabetes': diabetes_selected,
    'ejection_fraction': ejection_fraction,
    'high_blood_pressure': high_blood_pressure_selected,
    'platelets': platelets,
    'serum_creatinine': serum_creatinine,
    'serum_sodium': serum_sodium,
    'sex': sex_selected,
    'smoking': smoking_selected,
    'time': time
}

# Encode categorical features
encoded_data = encode_categorical(user_data)
def prediction( age,anaemia, creatinine_phosphokinase,diabetes,ejection_fraction, high_blood_pressure, platelets,serum_creatinine,serum_sodium,sex,smoking,time):  
    prediction=model.predict([[age,anaemia, creatinine_phosphokinase,diabetes,ejection_fraction, high_blood_pressure, platelets,serum_creatinine,serum_sodium,sex,smoking,time]])
    print(prediction)
    return prediction

# Call your machine learning model prediction function here (replace with your actual logic)
# This example assumes a function named 'predict' that takes encoded data as input
# and returns a prediction (e.g., probability of death event)
prediction = model.predict(encoded_data)
#prediction = round(model.predict(features)[0],0)

# Display prediction results
if st.button("Predict"):
  st.write(f"Predicted Probability of Death Event: {prediction:.2f}")  # Format prediction to 2 decimal places

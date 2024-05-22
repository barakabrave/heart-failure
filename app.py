import streamlit as st

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


def prediction(age, creatinine_phosphokinase, ejection_fraction, platelets,
                serum_creatinine, serum_sodium, anaemia, diabetes,
                high_blood_pressure, sex, smoking, time):
  """
  This function takes individual features as input and performs prediction using your model.
  Replace the placeholder logic with your actual prediction code using the provided features.
  """
  prediction = model.predict([[age, creatinine_phosphokinase, ejection_fraction, platelets,
                               serum_creatinine, serum_sodium, anaemia, diabetes,
                               high_blood_pressure, sex, smoking, time]])
  print(prediction)
  return prediction[0]  # Assuming the model returns a list or array, extract the first element (prediction)


def main():
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
    # Extract individual features from encoded data (assuming one-hot encoded)
  anaemia = encoded_data['anaemia'][0]  # Assuming the first element is encoded value (replace with appropriate indexing if different)
   diabetes = encoded_data['diabetes'][0]
high_blood_pressure = encoded_data['high_blood_pressure'][0]
sex = encoded_data['sex'][0]
smoking = encoded_data['smoking'][0]
 

  # Make prediction using the extracted features
  prediction = prediction(age, creatinine_phosphokinase, ejection_fraction, platelets,
                          serum_creatinine, serum_sodium, anaemia_selected, diabetes_selected,
                          high_blood_pressure_selected, sex_selected, smoking_selected, time)

  # Display prediction results
  if st.button("Predict"):
    st.write(f"Predicted Probability of Death Event: {prediction:.2f}")  # Format prediction to 2 decimal places


if __name__ == '__main__':
  main()

import streamlit as st

# Define function to take user inputs
def user_input():
    age = st.slider('Age', 40, 100, 5)
    anaemia = st.selectbox('Anaemia', ('No', 'Yes'))
    creatinine_phosphokinase = st.number_input('Creatinine Phosphokinase', min_value=20, max_value=10000, value=200)
    diabetes = st.selectbox('Diabetes', ('No', 'Yes'))
    ejection_fraction = st.slider('Ejection Fraction', 10, 80, 10)
    high_blood_pressure = st.selectbox('High Blood Pressure', ('No', 'Yes'))
    platelets = st.number_input('Platelets', min_value=0, max_value=1000000, value=250000)
    serum_creatinine = st.number_input('Serum Creatinine', min_value=0.0, max_value=10.0, value=1.0)
    serum_sodium = st.slider('Serum Sodium', 100, 150, 135)
    sex = st.selectbox('Sex', ('Female', 'Male'))
    smoking = st.selectbox('Smoking', ('No', 'Yes'))
    time = st.slider('Time', 0, 300, 150)

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
    st.title("Machine Learning Model Interface")
    
    # Get user input
    user_data = user_input()

    # Convert user data to dataframe (if needed for your model)
    import pandas as pd
    input_df = pd.DataFrame([user_data])
    pickle_in = open('model.pkl', 'rb')
    model = pickle.load(pickle_in)
    
    # Display the user input
    st.subheader('User Input')
    st.write(input_df)

    # Here you can add code to make predictions with your model
    # For example:
    # model = load_your_model()  # Load your trained model
    prediction = model.predict(input_df)
    st.subheader('Prediction')
    st.write(prediction)

if __name__ == '__main__':
    main()

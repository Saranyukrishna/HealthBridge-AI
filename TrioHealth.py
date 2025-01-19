import streamlit as st
import joblib
import pandas as pd
from streamlit_option_menu import option_menu

st.title("HealthBridge-AI")
with st.sidebar:
    selected = option_menu("Choose Model",
                           ["Obesity", "Depression", "Stroke"],
                           icons=['person', 'heart', 'brain'],
                           menu_icon="cast",
                           default_index=0,
                           styles={
                               "nav-link": {
                                   "font-size": "1.3rem",
                                   "padding": "12px 25px",
                                   "color": "#fff",
                                   "border-radius": "12px",
                                   "background-color": "#ff5f40",
                               },
                               "nav-link-selected": {
                                   "background-color": "#ff3a1b",
                               }
                           })

if selected == 'Depression':
    model = joblib.load('depression_model.pkl')

    st.title('Depression Prediction')

    age = st.number_input('Age', max_value=100)
    work_pressure = st.slider('Work Pressure (0-5)', min_value=0, max_value=5, step=1)
    job_satisfaction = st.slider('Job Satisfaction (0-5)', min_value=0, max_value=5, step=1, value=None)
    work_hours = st.slider('Work Hours (0-12)', min_value=0, max_value=12, step=1, value=None)
    financial_stress = st.slider('Financial Stress (0-5)', min_value=0, max_value=5, step=1, value=None)

    gender = st.selectbox('Gender (Male/Female)', ['Male', 'Female'], index=None)
    sleep_duration = st.selectbox('Sleep Duration (7-8 hours, 5-6 hours, More than 8 hours, Less than 5 hours)',
                                  ['7-8 hours', '5-6 hours', 'More than 8 hours', 'Less than 5 hours'], index=None)
    dietary_habits = st.selectbox('Dietary Habits (Moderate, Unhealthy, Healthy)', ['Moderate', 'Unhealthy', 'Healthy'],
                                  index=None)
    suicidal_thoughts = st.selectbox('Have you ever had suicidal thoughts? (Yes/No)', ['Yes', 'No'], index=None)
    family_history = st.selectbox('Family History of Mental Illness (Yes/No)', ['Yes', 'No'], index=None)

    # Check if mandatory fields are filled (not allowing nulls for critical fields)
    if st.button('Predict Depression Status'):
        if not all([gender, age, work_pressure, sleep_duration, dietary_habits, suicidal_thoughts, family_history]):
            st.warning("Please fill out all the critical fields before making a prediction.")
        else:
            new_data = pd.DataFrame({
                'Gender': [gender],
                'Age': [age],
                'Work Pressure': [work_pressure],
                'Job Satisfaction': [job_satisfaction],
                'Sleep Duration': [sleep_duration],
                'Dietary Habits': [dietary_habits],
                'Have you ever had suicidal thoughts ?': [suicidal_thoughts],
                'Work Hours': [work_hours],
                'Financial Stress': [financial_stress],
                'Family History of Mental Illness': [family_history]
            })

            # Make prediction
            prediction = model.predict(new_data)
            if prediction[0] == 'Yes':
                st.write("Predicted Depression Status: Yes")
                st.write(
                    "It is important to take precautions if you are feeling depressed. Please consider the following steps:")
                st.write("- Seek support from a mental health professional.")
                st.write("- Talk to someone you trust about your feelings.")
                st.write("- Practice relaxation techniques such as meditation or deep breathing.")
                st.write("- Make sure you get adequate sleep and exercise regularly.")
                st.write("- Avoid alcohol and drug use.")
            else:
                st.write("Predicted Depression Status: No")
                st.write("You're safe, but it's important to take care of your mental health.")
                st.write("- Maintain a healthy work-life balance.")
                st.write("- Keep a balanced diet and stay active.")
                st.write("- Get enough sleep and manage stress.")

elif selected == 'Obesity':
    st.title("Obesity Prediction")
    model = joblib.load('obesity_model.pkl')
    output_messages = {
        "Insufficient_Weight": "You are underweight. Consider consulting a healthcare provider to evaluate any underlying issues and increase your calorie intake with nutrient-rich foods to achieve a healthy weight.",
        "Normal_Weight": "You are in the normal weight range. Keep up with a balanced diet and regular physical activity to maintain your health.",
        "Overweight_Level_I": "You are slightly overweight. Reducing high-calorie food consumption, incorporating regular exercise, and monitoring your weight could help you achieve a healthier weight.",
        "Overweight_Level_II": "You are in the overweight category. It is advisable to seek guidance from a nutritionist or healthcare provider to develop a personalized weight management plan.",
        "Obesity_Type_I": "You are in the obesity type I category. Adopting a calorie-controlled diet and engaging in consistent physical activity are important steps. Consult a healthcare provider for further assistance.",
        "Obesity_Type_II": "You are in the obesity type II category. Professional medical advice and a structured weight loss program are strongly recommended to address health risks.",
        "Obesity_Type_III": "You are in the obesity type III category. Immediate medical intervention is necessary to manage severe obesity and associated health complications effectively."
    }

    gender = st.selectbox("Gender", ["", "Female", "Male"], index=0)
    age = st.text_input("Age", "")
    height = st.text_input("Height (in meters)", "")
    weight = st.text_input("Weight (in kg)", "")
    family_history = st.selectbox("Family History of Overweight", ["", "yes", "no"], index=0)
    favc = st.selectbox("Do you eat high caloric food frequently?", ["", "yes", "no"], index=0)
    fcvc = st.slider("How often do you eat vegetables in your meals?", 0, 3, 0)
    ncp = st.slider("How many main meals do you have daily?", 0, 6, 0)
    caec = st.selectbox("Do you eat any food between meals?", ["", "no", "Sometimes", "Frequently", "Always"], index=0)
    smoke = st.selectbox("Do you smoke?", ["", "yes", "no"], index=0)
    scc = st.selectbox("Do you monitor the calories you eat daily?", ["", "yes", "no"], index=0)
    calc = st.selectbox("How often do you drink alcohol?", ["", "no", "Sometimes", "Frequently", "Always"], index=0)
    mtrans = st.selectbox("Which transportation do you usually use?", ["", "Walking", "Bike", "Public Transportation", "Private Transportation", "Motorbike"], index=0)
    ch2o = st.slider("How much water do you drink daily? (in liters)", 0, 6, 0)
    faf = st.slider("How often do you have physical activity in a Week?", 0, 7, 0)
    tue = st.slider("How much time do you use technological devices daily? (in hours)", 0, 24, 0)

    if st.button("Predict Obesity Level", key='obesity'):
        if "" in [gender, age, height, weight, family_history, favc, caec, smoke, scc, calc, mtrans] or 0 in [fcvc, ncp, faf, tue] or ch2o == 0:
            st.error("Please fill out all fields before predicting.")
        else:
            input_data = pd.DataFrame({
                "Gender": [gender],
                "Age": [int(age)],
                "Height": [float(height)],
                "Weight": [float(weight)],
                "family_history": [family_history],
                "FAVC": [favc],
                "FCVC": [fcvc],
                "NCP": [ncp],
                "CAEC": [caec],
                "SMOKE": [smoke],
                "SCC": [scc],
                "CALC": [calc],
                "MTRANS": [mtrans],
                "CH2O": [ch2o],
                "FAF": [faf],
                "TUE": [tue]
            })

            try:
                obesity_prediction = model.predict(input_data)
                result = obesity_prediction[0]

                st.success(f"Prediction: {result}")
                st.info(output_messages[result])

            except Exception as e:
                st.error(f"Error: {e}")

elif selected == 'Stroke':
    st.title('Stroke Prediction')

    age = st.text_input('Age')
    gender = st.selectbox('Gender', ['', 'Male', 'Female'])
    hypertension = st.selectbox('Hypertension', ['', 'Yes', 'No'])
    heart_disease = st.selectbox('Heart Disease', ['', 'Yes', 'No'])
    ever_married = st.selectbox('Ever Married', ['', 'Yes', 'No'])
    work_type = st.selectbox('Work Type', ['', 'Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
    residence_type = st.selectbox('Residence Type', ['', 'Urban', 'Rural'])
    avg_glucose_level = st.text_input('Average Glucose Level')
    bmi = st.text_input('BMI')
    smoking_status = st.selectbox('Smoking Status', ['', 'Unknown', 'formerly smoked', 'never smoked', 'smokes'])

    if st.button('Predict'):
        if not all(
                [age, gender, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level,
                 bmi, smoking_status]):
            st.error("Please fill out all fields before making a prediction.")
        else:
            try:
                mappings = {
                    'Gender': {'Male': 1, 'Female': 0},
                    'Hypertension': {'Yes': 1, 'No': 0},
                    'Heart Disease': {'Yes': 1, 'No': 0},
                    'Ever Married': {'Yes': 1, 'No': 0},
                    'Work Type': {'Private': 2, 'Self-employed': 3, 'Govt_job': 0, 'children': 4, 'Never_worked': 1},
                    'Residence Type': {'Urban': 1, 'Rural': 0},
                    'Smoking Status': {'Unknown': 0, 'formerly smoked': 1, 'never smoked': 2, 'smokes': 3}
                }

                input_data = pd.DataFrame({
                    'gender': [mappings['Gender'][gender]],
                    'age': [int(age)],
                    'hypertension': [mappings['Hypertension'][hypertension]],
                    'heart_disease': [mappings['Heart Disease'][heart_disease]],
                    'ever_married': [mappings['Ever Married'][ever_married]],
                    'work_type': [mappings['Work Type'][work_type]],
                    'Residence_type': [mappings['Residence Type'][residence_type]],
                    'avg_glucose_level': [float(avg_glucose_level)],
                    'bmi': [float(bmi)],
                    'smoking_status': [mappings['Smoking Status'][smoking_status]]
                })

                model = joblib.load('brain_stroke.pkl')
                prediction = model.predict(input_data)

                if prediction[0] == 1:
                    st.warning("The person is likely to have a stroke.")
                    st.write("### Precautions to Prevent Stroke:")
                    st.write("""
                    - *Control High Blood Pressure:* Regularly monitor and manage your blood pressure with a healthy diet and medication if prescribed.
                    - *Quit Smoking:* Avoid smoking or exposure to tobacco.
                    - *Manage Diabetes:* Keep blood sugar levels in check through proper medication and a controlled diet.
                    - *Maintain Healthy Weight:* Avoid obesity through regular physical activity and a balanced diet.
                    - *Exercise Regularly:* Engage in moderate-intensity activities like walking, swimming, or cycling.
                    - *Limit Alcohol Consumption:* Avoid excessive alcohol intake.
                    - *Follow a Healthy Diet:* Focus on consuming vegetables, fruits, whole grains, and lean proteins while reducing salt and saturated fats.
                    - *Stay Hydrated:* Drink adequate water daily.
                    - *Regular Medical Checkups:* Visit your doctor for regular screenings and follow their advice.
                    """)
                else:
                    st.success("The person is unlikely to have a stroke.")
            except ValueError as e:
                st.error("Invalid input. Please check the data types.")
            except Exception as e:
                st.error(f"Error: {e}")

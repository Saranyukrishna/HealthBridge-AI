import streamlit as st
import joblib
import pandas as pd
from streamlit_option_menu import option_menu

st.title("HealthBridge-AI")
with st.sidebar:
    selected = option_menu("Choose Model",
                           ["Obesity", "Depression", "Brain Stroke"],
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
    st.title('Depression Prediction')
    age = st.number_input('Age', min_value=0, value=0)
    work_pressure = st.slider('Work Pressure', min_value=0, max_value=5, value=0)
    job_satisfaction = st.slider('Job Satisfaction', min_value=0, max_value=5, value=0)
    work_hours = st.slider('Work Hours', min_value=0, max_value=15, value=0)
    financial_stress = st.slider('Financial Stress', min_value=0, max_value=5, value=0)
    gender = st.selectbox('Gender', ['Male', 'Female'], index=None)
    sleep_duration = st.selectbox('Sleep Duration', ['7-8 hours', '5-6 hours', 'More than 8 hours', 'Less than 5 hours'], index=None)
    dietary_habits = st.selectbox('Dietary Habits', ['Moderate', 'Unhealthy', 'Healthy'], index=None)
    suicidal_thoughts = st.selectbox('Have you ever had suicidal thoughts?', ['Yes', 'No'], index=None)
    family_history = st.selectbox('Family History of Mental Illness', ['Yes', 'No'], index=None)

    if st.button('Predict', key='depression'):
        if age <= 0:
            st.error("Age must be a positive value.")
        elif work_pressure not in range(0, 6):
            st.error("Work Pressure should be between 0 and 5.")
        elif job_satisfaction not in range(0, 6):
            st.error("Job Satisfaction should be between 0 and 5.")
        elif work_hours not in range(0, 16):
            st.error("Work Hours should be between 0 and 15.")
        elif financial_stress not in range(0, 6):
            st.error("Financial Stress should be between 0 and 5.")
        elif gender is None:
            st.error("Gender cannot be empty.")
        elif sleep_duration is None:
            st.error("Sleep Duration cannot be empty.")
        elif dietary_habits is None:
            st.error("Dietary Habits cannot be empty.")
        elif suicidal_thoughts is None:
            st.error("Suicidal Thoughts cannot be empty.")
        elif family_history is None:
            st.error("Family History of Mental Illness cannot be empty.")
        else:
            input_data = pd.DataFrame({
                'Age': [age],
                'Work Pressure': [work_pressure],
                'Job Satisfaction': [job_satisfaction],
                'Work Hours': [work_hours],
                'Financial Stress': [financial_stress],
                'Gender': [gender],
                'Sleep Duration': [sleep_duration],
                'Dietary Habits': [dietary_habits],
                'Have you ever had suicidal thoughts ?': [suicidal_thoughts],
                'Family History of Mental Illness': [family_history]
            })

            try:
                model = joblib.load('depression_model.pkl')
                prediction = model.predict(input_data)

                if prediction[0] == 1:
                    st.warning("The person is likely to suffer from depression.")
                    st.write("### Precautions to Manage Depression:")
                    st.write("""
                    - **Seek Professional Help:** Consult a mental health professional for advice and treatment options.
                    - **Exercise Regularly:** Engage in physical activities like walking, running, or yoga to boost mood and health.
                    - **Maintain a Healthy Diet:** Focus on nutritious foods and avoid excessive junk food and alcohol.
                    - **Get Adequate Sleep:** Aim for 7-9 hours of sleep per night to help maintain emotional balance.
                    - **Build a Support System:** Reach out to family and friends for emotional support.
                    - **Practice Mindfulness:** Engage in mindfulness activities like meditation or breathing exercises to reduce stress.
                    - **Reduce Stress:** Learn to manage stress through relaxation techniques, hobbies, or activities that promote relaxation.
                    - **Avoid Substance Abuse:** Limit alcohol and avoid recreational drugs to keep mental health in check.
                    """)
                else:
                    st.success("The person is unlikely to suffer from depression.")
                    st.info("Maintain a healthy lifestyle and well-being.")
            except Exception as e:
                st.error(f"Error: {e}")
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

elif selected == 'Brain Stroke':
    st.title('Brain Stroke Prediction')

    # Input Fields for Brain Stroke Prediction
    age = st.text_input('Age')
    gender = st.selectbox('Gender', ['', 'Male', 'Female'])
    hypertension = st.selectbox('Hypertension', ['', 'Yes', 'No'])
    heart_disease = st.selectbox('Heart Disease', ['', 'Yes', 'No'])
    ever_married = st.selectbox('Ever Married', ['', 'Yes', 'No'])
    work_type = st.selectbox('Work Type', ['', 'Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
    residence_type = st.selectbox('Residence Type', ['', 'Urban', 'Rural'])
    avg_glucose_level = st.text_input('Average Glucose Level')
    bmi = st.text_input('BMI')
    smoking_status = st.selectbox('Smoking Status', ['', 'formerly smoked', 'never smoked', 'smokes'])

    if st.button('Predict Brain Stroke'):
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
                    'Work Type': {'Private': 0, 'Self-employed': 1, 'Govt_job': 2, 'children': 3, 'Never_worked': 4},
                    'Residence Type': {'Urban': 1, 'Rural': 0},
                    'Smoking Status': {'formerly smoked': 0, 'never smoked': 1, 'smokes': 2}
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

                # Model prediction
                model = joblib.load('stacking_model.pkl')
                prediction = model.predict(input_data)
                result = 'Stroke' if prediction[0] == 1 else 'The person is unlikely to have a  stroke'

                st.success(f"The model predicts: {result}")

                if result == 'Stroke':
                    st.warning("The person is likely to have a stroke.")
                    st.write("### Precautions to Prevent Stroke:")
                    st.write("""

                    - **Control High Blood Pressure:** Regularly monitor and manage your blood pressure with a healthy diet and medication if prescribed.
                    - **Quit Smoking:** Avoid smoking or exposure to tobacco.
                    - **Manage Diabetes:** Keep blood sugar levels in check through proper medication and a controlled diet.
                    - **Maintain Healthy Weight:** Avoid obesity through regular physical activity and a balanced diet.
                    - **Exercise Regularly:** Engage in moderate-intensity activities like walking, swimming, or cycling.
                    - **Limit Alcohol Consumption:** Avoid excessive alcohol intake.
                    - **Follow a Healthy Diet:** Focus on consuming vegetables, fruits, whole grains, and lean proteins while reducing salt and saturated fats.
                    - **Stay Hydrated:** Drink adequate water daily.
                    - **Regular Medical Checkups:** Visit your doctor for regular screenings and follow their advice.
                    """)
                else:
                    st.info(
                        "Maintain a healthy lifestyle, monitor your health regularly, and consult a doctor for any concerns.")

            except Exception as e:
                st.error(f"Error: {e}")

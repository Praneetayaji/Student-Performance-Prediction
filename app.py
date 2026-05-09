
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns


# Page Config
st.set_page_config(
    page_title='Student Performance Prediction',
    page_icon='🎓',
    layout='wide'
)


# Load Model
model = joblib.load('model.pkl')
encoder = joblib.load('label_encoder.pkl')


# Title
st.title('🎓 Student Performance Prediction System')

st.markdown('Predict student academic performance using Machine Learning')


# Tabs
home_tab, prediction_tab, analytics_tab = st.tabs([
    'Home',
    'Prediction',
    'Analytics'
])


# HOME TAB
with home_tab:

    st.header('Project Overview')

    st.write('''
    This system predicts student performance using:

    - Study time
    - Internal grades
    - Attendance
    - Family support
    - School support
    - Internet access
    - Activities
    ''')


# PREDICTION TAB
with prediction_tab:

    st.header('Student Prediction')

    col1, col2 = st.columns(2)

    with col1:

        sex = st.selectbox('Gender', ['M', 'F'])

        age = st.slider('Age', 15, 22, 17)

        studytime = st.slider('Study Time', 1, 4, 2)

        failures = st.slider('Previous Failures', 0, 4, 0)

        schoolsup = st.selectbox('School Support', ['yes', 'no'])

        famsup = st.selectbox('Family Support', ['yes', 'no'])

        paid = st.selectbox('Paid Classes', ['yes', 'no'])

    with col2:

        activities = st.selectbox('Extra Activities', ['yes', 'no'])

        internet = st.selectbox('Internet Access', ['yes', 'no'])

        higher = st.selectbox('Higher Education Interest', ['yes', 'no'])

        absences = st.slider('Absences', 0, 50, 5)

        G1 = st.slider('First Period Grade (G1)', 0, 20, 10)

        G2 = st.slider('Second Period Grade (G2)', 0, 20, 10)


    if st.button('Predict Performance'):

        student_data = pd.DataFrame({
            'sex': [sex],
            'age': [age],
            'studytime': [studytime],
            'failures': [failures],
            'schoolsup': [schoolsup],
            'famsup': [famsup],
            'paid': [paid],
            'activities': [activities],
            'internet': [internet],
            'higher': [higher],
            'absences': [absences],
            'G1': [G1],
            'G2': [G2]
        })


        prediction = model.predict(student_data)

        predicted_grade = encoder.inverse_transform(prediction)


        st.success(f'Predicted Grade: {predicted_grade[0]}')


        if predicted_grade[0] == 'A':
            st.success('Excellent Student Performance')

        elif predicted_grade[0] == 'B':
            st.info('Very Good Performance')

        elif predicted_grade[0] == 'C':
            st.warning('Average Performance')

        else:
            st.error('Student is At Risk')


# ANALYTICS TAB
with analytics_tab:

    st.header('Dataset Analytics')

    df = pd.read_csv('student-mat.csv', sep=';')


    st.subheader('Dataset Preview')
    st.dataframe(df.head())


    st.subheader('Dataset Shape')
    st.write(df.shape)


    # Grade Distribution
    st.subheader('Final Score Distribution')

    fig1, ax1 = plt.subplots(figsize=(8,5))

    sns.histplot(df['G3'], bins=20, kde=True, ax=ax1)

    st.pyplot(fig1)


    # Study Time Analysis
    st.subheader('Study Time vs Final Grade')

    fig2, ax2 = plt.subplots(figsize=(8,5))

    sns.boxplot(
        x=df['studytime'],
        y=df['G3'],
        ax=ax2
    )

    st.pyplot(fig2)


    # Absence Analysis
    st.subheader('Absences vs Final Grade')

    fig3, ax3 = plt.subplots(figsize=(8,5))

    sns.scatterplot(
        x=df['absences'],
        y=df['G3'],
        ax=ax3
    )

    st.pyplot(fig3)


# Footer
st.markdown('---')

st.markdown('### Developed using Machine Learning and Streamlit')

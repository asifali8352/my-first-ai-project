# 🏥 Disease Prediction System
# This app helps predict health risks based on simple information

import streamlit as st
import pandas as pd
import numpy as np

# Make our app look nice!
st.set_page_config(
    page_title="Health Risk Predictor", 
    page_icon="🏥",
    layout="wide"
)

# Title of our app
st.title("🏥 Health Risk Prediction System")
st.write("**Created by: Mohd Asif Ali**")  # Put your name here!

# Explanation of what our app does
st.write("""
### Welcome to our Health Predictor! 🎯

This app helps you understand your health risks based on simple information.
Just enter your details below and our AI will give you a prediction!

**Important:** This is just for learning! Always talk to a real doctor for health advice.
""")

# Create two columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📝 Enter Your Information")
    
    # Get information from the user
    age = st.number_input("Your Age", min_value=1, max_value=120, value=25)
    
    gender = st.selectbox("Gender", ["Male", "Female"])
    
    chest_pain = st.selectbox(
        "Do you ever have chest pain?",
        ["Never", "Sometimes during exercise", "Sometimes at rest", "Often"]
    )
    
    blood_pressure = st.slider("Blood Pressure (Top Number)", 80, 200, 120)
    
    cholesterol = st.slider("Cholesterol Level", 100, 400, 200)
    
    exercise = st.selectbox(
        "How often do you exercise?",
        ["Never", "1-2 times per week", "3-4 times per week", "Almost daily"]
    )
    
    family_history = st.selectbox(
        "Does anyone in your family have heart problems?",
        ["No", "Yes", "I don't know"]
    )

with col2:
    st.header("🔮 Your Health Prediction")
    
    # Simple prediction logic (this is our "AI model")
    def predict_health_risk(age, gender, chest_pain, bp, cholesterol, exercise, family):
        """
        This is our simple AI model!
        In real life, this would be much more complicated.
        """
        risk_score = 0
        
        # Age factor
        if age > 60:
            risk_score += 3
        elif age > 40:
            risk_score += 2
        elif age > 25:
            risk_score += 1
            
        # Gender factor (men have slightly higher risk)
        if gender == "Male":
            risk_score += 1
            
        # Chest pain factor
        if chest_pain == "Often":
            risk_score += 4
        elif chest_pain == "Sometimes at rest":
            risk_score += 3
        elif chest_pain == "Sometimes during exercise":
            risk_score += 1
            
        # Blood pressure factor
        if bp > 160:
            risk_score += 3
        elif bp > 140:
            risk_score += 2
        elif bp > 130:
            risk_score += 1
            
        # Cholesterol factor  
        if cholesterol > 300:
            risk_score += 3
        elif cholesterol > 250:
            risk_score += 2
        elif cholesterol > 200:
            risk_score += 1
            
        # Exercise factor (good exercise = lower risk)
        if exercise == "Never":
            risk_score += 2
        elif exercise == "1-2 times per week":
            risk_score += 1
        elif exercise == "Almost daily":
            risk_score -= 1
            
        # Family history factor
        if family == "Yes":
            risk_score += 2
        elif family == "I don't know":
            risk_score += 1
            
        return max(0, risk_score)  # Don't let score go below 0
    
    # Make the prediction when user clicks the button
    if st.button("🔍 Predict My Health Risk!", type="primary"):
        # Calculate risk score
        risk_score = predict_health_risk(
            age, gender, chest_pain, blood_pressure, 
            cholesterol, exercise, family_history
        )
        
        # Determine risk level
        if risk_score <= 3:
            risk_level = "Low"
            color = "green" 
            emoji = "✅"
            advice = "Great! Keep up the healthy lifestyle!"
        elif risk_score <= 7:
            risk_level = "Medium"
            color = "orange"
            emoji = "⚠️"
            advice = "Consider some lifestyle improvements and regular check-ups."
        else:
            risk_level = "High"
            color = "red"
            emoji = "🚨"
            advice = "Please consider talking to a healthcare professional."
            
        # Show the results
        st.markdown(f"### {emoji} Your Risk Level: **{risk_level}**")
        
        # Show risk level with color
        if color == "green":
            st.success(f"Risk Score: {risk_score}/15")
        elif color == "orange":
            st.warning(f"Risk Score: {risk_score}/15")
        else:
            st.error(f"Risk Score: {risk_score}/15")
            
        st.write(f"**Recommendation:** {advice}")
        
        # Show what factors contributed to the score
        st.write("### 📊 Factors that influenced your score:")
        factors = []
        if age > 40:
            factors.append(f"Age: {age} years")
        if gender == "Male":
            factors.append("Gender: Male (slightly higher risk)")
        if chest_pain != "Never":
            factors.append(f"Chest pain: {chest_pain}")
        if blood_pressure > 130:
            factors.append(f"Blood pressure: {blood_pressure}")
        if cholesterol > 200:
            factors.append(f"Cholesterol: {cholesterol}")
        if exercise == "Never":
            factors.append("Exercise: Not enough")
        if family_history == "Yes":
            factors.append("Family history: Yes")
            
        for factor in factors:
            st.write(f"• {factor}")
            
        # Fun celebration
        st.balloons()

# Educational section
st.write("---")
st.header("📚 Learn More About Heart Health")

col3, col4 = st.columns([1, 1])

with col3:
    st.write("""
    ### 🏃‍♂️ Ways to Improve Your Heart Health:
    - Exercise regularly (at least 30 minutes, 3 times per week)
    - Eat plenty of fruits and vegetables
    - Limit processed foods and sugar
    - Don't smoke
    - Get enough sleep (7-9 hours per night)
    - Manage stress through relaxation or meditation
    """)

with col4:  
    st.write("""
    ### ⚕️ When to See a Doctor:
    - Chest pain or discomfort
    - Shortness of breath
    - Unusual fatigue
    - Irregular heartbeat
    - High blood pressure readings
    - Family history of heart disease
    """)

# Footer
st.write("---")
st.write("💡 **Remember:** This is a learning project! Always consult real healthcare professionals for medical advice.")
st.write("""🎉 **"When you focus on your health, you awaken your creativity." – Stacey Morgenstern!**""")




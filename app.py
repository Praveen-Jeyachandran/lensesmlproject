import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn

st.title('Contact Lenses - Prediction')
st.write('Using the best performing model between Naive Bayes Algorithm, Support Vector Machine Classifier and Logistic Regression, this project helps to determine the type of lenses (if applicable) the user is to be fitted with!')
with st.expander("Project Details"):
    st.write("Developed by Praveen Jeyachandran : 19BEE1185 & S Bandyopadhyay : 19BEE1114")
    st.write(" ")
    st.write("The purpose of this project is to learn and implement Machine Learning.")
    st.write(
        "GitHub Repository: https://github.com/pravinaldo7/lensesmlproject")
model = pickle.load(open('model.pkl', 'rb'))

age = st.selectbox(
     'Age',
     ('Young', 'Pre-presbyopic','Presbyopic'))

specpres = st.selectbox(
     'Spectacle prescription',
     ('Myope', 'Hypermetrope'))

astig = st.selectbox(
     'Do you have astigmatism?',
     ('Yes', 'No'))

tear = st.selectbox('Tear Production Rate', ('Reduced', 'Normal'))

if st.button('Submit'):
    if(age=='Young'):
      age = 1
    elif(age == 'Pre-presbyopic'):
      age = 2
    else:
      age = 3

    if(specpres == 'Myope'):
      specpres = 1
    elif(specpres == 'Hypermetrope'):
      specpres = 2
    
    if(astig == 'Yes'):
      astig = 1
    else:
      astig = 0
    
    if(tear == 'Reduced'):
      tear = 1
    else:
      tear = 2
      
    df = pd.DataFrame([[age, specpres, astig, tear]])
    ans = model.predict(df)
    st.success('Prediction computed!')
    if(ans == [1]):
        st.write('You must get fitted with HARD CONTACT LENSES')
    elif(ans==[2]):
        st.write("You must get fitted with SOFT CONTACT LENSES")
    elif(ans == [3]):
        st.write("You do not need contact lenses!")
    else:
        st.write("Error in user input!")   

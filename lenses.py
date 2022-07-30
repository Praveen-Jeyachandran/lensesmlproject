import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title('Contact Lenses - Prediction')
model = 'D:\BOOKS\seventhsem\TARP\lens\model.pkl'
model = pickle.load(open('D:\BOOKS\seventhsem\TARP\lens\model.pkl', 'rb'))

age = st.selectbox(
     'What is your age classified as',
     ('Young', 'Pre-presbyopic','Presbyopic'))

specpres = st.selectbox(
     'spectacle prescription',
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
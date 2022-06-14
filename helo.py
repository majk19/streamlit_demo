import streamlit as st
import pandas as pd

st.title('hellofff')
st.header('header')
st.subheader('sub')
st.text('nannana')
#df=pd.read_excel('people.xlsx')
a=[1,2,3]
#st.dataframe(df)
if st.button('subs'):
    st.text('hej')
    
name=st.text_input('imie')     
st.write(name)
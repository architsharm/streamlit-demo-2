import streamlit as st

def get_square(num):
    return num*num

number = st.number_input("Insert a number", value=None, placeholder="Type a number...")

if st.button('Submit'):
    st.write('The square of the number is ', get_square(number))
else:
    st.write('PLease ennter a value and click on submit')



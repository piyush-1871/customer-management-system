import streamlit as st
import mysql.connector
st.title("CUSTOMER MANAGEMENT SYSTEM")
choice = st.sidebar.selectbox("My Menu", ("Home", "User", "Admin"))
if(choice == "Home"):
    st.image("https://chisellabs.com/glossary/wp-content/uploads/2023/05/f17fea9f-e83a-4f9b-924c-508d29a53f24.png")
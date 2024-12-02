import streamlit as st
import pandas as pd
import mysql.connector
st.title("CUSTOMER MANAGEMENT SYSTEM")
choice = st.sidebar.selectbox("My Menu", ("Home", "User", "Admin"))
if(choice == "Home"):
    st.image("https://chisellabs.com/glossary/wp-content/uploads/2023/05/f17fea9f-e83a-4f9b-924c-508d29a53f24.png")
elif(choice == 'Admin'):
    if 'alogin' not in st.session_state:
        st.session_state['alogin'] = False
    admin_id = st.text_input("admin id: ")
    admin_pass = st.text_input("admin password: ")  
    btn = st.button("Login")  
    if btn:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Piyush@2002", database="cms")
        c = mydb.cursor()
        c.execute("select * from admin")
        for r in c:
            if(r[0] == admin_id and r[1] == admin_pass):
                st.session_state['alogin'] = True
                break
    if(not st.session_state['alogin']):
        st.write("Incorrect ID or Password!")
        
    if(st.session_state['alogin']):
        st.write("Login Successfull!")
        choice2 = st.selectbox("Features", ("None", "View All Customers", "Add New Customer", "Remove Customer", "Update Customer Details", "Record Transaction", "View Customer Transacation"))
        if(choice2 == "View All Customers"):
            mydb = mysql.connector.connect(host="localhost", user="root", password="Piyush@2002", database="cms")
            df = pd.read_sql("select * from customers", mydb)
            df_no_index = df.to_records(index=False)
            #Display dataframe
            st.dataframe(df_no_index)
                
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
        elif(choice2 == "Add New Customer"):
            #Input Fields
            cust_id = st.number_input("Enter the Customer ID: ", min_value = 1, step = 1, format = '%d')
            first_name = st.text_input("Enter the first name: ")
            last_name = st.text_input("Enter the last name: ")    
            age = st.number_input("Enter the Customer ID: ", min_value = 18, max_value = 100, step = 1, format = '%d')     
            gender = st.selectbox("Enter the gender (M/F): ", ['M', 'F'])
            phone = st.text_input("Enter the phone no. : ")
            address = st.text_input("Enter the address : ")
            email_id = st.text_input("Enter the email : ")
            user_pass = st.text_input("Enter the password for Customer: ")
            btn3 = st.button("Submit")
            if(btn3):
                mydb = mysql.connector.connect(host="localhost", user="root", password="Piyush@2002", database="cms")
                c = mydb.cursor()
                #Check if customer id already exists
                c.execute("SELECT COUNT(*) FROM customers WHERE cust_id = %s", (cust_id,))
                if(c.fetchone()[0] > 0):
                    st.error("Customer ID already exists. Please choose different Customer ID.")
                else:
                    #Insert the new user into user table first
                    c.execute("INSERT INTO user (email_id, user_pass) VALUES (%s, %s)", (email_id, user_pass))
                    #Insert into customers table
                    c.execute("INSERT INTO customers (cust_id, first_name, last_name, age, gender, phone, address, email_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (cust_id, first_name, last_name, age, gender, phone, address, email_id))
                    
                    mydb.commit()
                    st.header("Customer Added Successfully!")
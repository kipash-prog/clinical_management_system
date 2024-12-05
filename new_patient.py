import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="add your host name ", 
    user="username",
    password="youe password",
    database=" your database name"  
)

def main():
    admin_name = "admin" #enter admin name
    admin_password = "admin_password"  #enter admin password
    
    name = input("Enter admin name: ").lower()
    password = input("Enter admin password: ")
    
    if name == admin_name and password == admin_password:
        print("Login successful!")
        
        wellcome()
    else:
        print("Incorrect admin name or password.")

def wellcome():
    
    while True:
        print(">>>>>>>>>>>>......ADDIS ABABA UNIVERSITY......<<<<<<<<<<<<")
        print(">>>>>>>......COLLEGE OF NATURAL AND COMPUTATIONAL SCIENCE......<<<<<<<<<")
        print(">>>>>>>>>>>......WELLCOME TO 4K CLINIC......<<<<<<<<<<")
        print("1. New patient")
        print("2. old patient")
        print("3. Medical Certificate")
        print("4. Exit")
    
        choice = input("Enter your choice: ")
        
        if choice == "1":
            new_patient()
        elif choice == "2":
            existed_patient()
        elif choice == "3":
            Medical_Certificate()
        elif choice == "4":
            exit() 
        else:
            print("Invalid choice.")
        
def new_patient():
    new_patient_name = input("Enter patient name: ")
    new_patient_father_name = input("Enter father name: ")
    new_patient_id = input("Enter ID number: ")
    new_patient_phone_number = input("Enter patient phone number: ")
    new_patient_case = input("Enter patient case: ")

    query = (
        "INSERT INTO clinical_management_system (name, father_name, id_number, phone_number, patient_case) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    
    values = (new_patient_name, new_patient_father_name, new_patient_id, new_patient_phone_number, new_patient_case)

    try:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        print("New patient added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        
def existed_patient():
    existed_patient_name = input("Enter patient name: ")
    existed_patient_father_name = input("Enter father name: ")
    existed_patient_id = (input("Enter patient ID: "))
    
    query = "SELECT * FROM clinical_management_system WHERE id_number = %s"
    values = (existed_patient_id,)

    try:
        cursor = conn.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()  
        
        if result:
            print("Patient found!")
            print("Patient Details:")
            print(f"Name: {result[1]} {result[2]}")
            print(f"Case of the {result[1]} {result[2]} is: {result[5]}")
            print(f"Date of the appointment was: {result[6]}")
        else:
            print("Patient not found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def Medical_Certificate():
    patient_name = input("Enter the name of the student: ")
    patient_father_name = input("Enter patient's father name: ")
    patient_id_number = input("Enter ID: ")
    
    query = "SELECT * FROM clinical_management_system WHERE name = %s AND father_name = %s AND id_number = %s"
    values = (patient_name, patient_father_name, patient_id_number)
    
    try:
        cursor = conn.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()
        
        if result:
            print("|................ADDIS ABABA UNIVERSITY........................|")
            print("|............ARAT KILO CAMPUS CLINICAL CENTER..................|")
            print("|.................MEDICAL CERTIFICATE .........................|")
            print(f"\n Full Name: {result[1]} {result[2]}")
            print(f"\n Date Examination: {result[6]}")
            print(f"\n Case of Student: {result[5]}\n")
        else:
            print("No record found for the specified student.")
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()  

def exit():
    print("Goodbye!")
    quit()
    
    


main()


conn.close()

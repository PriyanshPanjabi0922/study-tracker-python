# Project Name: Study Tracker

from datetime import datetime
import json

study_session_list = []
session_counter =1
highest_count =1

def get_valid_subject():
    while True : 
            session_subject = input("Enter the subject name:").strip()      
            if session_subject == '':
                print("subject name cannot be empty.") 
                print("please enter a valid subject name")
                continue
            return session_subject 

def get_valid_session_date():
    while True:

        session_date = input("Enter the date (formate : DD-MM-YYYY):").strip()
    
        if session_date == '':
            print("Date cannot be empty.")
            print("Please enter the date in DD-MM-YYYY format.")
            continue

        else:
            try :
                today_date = datetime.now().date()
                session_date = datetime.strptime(session_date,"%d-%m-%Y").date()
                if session_date > today_date:
                    print("Future dates are not allowed.")
                    print("please enter today's date or past date.")
                    continue

                return session_date

            except ValueError:
                print("invalid date format, Please use DD-MM-YYYY.")

def get_valid_session_hour():
    while True:

        try:
            hr_study = float(input("Enter the houre of study session:"))

        except ValueError:
            print("invalid input!")
            print("write the Hour of the session")
            continue

        if hr_study == 0:
            print("Study hours must be greater than 0.")
        elif hr_study < 0:
            print("Study hours cannot be negative.")
            print("Please enter a positive number.")
        elif hr_study > 12:
            print("Study hours must be between 1 and 12")
            
        else:
            return hr_study

def get_valid_session_topic():
    while True:
        valid_topic = True

        topic_covered= input("Enter the Topic name you covered:").strip()

        if topic_covered == '':
            print("Topic name cannot be empty.")
            print("Please enter a topic name")
            continue
                
        for each_char in topic_covered:
            if each_char.isalpha() or each_char == ' ':
                valid_topic  = True

            else:
                valid_topic = False
                print("Only letter and spaces are allowed.")
                break

        if valid_topic == False:
            continue
        if valid_topic:
            return topic_covered
    
def get_valid_session_difficulty():
    while True:
        session_difficulty = input("Enter the dificulty level of topic(ex. hard) :").strip().lower()

        if session_difficulty == '':
            print("Difficulty cannot be empty.")
            print("Please enter easy, medium or hard.")
            continue

        elif session_difficulty in ["easy","medium","hard"]:
            return session_difficulty

        else:
            print("invalid input!")
            print("Please enter only: easy,medium or hard.")

def add_session(study_session_list,session_counter):
        
    ### subject select
        session_subject = get_valid_subject() 
  
    ### session date 
        session_date = get_valid_session_date() 

    ### hours of session   
        hr_study = get_valid_session_hour()          
        
    ### Topic which is covered
        topic_covered = get_valid_session_topic()
            
    ### Difficulty level
        session_difficulty= get_valid_session_difficulty()

        ### dictionary creating.

        study_session_dict = {
            "session_counter": session_counter,
            "session_subject":session_subject,
            "session_date":session_date,
            "hr_study":hr_study,
            "topic_covered":topic_covered,
            "session_difficulty":session_difficulty,
        } 

        study_session_list.append(study_session_dict)
        session_counter+=1


        return session_counter

def view_session(study_session_list):
    print("\nBelow are the all the created Sessions by you:")
    print(study_session_list)

print("\nWelcome to the Study Tracker App- By Priyansh panjabi.")

with open("storing_session.json","r") as store_session:
    try:

        study_session_list = json.load(store_session)
        for each_turn in study_session_list:
            each_turn["session_date"] =datetime.strptime(each_turn["session_date"],"%d-%m-%Y").date()

    except json.JSONDecodeError:
        print("JSON file is empty or invalid.")
        print("\nCreating an empty study session list...")
        study_session_list = []
        
def search_session(study_session_list):
    subject_found = False
    user_search_sub = input("Enter the subject name you want to search:").strip()
        
    for each_sub in study_session_list:

        if user_search_sub == each_sub["session_subject"]:
            subject_found = True
            print(f"your search subject:{each_sub['session_subject']} is present!")
            break

    if subject_found is False:
        print("subject not found.")
        print("Please enter an existing subject name.")

def total_session_hour(study_session_list):
    total_hr = 0
        
    for each_subject in study_session_list:
        total_hr+=each_subject["hr_study"]

    print("\ntotal Hr:",total_hr) 

def today_session(study_session_list):
    today_date = datetime.now().date()
    total_hr =0
    found = False
    for each_turn in study_session_list:
                    
        if each_turn["session_date"] == today_date:
            found = True
            print("\nHere is your today's data:")
            print("Session Number:",each_turn["session_counter"])
            print("Subject Name:",each_turn["session_subject"])
            print("Topic you covered :",each_turn["topic_covered"])
            print("difficulty of the subject:",each_turn["session_difficulty"])
            print("Hour you study this subject for today:",each_turn["hr_study"])
                
            total_hr+= float(each_turn["hr_study"])

            print("today total hr are:",total_hr)
    if not found:
        print("There is no sesion for today.")

def delete_session(study_session_list):
    while True:

        try:
            user_delete_session = int(input("Enter the subject number to delete that subject:"))

        except ValueError:
            print("invalid input!")
            print("Enter the session number you want to delete")
            continue

        if user_delete_session > len(study_session_list):
            print("Session number not found.")
            print("Please enter a valid session number.")

        elif user_delete_session == 0:
            print("session number cannot be 0.")
            print("Enter the value greater than 0")

        elif user_delete_session < 0:
            print("Session number cannot be negative")
            print("Enter the sesssion which are present.")
            

        else:
            study_session_list.pop((user_delete_session)-1)
            print("\nSession deleted successfully.")
            break
            
for each_session in study_session_list:

    if each_session["session_counter"]>=highest_count:
        highest_count = each_session["session_counter"]

    session_counter = highest_count + 1

while True:

    print("\n==== Menu ====\n")
    print("1.Add Study session:")
    print("2.View all Session:")
    print("3.Search a Subject:")
    print("4.Total Study Hours:")
    print("5.Show today's study:")
    print("6.Delete Session:")
    print("7.Exit:")

    try:
        user_choice = int(input("\nEnter Your Choice here:"))       

    except ValueError:
        print("Invalid input.")
        print("Please enter a number between 1 and 7")
        continue            

### 1. Add Session  
    if user_choice == 1:
        session_counter = add_session(study_session_list,session_counter)
        
        
### 2. View all Session

    elif user_choice ==2:
        view_session(study_session_list)
                
### 3. Search a subject              

    elif user_choice == 3:
        search_session(study_session_list)
            
### 4. Total Study Hours

    elif user_choice == 4:
        total_session_hour(study_session_list)    

### 5. Show today's study

    elif user_choice == 5:
        today_session(study_session_list)
        
### 6. Delete Session:

    elif user_choice == 6:
        delete_session(study_session_list)     

### 7. Exit 

    elif user_choice == 7:

        with open("storing_session.json","w") as store_session:
            for each_turn in study_session_list:
                each_turn["session_date"] =each_turn["session_date"].strftime("%d-%m-%Y")
            json.dump(study_session_list,store_session)
        print("Thank you for using this app :)")

        break 

### Else part 
    else:
        print("invalid choice.")
        print("Please Select a number between 1 and 7.")

           

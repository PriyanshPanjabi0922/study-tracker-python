# Project Name: Study Tracker

from datetime import datetime
import json

class study_tacker:
    study_session_list = []
    session_counter =1
    highest_count =1

    with open("storing_session.json","r") as store_session:
        study_session_list = json.load(store_session)  
    
    for each_session in study_session_list:

        if each_session["session_counter"]>=highest_count:
            highest_count = each_session["session_counter"]

        session_counter = highest_count + 1

    while True:

        print("\nWelcome to the Study Tracker App- By Priyansh panjabi.")

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
            print("Invalid Input.")
            print("Please enter a numbeer between 1 to 7")
            continue            

### 1. Add Session  
        if user_choice == 1:
            
            ### subject select

            while True : 
                session_subject = input("Enter the subject name:").strip()      
                if session_subject == '':
                    print("Invalid Subject name!") 
                else:
                    break  

            ### session date  
            
            while True:

                session_date = input("Enter the date (formate : DD-MM-YYYY):").strip()
                
                if session_date == '':
                    print("Date cannot be empty.")
                    print("Please enter the date again.")
                    continue

                else:
                    try :
                        today_date = datetime.now().date()
                        session_date = datetime.strptime(session_date,"%d-%m-%Y").date()
                        if session_date > today_date:
                            print("Future dates are not allowed.")
                            print("please enter today's date or past date.")
                            
                        else:
                            break

                    except ValueError:
                        print("invalid date, use formate: DD-MM-YYYY ")

            ### hours of session   
                    
            while True:

                hr_study = float(input("Enter the houre of study session:"))

                if hr_study == 0:
                    print("hours should not be 0!")
                elif hr_study < 0:
                    print("hours should not be Negative!")
                elif hr_study > 12:
                    print("i think you had mistakely write wrong input.")
                else:
                    break
            
            ### Topic which is covered

            while True:
                valid_topic = True

                topic_covered= input("Enter the Topic name you covered:").strip()

                if topic_covered == '':
                    print("don't enter the empty space.")
                    continue
                        
                for each_char in topic_covered:
                    if each_char.isalpha() or each_char == ' ':
                        
                        valid_topic  = True
                    else:
                        valid_topic = False
                        print("Only character and space is allowed.")
                        break

                if valid_topic:
                    break
               
            ### Difficulty level
            
            while True:
                session_difficulty = input("Enter the dificulty level of topic(ex. hard) :").strip().lower()

                if session_difficulty == '':
                    print("Difficulty should not be empty!")
                elif session_difficulty in ["easy","medium","hard"]:
                    break 
                else:
                    print("Please enter only: easy,medium or hard:")


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
            
### 2. View all Session

        elif user_choice ==2:
            print("\nBelow are the all the created Sessions by you:")
            print(study_session_list)
            
### 3. Search a subject

        elif user_choice == 3:
            user_search_sub = input("Enter the subject name you want to search:")
            
            for each_sub in study_session_list:
                if each_sub["session_subject"] == "":
                    print("there is no subject in the study session!")
                    user_search_sub = input("Again try it:")
                elif user_search_sub==each_sub["session_subject"]:  
                     print(f"your search subject:{each_sub['session_subject']} is present!")

### 4. Total Study Hours

        elif user_choice == 4:
            total_hr = 0
            
            for each_subject in study_session_list:
                total_hr+=each_subject["hr_study"]

            print("\ntotal Hr:",total_hr)

### 5. Show today's study

        elif user_choice == 5:
            today_date = datetime.now().date().strftime("%d-%m-%Y") 
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
                    
                    total_hr+= int(each_turn["hr_study"])

                    print("today total hr are:",total_hr)
            if not found:
                print("There is no sesion for today.")

### 6. Delete Session:

        elif user_choice == 6:
            user_delete_session = int(input("Enter the subject number to delete that subject:"))

            if user_delete_session > len(study_session_list):
                print("There is no session of this number , sorry.")

            elif user_delete_session < 1:
                print("Negaive is not selected!")
            
            else:
                study_session_list.pop((user_delete_session)-1)

### 7. exit

        elif user_choice == 7:

            with open("storing_session.json","w") as store_session:
                json.dump(study_session_list,store_session)
            print("Thank you for using this app :)")

            break 

### Else part 

        else:
            print("Enter valid choice!")
            
           

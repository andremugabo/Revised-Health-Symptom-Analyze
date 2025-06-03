import initial
import userRegistration
import userLogin
import promptSymptoms
import illnessVisualisation

def main():
    initial.initialize_files()
    current_user = None

    while True:
        print("\n ==== Health Symptom Analyzer ====")
        print("1. Register")
        print("2. Login")


        if current_user:
            print("3. Check Symptoms")
            print("4. View Data Visualizations")
        print("5. Exit") 

        choice = input("Enter your choice: ")

        if choice == '1':
            userRegistration.register_user()
        elif choice == '2':
            current_user = userLogin.login_user()
        elif  current_user and choice == '3':
            promptSymptoms.prompt_symptoms(current_user)
        elif current_user and choice == '4':
            illnessVisualisation.generate_visualizations()
        elif choice == '5':
            print("Good Bye!")
            break
        else:
            print("Invalid Choice. Please try again.")     

if __name__ == "__main__":
    main()
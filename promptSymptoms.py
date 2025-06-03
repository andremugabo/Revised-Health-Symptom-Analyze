import pandas as pd  # type: ignore
import constant
import userAge
import predictIllness

def prompt_symptoms(user_info):
    print("\n--- Symptom Checker ---")

    # Load Symptom data 
    symptoms_df = pd.read_csv(constant.SYMPTOMS_FILE)
    print("Available Symptoms: ")
    for i, row in symptoms_df.iterrows():
        print(f"{i+1}. {row['symptom']} ({row['intensity']})")

    try:
        choice = int(input("Enter the number of your symptom: ")) - 1
        if choice < 0 or choice >= len(symptoms_df):
            print(" Invalid choice !")
            return
        
        selected_symptom = symptoms_df.iloc[choice]
        age = userAge.calculate_age(user_info['dob'])
        severity = selected_symptom['severity']

        # Predict illness level
        illness_level = predictIllness.predict_illness(age, severity)

        print("\n--- Analysis ---")
        print(f"Age: {age} years ")
        print(f"Symptom :{selected_symptom['symptom']} ({selected_symptom['intensity']})")
        print(f"Predicted illness level: {illness_level}/5")
        print("(1 = least severe, 5 = most severe )")
    except ValueError:
        print("Please enter a valid number!")    


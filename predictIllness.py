import pandas as pd 
import constant
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def predict_illness(age, symptom_severity):
    # Load illness data
    illness_data = pd.read_csv(constant.ILLNESS_FILE)

    #Prepare data for model 
    X = illness_data[['age', 'symptom_severity']]
    y = illness_data['illness_level']

    #Split data 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #Train model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Make prediction 
    prediction = model.predict([[age, symptom_severity]])
    return prediction[0]

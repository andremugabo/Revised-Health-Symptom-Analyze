 **Health Symptom Analyzer** 
It includes:

* Project overview
* Installation instructions
* Dependency setup
* File structure
* Function explanations
* Usage instructions

---

## 📘 README: Health Symptom Analyzer

### 🩺 Project Overview

The **Health Symptom Analyzer** is a command-line tool built with Python to:

* Allow users to register/login.
* Select symptoms and receive a predicted **illness severity level (1–5)** using a trained machine learning model.
* Generate meaningful **data visualizations** from past symptom and illness data.

---

### 🧱 Project Structure

```
health-symptom-analyzer/
├── main.py
├── users.csv
├── symptoms.csv
├── illness.csv
├── functions/
│   ├── initialize_files.py
│   ├── register_user.py
│   ├── login_user.py
│   ├── calculate_age.py
│   ├── predict_illness.py
│   ├── prompt_symptoms.py
│   ├── generate_visualizations.py
├── README.md
```

Each function is placed in its own file inside the `functions/` directory and imported into `main.py`.

---

### ⚙️ Requirements

* Python 3.7+
* pip

### 📦 Dependencies

Install them using:

```bash
pip install pandas scikit-learn matplotlib seaborn
```

Alternatively, you can use a `requirements.txt`:

```bash
# requirements.txt
pandas
scikit-learn
matplotlib
seaborn
```

Install with:

```bash
pip install -r requirements.txt
```

---

### 🚀 Installation & Setup

1. **Clone the repository**

```bash
git clone 
cd Revised-Health-Symptom-Analyzer
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Prepare CSV Files**

Ensure the following files exist:

* `users.csv`: Will be auto-created.
* `symptoms.csv`: Add rows with `symptom,intensity,severity`
* `illness.csv`: Add rows with `age,symptom_severity,illness_level,date,symptom_intensity,symptom_name`

Sample for `symptoms.csv`:

```csv
symptom,intensity,severity
Cough,Mild,2
Fever,High,4
Headache,Moderate,3
```

Sample for `illness.csv`:

```csv
age,symptom_severity,illness_level,date,symptom_intensity,symptom_name
30,3,2,2025-05-20,Moderate,Headache
25,4,4,2025-05-21,High,Fever
```

4. **Run the program**

```bash
python main.py
```

---

### 💡 Function Explanations

#### 1. `initialize_files()`

Creates `users.csv` if it doesn’t exist. Ensures the system can record new users.

---

#### 2. `register_user()`

Prompts for user info and adds a new row to `users.csv`.

* Fields: username, name, date of birth, password
* Uses `getpass.getpass()` for secure password entry.

---

#### 3. `login_user()`

Validates login credentials using the `users.csv` file.

Returns a user info dictionary (`username`, `name`, `dob`) if successful.

---

#### 4. `calculate_age(dob_str)`

Calculates user's age using their date of birth in `"YYYY-MM-DD"` format.

---

#### 5. `predict_illness(age, symptom_severity)`

Trains a **DecisionTreeClassifier** using historical `illness.csv` data and predicts illness severity level (1 to 5).

---

#### 6. `prompt_symptoms(user_info)`

Displays a list of symptoms from `symptoms.csv`. User selects a symptom, and the function calculates age, retrieves severity, and calls `predict_illness()`.

---

#### 7. `generate_visualizations()`

Reads `illness.csv` and generates:

* Histogram of ages
* Bar chart of illness levels
* Pie chart of symptom intensity
* Line chart of symptom occurrences over time
* Heatmap: Age vs Illness Level

Saves the figure as `enhanced_illness_visualization.png`.

---

### 📈 Output Example

After login and symptom selection:

```
--- Analysis ---
Age: 22 years
Symptom: Fever (High)
Predicted illness level: 4/5
(1 = least severe, 5 = most severe)
```

---

### 📊 Sample Visualization

Generates and displays plots like:

* Age distribution histogram
* Illness level bar chart
* Symptom intensity pie chart
* Heatmap showing correlations

File saved: `enhanced_illness_visualization.png`

---

### ✅ Features Summary

| Feature             | Description                                |
| ------------------- | ------------------------------------------ |
| User Registration   | Create a secure user account               |
| User Login          | Authenticate securely with password        |
| Symptom Checker     | Predicts illness severity (1–5)            |
| Data Visualizations | Charts and graphs for insights             |
| ML Integration      | Decision Tree classifier with scikit-learn |

---

### 👨‍🔧 Troubleshooting

* Make sure `.csv` files are not empty (except for `users.csv` initially).
* Use valid `YYYY-MM-DD` format for DOB and illness records.
* If you get `KeyError` or missing column errors, double-check column names.

---

### 📜 License

MIT License.

---


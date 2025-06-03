import constant
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import pandas as pd # type: ignore


def generate_visualizations():
    print("\nGenerating visualizations...")
    
    # Load illness data
    illness_data = pd.read_csv(constant.ILLNESS_FILE)

    # Ensure required columns are present
    required_columns = ['age', 'illness_level', 'symptom_intensity', 'date', 'symptom_name']
    for col in required_columns:
        if col not in illness_data.columns:
            print(f"Missing column: {col}")
            return

    # Set date to datetime if needed
    illness_data['date'] = pd.to_datetime(illness_data['date'])

    # Create figure layout
    fig = plt.figure(figsize=(18, 10))
    
    # 1. Age Distribution
    plt.subplot(2, 3, 1)
    illness_data['age'].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    
    # 2. Illness Level Distribution
    plt.subplot(2, 3, 2)
    illness_data['illness_level'].value_counts().sort_index().plot(kind='bar', color='lightgreen')
    plt.title('Illness Level Distribution')
    plt.xlabel('Illness Level (1–5)')
    plt.ylabel('Count')
    
    # 3. Pie Chart: Symptom Intensity
    plt.subplot(2, 3, 3)
    intensity_counts = illness_data['symptom_intensity'].value_counts()
    plt.pie(intensity_counts, labels=intensity_counts.index, autopct='%1.1f%%', colors=plt.cm.Pastel1.colors)
    plt.title('Symptom Intensity Distribution')

    # 4. Line Chart: Symptom occurrences over time
    plt.subplot(2, 3, 4)
    symptoms_over_time = illness_data.groupby(['date'])['symptom_name'].count()
    symptoms_over_time.plot(kind='line', marker='o', color='coral')
    plt.title('Symptoms Reported Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Symptoms')

    # 5. Heatmap: Age vs Illness Severity
    plt.subplot(2, 3, 5)
    heatmap_data = pd.crosstab(illness_data['age'], illness_data['illness_level'])
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='d')
    plt.title('Age vs Illness Level')
    plt.xlabel('Illness Level')
    plt.ylabel('Age')

    plt.tight_layout()
    plt.savefig('enhanced_illness_visualization.png')
    print("Visualizations saved as 'enhanced_illness_visualization.png'")
    plt.show()

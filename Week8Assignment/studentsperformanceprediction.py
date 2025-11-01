import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class StudentPerformanceModel:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.model = LinearRegression()

    def preprocess(self):
        print("Initial Dataset:")
        print(self.data.head())

        print("Missing values:")
        print(self.data.isnull().sum())
        self.data.dropna(inplace=True)

        print("Convert the string values in Extracurricular Activities column to numbers either 0 or 1:")
        self.data['Extracurricular Activities'] = self.data['Extracurricular Activities'].map({'Yes': 1, 'No': 0})

        self.X = self.data[[
            'Hours Studied',
            'Previous Scores',
            'Extracurricular Activities',
            'Sleep Hours',
            'Sample Question Papers Practiced'
        ]]
        self.y = self.data['Performance Index']

    def split_data(self, test_size=0.2, random_state=7):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state
        )

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        y_pred = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        print("Model Evaluation:")
        print(f"Mean squared error: {mse:.2f}")
        print(f"R2 Score:{r2:.2f}")

    def predict_user_input(self):
        print("Enter values for Students performance prediction:")
        hours_studied = float(input('Enter Hours Studied: '))
        prev_scores = float(input('Previous Scores: '))
        extra_activities = int(input('Extracurricular Activities: '))
        sleep_hrs = float(input('Sleep Hours: '))
        sample_ques_practiced = int(input('Sample Question Papers Practiced: '))

        test_data = pd.DataFrame({
            'Hours Studied': [hours_studied],
            'Previous Scores': [prev_scores],
            'Extracurricular Activities': [extra_activities],
            'Sleep Hours': [sleep_hrs],
            'Sample Question Papers Practiced': [sample_ques_practiced]
        })

        prediction = self.model.predict(test_data)
        print(f"Predicted Student Performance Index: {prediction[0]:.2f}")

    def visualize_data(self):
        for col in self.X.columns:
            plt.figure(figsize=(6, 4))
            sns.scatterplot(x=self.data[col], y=self.y)
            plt.title(f"{col} vs Performance Index")
            plt.xlabel(col)
            plt.ylabel("Performance Index")
            plt.show()


if __name__ == "__main__":
    model = StudentPerformanceModel(os.path.abspath("./Student_Performance.csv"))
    model.preprocess()
    model.split_data()
    model.train_model()
    model.evaluate_model()
    model.predict_user_input()
    model.visualize_data()




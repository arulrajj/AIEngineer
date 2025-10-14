import os

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class CovidEDA:
    def __init__(self, file_path):
        self.df = pd.read_csv(os.path.abspath(file_path))
        self.df = self.df[['Confirmed', 'New cases']]
        print("Initial dataset:")
        print(self.df.head())
    def compute_statistical_measures(self):
        print("\nStatistical Measures:")
        print(f"Mean:\n{self.df.mean()}")
        print(f"\nMedian:\n{self.df.median()}")
        print(f"\nVariance:\n{self.df.var()}")
        print(f"\nStandard Deviation:\n{self.df.std()}")
        print(f"\nCorrelation Matrix:\n{self.df.corr()}")

    # def detect_outliers_using_iqr(self, col):
    #     Q1 = self.df[col].quantile(0.25)
    #     print("Q1:", Q1)
    #     Q3 = self.df[col].quantile(0.75)
    #     print("Q3:", Q3)
    #     IQR = Q3 - Q1
    #     print("IQR:", IQR)
    #
    #     lowerbound = Q1 - 1.5 * IQR
    #     print("Lowerbound:", lowerbound)
    #     upperbound = Q3 + 1.5 * IQR
    #     print("Upperbound:", upperbound)
    #
    #     outlier_df = self.df[(self.df[col] < lowerbound) | (self.df[col] > upperbound)]
    #     #print(outlier_df)
    #     outlier_df = outlier_df[[col]]
    #     outlier_df.to_csv(os.path.abspath('./covid_data_outlier_for_'+col+'.csv'), index=False)
    #
    #     cleaned_df = self.df[(self.df[col] >= lowerbound) & (self.df[col] <= upperbound)]
    #     cleaned_df = cleaned_df[[col]]
    #     cleaned_df.to_csv('cleaned_covid_data_for_'+col+'.csv', index=False)
    #     return cleaned_df

    def detect_clean_outliers_using_iqr(self):
        Q1 = self.df.quantile(0.25)
        Q3 = self.df.quantile(0.75)
        IQR = Q3 - Q1
        self.cleaned_df = self.df[((self.df >= (Q1 - 1.5 * IQR)) & (self.df <= (Q3 + 1.5 * IQR))).all(axis=1)]
        print("Cleaned dataset:\n")
        print(self.cleaned_df.head())
        self.cleaned_df.to_csv('cleaned_covid_data.csv', index=False)
        return self.cleaned_df

    def normalization_using_standard_scalar(self):
        scaler = StandardScaler()
        x_train = pd.read_csv("./cleaned_covid_data.csv")
        x_train_scaled = scaler.fit_transform(x_train)
        print("Original data:\n", x_train)
        print("Scaled data:\n", x_train_scaled)
        return x_train, x_train_scaled

    def plot_histogram(self, df1, data2):
        df2 = pd.DataFrame(data2, columns=['Confirmed', 'New cases'])

        fig, axes = plt.subplots(2, 2, figsize=(12, 5), sharey=True)

        sns.histplot(data=df1, x='Confirmed', label='Confirmed', kde=True, bins=30, color='blue', ax=axes[0,0])
        axes[0,0].set_title('Histogram of Confirmed Covid Cases - Original Data')
        sns.histplot(data=df1, x='New cases', label='New cases', kde=True, bins=30, color='green', ax=axes[0,1])
        axes[0,1].set_title('Histogram of Covid New cases - Original Data')

        sns.histplot(data=df2, x='Confirmed', label='Confirmed', kde=True, bins=30, color='red', ax=axes[1,0])
        axes[1,0].set_title('Histogram of Confirmed Covid Cases - Normalized Data')
        sns.histplot(data=df2, x='New cases', label='New cases', kde=True, bins=30, color='orange', ax=axes[1,1])
        axes[1,1].set_title('Histogram of Covid New cases - Normalized Data')

        plt.tight_layout()
        plt.show()

    def plot_heatmap(self):
        df = pd.read_csv("./cleaned_covid_data.csv")
        plt.figure(figsize=(8, 6))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)

        plt.title('Heatmap to show correlation between Confirmed and New cases')
        plt.show()


if __name__ == "__main__":
    analysis = CovidEDA("./covid_country_wise_status.csv")
    analysis.compute_statistical_measures()
    analysis.detect_clean_outliers_using_iqr()
    original_data,normalized_data = analysis.normalization_using_standard_scalar()
    analysis.plot_histogram(original_data,normalized_data)
    analysis.plot_heatmap()

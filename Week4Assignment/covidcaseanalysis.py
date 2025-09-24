import os
import pandas as pd

class CovidData:

    def __init__(self, file_path):
        self.df = pd.read_csv(os.path.abspath(file_path))

class CovidAnalysis(CovidData):

    def summarize_regionwise_stats(self):
        #print("Region wise total confirmed, death, and recovered covid cases:")
        return self.df.groupby("WHO Region")[["Confirmed","Deaths","Recovered"]].sum()

    def filter_low_case_records(self):
        lowest_confirmed_case = self.df["Confirmed"].min()
        #print(f"Lowest confirmed case: {lowest_confirmed_case}")
        #print("Details of Lowest confirmed covid cases:")
        return self.df[self.df['Confirmed'] <= lowest_confirmed_case]

    def filter_high_case_records(self):
        highest_confirmed_case = self.df.groupby("WHO Region")["Confirmed"].sum()
        #print(highest_confirmed_case.idxmax())
        return highest_confirmed_case.idxmax()

    def sort_by_confirmed_cases(self):
        sorted_df = self.df.sort_values(by=['Confirmed'])
        #print(sorted_df.head(3))
        sorted_df.to_csv(os.path.abspath("./sorted_covid_case_results.csv"), index=False)
        #print("Sorted the Confirmed cases in ascending order and written it in a new csv file - sorted_covid_case_results.csv")

    def top_five_case_counts(self):
        sorted_df = self.df.sort_values(by=['Confirmed'], ascending=False)
        #print("Top 5 Countries with highest covid cases:")
        return sorted_df.head(5)

    def region_with_lowest_death_count(self):
        lowest_death_count = self.df.groupby("WHO Region")["Deaths"].sum()
        #print(lowest_death_count)
        #print(lowest_death_count.idxmin())
        return lowest_death_count.idxmin()

    def india_summary(self):
        #print("India's case summary:")
        india_df = self.df[self.df['Country/Region'] == 'India']
        return india_df[["Confirmed","Deaths","Recovered"]]

    def mortality_rate_by_region(self):
        region_wise_summary_df = self.summarize_regionwise_stats()
        #print("Mortality Rate by Region:")
        return region_wise_summary_df['Deaths']/region_wise_summary_df['Confirmed']

    def recovery_rate_by_region(self):
        region_wise_summary_df = self.summarize_regionwise_stats()
        return region_wise_summary_df['Recovered']/region_wise_summary_df['Confirmed']

    def detect_outliers(self):
        mean = self.df["Confirmed"].mean()
        std = self.df["Confirmed"].std()
        lower = mean - 2 * std
        upper = mean + 2 * std
        #print("Lower:",lower)
        #print("Upper:",upper)
        #print(self.df["Confirmed"] < lower)
        #print(self.df["Confirmed"] > upper)
        #print(self.df[(self.df["Confirmed"] < lower) | (self.df["Confirmed"] > upper)])
        outlier_df = self.df[(self.df["Confirmed"] < lower) | (self.df["Confirmed"] > upper)]
        return outlier_df[["Country/Region","Confirmed"]]

    def group_data_by_country_region(self):
        return self.df.groupby(["Country/Region","WHO Region"])["Confirmed"].sum()

    def regions_with_zero_recovered_cases(self):
        recovered_df = self.df[self.df['Recovered'] == 0]
        return recovered_df[["Country/Region","WHO Region"]]


if __name__ == "__main__":
    analysis = CovidAnalysis("./covid_country_wise_status.csv")
    print("Region wise total confirmed, death, and recovered covid cases: \n",analysis.summarize_regionwise_stats())
    print("\n")
    print("Details of Lowest confirmed covid cases: \n",analysis.filter_low_case_records())
    print("\n")
    print("Region with highest covid cases: \n",analysis.filter_high_case_records())
    print("\n")
    print("Sorted data saved to file - sorted_covid_case_results.csv \n",analysis.sort_by_confirmed_cases())
    print("\n")
    print("Top 5 Countries with highest covid cases: \n",analysis.top_five_case_counts())
    print("\n")
    print("Region with lowest death count: \n",analysis.region_with_lowest_death_count())
    print("\n")
    print("India's case summary: \n",analysis.india_summary())
    print("\n")
    print("Mortality Rate by Region: \n",analysis.mortality_rate_by_region())
    print("\n")
    print("Recovery Rate by Region: \n",analysis.recovery_rate_by_region())
    print("\n")
    print("Outliers in case count: \n",analysis.detect_outliers())
    print("\n")
    print("Group Covid case by Country and Region: \n",analysis.group_data_by_country_region())
    print("\n")
    print("Region with zero Recovered cases: \n",analysis.regions_with_zero_recovered_cases())
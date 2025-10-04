import os
import pandas as pd
import matplotlib.pyplot as plt

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

    def top_ten_confirmed_case_counts(self):
        sorted_df = self.df.sort_values(by=['Confirmed'], ascending=False)
        #print("Top 5 Countries with highest covid cases:")
        return sorted_df.head(10)

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


class CovidVisualization(CovidAnalysis):

    def barchart_top10_confirmed_cases(self):
        top10 = self.top_ten_confirmed_case_counts()
        plt.figure(figsize=(10, 6))
        plt.bar(top10['Country/Region'], top10['Confirmed'], color='skyblue')
        plt.title('Top 10 Countries by Confirmed Cases')
        plt.xlabel('Country')
        plt.ylabel('Confirmed Cases')
        #plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def pie_chart_death_distribution_by_region(self):
        region_deaths = self.df.groupby('WHO Region')['Deaths'].sum()
        plt.figure(figsize=(8, 8))
        plt.pie(region_deaths, labels=region_deaths.index, autopct='%1.1f%%', startangle=140)
        plt.title('Global Death Distribution by Region')
        plt.tight_layout()
        plt.show()

    def line_chart_confirmed_vs_deaths_top5(self):
        top5 = self.df.groupby('Country/Region')['Confirmed'].sum().nlargest(5).index
        confirmed = self.df[self.df['Country/Region'].isin(top5)].groupby('Country/Region')['Confirmed'].sum()
        deaths = self.df[self.df['Country/Region'].isin(top5)].groupby('Country/Region')['Deaths'].sum()

        plt.figure(figsize=(10, 6))
        plt.plot(confirmed.index, confirmed.values, marker='o', label='Confirmed')
        plt.plot(deaths.index, deaths.values, marker='x', label='Deaths')
        plt.title('Confirmed vs Deaths for Top 5 Countries')
        plt.xlabel('Country')
        plt.ylabel('Cases')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def histogram_death_counts_by_region(self):
        region_deaths = self.df.groupby('WHO Region')['Deaths'].sum()
        plt.figure(figsize=(8, 6))
        plt.hist(region_deaths, bins=10, color='darkred', edgecolor='black')
        plt.title('Histogram of Death Counts Across Regions')
        plt.xlabel('Deaths')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

    def stacked_bar_chart_selected_countries(self, countries):
        subset = self.df[self.df['Country/Region'].isin(countries)]
        grouped = subset.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].sum()
        grouped.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab20')
        plt.title('Confirmed, Deaths, and Recovered for Selected Countries')
        plt.ylabel('Cases')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def box_plot_confirmed_by_region(self):
        plt.figure(figsize=(10, 6))
        self.df.boxplot(column='Confirmed', by='WHO Region', grid=False)
        plt.title('Box Plot of Confirmed Cases Across Regions')
        plt.suptitle('')
        plt.xlabel('WHO Region')
        plt.ylabel('Confirmed Cases')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def trend_line_india_vs_country(self, other_country):
        countries = ['India', other_country]
        subset = self.df[self.df['Country/Region'].isin(countries)]
        grouped = subset.groupby('Country/Region')['Confirmed'].sum()

        plt.figure(figsize=(8, 6))
        plt.bar(grouped.index, grouped.values, color=['orange', 'blue'])
        plt.title(f'Confirmed Cases: India vs {other_country}')
        plt.xlabel('Country')
        plt.ylabel('Confirmed Cases')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    analysis = CovidVisualization("./covid_country_wise_status.csv")
    analysis.barchart_top10_confirmed_cases()
    analysis.pie_chart_death_distribution_by_region()
    analysis.line_chart_confirmed_vs_deaths_top5()
    analysis.histogram_death_counts_by_region()
    analysis.stacked_bar_chart_selected_countries(['India', 'United States', 'Brazil', 'Russia', 'South Africa'])
    analysis.box_plot_confirmed_by_region()
    analysis.trend_line_india_vs_country("US")
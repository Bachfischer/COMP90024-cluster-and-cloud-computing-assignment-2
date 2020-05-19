import data_constants
import csv, json
import pandas as pd

# sums up the total number of installations in all of the postcodes for each city
def sum_postcode_data():
    for city in data_constants.city_names:
        file_name = city + "AggregatedAurinData.csv"
        perform_summation(file_name, city)

# sums up all of the installations in the given file
def perform_summation(file_name, city):
    city_data = pd.read_csv(file_name)
    print(city + " sum is " + str(city_data[' total_installations_quantity'].sum()))

# Main method
if __name__ == "__main__":
    sum_postcode_data()

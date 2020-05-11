import sys, os, glob
import pandas as pd
import numpy as np
import data_constants

# loads the data from aurin into a df and aggregated the data from 2001-2018
class AurinDataLoad():

    # the given area is the area the user wants to collect aurin data from
    def __init__(self, area):
        self.area = area.lower()

    # loops through all of the aurin data and aggregates it into one dataframe
    def aggregate_aurin_data(self):
        data = pd.DataFrame()
        file_names_array = self.find_file_names()
        for file_name in file_names_array:
            year_data = self.open_file(file_name)
            if data.empty:
                data = data.append(year_data)
            else:
                data = data.add(year_data)
        data = data.reset_index()
        return data

    # finds the name of the file array based on the specificied area
    def find_file_names(self):
        if self.area == "melbourne":
            return data_constants.melbourne_file_names
        elif self.area == "sydney":
            return data_constants.sydney_file_names
        else:
            return data_constants.australia_file_names


    # opens the given Aurin data file and reads the contents into a dataframe
    def open_file(self, file_name):
        file_location = self.find_file(file_name)
        data = pd.read_csv(file_location[0], sep = ',')
        data = data.set_index('postcode')
        return data

    # finds the given file name in whatever subdirectory it is in
    def find_file(self, file_name):
        working_dir = os.getcwd()
        file_location = glob.glob(working_dir + "/**/" + file_name, recursive = True)
        return file_location

    # writes the given pandas dataframe to a csv file
    def write_to_csv(self, data):
        aggregated_data.to_csv(self.area + "AggregatedAurinData.csv")

# Main method
if __name__ == "__main__":
    if len(sys.argv) > 1:
        area_selection = sys.argv[1]
        data_loader = AurinDataLoad(area_selection)
        aggregated_data = data_loader.aggregate_aurin_data()
        data_loader.write_to_csv(aggregated_data)
    else:
        # return error message?
        data_loader = AurinDataLoad(area_selection)

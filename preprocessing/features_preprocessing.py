import pandas as pd
import time

def date_reducer(date):
    parsedTime = time.strptime(date,"%Y-%m-%d %H:%M:%S.000")
    year = int(parsedTime.tm_year)
    month = int(parsedTime.tm_mon)
    day = int(parsedTime.tm_mday)
    return (year,month,day)

class feature_preprocessing():

    def __init__(self):
        self.data = pd.read_csv("../../data/preprocessed_data.csv", sep=";")


    def preprocess_date(self):
        self.data["DATE"] = self.data ["DATE"].apply(date_reducer)
        self.data = self.data.groupby(['DATE','ASS_ASSIGNMENT','DAY_OFF','WEEK_DAY']).sum()
        self.data = self.data.reset_index()

    def transform_week_day_to_vector(self):
        days = { 1: "MONDAY", 2:"TUESDAY", 3:"WEDNESDAY", 4:"THURSDAY", 5:'FRIDAY', 6:"SATURDAY", 0:"SUNDAY"}
        print(days)
        for key,day in days.items():
            self.data[day]= self.data['WEEK_DAY'].apply(lambda x: int(x == key))

        self.data = self.data.drop(['WEEK_DAY'], axis = 1)

if __name__ == "__main__":
    pp = feature_preprocessing()
    pp.preprocess_date()
    print(pp)
    print(pp.data.columns)

    pp.transform_week_day_to_vector()
    print(pp.data)



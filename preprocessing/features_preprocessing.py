import pandas as pd
import time

def date_reducer(date):
    parsedTime =  time.strptime(date, "%Y-%m-%d %H:%M:%S.000")
    year = int(parsedTime.tm_year)
    month = int(parsedTime.tm_mon)
    day = int(parsedTime.tm_mday)
    hour = int(parsedTime.tm_hour*60 + parsedTime.tm_min)
    return year, month, day, hour

class feature_preprocessing():

    def __init__(self):
        self.data = pd.read_csv("../../data/preprocessed_data.csv", sep=";", nrows=1000)


    def preprocess_date(self):
        self.data["DATE"] = self.data ["DATE"].apply(date_reducer)
        #self.data = self.data.groupby(['DATE','ASS_ASSIGNMENT','DAY_OFF','WEEK_DAY']).sum()
        #self.data = self.data.reset_index()

    def date_vector(self):
        self.data['MONTH'] = self.data ["DATE"].apply(lambda x: x[1])
        self.data['TIME'] = self.data ["DATE"].apply(lambda x: x[3])

    def week_day_to_vector(self):
        days = {1: "MONDAY", 2: "TUESDAY", 3: "WEDNESDAY", 4: "THURSDAY", 5: 'FRIDAY', 6: "SATURDAY", 0: "SUNDAY"}
        print(days)
        for key,day in days.items():
            self.data[day] = self.data['WEEK_DAY'].apply(lambda x: int(x == key))

    def ass_assignement_to_vector(self):
        assignments = self.data['ASS_ASSIGNMENT'].unique()
        for ass in assignments:
            self.data[ass] = self.data['ASS_ASSIGNMENT'].apply(lambda x: int(x == ass))

    def full_preprocess(self):
        self.preprocess_date()
        self.date_vector()
        self.week_day_to_vector()
        self.data = pp.data.drop(['DATE', 'DAY_OFF'], axis=1)
        #self.data = self.data.drop(['WEEK_DAY'], axis=1)
        self.ass_assignement_to_vector()

if __name__ == "__main__":
    pp = feature_preprocessing()
    pp.full_preprocess()
    print(pp.data.columns)
    print(pp.data[['WEEK_DAY', 'MONTH', 'CSPL_CALLS', 'ASS_ASSIGNMENT']].sort_values(by=['CSPL_CALLS'], ascending=[0]))



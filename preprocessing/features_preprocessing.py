import pandas as pd
import time
from configuration import CONFIG

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
        self.data['YEAR'] = self.data['DATE'].apply(lambda x: x[0])
        self.data['MONTH'] = self.data['DATE'].apply(lambda x: x[1])

        for key, month in CONFIG.months.items():
            self.data[month] = self.data['MONTH'].apply(lambda x: int(x == key))
        self.data['TIME'] = self.data ["DATE"].apply(lambda x: x[3])

    def week_day_to_vector(self):
        for key,day in CONFIG.days.items():
            self.data[day] = self.data['WEEK_DAY'].apply(lambda x: int(x == key))

    def ass_assignement_to_vector(self):
        assignments = self.data['ASS_ASSIGNMENT'].unique()
        print(list(assignments))
        for ass in assignments:
            self.data[ass] = self.data['ASS_ASSIGNMENT'].apply(lambda x: int(x == ass))

    def full_preprocess(self, used_columns = CONFIG.default_columns, keep_all = False, remove_columns = []):
        self.preprocess_date()
        self.date_vector()
        self.week_day_to_vector()
        self.ass_assignement_to_vector()
        #self.data = self.data.drop(['DATE', 'DAY_OFF', 'YEAR'], axis=1)
        #self.data = self.data.drop(['WEEK_DAY'], axis=1)

        if not keep_all:
            self.data = self.data[used_columns]
        else:
            self.data = self.data.drop(remove_columns, axis=1)

if __name__ == "__main__":
    pp = feature_preprocessing()
    pp.full_preprocess()
    print(pp.data.columns)
    print(pp.data.sort_values(by=['CSPL_CALLS'], ascending=[0]))



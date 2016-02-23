import pandas as pd
import time
import datetime
from configuration import CONFIG

def date_reducer(date):
    parsedTime = time.strptime(date,"%Y-%m-%d %H:%M:%S.000")
    year = int(parsedTime.tm_year)
    month = int(parsedTime.tm_mon)
    day = int(parsedTime.tm_mday)
    hour = int(parsedTime.tm_hour*60 + parsedTime.tm_min)
    return year, month, day, hour
    
def get_week_day(date):    
    return (datetime.datetime(date[0],date[1],date[2]).weekday()+1)%7
    
    
class submission_preprocessing():

    def __init__(self):
        self.data = pd.read_csv("../../data/submission.txt", sep="\t")

    def preprocess_date(self):
        self.data["DATE"] = self.data ["DATE"].apply(date_reducer)
        self.data["WEEK_DAY"] = self.data["DATE"].apply(get_week_day)
        
    def date_vector(self):
        self.data['YEAR'] = self.data['DATE'].apply(lambda x: x[0])
        self.data['MONTH'] = self.data['DATE'].apply(lambda x: x[1])

        for key, month in CONFIG.months.items():
            self.data[month] = self.data['MONTH'].apply(lambda x: int(x == key))
        self.data['TIME'] = self.data ["DATE"].apply(lambda x: x[3])

    def transform_week_day_to_vector(self):
        for key,day in _Config.days.items():
            self.data[day] = self.data['WEEK_DAY'].apply(lambda x: int(x == key))

        self.data = self.data.drop(['WEEK_DAY'], axis = 1)
        
    def ass_assignement_to_vector(self):
        assignments =  CONFIG.ass_assign
        for ass in assignments:
            self.data[ass] = self.data['ASS_ASSIGNMENT'].apply(lambda x: int(x == ass))    
        
    def full_preprocess(self, used_columns = CONFIG.default_columns, keep_all = False, remove_columns = []):
        self.preprocess_date()
        self.date_vector()
        self.transform_week_day_to_vector()
        self.ass_assignement_to_vector()
        #self.data['CSPL_CALLS'] = self.data['prediction'] 
        self.data = self.data.rename(columns = {'prediction':'CSPL_CALLS'})
        
        if not keep_all:
            self.data = self.data[used_columns]
        else:
            self.data = self.data.drop(remove_columns, axis=1)
        
if __name__ == "__main__":    
    pp = submission_preprocessing()
    pp.full_preprocess(used_columns = CONFIG.default_columns[:])
    submission_data = pp.data
    print(submission_data.columns)
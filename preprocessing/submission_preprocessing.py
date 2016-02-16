import pandas as pd
import time
import datetime

def date_reducer(date):
    parsedTime = time.strptime(date,"%Y-%m-%d %H:%M:%S.000")
    year = int(parsedTime.tm_year)
    month = int(parsedTime.tm_mon)
    day = int(parsedTime.tm_mday)
    return (year,month,day)
    
def get_week_day(date):    
    return (datetime.datetime(date[0],date[1],date[2]).weekday()+1)%7
    
class submission_preprocessing():

    def __init__(self):
        self.data = pd.read_csv("../../data/submission.txt", sep="\t")


    def preprocess_date(self):
        self.data["DATE"] = self.data ["DATE"].apply(date_reducer)
        self.data["WEEK_DAY"] = self.data["DATE"].apply(get_week_day)
        #print(self.data['DATE'])
        #self.data['WEEK_DAY'] = self.data['DATE'].dayofweek
        #self.data = self.data.reset_index()

    def transform_week_day_to_vector(self):
        days = { 1: "MONDAY", 2:"TUESDAY", 3:"WEDNESDAY", 4:"THURSDAY", 5:'FRIDAY', 6:"SATURDAY", 0:"SUNDAY"}
        #print(days)
        for key,day in days.items():
            self.data[day]= self.data['WEEK_DAY'].apply(lambda x: int(x == key))

        self.data = self.data.drop(['WEEK_DAY'], axis = 1)
        
if __name__ == "__main__":    
    pp = submission_preprocessing()
    pp.preprocess_date()
    pp.transform_week_day_to_vector()
    df = pp.data
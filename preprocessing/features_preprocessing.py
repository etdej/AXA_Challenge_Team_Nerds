import pandas as pd
import time

def date_reducer(date):
    parsedTime = time.strptime(date,"%Y-%m-%d %H:%M:%S.000")
    year = int(parsedTime.tm_year)
    month = int(parsedTime.tm_mon)
    day = int(parsedTime.tm_mday)
    return (year,month,day)
preprocessed_data = pd.read_csv("../../data/preprocessed_data.csv", sep=";")

grouped_by_date_data = preprocessed_data

grouped_by_date_data["DATE"] = preprocessed_data ["DATE"].apply(date_reducer)
grouped_by_date_data = grouped_by_date_data.groupby(['DATE','ASS_ASSIGNMENT','DAY_OFF','WEEK_DAY']).sum()
print(grouped_by_date_data)
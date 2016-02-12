import pandas as pd
from configuration import CONFIG

def find_day(day) :
    if(day == "Dimanche"):
        return 0
    if(day == "Lundi"):
        return 1
    if(day == "Mardi"):
        return 2
    if(day == "Mercredi"):
        return 3
    if(day == "Jeudi"):
        return 4
    if(day == "Vendredi"):
        return 5
    if(day == "Samedi"):
        return 6

class load_data:

    def __init__(self):
        data = pd.read_csv("../../data/train_2011_2012.csv", sep=";", nrows=10000, usecols = CONFIG.useful_columns)
        week_day = data['DAY_WE_DS'].map(lambda day: find_day(day))
        data.add(pd.Series(week_day), axis='columns')
        data.remove(['DAY_DS', 'WEEK_END', 'DAY_WE_DS'])
        self.data = data

if __name__ == "__main__":
    data = load_data()

    print(data.data.columns)
    print(data.data[['']].sort(['CSPL_CALLS'], ascending = [0]))
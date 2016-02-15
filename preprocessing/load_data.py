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
        data = pd.read_csv("../../data/train_2011_2012.csv", sep=";", usecols = CONFIG.useful_columns)
        week_day = data['DAY_WE_DS'].map(lambda day: find_day(day))
        data['WEEK_DAY'] = week_day
        data = data.drop(['DAY_DS', 'WEEK_END', 'DAY_WE_DS'], axis = 1)
        grouped = data.groupby(['DATE', 'ASS_ASSIGNMENT', 'DAY_OFF', 'WEEK_DAY']).sum()

        print(grouped.sort_values(['CSPL_CALLS'], ascending = [0]))
        self.data = grouped


if __name__ == "__main__":
    loader = load_data()
    loader.data.to_csv('../../data/preprocessed_data.csv', sep=";")


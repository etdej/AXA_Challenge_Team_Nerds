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
        data['ASS_ID'] = data['ASS_ASSIGNMENT'].apply(lambda x: int(CONFIG.ass_assign[x]))
        data = data.drop(['ASS_ASSIGNMENT', 'DAY_WE_DS', 'WEEK_END'], axis = 1)
        data = data.query('ASS_ID not in [52, 10, 13, 38, 16, 37]')
        grouped = data.groupby(['DATE', 'ASS_ID', 'DAY_OFF', 'WEEK_DAY']).sum()
        self.data = grouped


if __name__ == "__main__":
    loader = load_data()
    loader.data.to_csv('../../data/preprocessed_data.csv', sep=";")


import pandas as pd
import time
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

def get_year_day(date):
    parsedTime = time.strptime(date,"%Y-%m-%d %H:%M:%S.000")
    return parsedTime.tm_yday, parsedTime.tm_year

def find_day_off(year_day, year):
    if(year == 2011):
        if(year_day == 1):
            return "jour de l'an"
        elif(year_day == 115):
            return "lundi de paques"
        elif(year_day == 121):
            return "fete du travail"
        elif(year_day == 128):
            return "victoire 45"
        elif(year_day == 153):
            return "ascension"
        elif(year_day == 163):
            return "pentecote"
        elif(year_day == 195):
            return "fete nationale"
        elif(year_day == 227):
            return "assomption"
        elif(year_day == 305):
            return "toussaint"
        elif(year_day == 315):
            return "armistice 18"
        elif(year_day == 359):
            return "noel"
        else:
            return "nan"
    if(year == 2012):
        if(year_day == 1):
            return "jour de l'an"
        elif(year_day == 116):
            return "lundi de paques"
        elif(year_day == 122):
            return "fete du travail"
        elif(year_day == 129):
            return "victoire 45"
        elif(year_day == 154):
            return "ascension"
        elif(year_day == 164):
            return "pentecote"
        elif(year_day == 196):
            return "fete nationale"
        elif(year_day == 228):
            return "assomption"
        elif(year_day == 306):
            return "toussaint"
        elif(year_day == 316):
            return "armistice 18"
        elif(year_day == 360):
            return "noel"
        else:
            return "nan"
    
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


    def add_day_off(self):
        self.data['YEAR_DAY_AND_YEAR'] = self.data['DATE'].apply(lambda date: get_year_day(date))
        self.data['DAY_DS'] = self.data['YEAR_DAY_AND_YEAR'].apply(lambda date: find_day_off(date[0],date[1]))
        self.data['DAY_OFF'] = self.data['DAY_DS'].apply(lambda label: int(label != "nan"))
        

if __name__ == "__main__":
    loader = load_data()
    loader.add_day_off()
    loader.data.to_csv('../../data/preprocessed_data.csv', sep=";")
    data_loaded = loader.data

    print(sum((data_loaded['CSPL_CALLS'] > 10) * data_loaded['WEEK_END']))
    print(sum((data_loaded['CSPL_CALLS'] > 10))/7*2)
    print(sum(data_loaded['CSPL_CALLS'] > 50))
    print(sum(data_loaded['CSPL_CALLS'] > 10))
    
    loader.add_day_off();
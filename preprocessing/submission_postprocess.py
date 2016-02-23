import pandas as pd
import time
import datetime
from configuration import CONFIG

def date_reducer(date):
    hour = str(date[3]/60)
    minute = str(date[3]%60)
    year = str(date[0])
    month = str(date[1])
    day = str(date[2])
    return year + "-" + month + "-" + day + " " + hour + "-" + minute + "-00.000"

class submission_postprocess():
    
    def __init__(self):
        print(0)
    
    def transform_vector_to_date(self):
        for key, month in CONFIG.months.items():
            self.data['MONTH'] = self.data['MONTH'] + self.data[month].apply(lambda x: str(key)*1)
        self.data['YEAR'] = self.data['MONTH'].apply(lambda x: 2012)
        #Il faut que je recupere les dates da
    
    def postprocess_date(self):
        
        self.data["DATE"] = self.data["DATE"].apply(date_reducer)
        
    def premier_submit(self,pred):
        self.data = pd.read_csv("../../data/submission.txt", sep="\t")
        self.data['prediction'] = pred
        self.data.to_csv("result_submission_axa.txt", sep='\t', encoding='utf-8', index=False)
    
if __name__ == "__main__":  
    print(0)
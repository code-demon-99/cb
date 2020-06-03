import pandas as pd
import numpy as np
import json
import urllib

class ModelRefiner():
    def __init__(self,url="https://api.covid19india.org/raw_data2.json"):
        """ this is default constructor which will
        load the data from default url """

        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        normalized_data = pd.json_normalize(data["raw_data"])
        self.df  = pd.DataFrame(normalized_data)


    def result_one(self):
        """ this will update the CSV file data"""
        res1 =self.df[['detectedstate','detecteddistrict','gender']]
        list_unique_districts = res1['detecteddistrict'].unique()
        res1 = res1.apply(lambda x: x.str.strip() if isinstance(x, str) else x).replace('', np.nan)
        res1['gender'] =res1['gender'].fillna('O') # seted all nul;l values as a gender others so their must be no data loss
        res1['detecteddistrict']=res1['detecteddistrict'].fillna('unknown') # set the na districts to unknown
        res1['detectedstate']=res1['detectedstate'].fillna('unknownstate') # set the detected na to unknown state
        res1=res1.sort_values('detectedstate')
        res=res1.groupby(['detectedstate','detecteddistrict','gender'])['gender'].count().rename_axis(['ds','dd','dg'])
        res=pd.DataFrame(res)
        res.to_csv('static/CSV/res1.csv')
        return True
    def result_two(self):
        """ this will update the res2 CSV file """
        res2 = self.df[['detectedstate','dateannounced']]
        pd.to_datetime(res2['dateannounced'])
        res2.to_csv('static/CSV/res2.csv')
        return True

    def result_three(self):
        """ this will update res3.csv """
        res3 = self.df[['detectedstate','statecode','gender']]
        no_of_people = pd.Series(np.array(res3.groupby(['detectedstate','statecode'])['gender'].count()))
        percentage_people = pd.Series((no_of_people/sum(no_of_people)) * 100 )
        unique_states =pd.Series( res3['detectedstate'].unique())
        statecode = pd.Series(res3['statecode'].unique())
        res3 = pd.DataFrame({'DetectedState':unique_states,
                            'Statecode':statecode,
                            'no_people':no_of_people,
                            'PercentageofPeople':percentage_people,})
        res3.to_csv('static/CSV/res3.csv')
        return True

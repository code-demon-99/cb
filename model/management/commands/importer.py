"""
Import json data from URL to Database
"""
import requests
import json
from model.models import CovidData #Import your model here
from django.core.management.base import BaseCommand
from datetime import datetime
 
IMPORT_URL = 'https://api.covid19india.org/raw_data2.json' # URL to import from
 
class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Makes a GET request to the API.
        """
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
        url=IMPORT_URL,
        headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        id1=0
        for i in range(len(data['raw_data'])):
            
            self.import_covid_data(data['raw_data'][i],i)


    def import_covid_data(self, data,id1):
        
        PatientNumber	=  data['patientnumber']
        StatePatientNumber	=  data['statepatientnumber']
        DateAnnounced	= data['dateannounced']
        EstimatedOnsetDate	= data['estimatedonsetdate']
        AgeBracket = data['agebracket']
        Gender	= data['gender']
        DetectedCity =data['detectedcity']
        DetectedDistrict = data['detecteddistrict']
        DetectedState = data['detectedstate']
        Statecode =	 data['statecode']
        CurrentStatus =	data['currentstatus']
        notes =    data['notes']
        ContractedfromwhichPatient = data['contractedfromwhichpatientsuspected']
        Nationality =data['nationality']
        Typeoftransmission = data['typeoftransmission']
        StatusChangeDate = data['statuschangedate']
        Source_1  = data['source1']
        Source_2 = data['source2']
        Source_3 = data['source3']
        BackupNotes = data['backupnotes']
        Numcases =  data['numcases']
    
        try: #try and catch for saving the objects
            created = CovidData(
                id1,
                PatientNumber,
                StatePatientNumber,
                DateAnnounced,
                EstimatedOnsetDate,
                AgeBracket,
                Gender,
                DetectedCity,
                DetectedDistrict,
                DetectedState,
                Statecode,
                CurrentStatus,
                notes,
                ContractedfromwhichPatient,
                Nationality,
                Typeoftransmission, 
                StatusChangeDate,
                Source_1,
                Source_2,
                Source_3,
                BackupNotes,
                Numcases
            )
            if created:
                created.save()
            display_format = "\n covid, {}, has been saved."
            print(display_format.format(created))
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this Covid: {}\n{}".format(PatientNumber, str(ex))
            print(msg)
    
    
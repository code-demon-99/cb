from django.db import models

# Create your models here.
class CovidData(models.Model):
    PatientNumber	= models.CharField(max_length=256)
    StatePatientNumber	= models.CharField(max_length=256)
    DateAnnounced	= models.CharField(max_length=256)
    EstimatedOnsetDate	= models.CharField(max_length=256)
    AgeBracket = models.CharField(max_length=256)
    Gender	= models.CharField(max_length=2) 
    DetectedCity = models.CharField( max_length=50)
    DetectedDistrict =	models.CharField(max_length=50)
    DetectedState = models.CharField(max_length=50)
    Statecode =	models.CharField(max_length=50)
    CurrentStatus =	models.CharField( max_length=50)
    notes = models.TextField()
    ContractedfromwhichPatient = models.CharField( max_length=50)
    Nationality = models.CharField( max_length=50)
    Typeoftransmission = models.CharField( max_length=50)
    StatusChangeDate = models.CharField(max_length=256)
    Source_1  = models.TextField()
    Source_2 = models.TextField()
    Source_3 = models.TextField()
    BackupNotes = models.TextField()	
    Numcases = models.CharField(max_length=256)

    def __str__(self):
        return self.PatientNumber       

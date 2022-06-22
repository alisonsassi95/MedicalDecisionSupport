from pydoc import describe
from django.db import models
#from model_utils.models import TimeStampedModel

class DataPatient(models.Model):
    patient = models.CharField(max_length=200)
    age = models.IntegerField()
    neurological = models.IntegerField()
    MeaningNeurological = models.CharField(max_length=200)
    cardiovascular = models.IntegerField()
    MeaningCardiovascular = models.CharField(max_length=200)
    respiratory = models.IntegerField()
    MeaningRespiratory = models.CharField(max_length=200)
    coagulation = models.IntegerField()
    MeaningCoagulation = models.CharField(max_length=200)
    hepatic = models.IntegerField()
    MeaningHepatic = models.CharField(max_length=200)
    renal = models.IntegerField()
    MeaningRenal = models.CharField(max_length=200)
    icc = models.IntegerField()
    MeaningIcc = models.CharField(max_length=200)
    ecog = models.IntegerField()
    MeaningEcog = models.CharField(max_length=200)
    scoreSOFA = models.IntegerField()
    scoreFragility = models.IntegerField()
    scoreTotal = models.IntegerField()
    classification = models.IntegerField()
    active = models.BooleanField()

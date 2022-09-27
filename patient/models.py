
from django.db import models
#from model_utils.models import TimeStampedModel

class DataPatient(models.Model):
    name_patient = models.CharField(max_length=200)
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
    spict = models.IntegerField()
    MeaningSpict = models.CharField(max_length=200)
    ecog = models.IntegerField()
    MeaningEcog = models.CharField(max_length=200)
    scoreSOFA = models.IntegerField()
    scoreAmib = models.IntegerField()
    classification = models.IntegerField()
    active = models.BooleanField()
    exported = models.BooleanField()
    class Meta:
        db_table = 'patient'

    def __str__(self):
        return self.patient


class ValidationPatient(models.Model):
    idPatient = models.ForeignKey('DataPatient', on_delete=models.PROTECT)
    validationNumber = models.IntegerField()
    medicalName = models.CharField(max_length=200)
    medicalClassification = models.IntegerField()
    class Meta:
        db_table = 'validation_patient'

    def __str__(self):
        return self.medicalClassification
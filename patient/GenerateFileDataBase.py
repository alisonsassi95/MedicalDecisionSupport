import os
from time import sleep
from .CalculateMDS import PersonalData
from .CalculateMDS import ShortLifeForecast
from .CalculateMDS import LongLifeForecast
from .CalculateMDS import CalculateValuesOfPatient
from .models import DataPatient
from .measurementNames import longTermSurvival
from .measurementNames import shortTermSurvival

# Main Program
def runScriptGenerateDataPatient():
    exist = os.path.exists(NameFileExport)
    if not (exist):
        createFile()
    counter = 0
    while counter < 100:
        print("Passou Sleep"+counter)
        sleep(1)
        insertOneRegisterInFile()
    counter += 1

def insertOneRegisterInFile():
    arq = open(NameFileExport,'a')
    arq.write('\n')
    dataGenerateRegister = generateRegister()
    arq.write(dataGenerateRegister)
    arq.close()

NameFileExport = 'data_Calculate.csv'

def createFile():
    arq = open(NameFileExport,'w')
    arq.write('PATIENT,AGE,NEUROLOGICAL,CARDIOVASCULAR,RESPIRATORY,COAGULATION,HEPATIC,RENAL,ICC,ECOG,SCORE_MINOR_TOTAL,SCORE_FRAGILITY,SCORE_SOFA,CLASSIFICATION')
    arq.close()

def generateRegister():
    patient = PersonalData.patient()
    age = PersonalData.age()
    neurological = ShortLifeForecast.neurological()
    cardiovascular = ShortLifeForecast.cardiovascular()
    respiratory = ShortLifeForecast.respiratory()
    coagulation = ShortLifeForecast.coagulation()
    hepatic = ShortLifeForecast.hepatic()
    renal = ShortLifeForecast.renal()
    icc = LongLifeForecast.ICC()
    ecog = LongLifeForecast.ECOG(age)
    scoreSOFA = CalculateValuesOfPatient.calculateSOFA(
        NEUROLOGICAL = neurological,
        CARDIOVASCULAR = cardiovascular,
        RESPIRATORY= respiratory,
        COAGULATION= coagulation,
        HEPATIC= hepatic,
        RENAL= renal
        )
    scoreFragility = CalculateValuesOfPatient.calculateFragility(ecog)
    scoreMinorTotal = CalculateValuesOfPatient.calculateTotal(
        SOFA= int(scoreSOFA),
        ICC= int(icc),
        AGE= int(age)
        )
    classification = CalculateValuesOfPatient.Classification(
        SCORE_SOFA = int(scoreSOFA),
        SCORE_FRAGILITY = int(scoreFragility),
        SCORE_TOTAL =int(scoreMinorTotal)
        )
    classification = 0

    DataBase(patient,age,neurological,cardiovascular,respiratory,coagulation,hepatic,renal,icc,ecog,scoreMinorTotal,scoreFragility,scoreSOFA,classification)

    concatenationPersonalData = "%s,%s" % (str(patient), str(age))
    concatenationShortLifeForecast = "%s,%s,%s,%s,%s,%s" % (
        str(neurological),
        str(cardiovascular),
        str(respiratory),
        str(coagulation),
        str(hepatic),
        str(renal)
        )
    concatenationLongLifeForecast = "%s,%s" % (str(icc), str(ecog))
    concatenationCalculate = "%s,%s,%s,%s" % (
        str(scoreMinorTotal),
        str(scoreFragility),
        str(scoreSOFA),
        str(classification)
        )
    concatenation = "%s,%s,%s,%s" % (
        str(concatenationPersonalData), 
        str(concatenationShortLifeForecast),
        str(concatenationLongLifeForecast),
        str(concatenationCalculate)
        )
    return concatenation

def DataBase(patient,age,neurological,cardiovascular,respiratory,coagulation,hepatic,renal,icc,ecog,scoreMinorTotal,scoreFragility,scoreSOFA,classification):

    DataPatient.objects.create(
        patient=patient,
        age=age,
        neurological=neurological,
        MeaningNeurological = shortTermSurvival.neurologicalName(neurological),
        cardiovascular=cardiovascular,
        MeaningCardiovascular = shortTermSurvival.cardiovascularName(cardiovascular),
        respiratory=respiratory,
        MeaningRespiratory = shortTermSurvival.respiratoryName(respiratory),
        coagulation=coagulation,
        MeaningCoagulation = shortTermSurvival.coagulationName(coagulation),
        hepatic=hepatic,
        MeaningHepatic = shortTermSurvival.hepaticName(hepatic),
        renal=renal,
        MeaningRenal = shortTermSurvival.renalName(renal),
        icc=icc,
        MeaningIcc = longTermSurvival.iccName(icc),
        ecog=ecog,
        MeaningEcog = longTermSurvival.ecogName(ecog),
        scoreSOFA = scoreSOFA,
        scoreFragility = scoreFragility,
        scoreTotal = scoreMinorTotal,
        classification=classification,
        active = False,
        exported = False
    )




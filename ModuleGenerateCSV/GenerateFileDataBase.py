import os
import CalculateMDS

NameFileExport = 'data_Calculate.csv'

def createFile():
    arq = open(NameFileExport,'w') 
    arq.write('PATIENT,AGE,NEUROLOGICAL,CARDIOVASCULAR,RESPIRATORY,COAGULATION,HEPATIC,RENAL,ICC,ECOG,SCORE_MINOR_TOTAL,SCORE_FRAGILITY,SCORE_SOFA,CLASSIFICATION')
    arq.close()

def generateRegister():
    patient = CalculateMDS.PersonalData.patient()
    age = CalculateMDS.PersonalData.age()
    neurological = CalculateMDS.ShortLifeForecast.neurological()
    cardiovascular = CalculateMDS.ShortLifeForecast.cardiovascular()
    respiratory = CalculateMDS.ShortLifeForecast.respiratory()
    coagulation = CalculateMDS.ShortLifeForecast.coagulation()
    hepatic = CalculateMDS.ShortLifeForecast.hepatic()
    renal = CalculateMDS.ShortLifeForecast.renal()
    icc = CalculateMDS.LongLifeForecast.ICC()
    ecog = CalculateMDS.LongLifeForecast.ECOG()
    scoreSOFA = CalculateMDS.CalculateValuesOfPatient.calculateSOFA(
        NEUROLOGICAL = neurological,
        CARDIOVASCULAR = cardiovascular,
        RESPIRATORY= respiratory,
        COAGULATION= coagulation,
        HEPATIC= hepatic,
        RENAL= renal
        )
    scoreFragility = CalculateMDS.CalculateValuesOfPatient.calculateFragility(ecog)
    scoreMinorTotal = CalculateMDS.CalculateValuesOfPatient.calculateTotal(
        SOFA= int(scoreSOFA),
        ICC= int(icc),
        AGE= int(age)
        )
    classification = CalculateMDS.CalculateClassification.Classification(
        SCORE_SOFA = int(scoreSOFA),
        SCORE_FRAGILITY = int(scoreFragility),
        SCORE_TOTAL =int(scoreMinorTotal)
        )
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

def insertOneRegisterInFile():
    arq = open(NameFileExport,'a')
    arq.write('\n')
    dataGenerateRegister = generateRegister()
    arq.write(dataGenerateRegister)
    arq.close()

# Main Program
exist = os.path.exists(NameFileExport)
if not (exist):
    createFile()

counter = 0
while counter < 100:
  insertOneRegisterInFile()
  counter += 1

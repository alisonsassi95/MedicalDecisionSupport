
from asyncio.windows_events import NULL
from cmath import isnan
from itertools import count
from django.db.models import Count
from django.db.models import Max
from django.shortcuts import redirect, render
from .measurementNames import longTermSurvival
from .measurementNames import shortTermSurvival
import pandas as pd
from .models import DataPatient
from .models import ValidationPatient
from .GenerateFileDataBase import runScriptGenerateDataPatient

#For test
from faker import Faker
import random


def home(request):
    return render(request, 'home.html')

def generateData(self):
    runScriptGenerateDataPatient()
    makeGroups()
    pass

def validation(request, validateNumb):

    patientRecords = ValidationPatient.objects.filter(validationNumber = validateNumb
        ).values(
        'idPatient__id',
        'idPatient__patient',
        'idPatient__age',                    
        'idPatient__neurological',           
        'idPatient__MeaningNeurological',    
        'idPatient__cardiovascular',         
        'idPatient__MeaningCardiovascular',  
        'idPatient__respiratory',            
        'idPatient__MeaningRespiratory',     
        'idPatient__coagulation',            
        'idPatient__MeaningCoagulation',     
        'idPatient__hepatic',                
        'idPatient__MeaningHepatic',         
        'idPatient__renal',                  
        'idPatient__MeaningRenal',           
        'idPatient__icc',                    
        'idPatient__MeaningIcc',             
        'idPatient__ecog',                   
        'idPatient__MeaningEcog',            
        'idPatient__scoreSOFA',              
        'idPatient__scoreFragility',         
        'idPatient__scoreTotal',             
        'idPatient__classification',
        'idPatient__active',
        'idPatient__exported',
        'validationNumber'
        ).order_by('validationNumber')

    return render(request, 'validation.html', {'patient_records': patientRecords})


def patient(request):
    decisionAlgorithm = pd.read_pickle('Model_MDS.pickle')
    
    # Dados gerados.
    faker = Faker()
    patient = faker.name()
    age = random.randint(10,95)
    neurological = random.randint(0,4)
    MeaningNeurological = shortTermSurvival.neurologicalName(neurological)
    cardiovascular = random.randint(0,4)
    MeaningCardiovascular = shortTermSurvival.cardiovascularName(cardiovascular)
    respiratory = random.randint(0,4)
    MeaningRespiratory = shortTermSurvival.respiratoryName(respiratory)
    coagulation = random.randint(0,4)
    MeaningCoagulation = shortTermSurvival.coagulationName(coagulation)
    hepatic = random.randint(0,4)
    MeaningHepatic = shortTermSurvival.hepaticName(hepatic)
    renal = random.randint(0,4)
    MeaningRenal = shortTermSurvival.renalName(renal)
    icc = random.randrange(2, 5, 2)
    MeaningIcc = longTermSurvival.iccName(icc)
    if (age >= 60): ecog = random.randrange(0,4)
    else: ecog = 0
    MeaningEcog = longTermSurvival.ecogName(ecog)
    
    ''' # Dados do form.
    patient = request.GET['patient']
    age = request.GET['age']
    neurological = request.GET['neurological']
    MeaningNeurological = shortTermSurvival.neurologicalName(int(neurological))
    cardiovascular = request.GET['cardiovascular']
    MeaningCardiovascular = shortTermSurvival.cardiovascularName(int(cardiovascular))
    respiratory = request.GET['respiratory']
    MeaningRespiratory = shortTermSurvival.respiratoryName(int(respiratory))
    coagulation = request.GET['coagulation']
    MeaningCoagulation = shortTermSurvival.coagulationName(int(coagulation))
    hepatic = request.GET['hepatic']
    MeaningHepatic = shortTermSurvival.hepaticName(int(hepatic))
    renal = request.GET['renal']
    MeaningRenal = shortTermSurvival.renalName(int(renal))
    icc = request.GET['icc']
    MeaningIcc = longTermSurvival.iccName(int(icc))
    ecog = request.GET['ecog']
    MeaningEcog = longTermSurvival.ecogName(int(ecog))
    '''
    scoreSOFA = calculateSOFA(
        NEUROLOGICAL = neurological,
        CARDIOVASCULAR = cardiovascular,
        RESPIRATORY= respiratory,
        COAGULATION= coagulation,
        HEPATIC= hepatic,
        RENAL= renal
        )
    scoreFragility = ecog

    scoreTotal = calculateTotal(
        SOFA= int(scoreSOFA),
        ICC= int(icc),
        AGE= int(age)
        )

    list_var = []

    list_var.append(age)
    list_var.append(neurological)
    list_var.append(cardiovascular)
    list_var.append(respiratory)
    list_var.append(coagulation)
    list_var.append(hepatic)
    list_var.append(renal)
    list_var.append(icc)
    list_var.append(ecog)
    list_var.append(scoreSOFA)
    list_var.append(scoreFragility)
    list_var.append(scoreTotal)

    
    print(list_var)
 

    classification = decisionAlgorithm.predict([list_var])

    

    DataPatient.objects.create(
        patient=patient,
        age=age,
        neurological=neurological,
        MeaningNeurological = MeaningNeurological,
        cardiovascular=cardiovascular,
        MeaningCardiovascular = MeaningCardiovascular,
        respiratory=respiratory,
        MeaningRespiratory = MeaningRespiratory,
        coagulation=coagulation,
        MeaningCoagulation = MeaningCoagulation,
        hepatic=hepatic,
        MeaningHepatic = MeaningHepatic,
        renal=renal,
        MeaningRenal = MeaningRenal,
        icc=icc,
        MeaningIcc = MeaningIcc,
        ecog=ecog,
        MeaningEcog = MeaningEcog,
        scoreSOFA = scoreSOFA,
        scoreFragility = scoreFragility,
        scoreTotal = scoreTotal,
        classification=classification[0],
        active = True,
        exported = False
    )

    activePatients = DataPatient.objects.filter(active=True).count()
    totalPatients = DataPatient.objects.values_list().count()
    exportedPatients = DataPatient.objects.filter(exported=True).count()
    waitingExportPatients = DataPatient.objects.filter(exported=False).count()
    topfive = DataPatient.objects.all()[:5]


    return render(request, 'patients.html',
            {'patient':patient,
            'total_patients': totalPatients,
            'active_patients': activePatients,
            'exported_patients': exportedPatients,
            'waiting_export_patients': waitingExportPatients,
            'classification_result': classification[0],
            'topfive': topfive
            })

def modifyValueExported(ValueId):
    for idPatient in DataPatient.objects.filter(id=ValueId):
        idPatient.exported = True
        idPatient.save()

def createRegisterValidatePatient(valueIdPatient, ValidationGroup):
    #faker = Faker()
    ValidationPatient.objects.create(
        idPatient= DataPatient.objects.get(id= int(valueIdPatient)),
        validationNumber= int(ValidationGroup),
        medicalName = NULL,
        medicalClassification = NULL
    )

def makeGroups(request):
    
    quantityGroup = 10
    if(len(ValidationPatient.objects.all()) < 1):
        nextValueGroup = 1
    else:
        nextValueGroup = 1 + (ValidationPatient.objects.aggregate(Max('validationNumber'))['validationNumber__max'])

    def split_list(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    
    patient_list_notExport = list(DataPatient.objects.values_list('id', flat=True).filter(exported=False))
    random.shuffle(patient_list_notExport)
    groupList = list(split_list(patient_list_notExport, quantityGroup))


    for gru in range(0,len(groupList),1):
        for ite in range(0, len(groupList[gru]), 1):
            idPatient = groupList[gru][ite]
            createRegisterValidatePatient(idPatient,(gru + nextValueGroup))
            modifyValueExported(idPatient)        
    
    allPatientsData = ValidationPatient.objects.filter(medicalClassification = '0').values('validationNumber').annotate(countPatient=Count('idPatient__patient')).order_by('validationNumber')

    return render(request, 'makeGroups.html', {'dataPatients': allPatientsData, 'patient_list_notExport': len(patient_list_notExport)})

def db_record(request):
    patientRecords = DataPatient.objects.all()

    context = {
        'patient_records': patientRecords
    }

    return render(request, 'database.html', context)

def calculateSOFA(NEUROLOGICAL,CARDIOVASCULAR,RESPIRATORY,COAGULATION,HEPATIC,RENAL):

        scoreCalculateSOFA = (
            int(NEUROLOGICAL) + 
            int(CARDIOVASCULAR) +
            int(RESPIRATORY) +
            int(COAGULATION) +
            int(HEPATIC) +
            int(RENAL))

        return scoreCalculateSOFA

def calculateTotal(SOFA, ICC, AGE):

        def calculatePointSOFA(SOFA):
            if SOFA <= 8:
                scorePointSOFA = 1
            elif SOFA >= 9 and SOFA <= 11:
                scorePointSOFA = 2    
            elif SOFA >= 12 and SOFA <= 14:
                scorePointSOFA = 3
            elif SOFA > 14:
                scorePointSOFA = 4
            else:
                print("the scorePointSOFA with problem")
                scorePointSOFA = 1000

            return scorePointSOFA

        def calculatePointICC(ICC):

            if ICC == 4:
                scorePointICC = 3
            else:
                scorePointICC = 0
            
            return scorePointICC

        def calculatePointAgeGroup(AGE):

            if AGE <= 49:
                scorePointAgeGroup = 1
            elif AGE >= 50 and AGE <= 69:
                scorePointAgeGroup = 2    
            elif AGE >= 70 and AGE <= 84:
                scorePointAgeGroup = 3
            elif AGE >= 85:
                scorePointAgeGroup = 4
            else:
                print("the scorePointAgeGroup with problem")
                scorePointAgeGroup = 1000

            return scorePointAgeGroup

        scoreCalculateTotal = (
                                calculatePointAgeGroup(AGE) + 
                                calculatePointICC(ICC) + 
                                calculatePointSOFA(SOFA)
                            )

        return scoreCalculateTotal

def disablePatient(request, ValueId):
    for idPatient in DataPatient.objects.filter(id=ValueId):
        idPatient.active = False
        idPatient.save()
    return redirect('records')
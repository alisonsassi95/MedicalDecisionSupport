
from django.shortcuts import redirect, render
from .measurementNames import longTermSurvival
from .measurementNames import shortTermSurvival
import pandas as pd
from .models import DataPatient
from .models import ValidationPatient

#For test
from faker import Faker
import random

def home(request):
    return render(request, 'home.html')

def validation(request):

    patientRecords = DataPatient.objects.all().order_by('classification').values()

    return render(request, 'validation.html', {'patient':patient,'patient_records': patientRecords})

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
    ecog = random.randrange(0,4)
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
    scoreFragility = ecog #(verificar se é valido para pessoas acima de 60 anos)

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

    patientRecords = DataPatient.objects.filter(active=True)
    
    ValueIdPatient = DataPatient.objects.last().__getattribute__('id')

    createRegisterValidatePatient(ValueIdPatient)
    
    return render(request, 'patients.html', {'patient':patient,'patient_records': patientRecords,'classification_result': classification[0]})

def createRegisterValidatePatient(ValueIdPatient):
    faker = Faker()
    ValidationPatient.objects.create(
        idPatient= DataPatient.objects.get(id= int(ValueIdPatient)),
        validationNumber=1,
        medicalName = faker.name(),
        medicalClassification = 1
    )


def dividePatientsIntoGroups():
    #Pegar todos os registros do BD que náo estejam como "exportado"
    #Dividir em grupos entre 5 e 10
    #Colocar esses grupos no BD validação
    #Fazer update nos pacientes ( Colocar coluna Exportado) e ativar essa coluna
    return True

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
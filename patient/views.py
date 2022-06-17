
from django.shortcuts import redirect, render
import pandas as pd
from .models import DataPatient
#For test
from faker import Faker
import random

def home(request):
    return render(request, 'home.html')

def validation(request):
    dataPacientReturn = DataPatient.objects.all()

    imageAvatar = [
        'w-40 avatar gd-warning',
        'w-40 avatar gd-info',
        'w-40 avatar gd-success',
        'w-40 avatar gd-danger',
        'w-40 avatar gd-primary'
        ]
    avatarPatient = random.choice(imageAvatar)

    return render(request, 'validation.html', {'patient':patient,'avatarPatient':imageAvatar,'patient_records': dataPacientReturn})

def patient(request):
    model = pd.read_pickle('Model_MDS.pickle')
    
    # Dados gerados.
    faker = Faker()
    patient = faker.name()
    age = random.randint(10,95)
    neurological = random.randint(0,4)
    cardiovascular = random.randint(0,4)
    respiratory = random.randint(0,4)
    coagulation = random.randint(0,4)
    hepatic = random.randint(0,4)
    renal = random.randint(0,4)
    icc = random.randrange(2, 5, 2)
    ecog = random.randrange(2, 5, 2)
     
    ''' # Dados do form.
    patient = request.GET['patient']
    age = request.GET['age']
    neurological = request.GET['neurological']
    cardiovascular = request.GET['cardiovascular']
    respiratory = request.GET['respiratory']
    coagulation = request.GET['coagulation']
    hepatic = request.GET['hepatic']
    renal = request.GET['renal']
    icc = request.GET['icc']
    ecog = request.GET['ecog']
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

    classification = model.predict([list_var])

    DataPatient.objects.create(
        patient=patient,
        age=age,
        neurological=neurological,
        cardiovascular=cardiovascular,
        respiratory=respiratory,
        coagulation=coagulation,
        hepatic=hepatic,
        renal=renal,
        icc=icc,
        ecog=ecog,
        scoreSOFA = scoreSOFA,
        scoreFragility = scoreFragility,
        scoreTotal = scoreTotal,
        classification=classification[0],
        active = False
    )

    dataPacientReturn = DataPatient.objects.filter(active=True)

    return render(request, 'patients.html', {'patient':patient,'patient_records': dataPacientReturn,'classification_result': classification[0]})



def db_record(request):
    dataPacientReturn = DataPatient.objects.all()

    context = {
        'patient_records': dataPacientReturn
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

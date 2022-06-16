import random
from faker import Faker

# Classe para gerar dados pessoais do Paciente (PATIENT,AGE)
class PersonalData:
    faker = Faker()
    def patient():
        return PersonalData.faker.name()
    def age():
        return random.randint(10,95)
# Classe para gerar dados do SOFA curto prazo (NEUROLOGICAL,CARDIOVASCULAR,RESPIRATORY,COAGULATION,HEPATIC,RENAL)
class ShortLifeForecast:
    def neurological():
        return random.randint(0,4)
    def cardiovascular():
        return random.randint(0,4)
    def respiratory():
        return random.randint(0,4)
    def coagulation():
        return random.randint(0,4)
    def hepatic():
        return random.randint(0,4)
    def renal():
        return random.randint(0,4)
# Classe para gerar dados do SOFA longo prazo (ICC,ECOG)
class LongLifeForecast:
    def ICC():
        return random.randrange(2, 5, 2)
    def ECOG():
        return random.randrange(2, 5, 2)
# Classe para gerar dados do SOFA longo prazo (ICC,ECOG)
class PersonalData:
    faker = Faker()
    def patient():
        return PersonalData.faker.name()
    def age():
        return random.randint(10,95)

class CalculateValuesOfPatient:
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

    def calculateFragility(ECOG):

        scoreFragility = ECOG

        return scoreFragility

    def calculateSOFA(NEUROLOGICAL,CARDIOVASCULAR,RESPIRATORY,COAGULATION,HEPATIC,RENAL):

        scoreCalculateSOFA = (
            int(NEUROLOGICAL) + 
            int(CARDIOVASCULAR) +
            int(RESPIRATORY) +
            int(COAGULATION) +
            int(HEPATIC) +
            int(RENAL))

        return scoreCalculateSOFA

class CalculateClassification:
    def Classification(SCORE_SOFA, SCORE_FRAGILITY, SCORE_TOTAL):
        calc = (SCORE_SOFA + SCORE_FRAGILITY + SCORE_TOTAL)
        return calc

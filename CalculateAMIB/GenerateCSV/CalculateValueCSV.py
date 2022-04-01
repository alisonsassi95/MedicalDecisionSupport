import os
import csv

def calculateTotal(SOFA, ICC, AGE):
    # Menor pontuação total

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
        if AGE >= 50 and AGE <= 69:
            scorePointAgeGroup = 2    
        if AGE >= 70 and AGE <= 84:
            scorePointAgeGroup = 3
        if AGE >= 85:
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

def MinorTotal():
    # ler da base de dados
    return

def insertDataCalculateCSV(HEADER_FILE, DATA_FILE):
    #field_names = ['No', 'Company', 'Car Model'] 
    #cars = [ 
    #{'No': 1, 'Company': 'Ferrari', 'Car Model': '488 GTB'}, 
    #{'No': 2, 'Company': 'Porsche', 'Car Model': '918 Spyder'}, 
    #{'No': 3, 'Company': 'Bugatti', 'Car Model': 'La Voiture Noire'}, 
    #{'No': 4, 'Company': 'Rolls Royce', 'Car Model': 'Phantom'}, 
    #{'No': 5, 'Company': 'BMW', 'Car Model': 'BMW X7'}, 
    #] 

    with open('data_calculate.csv', 'w') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = HEADER_FILE) 
        writer.writeheader() 
        writer.writerows(DATA_FILE) 

    return True

# Main Program
existFile = os.path.exists('data.csv')
if not (existFile):
    print("Arquivo CSV nao existe.")
    exit()



with open("data.CSV") as fileCSV:
    readingCSV = csv.DictReader(fileCSV, delimiter=",")
    listData=[]
    listHeader =[]
    for line in readingCSV:
        scoreSOFA = calculateSOFA(
                                  NEUROLOGICAL=line.get("NEUROLOGICAL"),
                                  CARDIOVASCULAR=line.get("CARDIOVASCULAR"),
                                  RESPIRATORY=line.get("RESPIRATORY"),
                                  COAGULATION=line.get("COAGULATION"),
                                  HEPATIC=line.get("HEPATIC"),
                                  RENAL=line.get("RENAL")
                                  )
        line['SCORE_SOFA'] = scoreSOFA
        scoreFragility = calculateFragility(line.get("ECOG"))
        line['SCORE_FRAGILITY'] = scoreFragility
        scoreTotal = calculateTotal(SOFA= int(scoreSOFA), ICC= int(line.get("ICC")), AGE= int(line.get("AGE")) )
        line['CALCULATE_TOTAL'] = scoreTotal

        listData.append(line.values())
    listHeader.append(line.keys())
    print(list(listHeader))
    print("-----------------")
    print(listData)
    
#print(list(line.keys())[1])
#print(list(line.keys()))
#print(line.values())

insertDataCalculateCSV(list(listHeader), list(listData))




#Passo 1 Preciso saber o menor total 
# Tem empate?
#Passo 2 Preciso saber o menor Fragilidade
# Tem empate?
#Passo 3 Preciso saber o menor SOFA
# Tem empate?
# vamos ver.....




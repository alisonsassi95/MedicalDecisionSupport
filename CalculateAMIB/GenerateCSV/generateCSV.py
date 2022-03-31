import os
import csv
import random
from xml.dom.minidom import Identified

# Parte do CSV: Dados Pessoais
# Ler o arquivo "nome" coluna 1 para preencher a coluna Paciente;
# Gerar idades entre 10 e 95 anos para preencher a coluna idade;
# Ler o arquivo "sexo" coluna 2 para preencher a coluna sexo;

class PersonalData:

    def personDataExternal(typeData):
        # Find file extern
        # Aqui tem um problema, está randomizando a cada iteração. 
        # Mas a pessoal deve ser a mesma nome e sexo.
        peopleRandom = random.randint(2,100728)

        with open('data_name_sex.csv', encoding='utf-8') as referenceFile:
            readFile = csv.reader(referenceFile, delimiter=',')
            print()
            for table in readFile:
                if(readFile.line_num == peopleRandom):
                    name = table[0]
                    gender = table[1]
        
        if(typeData == 'patient'):
            return name
        if(typeData == 'gender'):
            return gender

    def id(IdRange):
        return range(IdRange)

    def patient():
        return PersonalData.personDataExternal('patient')

    def age():
        return random.randint(10,95)
        
    def gender():
        return PersonalData.personDataExternal('gender')


# Parte do CSV: Previsão de sobrevivência a curto prazo					
# Gerar dados entre 0 e 4 para preencher a coluna NEUROLOGICAL;
# Gerar dados entre 0 e 4 para preencher a coluna CARDIOVASCULAR;
# Gerar dados entre 0 e 4 para preencher a coluna RESPIRATORY;
# Gerar dados entre 0 e 4 para preencher a coluna COAGULATION;
# Gerar dados entre 0 e 4 para preencher a coluna HEPATIC;
# Gerar dados entre 0 e 4 para preencher a coluna RENAL;
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


# Parte do CSV: Previsão de sobrevivência a longo prazo
# Gerar dados 2 OU 4 pontos para preencher a coluna ICC;
    #Pacientes com expectativa de sobrevida inferior a cinco anos = 2
    #Pacientes com expectativa de sobrevida inferior a um ano = 4
# Gerar dados 2 OU 4 pontos para preencher a coluna ECOG;

class LongLifeForecast:
    def ICC():
        return random.randrange(2, 5, 2)
    def ECOG():
        return random.randrange(2, 5, 2)

def printRegister():
        #imprime os registros
    arq = open('data.csv','r')
    registros = arq.readlines()
    arq.close()
    #Imprime os registros do arquivo csv formatados e alinhados
    commafound = True #variável que verifica se a lista registros ainda possui elementos com vírgula
    while(commafound):
        commapos = 0 #Index da posição da vírgula no registro onde a vírgula está na maior posição em relação aos outros registros
        commafound = False
        #Verifica se os registros possuem vírgulas e atualiza commapos para o index da posição da vírgula de um dos registros
        for registro in registros:
            if registro.find(',') != -1 and commapos < registro.find(','):
                commafound = True
                commapos = registro.find(',')
        #------------------------------------------------------------------------------
        if not commafound: break #Checa se algum registro ainda possui vírgulas e se não sai do while
        #Coloca a vírgula de todos os registros no mesmo index, preenchendo os índices vazios com espaço, por fim substitue as vírgulas por uma barra reta
        for i in range(len(registros)):
            registro = registros[i]
            if registros[i].find(',') !=-1 and registros[i].find(',') < commapos:
                registro = registro[0:registro.find(','):1] + (' '*(commapos-registro.find(','))) + registro[registro.find(',')::]
            registro = registro.replace(',','|',1)
            registros.pop(i) 
            registros.insert(i,registro)
        #-------------------------------------------------------------------------------
    for registro in registros: # imprime todos os registros
        registro = registro.replace(',','|')
        print(registro,end='')
    #---------------------------------------------------------------------------------

def generateRegister(idPerson):
    Id = PersonalData.id(idPerson)
    patient = PersonalData.patient()
    age = PersonalData.age()
    gender = PersonalData.gender()
    neurological = ShortLifeForecast.neurological()
    cardiovascular = ShortLifeForecast.cardiovascular()
    respiratory = ShortLifeForecast.respiratory()
    coagulation = ShortLifeForecast.coagulation()
    hepatic = ShortLifeForecast.hepatic()
    renal = ShortLifeForecast.renal()
    icc = LongLifeForecast.ICC()
    ecog = LongLifeForecast.ECOG()
    
    concatenationPersonalData = "%s,%s,%s,%s" % (str(Id), str(patient), str(age),str(gender))
    concatenationShortLifeForecast = "%s,%s,%s,%s,%s,%s" % (str(neurological), str(cardiovascular),str(respiratory),str(coagulation),str(hepatic),str(renal))
    concatenationLongLifeForecast = "%s,%s" % (str(icc), str(ecog))
    concatenation = "%s,%s,%s" % (str(concatenationPersonalData), str(concatenationShortLifeForecast),str(concatenationLongLifeForecast))
    return concatenation

def insertOneRegisterInFile(numRegister):
    #Adiciona um registro no arquivo csv
    arq = open('data.csv','r')
    arq.close()
    arq = open('data.csv','a')
    arq.write('\n')
    dataGenerateRegister = generateRegister(numRegister)
    arq.write(dataGenerateRegister)
    arq.close()


def createFile():
    #Cria um arquivo csv
    arq = open('data.csv','w')
    arq.write('ID,PATIENT,AGE,GENDER,NEUROLOGICAL,CARDIOVASCULAR,RESPIRATORY,COAGULATION,HEPATIC,RENAL,ICC,ECOG')
    arq.close()

# Main Program
exist = os.path.exists('data.csv')
if not (exist):
    createFile()

counter = 0
while counter < 100:
  insertOneRegisterInFile(counter)
  counter += 1

printRegister()

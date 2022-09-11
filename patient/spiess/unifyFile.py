import csv
import os
from faker import Faker
faker = Faker()

NameFileExport = "NameFileExport.csv"
def __main__():

    exist = os.path.exists(NameFileExport)
    if not (exist):
        createFile()

    data = []
    patient = []
    for n in range(100):
        reader = csv.reader(open(f'Arquivos/temp_{n}.csv'))
        for l in reader:
            if l:
                l.append(n)
                data.append(l)
    for R in data:
        patient.append(faker.name())

        patient.append(R[0])
        patient.append(neurologicalName(int(R[0])))

        patient.append(R[1])
        patient.append(cardiovascularName(int(R[1])))

        patient.append(R[2])
        patient.append(respiratoryName(int(R[2])))

        patient.append(R[3])
        patient.append(coagulationName(int(R[3])))

        patient.append(R[4])
        patient.append(hepaticName(int(R[4])))

        patient.append(R[5])
        patient.append(renalName(int(R[5])))

        patient.append(R[6])
        patient.append(SPICTName(int(R[6])))
        
        patient.append(R[7])
        patient.append(ecogName(int(R[7])))
        #SOFA
        patient.append(R[8])
        #AMIB
        patient.append(R[9])
        #GRUPO
        patient.append(R[10])

        File = str(patient).replace("'","").replace("[","'").replace("]","").replace("\u2264", "-")
        print(File)
        patient.clear()
        insertOneRegisterInFile(File)

def insertOneRegisterInFile(data_file):
    arq = open(NameFileExport,'a')
    arq.write('\n')
    arq.write(data_file)
    arq.close()

def neurologicalName(value):
        neurologicalName = {
            0: "15",
            1: "13 a 14",
            2: "10 a 12",
            3: "6 a 9",
            4: "<6"
        }
        return neurologicalName[value]

def cardiovascularName(value):
    cardiovascularName = {
            0: "Sem valor",
            1: "PAM<70mmHg",
            2: "Dopamina ≤ 5 ou Dobutamina qualquer dose",
            3: "Dopamina > 5 ou Noradrenalina ≤ 0.1",
            4: "Dopamina > 15 ou Noradrenalina > 0.1"
        }
    return cardiovascularName[value]
def respiratoryName(value):
    respiratoryName = {
            0: "Sem valor",
            1: "SpO2>92% com Cateter nasal O2 até 2l/min",
            2: "SpO2> 92% com Cateter nasal O2 até 5l/min",
            3: "SpO2>92% com ventilação mecânica com FiO2 até 40%",
            4: "SpO2> 92% com ventilação mecânica com FiO2> 40%"
        }
    return respiratoryName[value]
def coagulationName(value):
    coagulationName = {
            0: "Sem valor",
            1: "<150",
            2: "<100",
            3: "<50",
            4: "<20"
        }
    return coagulationName[value]
def hepaticName(value):
    hepaticName = {
            0: "Sem valor",
            1: "<1.1 Anicterico",
            2: "1.1 - 1.36",
            3: "1.36 - 1.8",
            4: "1.88 - 2.15 Icterico"
        }
    return hepaticName[value]

def renalName(value):
    renalName = {
            0: "Sem valor",
            1: "1.2 - 1.9 >500",
            2: "2 - 3.4 -",
            3: "3.5 - 4.9 <500",
            4: ">5.0 <200"
        }
    return renalName[value]

def SPICTName(value):
    SPICTName = {
        0: "Paciente sem problemas graves",
        3: "Pacientes com expectativa de sobrevida inferior a um ano"
    }
    return SPICTName[value]

def ecogName(value):
    ecogName = {
        0: "Completamente ativo",
        1: "Restricao a atividades físicas rigorosas",
        2: "Auto-cuidados",
        3: "Auto-cuidados limitados",
        4: "Completamente incapaz"
    }
    return ecogName[value]

def createFile():
    arq = open(NameFileExport,'w')
    arq.write('NAME_PATIENT,NEUROLOGICAL,DESCR_NEUROLOGICAL,CARDIOVASCULAR,DESCR_CARDIOVASCULAR,RESPIRATORY,DESCR_RESPIRATORY,COAGULATION,DESCR_COAGULATION,HEPATIC,DESCR_HEPATIC,RENAL,DESCR_RENAL,SPICT,DESCR_SPICT,ECOG,DESCR_ECOG,SOFA,AMIB,GROUP')
    arq.close()

if __name__ == '__main__':
    __main__()












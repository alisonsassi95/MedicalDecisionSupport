class shortTermSurvival:

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
                0: "-",
                1: "PAM<70mmHg",
                2: "Dopamina ≤ 5 ou Dobutamina qualquer dose",
                3: "Dopamina > 5 ou Noradrenalina ≤ 0,1",
                4: "Dopamina > 15 ou Noradrenalina > 0,1"
            }
        return cardiovascularName[value]
    def respiratoryName(value):
        respiratoryName = {
                0: "-",
                1: "SpO2>92% com Cateter nasal O2 até 2l/min",
                2: "SpO2> 92% com Cateter nasal O2 até 5l/min",
                3: "SpO2>92% com ventilação mecânica com FiO2 até 40%",
                4: "SpO2> 92% com ventilação mecânica com FiO2> 40%"
            }
        return respiratoryName[value]
    def coagulationName(value):
        coagulationName = {
                0: "-",
                1: "<150",
                2: "<100",
                3: "<50",
                4: "<20"
            }
        return coagulationName[value]
    def hepaticName(value):
        hepaticName = {
                0: "-",
                1: "<1,1 Anictérico",
                2: "1,1 - 1,36",
                3: "1,36 - 1,8",
                4: "1,88 - 2,15 Ictérico"
            }
        return hepaticName[value]

    def renalName(value):
        renalName = {
                0: "-",
                1: "1,2 - 1,9 >500",
                2: "2 - 3,4 -",
                3: "3,5 - 4,9 <500",
                4: ">5,0 <200"
            }
        return renalName[value]

class longTermSurvival:
    def SPICTName(value):
        SPICTName = {
            0: "Paciente sem problemas graves",
            3: "Pacientes com expectativa de sobrevida inferior a um ano"
        }
        return SPICTName[value]

    def ecogName(value):
        ecogName = {
            0: "Completamente ativo",
            1: "Restrição a atividades físicas rigorosas",
            2: "Auto-cuidados",
            3: "Auto-cuidados limitados",
            4: "Completamente incapaz"
        }
        return ecogName[value]
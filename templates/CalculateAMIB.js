const SOFA = 9; //Possibilidade entre 1 a 4
const Comorbidity = true; // Somente true ou false
const ECOG = 3; // Possibilidade entre 0 a 4

calculateAMIB() {
    calculateSOFAPoints();
    calculateComorbidityPoints();
    calculateECOGPoints();
    patientTiebreaker();

}

calculateSOFAPoints(SOFA) {
    let totalPoints = 0;
    // Step 1  Calcular SOFA (total:_____) e pontuar
    if (SOFA <= 8) {
        totalPoints = 1;
    } else if (SOFA > 9 && SOFA < 11) {
        totalPoints = 2;
    } else if (SOFA > 12 && SOFA < 14) {
        totalPoints = 3;
    } else if (SOFA > 14) {
        totalPoints = 4;
    }
    return totalPoints;
}

calculateComorbidityPoints(Comorbidity) {
    let totalPoints = 0;
    // Step 2  Tem comorbidades graves, com expectativa de sobrevida < que um ano?*
    if (Comorbidity) {
        totalPoints = totalPoints + 3;
    }
}

// CFS - Clinical Frailtv Scale * Só deve ser aplicada para doentes com idade igual ou superior a 60 anos.

calculateECOGPoints(SOFA) {
    let totalPoints = 0;
    // Step 3  Aplicar a ECOG e pontuar
    if (ECOG === 0) {
        totalPoints = totalPoints + 1;
    } else {
        totalPoints = totalPoints + ECOG;
    }
    return totalPoints
}

patientTiebreaker() {
    //Essa função deve estar junto com outros Paceientes.
    let MenorScoreSOFA;


}

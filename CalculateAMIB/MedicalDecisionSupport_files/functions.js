//localStorage.clear();
$('input[type=checkbox], input[type=radio]').prop('checked', false).each(function(){
	$(this).siblings('.check-btn').attr('data-val', $(this).val()>0?'+'+$(this).val():0);
});
var i = 0;
$('#somaICC-trigger label').each(function(){
	$(this).attr('for','icc'+i);
	$(this).children('input').attr('id','icc'+i);
	i++;
});

var config = {
	storage: false,
	sofa: 0,
	iccECOG: {
		icc: 0,
		ECOG: 0,
		maiorVal: 0,
		maiorName: ''
	},
	kps: 0,
	eup: 0
}

function addStorage(chave,valor){
	if(config.storage){
		localStorage.setItem(chave,valor);
	}
}
function getStorage(chave){
	return localStorage.getItem(chave);
}
function clearStorage(chave){
	localStorage.removeItem(chave);
}
function clearAllStorage(){
	localStorage.clear();
}


function somaSOFA(){
	var neuro=0,cardio=0,resp=0,coag=0,hepa=0,renal=0;

	$('#somaSOFA-trigger input[name=neuro]').each(function(){
		if($(this).prop('checked')){ neuro = $(this).val(); }
	});
	$('#somaSOFA-trigger input[name=cardio]').each(function(){
		if($(this).prop('checked')){ cardio = $(this).val(); }
	});
	$('#somaSOFA-trigger input[name=resp]').each(function(){
		if($(this).prop('checked')){ resp = $(this).val(); }
	});
	$('#somaSOFA-trigger input[name=coag]').each(function(){
		if($(this).prop('checked')){ coag = $(this).val(); }
	});
	$('#somaSOFA-trigger input[name=hepa]').each(function(){
		if($(this).prop('checked')){ hepa = $(this).val(); }
	});
	$('#somaSOFA-trigger input[name=renal]').each(function(){
		if($(this).prop('checked')){ renal = $(this).val(); }
	});

	var sofa = parseInt(neuro) + parseInt(cardio) + parseInt(resp) + parseInt(coag) + parseInt(hepa) + parseInt(renal);
	return sofa; 
}


function somaICC(){
	var icc=0;
	$('#somaICC-trigger input[type=checkbox]').each(function(){
		icc = $(this).prop('checked') ? parseInt(icc)+parseInt($(this).val()) : icc;
	});
	return icc;
}


function calcEUP(){

	if(config.storage){
		var sofa 	= (getStorage('sofa') !== null) ? getStorage('sofa') : 0;
		var icc 	= (getStorage('icc') !== null) ? getStorage('icc') : 0;
		var ECOG 	= (getStorage('ECOG') !== null) ? getStorage('ECOG') : 0;
		var kps 	= (getStorage('kps') !== null) ? getStorage('kps') : 0;
	}else{
		var sofa 	= config.sofa;
		var icc 	= config.iccECOG.icc;
		var ECOG 	= config.iccECOG.ECOG;
		var kps 	= config.kps;
	}

	var eup_sofa = (sofa<6 & sofa>=0)  ? 1 : (sofa>=6 & sofa<=9) ? 2 : (sofa>=10 & sofa<=12) ? 3 : (sofa>12) ? 4 : 0;
	var eup_icc = (icc==1 & icc>=0) ? 1 : (icc==2) ? 2 : (icc>=3 & icc<=5) ?  3 : (icc>5) ? 4 : 0;
	var eup_ECOG = (ECOG<4 & ECOG>=0) ? 1 : (ECOG==4) ? 2 : (ECOG==5 | ECOG==6) ?  3 : (ECOG==7 | ECOG==8) ? 4 : 0;
	var eup_kps = (kps==0) ? 1 : kps;

	var iccECOG_maiorVal = (eup_icc > eup_ECOG ? eup_icc : eup_ECOG);
	var iccECOG_maiorName = (eup_icc > eup_ECOG ? 'ICC' : 'ECOG');
	//addStorage('iccECOGVal',iccECOG_maiorVal);
	//addStorage('iccECOGName',iccECOG_maiorName);
	//config.iccECOG.maiorVal = iccECOG_maiorVal;
	//config.iccECOG.maiorName = iccECOG_maiorName;
	//if(sofa){
		$('.view-result-sofa').html('('+sofa+' pontos SOFA)');
		$('.view-result-kps').html(eup_kps);
	//}
	//if(iccECOG_maiorVal){
		$('.view-result-iccECOG').html('('+(iccECOG_maiorName=='ICC'?icc:ECOG)+' pontos '+iccECOG_maiorName+')');
	//}
	$('.view-result-eup-sofa').html(eup_sofa);
	$('.view-result-eup-iccECOG').html(iccECOG_maiorVal);


	var eup = parseInt(eup_sofa) + parseInt(iccECOG_maiorVal) + parseInt(eup_kps);
	addStorage('eup',eup);
	config.eup = eup;

	$('.EUP-view').html(eup);
	
}


/*
 CLIQUE - CHECKBOX/RADIO
 */
 $('#somaSOFA-trigger .check-act').on('click',function(){
 	var sofa = somaSOFA();
 	$('.somaSOFA-view').html(sofa);

	addStorage('sofa',sofa);
	config.sofa = sofa;
	calcEUP();
});

$('#somaICC-trigger .check-act').on('click',function(){
 	var icc = somaICC();
 	$('.somaICC-view').html(icc);
 	
 	addStorage('icc', icc);
	config.iccECOG.icc = icc;
	calcEUP();
});

$('#serializeECOG input[type=radio]').on('click',function(){
 	var ECOG = $(this).val();
 	$('.serializeECOG-view').html(ECOG);

 	addStorage('ECOG',ECOG);
 	config.iccECOG.ECOG = ECOG;
	calcEUP();
});

$('#serializeKPS input[type=radio]').on('click',function(){
 	var kps = $(this).val();
 	$('.serializeKPS-view').html(kps);

 	addStorage('kps',kps);
 	config.kps = kps;
	calcEUP();
});
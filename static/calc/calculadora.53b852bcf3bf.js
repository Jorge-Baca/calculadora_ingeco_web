const input = document.getElementById('rspt');
const bar_button = document.getElementById("bar_button");
const list = document.getElementById('bar');
const factores = document.getElementById('factores');
const tipo_cambio = document.getElementById('tipo_cambio');
const bonos = document.getElementById('bonos');
const calendarios = document.getElementById('calendarios');
const f_factores = document.getElementById('f_factores').children;
const f_tipo_cambio = document.getElementById('f_tipo_cambio').children;
const f_bonos = document.getElementById('f_bonos').children;
const f_calendarios = document.getElementById('f_calendarios').children;
const functions_list = [f_factores, f_tipo_cambio, f_bonos, f_calendarios];
/*
input.addEventListener('keydown', (e) => {
    if(e.keyCode == 13){
        e.preventDefault();
        //input.value = eval(input.value);
		e.target.dispatchEvent('submit');
    }
});
*/

function inputSubmit(){
    input.submit;
}

input.addEventListener('keypress',(e)=>{
    if(e.keyCode == 13){
        e.target.submit;
    }
});

input.addEventListener('dblclick', (e) => {
        e.preventDefault();
        cad = input.value;

        if(cad.endsWith(']'))
            cad = cad.substring(1,cad.length-1);
        if(cad.endsWith(']'))
            while(1){
                if(!cad.includes('], ['))
                    break;
                cad = cad.replace('], [',']\n[');
            }
        alert(cad);
});

function quita(){
    x = input.value;
    x = x.toString();
    x = x.substring(0, x.length-1);
    input.value = x;

//    input.value /= 10;
//    input.value = Math.floor(input.value);
}

bar_button.addEventListener('click', (e) => {
    const form = document.getElementById("bar");
	e.preventDefault();
	change(form);
});

factores.addEventListener('click', (e) => {
	const form = document.getElementById("f_factores");
	e.preventDefault();

	change(form);
});

tipo_cambio.addEventListener('click', (e) => {
	const form = document.getElementById("f_tipo_cambio");
	e.preventDefault();

	change(form);
});

bonos.addEventListener('click', (e) => {
	const form = document.getElementById("f_bonos");
	e.preventDefault();

	change(form);
});

calendarios.addEventListener('click', (e) => {
	const form = document.getElementById("f_calendarios");
	e.preventDefault();

	change(form);
});

function change(form){
    let bool = form.style.display == 'none';

	if(bool)
		form.style.display = 'block';
	else
		form.style.display = 'none';
}


for(i = 0; i < functions_list.length; i++)
    for(j = 0; j < functions_list[i].length; j++)
        functions_list[i][j].addEventListener('click', (e) => {
            input.value += e.target.innerText + "(";
            const form = document.getElementById("bar");
        	change(form);
        });

function add(c){
    input.value += c;
}

function limpia(){
    input.value = '';
}

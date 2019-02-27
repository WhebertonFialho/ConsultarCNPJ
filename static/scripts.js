$(document).ready(function() {
    $('#btnConsultar').click(function(){
        consultarCNPJ();
    });
	
	$("#txtCNPJ").keypress(function (e) {
		if (e.which == 13) 
			consultarCNPJ();
	});
});


function consultarCNPJ(){
	var cnpj = $('#txtCNPJ').val();
	
	$('#txtCNPJ').val(cnpj);
	if(cnpj.length != 14)
	{
		alert("CNPJ deve ter 14 Digitos");
		return;
	}
	
	window.location.href = "/consultar_cnpj/" + cnpj
}
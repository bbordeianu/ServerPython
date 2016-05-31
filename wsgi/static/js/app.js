app = {
	
	inizializza: function() {
		this.init_bottone();
		this.init_bottone2();
	},
	
	init_bottone: function() {
		$("#bottone").on("click", function(){
			var miaMatricola = $("#matricola").val();
			var mioNome = $("#nome").val();
			var mioCognome = $("#cognome").val();
			var mioAnno = $("#anno").val();
			$.ajax({
				type: "POST",
				contentType: "application/json; charset=UTF-8",
				dataType: "json",
				url: "aggiungiStudente",
				crossdomain: true,
				data: JSON.stringify({matricola: miaMatricola, nome: mioNome , cognome: mioCognome, anno: mioAnno}),
				success: function(result) {
					$("#risultato").html("Studente aggiunto al registro!");
					$("#risultato").css("color","green");
				},
				error: function(){
					$("#risultato").html("Studente non aggiunto al registro!");
					$("#risultato").css("color","red");
				},
				
			});
		});
	},
	
	init_bottone2: function() {
		$("#bottone2").on("click",function(){
			var miaMatricola = $("#matricola2").val();
			$.ajax({
				type: "POST",
				contentType: "application/json; charset=UTF-8",
				dataType: "json",
				url: "ottieniStudente",
				crossdomain: true,
				data: JSON.stringify({matricola: miaMatricola}),
				success: function(result) {
					$("#risultato2").html("Studente letto correttamente!");
					$("#risultato2").css("color","green");
					$("#stampaNome").html(result.nome);
					$("#stampaCognome").html(result.cognome);
					$("#stampaAnno").html(result.anno);
				},
				error: function(){
					$("#risultato2").html("Studente non letto correttamente!");
					$("#risultato2").css("color","red");
				},
				
			});
			
		});
	}
};
$(document).ready(function() {
	app.inizializza();
});

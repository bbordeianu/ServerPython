/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var APP = {
    /*Returning jQuery Promise For a AJAX call with Product type*/
    // ...
    /*Handler For AJAX response*/
    // ...
    /*jQuery Template building with JSON data  from Server*/
    // ...
    /*Event Listener per il  tag h3 con id h3_1,
     * associa una funzione anonima alla gestione evento*/
    init_h3_1_Click: function () {
        $("#h3_1").on('click', function () {
            // copia il contenuto di h3_1 in h3_2
            // 
            // trova questo h3
            var contenuto = $("#h3_1").html();
            elementoSelezionato2 = $("#h3_2")
            elementoSelezionato2.html(contenuto);
        });
    },
    init_h3_2_Click: function () {
        elementoSelezionato = $("#h3_2")
        elementoSelezionato.on('click', function () {
            // copia il contenuto di h3_1 in h3_2
            // trova questo h3
            $("#h3_2").html("");
        });
    },
    //  associa event click su button leggiCampoText1
    init_leggiCampoText1_click: function () {
        elementoSelezionato = $('#leggiCampoText1');
        elementoSelezionato.on('click', function ()
        {
            /* copia dal campotesto */
            elementoSelezionato2 = $("#campoText1");
            contenuto = elementoSelezionato2.val();
            /* chiamata asincrona, non aspetta la fine */
            $.ajax(
                    {   method: "POST",
                        url :"/alunnoByNumeroReg/",
                        contentType: 'application/json',
                        crossDomain: true,   
                        type: "json",
                        data: JSON.stringify({"numeroReg": contenuto}),
                        dataType: "json",
                        success: function (data) {
                            contenuto = data.numeroReg + " " +
                            data.nome + " " +
                            data.cognome + " " +
                            data.annoNascita;
                            // oggetto arrivato json in data
                            elementoSelezionato = $("#campoText1-div");
                            elementoSelezionato.html(contenuto);
                        },
                        error: function (data) {
                            elementoSelezionato = $("#campoText1-div");
                            elementoSelezionato.html("errore");
                        }
               });



        });
    },
    init_leggiCampoText2_click: function (){
        button = $('#leggiCampoTextRegistrazione');
        button.on('click', function ()
        {
            /* copia dal campotesto */
            el1 = $("#campoTextNumReg");
            numeroReg = el1.val();
            
            el2 = $("#campoTextNome");
            nome = el2.val();
            
            el3 = $("#campoTextCognome");
            cognome = el3.val();
            
            el4 = $("#campoTextAnnoNascita");
            annoNascita = el4.val();
            /* chiamata asincrona, non aspetta la fine */
            $.ajax(
                    {   method: "POST",
                        url :"/insertAlunnoPOST/",
                        contentType: 'application/json',
                        crossDomain: true,   
                        type: "json",
                        data: JSON.stringify({"numeroReg": numeroReg, "nome": nome, "cognome": cognome, "annoNascita": annoNascita}),
                        dataType: "json",
                        success:  function(data){
                            alert("ok");
                        },
                        error: function(){
                            alert("errore");
                        }
               });



        });
        
    }
};


//  LISTENER che fa partire il programma,
//  si aspetta che il document sia pronto => tutti i .js .css ecc.  caricati

$(document).ready(function () {

    /*Initialize Click Of Menu Item*/
    APP.init_h3_1_Click();
    APP.init_h3_2_Click();
    APP.init_leggiCampoText1_click();
    APP.init_leggiCampoText2_click();
});


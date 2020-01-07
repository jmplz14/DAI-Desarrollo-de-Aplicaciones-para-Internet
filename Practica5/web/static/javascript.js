$(document).ready(function () {
    $("#ocultar").click(function () {
        var main = $("#contenido");
        $("#menuLateral").toggle(1000);

        if (main.hasClass("col-md-9")) {
            main.addClass("col-md-11");
            main.removeClass("col-md-9");
        } else {
            main.addClass("col-md-9");
            main.removeClass("col-md-11");
        }
        $(window).resize();
    });
    $("#cambiarTabla").click(function () {
        var tabla = $("#datos");

        if (tabla.hasClass("table-dark")) {
            tabla.removeClass("table-dark");
        } else {
            tabla.addClass("table-dark");
        }

    });


});
var numIndices = 3;
var tamTabla = 5;
var posPaginador = 2;


function ocultarElementos(pagina) {
    var tablaDatos = document.getElementById("tablaPaginada");
    var inicio = tamTabla * (pagina - 1);
    var final = inicio + tamTabla - 1
    var numeroElementos = tablaDatos.tBodies[0].rows.length;

    for (i = 0; i < numeroElementos; i++) {
        if (inicio <= i && i <= final) {
            tablaDatos.tBodies[0].rows[i].setAttribute("style", "display:compact")
        } else {
            tablaDatos.tBodies[0].rows[i].setAttribute("style", "display:none")
        }

    }

    tablaDatos.tBodies[0].rows[7].style.display = "compact";



}
function hola() {
    alert("holaaa")
}
function generarLista(pagina) {
    var tablaDatos = document.getElementById("tablaPaginada");
    var numeroElementos = tablaDatos.tBodies[0].rows.length;
    var tablaPaginar = document.getElementById("paginador");
    var campos = tablaPaginar.getElementsByTagName("td")
    var paginaMax = Math.trunc(numeroElementos / tamTabla) + 1;

    var inicio;
    if (pagina == 1) {
        inicio = 1;
    } else if (pagina == paginaMax) {
        inicio = pagina - 2;
        if (inicio == 0) {
            inicio = 1;
        }
    } else {
        inicio = pagina - 1;
    }

    for (i = 0; i < 3 && inicio + i <= paginaMax; i++) {

        campos[posPaginador + i].innerHTML = inicio + i;
        if (inicio + i == pagina) {
            campos[posPaginador + i].style.fontWeight = "bold";

        } else {
            campos[posPaginador + i].style.fontWeight = "normal";
        }

        campos[posPaginador + i].onclick = function () { generarLista(this.innerHTML); }

    }
    ocultarElementos(pagina)
}

function generarListaAjax(pagina) {

    jQuery.ajax({
        url: '/Discografica/obtener_pagina/' + pagina,
        type: 'get',
        dataType: 'json',
        success: function (data) {

            $.each(data, function (key, value) {
                if (key == "numElementos") {
                    total = value
                } else {
                    var cuerpoTabla = $("#tbody");
                    cuerpoTabla.empty()

                    const options = { year: 'numeric', month: 'long', day: 'numeric' };

                    datos = JSON.parse(value);

                    numDatos = datos.length;
                    for (i = 0; i < numDatos; i++) {
                        propiedades = datos[i].fields
                        columna = "<tr>"
                        columna += "<td>" + propiedades.nombre + "</td>"
                        var from = propiedades.fechaNacimiento.split("-")
                        var f = new Date(from[0], from[1] - 1, from[2])
                        columna += "<td>" + f.toLocaleDateString("es-ES", options) + "</td>"
                        columna += "<td>" + propiedades.instrumentoPrincipal + "</td>"
                        columna += "<td>" + propiedades.grupo + "</td>"
                        columna += "<td>" + propiedades.edad + "</td> </tr>"
                        $('#tbody').append(columna)
                    }
                }
            });

            var tablaPaginar = document.getElementById("paginadorAjax");
            var campos = tablaPaginar.getElementsByTagName("td")
            var paginaMax = Math.trunc(total / tamTabla) + 1;
            var inicio;

            if (pagina == 1) {
                inicio = 1;
            } else if (pagina == paginaMax) {
                inicio = pagina - 2;
                if (inicio == 0) {
                    inicio = 1;
                }
            } else {
                inicio = pagina - 1;
            }

            for (i = 0; i < 3 && inicio + i <= paginaMax; i++) {
                

                campos[posPaginador + i].innerHTML = inicio + i;
                if (inicio + i == pagina) {
                    campos[posPaginador + i].style.fontWeight = "bold";

                } else {
                    campos[posPaginador + i].style.fontWeight = "normal";
                }

                campos[posPaginador + i].onclick = function () { generarListaAjax(this.innerHTML); }

            }

        },
        failure: function (data) {
            alert('Got an error dude');
        }
    });






}

function generarUltimo() {
    var tablaDatos = document.getElementById("tablaPaginada");
    var numeroElementos = tablaDatos.tBodies[0].rows.length;
    var paginaMax = Math.trunc(numeroElementos / tamTabla) + 1;
    generarLista(paginaMax)
}

function generarSiguiente() {

    var tablaDatos = document.getElementById("tablaPaginada");
    var numeroElementos = tablaDatos.tBodies[0].rows.length;
    var tablaPaginar = document.getElementById("paginador");
    var campos = tablaPaginar.getElementsByTagName("td");
    var pagina;
    var numeroElementos = tablaDatos.tBodies[0].rows.length;
    var paginaMax = Math.trunc(numeroElementos / tamTabla) + 1;

    for (i = 0; i < numIndices; i++) {

        if (campos[posPaginador + i].style.fontWeight == "bold") {
            pagina = parseInt(campos[posPaginador + i].innerHTML) + 1;
        }

    }
    if (pagina <= paginaMax) {
        generarLista(pagina);
    }

}
function generarAnterior() {

    var tablaDatos = document.getElementById("tablaPaginada");
    var numeroElementos = tablaDatos.tBodies[0].rows.length;
    var tablaPaginar = document.getElementById("paginador");
    var campos = tablaPaginar.getElementsByTagName("td");
    var pagina;
    var numeroElementos = tablaDatos.tBodies[0].rows.length;
    var paginaMax = Math.trunc(numeroElementos / tamTabla) + 1;

    for (i = 0; i < numIndices; i++) {

        if (campos[posPaginador + i].style.fontWeight == "bold") {
            pagina = parseInt(campos[posPaginador + i].innerHTML) - 1;
        }

    }
    if (pagina >= 1) {
        generarLista(pagina);
    }

}

function generarSiguienteAjax() {


    var tablaDatos = document.getElementById("tablaPaginadaAjax");
    var numeroElementos = tablaDatos.tBodies[0].rows.length;
    var tablaPaginar = document.getElementById("paginadorAjax");
    var campos = tablaPaginar.getElementsByTagName("td");
    var pagina;
    var numeroElementos = tablaDatos.tBodies[0].rows.length;

    jQuery.ajax({
        url: '/Discografica/obtener_total/',
        type: 'get',
        dataType: 'json',
        success: function (data) {
            $.each(data, function (key, value) {
                total = value

            });

            var paginaMax = Math.trunc(total / tamTabla) + 1;
            for (i = 0; i < numIndices; i++) {

                if (campos[posPaginador + i].style.fontWeight == "bold") {
                    pagina = parseInt(campos[posPaginador + i].innerHTML) + 1;
                }

            }

            if (pagina <= paginaMax) {
                generarListaAjax(pagina);
            }





        },
        failure: function (data) {
            alert('Got an error dude');
        }
    });


}

function generarAnteriorAjax() {


    var tablaDatos = document.getElementById("tablaPaginadaAjax");
    var numeroElementos = tablaDatos.tBodies[0].rows.length;
    var tablaPaginar = document.getElementById("paginadorAjax");
    var campos = tablaPaginar.getElementsByTagName("td");
    var pagina;
    var numeroElementos = tablaDatos.tBodies[0].rows.length;

    jQuery.ajax({
        url: '/Discografica/obtener_total/',
        type: 'get',
        dataType: 'json',
        success: function (data) {
            $.each(data, function (key, value) {
                total = value

            });

            var paginaMax = Math.trunc(total / tamTabla) + 1;

            for (i = 0; i < numIndices; i++) {

                if (campos[posPaginador + i].style.fontWeight == "bold") {
                    pagina = parseInt(campos[posPaginador + i].innerHTML) - 1;
                }
            }
            if (pagina >= 1) {
                generarListaAjax(pagina);
            }



        },
        failure: function (data) {
            alert('Got an error dude');
        }
    });


}

function generarUltimoAjax() {
    var tablaDatos = document.getElementById("tablaPaginadaAjax");
    var numeroElementos = tablaDatos.tBodies[0].rows.length;
    jQuery.ajax({
        url: '/Discografica/obtener_total/',
        type: 'get',
        dataType: 'json',
        success: function (data) {
            $.each(data, function (key, value) {
                total = value

            });

            var paginaMax = Math.trunc(total / tamTabla) + 1;

            generarListaAjax(paginaMax)



        },
        failure: function (data) {
            alert('Got an error dude');
        }
    });

}


function iniciarPaginador() {

    if (document.getElementById("tablaPaginada")) {
        var tablaDatos = document.getElementById("tablaPaginada");
        var tablaPaginar = document.getElementById("paginador");
        var numeroElementos = tablaDatos.tBodies[0].rows.length;
        var row = tablaPaginar.insertRow(0);
        var principio = row.insertCell(0);
        var atras = row.insertCell(1);
        var indice1 = row.insertCell(2)
        var indice2 = row.insertCell(3)
        var indice3 = row.insertCell(4)
        var siguiente = row.insertCell(5);
        var final = row.insertCell(6);


        principio.innerHTML = "&lt&lt";
        final.innerHTML = "&gt&gt";
        siguiente.innerHTML = "&gt";
        atras.innerHTML = "&lt";
        principio.onclick = function () { generarLista(1); }
        final.onclick = function () { generarUltimo(); }
        siguiente.onclick = function () { generarSiguiente(); }
        atras.onclick = function () { generarAnterior(); }
        generarLista(1);
    }

}

function iniciarPaginadorAjax() {

    if (document.getElementById("paginadorAjax")) {
        var tablaDatos = document.getElementById("tablaPaginadaAjax");
        var tablaPaginar = document.getElementById("paginadorAjax");
        var numeroElementos = tablaDatos.tBodies[0].rows.length;
        var row = tablaPaginar.insertRow(0);
        var principio = row.insertCell(0);
        var atras = row.insertCell(1);
        var indice1 = row.insertCell(2)
        var indice2 = row.insertCell(3)
        var indice3 = row.insertCell(4)
        var siguiente = row.insertCell(5);
        var final = row.insertCell(6);


        principio.innerHTML = "&lt&lt";
        final.innerHTML = "&gt&gt";
        siguiente.innerHTML = "&gt";
        atras.innerHTML = "&lt";

        //paginas = {{ paginas }}
        jQuery.ajax({
            url: '/Discografica/obtener_total/',
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $.each(data, function (key, value) {
                    total = value

                });

                var paginaMax = Math.trunc(total / tamTabla) + 1;

                pos = 2;
                var paginas = []
                paginas.push(1)

                if (paginaMax >= 2){
                    paginas.push(2)
                }

                if (paginaMax >= 3){
                    paginas.push(3)
                }
                var campos = tablaPaginar.getElementsByTagName("td")
                for (x = 0; x < paginas.length; x++) {
                    campos[pos + x].innerHTML = paginas[x];
                }

                campos[pos].style.fontWeight = "bold"

                principio.onclick = function () { generarListaAjax(1); }
                siguiente.onclick = function () { generarSiguienteAjax(); }
                atras.onclick = function () { generarAnteriorAjax(); }
                final.onclick = function () { generarUltimoAjax(); }
                generarListaAjax(1) 
                

            },
            failure: function (data) {
                alert('Got an error dude');
            }
        });
    }





    /*generarLista(1);*/


}


window.onload = function () {

    iniciarPaginador();
    iniciarPaginadorAjax();



}
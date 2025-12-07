var tabla=document.getElementById("tablaLoca");
var cuerpo=document.getElementById("cuerpo");

tabla.addEventListener("mouseenter", function( event ) {
	console.log("entre a la tabla");
	cabecera.classList.add("desacomodar_cabecera");
	cuerpo.classList.add("desacomodar");
});

tabla.addEventListener("mouseleave", function( event ) {
	console.log("sali de la tabla");
	cuerpo.classList.remove("desacomodar");
});
addEventListener("load", (event) => {

});



const toggle=document.querySelector(".toggle");
const barraPlegable=document.querySelector(".barraPlegable");
const contenido=document.querySelector(".contenedorContenidoPrincipal");


toggle.onclick = function(){
    barraPlegable.classList.toggle("activa");
    contenido.classList.toggle("activa");
}









const list=document.querySelectorAll(".lista");

function activeList(){
    list.forEach(
        (item) => item.classList.remove("activo")
    );
    this.classList.add("activo");
}



list.forEach(
    (item) => item.addEventListener("mouseenter",activeList)
);

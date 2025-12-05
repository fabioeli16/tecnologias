addEventListener("load", (event) => {

});



const toggle=document.querySelector(".toggle");
const barraPlegable=document.querySelector(".barraPlegable");
const contenido=document.querySelector(".contenedorContenidoPrincipal");
const list=document.querySelectorAll(".lista");


function eventoToggle(){
    barraPlegable.classList.toggle("activa");
    contenido.classList.toggle("activa");

}



function activeList(){
    list.forEach(
        (item) => item.classList.remove("activa")
    );
    this.classList.add("activa");
    if (!barraPlegable.classList.contains('activa')) {
        barraPlegable.classList.add('activa');
        contenido.classList.remove('activa');
    }
    
}


toggle.onclick = eventoToggle;
list.forEach(
    (item) => item.addEventListener("click",activeList)
);

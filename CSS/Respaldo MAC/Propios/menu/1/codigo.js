const contenedor = document.getElementById('contenedorTabla');
const encabezado = document.querySelector('thead');
const menu = document.getElementById('menu');

document.addEventListener("DOMContentLoaded",()=>{



	encabezado.addEventListener("click",(e)=>{
		e.preventDefault();
		e.stopPropagation();
		const rect = contenedor.getBoundingClientRect();
	    const x = e.clientX - rect.left;
	            const y = e.clientY - rect.top;

	    menu.style.top = `${y}px`;
	    menu.style.left = `${x}px`;
	   	menu.classList.toggle('contenedor-menu-oculto');	
	  	document.addEventListener('click', manejadorDocumento);

	});



});




		
const manejadorDocumento = function (e) {
    const isClickedOutside = !menu.contains(e.target);
    if (isClickedOutside) {
        menu.classList.add('contenedor-menu-oculto');
        document.removeEventListener('click', manejadorDocumento);
    }

 };
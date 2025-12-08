const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");
const menuBtnIcon = menuBtn.querySelector("i");

menuBtn.addEventListener("click",()=>{
    navLinks.classList.toggle("open");
    const isOpen = navLinks.classList.contains("open");
    const classmenuBtnIcon = isOpen? "ri-close-line": "ri-menu-4-line";
    menuBtnIcon.setAttribute("class",classmenuBtnIcon);
});

navLinks.addEventListener("click", () => {
  navLinks.classList.remove("open");
  menuBtnIcon.setAttribute("class", "ri-menu-4-line");
});
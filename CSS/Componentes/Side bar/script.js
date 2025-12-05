const body=document.querySelector("body");
const sidebar=document.querySelector(".sidebar");
const modeSwitch=document.querySelector(".toggle-switch");
const toggle=document.querySelector(".toggle");
const search=document.querySelector(".search-box");
const modeText=document.querySelector(".mode-text");

modeSwitch.addEventListener("click",()=>{
    body.classList.toggle("dark");
})


toggle.addEventListener("click",()=>{

    sidebar.classList.toggle("close");
})
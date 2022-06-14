const nav = document.querySelector(".nav");

window.addEventListener("scroll", fixNav);

function fixNav() {
    if(window.scrollY > nav.offsetHeight - 50) {
        nav.classList.add("active");
    } else {
        nav.classList.remove("active");
    }
}


const numb = document.querySelector(".number");
let counter = 0;
setInterval(() => {
  if(counter == 100 ){
    clearInterval();
  }else{
    counter+=1;
    numb.textContent = counter + "%";
  }
}, 80);
const header = document.querySelector("header");
const div = document.querySelector("div");

function changeColor() {
  header.classList.add("red");
}

div.addEventListener("click", changeColor);

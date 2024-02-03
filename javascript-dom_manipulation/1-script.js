const header = document.querySelector("header");
const div = document.querySelector("div");

function changeColor() {
  header.style.color = "red";
}

div.addEventListener("click", changeColor);

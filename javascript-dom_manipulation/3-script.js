const toggleHeader = document.querySelector("#toggle_header");
const header = document.querySelector("header");

function changeColor() {
  header.classList.toggle("red");
  header.classList.toggle("green");
}

toggleHeader.addEventListener("click", changeColor);

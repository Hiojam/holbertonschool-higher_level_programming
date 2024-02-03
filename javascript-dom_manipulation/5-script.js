const update = document.querySelector("#update_header");
const header = document.querySelector("header");

function changeText() {
  header.textContent = "New Header!!!";
}

update.addEventListener("click", changeText);

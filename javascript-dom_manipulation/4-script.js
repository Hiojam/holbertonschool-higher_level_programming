const addItem = document.getElementById("add_item");
const list = document.querySelector(".my_list");

function addItemFunction() {
  const liElement = document.createElement("li");
  liElement.textContent = "Item";
  list.appendChild(liElement);
}

addItem.addEventListener("click", addItemFunction);

function handleResponse(response) {
  if (!response.ok) {
    console.log("network response was not ok");
  } else {
    return response.json();
  }
}

function translate(respose_data) {
  const helloElement = document.querySelector("#hello");
  const textElement = document.createElement("p");
  textElement.textContent = respose_data.hello;

  helloElement.appendChild(textElement);
}

function handleError(error) {
  console.log(error);
}

const urlPromise = fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
urlPromise.then(handleResponse).then(translate).catch(handleError);

function handleResponse(response) {
  if (!response.ok) {
    console.log("network response was not ok");
  } else {
    return response.json();
  }
}

function appendTitle(respose_data) {
  const listMovies = document.querySelector("#list_movies");
  const movies = respose_data.results;

  movies.forEach(element => {
    let item = document.createElement("li");
    item.textContent = element.title;

    listMovies.appendChild(item);
  });
}

function handleError(error) {
  console.log(error);
}

const urlPromise = fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
urlPromise.then(handleResponse).then(appendTitle).catch(handleError);

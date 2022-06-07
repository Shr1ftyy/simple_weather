resultsDiv = document.getElementById("results-div")
searchInput = document.getElementById("search-input")

// Execute a function when the user presses a key on the keyboard
searchInput.addEventListener("keypress", function(event) {
  // If the user presses the "Enter" key on the keyboard
  if (event.key === "Enter") {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("submit-button").click();
  }
});

function startSearch() {
  searchText = searchInput.value
  console.log(searchText)
  fetch("/getData", {
    method: "POST",
    headers: {
      "Content-Type": "applications/json"
    },
    body: searchText
  })
  .then(resp => {
    console.log(resp)
    if (resp.ok)
      resp.json().then(data =>  {
        data = JSON.stringify(data, undefined, 2)
        console.log(data)
        showResult(data);
      })
  });
}

function showResult(data){
  resultsDiv.innerHTML = data
}
let movieList = [];

fetch('/movies')
    .then(response => response.json())
    .then(data => movieList = data);

function showSuggestions() {
    let input = document.getElementById("movieInput").value.toLowerCase();
    let suggestionsBox = document.getElementById("suggestions");

    suggestionsBox.innerHTML = "";

    if (input.length === 0) return;

    let filtered = movieList.filter(movie => movie.toLowerCase().includes(input));

    filtered.slice(0, 5).forEach(movie => {
        let div = document.createElement("div");
        div.innerHTML = movie;

        div.onclick = function () {
            document.getElementById("movieInput").value = movie;
            suggestionsBox.innerHTML = "";
        };

        suggestionsBox.appendChild(div);
    });
}

function openMovie(title) {
    window.open(`https://www.google.com/search?q=${title}+movie`, '_blank');
}
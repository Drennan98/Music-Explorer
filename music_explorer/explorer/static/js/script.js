const searchInput = document.getElementById("search");
const resultsDiv = document.getElementById("results");

let timeout;

searchInput.addEventListener("input", () => {

    clearTimeout(timeout);

    timeout = setTimeout(() => {
        searchMusic(searchInput.value);
    }, 300);
});

async function searchMusic(query) {

    if (!query.trim()) {
        resultsDiv.innerHTML = "";
        return;
    }

    const response = await fetch(
        `/search/?q=${query}`
    );

    const data = await response.json();

    renderResults(data);
}

function renderResults(data) {

    let html = "";

    html += `
        <h2>Artists</h2>
    `;

    data.artists.forEach(artist => {
        html += `
            <div class="card">
                <h3>${artist.name}</h3>
                <p>${artist.album_count} albums</p>
            </div>
        `;
    });

    html += `
        <h2>Albums</h2>
    `;

    data.albums.forEach(album => {
        html += `
            <div class="card">
                <h3>${album.title}</h3>
                <p>${album.artist}</p>
            </div>
        `;
    });

    html += `
        <h2>Songs</h2>
    `;

    data.songs.forEach(song => {
        html += `
            <div class="card">
                <h3>${song.title}</h3>
                <p>${song.artist}</p>
                <small>${song.length}</small>
            </div>
        `;
    });

    resultsDiv.innerHTML = html;
}
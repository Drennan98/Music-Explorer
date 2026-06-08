// Get the search box from the page. 
const searchInput = document.getElementById("search");

// Get the area where search results will be displayed. 
const resultsDiv = document.getElementById("results");

// Used to prevent lots of searches being while the user is typing. 
let timeout;

// Run code when the user types in the search box. 
searchInput.addEventListener("input", () => {

    // Cancel any previous search timer. 
    clearTimeout(timeout);

    // Wait 300 milliseconds after the user stops typing. 
    timeout = setTimeout(() => {
        // Search for what the user typed. 
        searchMusic(searchInput.value);
    }, 300);
});

// Search the given music data. 
async function searchMusic(query) {

    // If the search box is empty, clear the results.
    if (!query.trim()) {
        resultsDiv.innerHTML = "";
        return;
    }

    // Send the result to the Django backend. 
    const response = await fetch(
        `/search/?q=${query}`
    );

    // Convert the JSON response into JavaScript. 
    const data = await response.json();

    // Display the results on the page 
    renderResults(data);
}

// Display artists, albums and songs on the page. 
function renderResults(data) {

    let html = "";

    // This creates the Artists section heading. 
    html += `
        <h2>Artists</h2>
    `;

    // Display matching artists. 
    data.artists.forEach(artist => {
        html += `
            <div class="card">
                <h3>${artist.name}</h3>
                <p>${artist.album_count} albums</p>
            </div>
        `;
    });

    // Create album section heading.
    html += `
        <h2>Albums</h2>
    `;
 
    // Display matching albums.
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

    // Create songs section heading. 
    data.songs.forEach(song => {
        html += `
            <div class="card">
                <h3>${song.title}</h3>
                <p>${song.artist}</p>
                <small>${song.length}</small>
            </div>
        `;
    });

    // Add all generated HTML to the page.
    resultsDiv.innerHTML = html;
}
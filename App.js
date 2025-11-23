function searchItem() {
    const query = document.getElementById("searchGrocery").value;

    // mock result
    const resultHTML = `
        <h2>Results for: <strong>${query}</strong></h2>
        <p>(Your store prices appear here.)</p>
    `;

    document.getElementById("results").innerHTML = resultHTML;

    // placeholders for prices and images (optional)
}

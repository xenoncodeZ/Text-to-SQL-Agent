document.getElementById("agent-form").addEventListener("submit", async function(event) {
    // 1. Stop the browser from refreshing the page
    event.preventDefault(); 

    // 2. Grab the UI elements
    const submitBtn = document.getElementById("submit-btn");
    const loadingIndicator = document.getElementById("loading");
    const resultsContainer = document.getElementById("results-container");

    // 3. Grab the data from the inputs
    const apiKey = document.getElementById("apiKey").value;
    const fileInput = document.getElementById("dbFile").files[0];
    const question = document.getElementById("question").value;

    // 4. Update the UI to show it is loading
    resultsContainer.innerHTML = "";
    loadingIndicator.classList.remove("hidden");
    submitBtn.disabled = true;
    submitBtn.textContent = "Processing...";

    // 5. Package the data for FastAPI
    const formData = new FormData();
    formData.append("api_key", apiKey);
    formData.append("db_file", fileInput);
    formData.append("question", question);

    try {
        // 6. Send the POST request to your Python server
        const response = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",
            body: formData
        });

        // Parse the JSON response back from Python
        const result = await response.json();

        // 7. Display the result
        if (result.status === "success") {
            renderTable(result.data, resultsContainer);
        } else {
            resultsContainer.innerHTML = `<p style="color: #e74c3c; font-weight: bold;">Error: ${result.message}</p>`;
        }
    } catch (error) {
        resultsContainer.innerHTML = `<p style="color: #e74c3c; font-weight: bold;">Network Error: Make sure your FastAPI server is running in the terminal!</p>`;
    } finally {
        // 8. Restore the UI back to normal
        loadingIndicator.classList.add("hidden");
        submitBtn.disabled = false;
        submitBtn.textContent = "Run Query";
    }
});

// --- Helper Function to Build the HTML Table ---
function renderTable(data, container) {
    if (!data || data.length === 0) {
        container.innerHTML = "<p>No results found for that query.</p>";
        return;
    }

    const table = document.createElement("table");
    const thead = document.createElement("thead");
    const tbody = document.createElement("tbody");

    // Extract the column names from the first row of data
    const keys = Object.keys(data[0]);
    const headerRow = document.createElement("tr");
    
    keys.forEach(key => {
        const th = document.createElement("th");
        th.textContent = key;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);

    // Loop through the data and create rows
    data.forEach(row => {
        const tr = document.createElement("tr");
        keys.forEach(key => {
            const td = document.createElement("td");
            td.textContent = row[key];
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });

    table.appendChild(thead);
    table.appendChild(tbody);
    container.appendChild(table);
}
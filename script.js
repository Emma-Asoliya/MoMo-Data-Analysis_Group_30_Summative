let allData = [];
let chartInstance = null;

async function loadData() {
    const category = document.getElementById("category").value;
    const tableBody = document.getElementById("data-table");
    const loader = document.getElementById("loader");
    tableBody.innerHTML = "";
    allData = [];
    loader.style.display = "block";

    try {
        // Fetch data from the Flask API instead of static files
        const response = await fetch(`http://127.0.0.1:5000/transactions?category=${category}`);
        const data = await response.json();
        allData = data;
        applyFilters();
    } catch (error) {
        console.error("Error loading data:", error);
    } finally {
        loader.style.display = "none";
    }
}

function applyFilters() {
    const startDate = document.getElementById("start-date").value;
    const endDate = document.getElementById("end-date").value;
    const searchText = document.getElementById("search").value.toLowerCase();
    const tableBody = document.getElementById("data-table");
    const tableHeader = document.querySelector("table thead");
    tableBody.innerHTML = "";
    tableHeader.innerHTML = ""; // Clear previous headers

    let filteredData = allData.filter(entry => {
        if (startDate && entry.transaction_date < startDate) return false;
        if (endDate && entry.transaction_date > endDate) return false;
        if (searchText && !JSON.stringify(entry).toLowerCase().includes(searchText)) return false;
        return true;
    });

    let totalAmount = 0;

    // Define table headers dynamically
    let headerRow = `<tr>
                        <th>Date</th>
                        <th>Time</th>
                        <th>Amount</th>`;

    if (category === 'incoming_money') {
        headerRow += `<th>Sender</th>`;
    } else if (category === 'payment_to_code') {
        headerRow += `<th>Code</th><th>Receiver</th>`;
    } else if (category === 'third_party_transactions') {
        headerRow += `<th>Transaction Type</th>`;
    } else if (category === 'transfer_to_number') {
        headerRow += `<th>Receiver</th><th>Phone Number</th>`;
    }

    headerRow += `</tr>`;
    tableHeader.innerHTML = headerRow;

    filteredData.forEach(entry => {
        totalAmount += parseFloat(entry.amount);

        let row = `<tr>
                        <td>${entry.transaction_date}</td>
                        <td>${formatTime(entry.transaction_time)}</td>
                        <td>${entry.amount.toLocaleString()} RWF</td>`;

        if (category === 'incoming_money') {
            row += `<td>${entry.sender || "N/A"}</td>`;
        } else if (category === 'payment_to_code') {
            row += `<td>${entry.code || "N/A"}</td><td>${entry.receiver || "N/A"}</td>`;
        } else if (category === 'third_party_transactions') {
            row += `<td>${entry.transaction_type || "N/A"}</td>`;
        } else if (category === 'transfer_to_number') {
            row += `<td>${entry.receiver || "N/A"}</td><td>${entry.phone_number || "N/A"}</td>`;
        }

        row += `</tr>`;
        tableBody.innerHTML += row;
    });

    document.getElementById("total-messages").textContent = filteredData.length;
    document.getElementById("total-amount").textContent = totalAmount.toLocaleString();
    updateChart(filteredData);
}

// Convert time in seconds to HH:MM:SS format
function formatTime(seconds) {
    let date = new Date(0);
    date.setSeconds(seconds);
    return date.toISOString().substr(11, 8);
}

// Update chart dynamically
function updateChart(filteredData) {
    const ctx = document.getElementById("chart").getContext("2d");
    const transactionsByMonth = {};

    filteredData.forEach(entry => {
        const month = entry.transaction_date.substring(0, 7); // Get YYYY-MM format
        transactionsByMonth[month] = (transactionsByMonth[month] || 0) + parseFloat(entry.amount);
    });

    const labels = Object.keys(transactionsByMonth).sort();
    const data = labels.map(month => transactionsByMonth[month]);

    if (chartInstance) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {
        type: "bar",
        data: {
            labels,
            datasets: [{
                label: "Transaction Volume",
                data,
                backgroundColor: "#ffcc00",
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Month'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Total Amount'
                    }
                }
            }
        }
    });
}

// Load data when the page loads
loadData();

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
        const response = await fetch(`Categorised_Data/Cleaned_Data/${category}`);
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
        if (startDate && entry.Date < startDate) return false;
        if (endDate && entry.Date > endDate) return false;
        if (searchText && !JSON.stringify(entry).toLowerCase().includes(searchText)) return false;
        return true;
    });

    let totalAmount = 0;
    const category = document.getElementById("category").value;

    // Define the header dynamically based on category
    let headerRow = `<tr>
                        <th>Date</th>
                        <th>Time</th>
                        <th>Amount</th>`;

    if (category === 'cleaned_incoming_money.json') {
        headerRow += `<th>Sender</th>`;
    } else if (category === 'cleaned_payment_to_code.json') {
        headerRow += `<th>Code</th>
                      <th>Receiver</th>`;
    } else if (category === 'cleaned_third_party_transactions.json') {
        headerRow += `<th>Transaction Type</th>`;
    } else if (category === 'cleaned_transfer_to_number.json') {
        headerRow += `<th>Receiver</th>
                      <th>Phone Number</th>`;
    }

    headerRow += `</tr>`;
    tableHeader.innerHTML = headerRow; // Insert the header

    filteredData.forEach(entry => {
        totalAmount += entry.amount;

        // Define table row dynamically based on category
        let row = `<tr>
                        <td>${entry.Date}</td>
                        <td>${entry.Time || "N/A"}</td>
                        <td>${entry.amount.toLocaleString()} RWF</td>`;

        if (category === 'cleaned_incoming_money.json') {
            row += `<td>${entry.sender || "N/A"}</td>`;
        } else if (category === 'cleaned_payment_to_code.json') {
            row += `<td>${entry.code || "N/A"}</td>
                    <td>${entry.receiver || "N/A"}</td>`;
        } else if (category === 'cleaned_third_party_transactions.json') {
            row += `<td>${entry.transaction_type || "N/A"}</td>`;
        } else if (category === 'cleaned_transfer_to_number.json') {
            row += `<td>${entry.receiver || "N/A"}</td>
                    <td>${entry.phone_number || "N/A"}</td>`;
        }

        row += `</tr>`;
        tableBody.innerHTML += row;
    });

    document.getElementById("total-messages").textContent = filteredData.length;
    document.getElementById("total-amount").textContent = totalAmount.toLocaleString();
    updateChart(filteredData);
}



function updateChart(filteredData) {
    const ctx = document.getElementById("chart").getContext("2d");
    const transactionsByMonth = {};

    filteredData.forEach(entry => {
        const month = entry.Date.substring(0, 7); // Get YYYY-MM format
        transactionsByMonth[month] = (transactionsByMonth[month] || 0) + entry.amount;
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
                        text: 'Total' // Label for X-axis
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Month' // Label for Y-axis
                    }
                }
            }
        }
    });
}


loadData();

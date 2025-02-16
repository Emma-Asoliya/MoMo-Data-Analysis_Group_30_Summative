// script.js

const transactions = [
    { id: 123456, type: "Incoming Money", amount: 5000, date: "2024-01-01", details: "Received from John Doe" },
    { id: 789012, type: "Payments to Code Holders", amount: 1500, date: "2024-01-02", details: "Payment to Jane Smith" },
    { id: 345678, type: "Airtime Bill Payments", amount: 3000, date: "2024-01-03", details: "Airtime payment" },
    { id: 456789, type: "Withdrawals from Agents", amount: 20000, date: "2024-01-04", details: "Withdrawn via Jane Doe" },
    { id: 567890, type: "Internet and Voice Bundle Purchases", amount: 2000, date: "2024-01-05", details: "Purchased 1GB internet bundle" },
    // Add more sample transactions as needed
];

function displayTransactions(filteredTransactions) {
    const tbody = document.getElementById("transactions").getElementsByTagName('tbody')[0];
    tbody.innerHTML = ''; // Clear current table

    filteredTransactions.forEach(transaction => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${transaction.id}</td>
            <td>${transaction.type}</td>
            <td>${transaction.amount} RWF</td>
            <td>${transaction.date}</td>
            <td><button onclick="viewDetails(${transaction.id})">View</button></td>
        `;
        tbody.appendChild(row);
    });
}

function filterTransactions() {
    const type = document.getElementById('search-type').value.toLowerCase();
    const amount = document.getElementById('search-amount').value;
    const date = document.getElementById('search-date').value;

    const filteredTransactions = transactions.filter(transaction => {
        const matchType = type ? transaction.type.toLowerCase().includes(type) : true;
        const matchAmount = amount ? transaction.amount === parseInt(amount) : true;
        const matchDate = date ? transaction.date === date : true;

        return matchType && matchAmount && matchDate;
    });

    displayTransactions(filteredTransactions);
}

function viewDetails(id) {
    const transaction = transactions.find(t => t.id === id);
    alert(`Details for Transaction ID ${id}: ${transaction.details}`);
}

// Initially display all transactions
displayTransactions(transactions);

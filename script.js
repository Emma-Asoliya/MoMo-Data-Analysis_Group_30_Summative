let allData = [];

        async function loadData() {
            const category = document.getElementById("category").value;
            const tableBody = document.getElementById("data-table");
            const loader = document.getElementById("loader");
            tableBody.innerHTML = "";
            allData = []; // Reset stored data

            loader.style.display = "block"; // Show loader

            try {
                const response = await fetch(`Categorised_Data/Cleaned_Data/${category}`);
                const data = await response.json();
                allData = data; // Store data for filtering
                applyFilters(); // Apply filters after loading data
            } catch (error) {
                console.error("Error loading data:", error);
            } finally {
                loader.style.display = "none"; // Hide loader when done
            }
        }

        function applyFilters() {
            const startDate = document.getElementById("start-date").value;
            const endDate = document.getElementById("end-date").value;
            const tableBody = document.getElementById("data-table");
            tableBody.innerHTML = "";

            let filteredData = allData.filter(entry => {
                if (startDate && entry.Date < startDate) return false;
                if (endDate && entry.Date > endDate) return false;
                return true;
            });

            let totalAmount = 0;
            filteredData.forEach(entry => {
                const message = `On ${entry.Date} at ${entry.Time}, a transaction of ${entry.amount} ${entry.currency} occurred (${entry.transaction_type}).`;
                totalAmount += entry.amount;

                const row = `<tr>
                                <td>${document.getElementById("category").value.replace("cleaned_", "").replace(".json", "").replace(/_/g, " ")}</td>
                                <td>${message}</td>
                            </tr>`;
                tableBody.innerHTML += row;
            });

            // Update totals
            document.getElementById("total-messages").textContent = filteredData.length;
            document.getElementById("total-amount").textContent = totalAmount.toLocaleString();
        }

        loadData(); // Load initial data on page load

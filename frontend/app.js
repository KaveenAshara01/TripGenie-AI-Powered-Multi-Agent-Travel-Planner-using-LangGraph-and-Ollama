async function planTrip() {
    const input = document.getElementById('userRequest').value;
    if (!input.trim()) {
        alert("Please enter a travel request!");
        return;
    }

    const btn = document.getElementById('planBtn');
    const loader = document.getElementById('loader');
    const results = document.getElementById('results');

    // UI Updates
    btn.disabled = true;
    loader.classList.remove('hidden');
    results.classList.add('hidden');

    try {
        const response = await fetch('/api/plan-trip', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_request: input })
        });

        const data = await response.json();

        if (data.status === 'success') {
            // Update Summary Cards (Handled by Student 1's Agent)
            document.getElementById('resDestination').innerText = data.destination || 'N/A';
            document.getElementById('resDays').innerText = data.days ? `${data.days} Days` : 'N/A';
            document.getElementById('resTravelers').innerText = data.travelers ? `${data.travelers} Pax` : 'N/A';
            document.getElementById('resBudget').innerText = data.budget_type || 'N/A';
            
            // Update final itinerary
            document.getElementById('resItinerary').innerText = data.itinerary || 'No itinerary generated.';
            
            // Reveal Results
            results.classList.remove('hidden');
        } else {
            alert("Error generating trip: " + data.message);
        }
    } catch (err) {
        alert("Failed to connect to the backend server. Is it running?");
    } finally {
        btn.disabled = false;
        loader.classList.add('hidden');
    }
}

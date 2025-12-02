// Handle track form submission
document.getElementById('trackForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);
    const response = await fetch('/add_data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (response.ok) {
        alert('Data submitted successfully!');
        e.target.reset();
    } else {
        alert('Error submitting data.');
    }
});

// Load and display chart on dashboard
if (window.location.pathname === '/dashboard') {
    const userId = new URLSearchParams(window.location.search).get('user_id');
    if (userId) {
        fetch(`/api/data/${userId}`)
            .then(res => res.json())
            .then(data => {
                const ctx = document.getElementById('healthChart').getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: data.map(d => d.date.split('T')[0]),
                        datasets: [
                            { label: 'Steps', data: data.map(d => d.steps || 0), borderColor: 'blue' },
                            { label: 'Heart Rate', data: data.map(d => d.heart_rate || 0), borderColor: 'red' },
                            { label: 'Oxygen Level', data: data.map(d => d.oxygen_level || 0), borderColor: 'green' }
                        ]
                    }
                });
            });
    }
}
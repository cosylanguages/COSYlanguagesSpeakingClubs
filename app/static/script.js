document.addEventListener('DOMContentLoaded', () => {
    const languageSelect = document.getElementById('language');
    const levelSelect = document.getElementById('level');
    const clubListContainer = document.querySelector('.club-list-container'); // Assuming a container div

    function updateClubs() {
        const language = languageSelect.value;
        const level = levelSelect.value;

        let apiUrl = '/api/clubs?';
        if (language) {
            apiUrl += `language=${language}&`;
        }
        if (level) {
            apiUrl += `level=${level}`;
        }

        fetch(apiUrl)
            .then(response => response.json())
            .then(clubs => {
                let newHtml = '';
                if (clubs.length > 0) {
                    newHtml += '<ul class="club-list">';
                    clubs.forEach(club => {
                        let summary = '';
                        if (club.name === "The Greatest Quotes") {
                            summary = `${club.quote.substring(0, 100)}...`;
                        } else if (club.name === "Keeping Up With Science") {
                            summary = `${club.summary.substring(0, 100)}...`;
                        } else if (club.name === "Let's Celebrate" || club.name === "Let's Celebrate: Science Edition") {
                            summary = `A day to celebrate ${club.holiday_name}.`;
                        }

                        newHtml += `
                            <li>
                                <h3><a href="/club/${club.key}">${club.name}</a></h3>
                                <p>${summary}</p>
                            </li>
                        `;
                    });
                    newHtml += '</ul>';
                } else {
                    newHtml = '<p>No clubs found for the selected filters.</p>';
                }
                clubListContainer.innerHTML = newHtml;
            })
            .catch(error => {
                console.error('Error fetching clubs:', error);
                clubListContainer.innerHTML = '<p>Error loading clubs. Please try again later.</p>';
            });
    }

    languageSelect.addEventListener('change', updateClubs);
    levelSelect.addEventListener('change', updateClubs);
});

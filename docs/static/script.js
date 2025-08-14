document.addEventListener('DOMContentLoaded', () => {
    const languageSelect = document.getElementById('language');
    const levelSelect = document.getElementById('level');
    const clubListContainer = document.querySelector('.club-list-container');

    function updateClubs() {
        const selectedLanguage = languageSelect.value;
        const selectedLevel = levelSelect.value;

        fetch('data.json')
            .then(response => response.json())
            .then(allClubs => {
                let filteredClubs = allClubs;

                if (selectedLanguage) {
                    filteredClubs = filteredClubs.filter(club => club.language === selectedLanguage);
                }
                if (selectedLevel) {
                    filteredClubs = filteredClubs.filter(club => club.level === selectedLevel);
                }

                let newHtml = '';
                if (filteredClubs.length > 0) {
                    newHtml += '<ul class="club-list">';
                    filteredClubs.forEach(club => {
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
                                <h3><a href="club/${club.key}.html">${club.name}</a></h3>
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

    // Initial load
    updateClubs();
});

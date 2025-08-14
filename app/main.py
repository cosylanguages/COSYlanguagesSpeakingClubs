from flask import Flask, render_template, request, abort, jsonify
from data import greatest_quotes_club, science_club, lets_celebrate_club, science_celebration_club

app = Flask(__name__)

# A dictionary of all the clubs, with a unique key for each
all_clubs = {
    "quotes": greatest_quotes_club,
    "science": science_club,
    "celebrate": lets_celebrate_club,
    "science_celebration": science_celebration_club,
}
# Add the key to each club dictionary so we can use it in the template
for key, club in all_clubs.items():
    club['key'] = key

@app.route('/')
def index():
    selected_language = request.args.get('language')
    selected_level = request.args.get('level')

    filtered_clubs = list(all_clubs.values())

    if selected_language:
        filtered_clubs = [club for club in filtered_clubs if club['language'] == selected_language]

    if selected_level:
        filtered_clubs = [club for club in filtered_clubs if club['level'] == selected_level]

    return render_template(
        'home.html',
        clubs=filtered_clubs,
        selected_language=selected_language,
        selected_level=selected_level
    )

@app.route('/club/<string:club_key>')
def club_detail(club_key):
    club = all_clubs.get(club_key)
    if not club:
        abort(404)
    return render_template('club_detail.html', club=club)

@app.route('/api/clubs')
def api_clubs():
    selected_language = request.args.get('language')
    selected_level = request.args.get('level')

    filtered_clubs = list(all_clubs.values())

    if selected_language:
        filtered_clubs = [club for club in filtered_clubs if club['language'] == selected_language]

    if selected_level:
        filtered_clubs = [club for club in filtered_clubs if club['level'] == selected_level]

    return jsonify(filtered_clubs)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

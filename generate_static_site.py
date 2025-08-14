import os
import shutil
import json
from flask import url_for
from app.main import app, all_clubs

# The directory to build the static site in
BUILD_DIR = 'build'

def generate_static_site():
    """Generates a static version of the website."""
    # Create the build directory, or clear it if it exists
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR)

    # Copy the static files
    shutil.copytree('app/static', os.path.join(BUILD_DIR, 'static'))

    # Create the club directory
    club_dir = os.path.join(BUILD_DIR, 'club')
    os.makedirs(club_dir)

    # Generate the data.json file
    with open(os.path.join(BUILD_DIR, 'data.json'), 'w') as f:
        json.dump(list(all_clubs.values()), f, indent=4)

    with app.test_request_context():
        # Generate the homepage
        # We need to render the template directly, not through a test client
        # because the test client will not have the correct context for url_for
        from flask import render_template
        home_html = render_template('home.html', clubs=list(all_clubs.values()))
        home_html = home_html.replace('href="/club/', 'href="club/')
        home_html = home_html.replace('href="/static/', 'href="static/')
        with open(os.path.join(BUILD_DIR, 'index.html'), 'w') as f:
            f.write(home_html)

        # Generate the club detail pages
        for key, club in all_clubs.items():
            club_html = render_template('club_detail.html', club=club)

            # Make links relative for static site
            club_html = club_html.replace('href="/static/', 'href="../static/')
            club_html = club_html.replace('href="/"', 'href="../index.html"')

            with open(os.path.join(club_dir, f'{key}.html'), 'w') as f:
                f.write(club_html)

    print("Static site generated successfully in 'build' directory.")

if __name__ == '__main__':
    generate_static_site()

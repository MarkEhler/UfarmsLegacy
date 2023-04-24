from flask import Flask, render_template

'''
This code defines a route for the root URL (/), which will display the landing page. The render_template function will render the landing.html template and return the HTML to the user's browser.

Note that you'll need to create a landing.html file in the templates/ directory of your Flask application. This file should contain the HTML for your landing page. You can also use a static folder to serve static files such as CSS and JavaScript, by creating a folder called static/ in the root directory of your Flask application.

You can customize the landing page by editing the landing.html file and adding any additional static files to the static/ folder.
'''
app = Flask(__name__)

@app.route('/')
def landing():
    # Render the landing page template
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)

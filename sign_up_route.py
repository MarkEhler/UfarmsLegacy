from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

"""
This code defines a route for the /signup page, which will display a form for users to enter their username, email, and password. When the form is submitted, the code will hash the user's password for security and store their information in a database. Finally, the user will be redirected to the login page.

Note that this code assumes you have a database set up and that you've defined an insert_user function to insert a new user into the database. You'll also need to create a signup.html template to render the signup form.
"""

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get the user's input from the signup form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']
        #additional fields
        address = request.form['address']
        farmer_img = request.form['farmer_img']
        host_img = request.form['host_img']
        payment = request.form['payment']
        exp = request.form['exp']
        bio = request.form['bio']
        newsletter = 
        # maybe by linking to a larger provider we can offlaod some of the user/signup reqs


        # Hash the user's password for security
        hashed_password = generate_password_hash(password)
        
        # Store the user's information in a database
        # You will need to replace this with your own database code
        db.insert_user(username, email, hashed_password, fname, lname)
        
        # Redirect the user to the login page after signup
        return redirect(url_for('login'))
    
    # Render the signup page template for GET requests
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)



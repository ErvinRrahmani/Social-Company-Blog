# # from myproject import app,db
# # from flask import render_template, redirect, request, url_for, flash,abort
# # from flask_login import login_user,login_required,logout_user
# # from myproject.models import User
# # from myproject.forms import LoginForm, RegistrationForm
# # from werkzeug.security import generate_password_hash, check_password_hash
# #
# #
# # @app.route('/')
# # def home():
# #     return render_template('home.html')
# #
# #
# # @app.route('/welcome')
# # @login_required
# # def welcome_user():
# #     return render_template('welcome_user.html')
# #
# # @app.route('/logout')
# # @login_required
# # def logout():
# #     logout_user()
# #     flash('You logged out!')
# #     return redirect(url_for('home'))
# #
# #
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #
# #     form = LoginForm()
# #     if form.validate_on_submit():
# #         # Grab the user from our User Models table
# #         user = User.query.filter_by(email=form.email.data).first()
# #
# #         # Check that the user was supplied and the password is right
# #         # The verify_password method comes from the User object
# #         # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not
# #
# #         if user.check_password(form.password.data) and user is not None:
# #             #Log in the user
# #
# #             login_user(user)
# #             flash('Logged in successfully.')
# #
# #             # If a user was trying to visit a page that requires a login
# #             # flask saves that URL as 'next'.
# #             next = request.args.get('next')
# #
# #             # So let's now check if that next exists, otherwise we'll go to
# #             # the welcome page.
# #             if next == None or not next[0]=='/':
# #                 next = url_for('welcome_user')
# #
# #             return redirect(next)
# #     return render_template('login.html', form=form)
# #
# # @app.route('/register', methods=['GET', 'POST'])
# # def register():
# #     form = RegistrationForm()
# #
# #     if form.validate_on_submit():
# #         user = User(email=form.email.data,
# #                     username=form.username.data,
# #                     password=form.password.data)
# #
# #         db.session.add(user)
# #         db.session.commit()
# #         flash('Thanks for registering! Now you can login!')
# #         return redirect(url_for('login'))
# #
# #     return render_template('register.html', form=form)
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
#
#
#
# import os
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
# os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
# ############################################
# from flask import Flask, redirect, url_for, render_template
# from flask_dance.contrib.google import make_google_blueprint, google
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecret'
#
# blueprint = make_google_blueprint(client_id='75995445696-n12j10id028nhvemgvgsp7m4vu4i6tv3.apps.googleusercontent.com',
#                         client_secret='lccJhbwp69QukMPSyZnj5mtH',
#                         offline=True,scope=['profile','email'])
#
# app.register_blueprint(blueprint,url_prefix='/login')
#
# @app.route('/')
# def index():
#     return render_template('home.html')
#
#
# @app.route('/welcome')
# def welcome():
#     # RETURN ERROR INTERNAL SERVER ERROR IF NOT LOGGED IN!!!
#     resp = google.get('/oauth2/v2/userinfo')
#     assert resp.ok, resp.text
#     email = resp.json()['email']
#     return render_template('welcome.html',email=email)
#
#
# @app.route('/login/google')
# def login():
#     if not google.authorized:
#         return render_template(url_for('google.login'))
#     response = google.get('/oauth2/v2/userinfo')
#     assert resp.ok, resp.text
#     email = resp.json()['email']
#
#     return render_template('welcome.html', email=email)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
#
#

from puppycompanyblog import app

if __name__ == '__main__':
    app.run(debug=True)

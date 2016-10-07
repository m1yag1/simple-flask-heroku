# simple-flask-heroku

A simple flask web application example template to be used on heroku.

This is an ideal solution if you need something simple that is easy to get deployed on heroku. 

## Quick start

Make changes to the html in `templates/index.html`.

Add the changes and commit them.

`$ git add .`

`$ git commit -m 'initial commit'`

Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)

Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

`$ heroku login`

Add a remote to your git that can push to Heroku

`$ heroku git:remote -a <your-heroku-app-name>` 

Deploy your application using Heroku using Git.

`$ git push heroku master`



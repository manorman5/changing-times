# changing-times
Heroku no longer freely hosts apps. I have not migrated the app to a different free service at this point. To check out the app you must clone the repository and follow the steps below.

* Run `docker image build -t dash-heroku:latest .` in terminal from the repo root.
* Run `docker container run -d -p 5000:5000 dash-heroku` in terminal.
* Visit http://localhost:5000/ in your browser.

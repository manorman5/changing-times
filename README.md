# changing-times
Heroku app investigating trends in marathon finish times through time. Find the app [here](http://chachachanging-times.herokuapp.com/).

## Re-Deployment instructions
#### Step (1) Build Docker Image
`docker image build -t dash-heroku:latest .`  
Confirm the image is working by running the image.  
`docker container run -d -p 5000:5000 dash-heroku`  
#### Step (2) Deploy to Heroku
Create the container in Heroku  
`heroku container:push web --app chachachanging-times`  
Release the app  
`heroku container:release web --app chachachanging-times`  
#### References
* https://samedwardes.com/post/2019-11-15-dash-heroku-cookie-cutter/

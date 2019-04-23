# Welcome to The Happy Cooking recipe webpage.

This project is a website that has been created with different food recipes such as breakfast, lunch and dessert.
I have created a multi-page website with a recipes page .
My primary target is to be able to view recipes with ingredients  on avaliablity of recipes.

[Here is a link to the live version of my project ](http://happy-cooking.herokuapp.com/)

# UX 

This is a data-driven web application created for users, my primary target is to achieve the goal of being able view recipes with ingredients  on avaliablity of recipes. this is shown in the recipes page.

My data-driven web application will be a online cookbook created with  a homepage, a recipes page, my recipes page, and a login form. These pages will allow me to achieve my goals.

* As a user type, I would like to create a recipe page to view recipes.
* As a user type, I would like to create a add recipes page to add a recipe.
* As a user type, I would like to achieve a goal of deleting and updating a recipe by editing it.
* As a user type, I would like to be able to login as a user.
* My goal was to make information accessible on the site and user friendly, as shown through the  data-driven web application  I have created.


# Features of my data-driven web application

### Recipes

This is the page where the user  can view recipes which includes a  name, image of the recipe, ingredients, instructions, serves and cooking time. if you click on the recipe image you can see the recipe as a single recipe in full.
Here you can edit which updated the recipe and delete a recipe also which deleted the recipe off the database completely.

### Full Recipe page 

This is where the recipe can be clicked on and then the page for a full recipe shows the following items:

* An image of the recipe shown
* The name of the recipe 
* ingredients
* instructions
* cooking time
* author
* cuisine 
* dietary requirement
* serves
* edit button
* delete buttin


### Add Recipe 
The user can add a recipe to the recipes page using this page the user must login using the username as "proxie" and the password is "password".  they cann fill in  recipe name, recipe ingredients, Recipe Meathod, cooking time,author, Meal type, dietary requirements.
Any recipes that have been added will be shown on the recipes page.

### Edit Recipe
When the user clicks on a recipe  it brings the user into the recipe in full then down the bottom of the recipe  there is an edit button.


### Delete Recipe
A button is shown on a recipe page. This will delete the recipe from the database if the user chooses to do so.

### User Login

A user can login using the username which is "proxie" and  password which is "password" to be able to login. This username will be used to log in and add, edit and delete a recipe.

### Wire frames I designed 


Here I have included wire frames of diffrent pages such as the home page, recipe page, add recipe page, and login.

My design process for me was to draw my wireframes and add them to my project once i had figured out what I needed to create 
an acheviable site.

* [Homepage wireframe](https://github.com/noellebrowne/happy_cooking/blob/master/Wireframes/homepage.jpg "Homepage")
* [Recipe page wireframe](https://github.com/noellebrowne/happy_cooking/blob/master/Wireframes/recipes.jpg "Recipes")
* [Add recipes page wireframe](https://github.com/noellebrowne/happy_cooking/blob/master/Wireframes/addrecipes.jpg "Add recipe")
* [Login wireframe](https://github.com/noellebrowne/happy_cooking/blob/master/Wireframes/login.jpg "login")


### Planning  my website

I decided to plan my website, I looked at google.com at images of diffrent websites that came up in google images that I thought would help me and give me an idea of a layout of what should be included in my page for design of the navbar, the flow of my page and the pages I would include that would tie in my website together

I understood the base of my data-driven web application should include a hmoe page to start with and then a recipes page to view recipes, another page was my recipes and the login function for a user to login.

I decided that I would draw my wire frames with a pen and paper for each of my pages.

I researched diffrent pop colours such as light blue, baby pink and background images from google i could use as a background to home, recipes page, my recipes page.

Most web applicationa are well structured but simple to use as I wanted mine to be user friendly.

### Technologies

#### Technologies I used for this project is:

* [HTML](https://html.com/)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [MongoDB](https://www.mongodb.com/)
* [Pymongo](https://www.w3schools.com/python/python_mongodb_getstarted.asp)
* [Python](https://www.python.org/)
* [Heroku](https://www.heroku.com)
* [Flask](http://flask.pocoo.org/)
* [Javascript](https://www.javascript.com/)
* [Startboostrap](https://startbootstrap.com/themes/creative/)
* [Github](https://github.com/)
* [Cloud9](https://c9.io/login)
* [Formatter](https://www.freeformatter.com/html-formatter.html)
* [Validator](https://validator.w3.org/)
* [Materialize](http://archives.materializecss.com/0.100.2/forms.html)
* [Jamie Oliver Recipe site]( https://www.jamieoliver.com/)
* [Holistics - draw.oi](https://www.holistics.io/blog/top-5-free-database-diagram-design-tools/)

### Testing of my project

There were two options of testing my project the first one was by manual testing it by 
making sure the navbar worked by clicking on the recipe button to link to the recipe page, the login modal popping up and 
that i was able to login using the username "proxie" and the password "password".

I tested each section to see that every link worked correctly as i built the website.
When I created my recipe form  it didnt work as I never put the javascript link to make it come live  but I recorrected this error, it worked straight away and it loaded the data that was to load. 

Also in the terminal I ran my project locally by opening the terminal and the typing in python3 app.py to run the application and this would run my code.
              
            To View a recipe in the recipe page 
         
        There are two ways to view the recipes page
     
    1. The first one is to click the home button in the navbar link 
    and you will be directed to the homepage and click 
    the orange button that says 'CHECK OUT THESE RECIPES'
    this button will direct you to the recipes page.
    2. The second one is to click the recipes page on the right handside of the navbar
    and this will bring you to the recipes page.
    
                            login
            
     1.Click on the login button on the right hand corner of the navbar
     2.A login form will pop up like a modal.
     3. The user will see "Username" and "password"
     4. Type 'proxie' where it says username with a line underneath
     5. Type 'password' where it says password with a line underneath
     6. Then press the login button.
     
     
     
                            Add Recipe
         
     1. Click on the Add recipes button on the right hand corner of the navbar
     2. If you have not logged in using 'proxie' as the username and 'password' as the password then log in.
     3. Then click on Add recipes button again.
     4. This will bring you to the add recipe form and you can add the following:
        * Recipe Name
        * Recipe Ingredients
        * Recipe Meathod
        * Cooking Time
        * Author
        * Meal Type 
        * Dietary Requirement
        * serves
    5. Then pressthe recipe =+ button and your recipe will be added to the recipes page.   
    
                        Redirect to the home page
                
    1. Press the Happy Cooking logo on the upper left hand corner of the navbar.
    2. This will redirect you back to the home page.
    3. Press Home on the navbar from any of the three pages and it will bring you back to the homepage.
    
                                 run
                            
    1. open terminal.
    2. type in "python3 app.py"
    3. command will run link for application
    
    
                             Create connection
                            
    1. Go to "Command Line Tools".
    2. Click on "Connect Instructions"
    3. This will bring up three options : connect with the mongo shell, Connect your application and connect with MongoDB compass
    4. Click on "connect with the mongo shell"
    5. Then click "I have the mongo shell installed"
    6. Select your Mongo Shell version or if not sure insert "mongo --version" into terminal to check
    7. Then insert the connection string in your command line.
                                                
                         
                         
    

       
### Deployment of my project


I deployed my page from github through github pages. I went to settings in my github repository and scrolled down to Github pages title and changed my source from disabled to master branch and clicked save. now my website has been deployed.

Heroku was used also to deploy my project i created an new application and called it happy cooking.
                
                    
                       
                       
                       
                       
                       
                       
                        deployment of project through github 
                
    1. Go to the terminal 
    2. Typed in git add "filename of what you want to push" and press enter key
    3. Typed in commit -m "type in the message that I would explain about the commit in quotations"
    4. Repeat if neccessary for more files 
    5. Typed in  git push.
    6. Typed in username for github
    7. Typed in password for guthub 
    8. files are now pushed to github


                        
                       
                       deployment of page through github pages
                       
                        
                
    1.Go to the github repository of happy cooking
    2. Then click on settings up on the right handside of the screen under the watch button
    3. Scroll down to the Github Pages
    4. In the container there is a source heading and a option button that has the word "none" with a little arrow pointing down the right
    5. Click on this and it will give you three options master branch, master branch/docs folder or none.
    6. click the master branch.
                      
                      
                      
                      
                      
                        creating up herokua app
                
    1. Log in using username and password
    2. In the personal page click the "NEW" button
    3. Click "Create new app"
    4. This brought me to Create new app page
    5. Type in an app name you want to call the app i called mine happy_cooking
    6. Choose a region united states or europe, i choose europe
    7. Press "create app" button.
    8. The app is now created.
    
    
    
    
                        Create a new Git repository
                        
    1. Type in "cd my-project/" in the terminal
    2. Next type in "git init"
    3. After that I typed in "heroku git:remote -a happy_cooking"                    
                        
            set up Deployment to Heroku in terminal of cloud9
                
    1. Go to the "deploy" page in heroku app
    2. To set up heroku deployment from github to heroku scroll down to "Deploy using Heroku Git" section
    3. Typed in "heroku login" to the terminal of cloud9
    5. Typed in "username" of my heroku username to the terminal of cloud9
    6. Types in "password" of my heroku password to the terminal of cloud9
    
    
                     set up Deployment to Heroku app
                
    1. Go to the "settings" page in heroku app
    2. To set up heroku config vars from cloud9 to heroku scroll down  and click on "Reveal Config Vars" section:
    
    3. Typed in "IP" to KEY and "0.0.0.0" to value 
    4. Typed in "PORT" to KEY and "5000" to value 
    5. Typed in "MONGO_URI" to KEY and "mongodb+srv://<username>:<password>@cluster0-ryuq4.mongodb.net/happy_cooking?retryWrites=true" to value 
    6. Typed in "SECRET_KEY" to KEY and "<secret_key>"" to value 
    
                connected to heroku config vars through cloud9 in app.py
             
    1. app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    2. app.config["MONGO_DBNAME"] = 'happy_cooking'
    3. app.config["MONGO_URI"] = os.environ.get('MONGO_URI')  
    
    
                Commit my code to the repository and deploy it to Heroku using cloud9 terminal 
                
    1. Open terminal
    2. Typed in git add .
    3. Typed in git commit -am "message to explain about the commit you are commiting"
    4. Typed in git push heroku master
    5. Its pushed now.
    
    
    
                         
                setting up mongodb database for collection to connect to deploy to database
                          
    1.Sign up using first name,last name and email address.
    2. Choose M0, the free forever tier.
    3. Scroll right down to the bottom of the page, click on the little arrow, and type cluster name.
    4.Then click on the create cluster button.
    5.Click on the security tab 
    6.Create a username
    7.Create a password
    8. select allow access from anywhere
    

                Create a collection for data to deploy when recipes are added in web application
                            
    1. click on the collections button
    2. click Create Database button
    3. enter "DATABASE NAME"
    4. enter "COLLECTION NAME"
    5.click "create" button
    6. click insert document and enter in data of choice to database

        
                                  
                    
                            

### Credit

To start bootstrap website where i got my template for my website.
I got the recipes from [Jamie Olivers website]( https://www.jamieoliver.com/) and the images too for my website.
I got my background images from [google images]( https://www.google.ie/)
I did my dataschema drawing in draw.io in [Holistics](https://www.holistics.io/blog/top-5-free-database-diagram-design-tools/) 

### Acknowledgements

I got inspiration on google Images I googled on google.com to see different websites and also for my colour scheme and background colour for my pages in my data-driven  web application.
I also got the recipes from Jamie Olivers website and the images too for my website.
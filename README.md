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

* wire frame 1 - homepage
* wireframe 2 - recipe page
* wireframe3 -  add recipes page
* wireframe 4 - login 

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
    5. Then pressthe recipe =+ button and your recipe will be added to the recipes page.   
    
                        Redirect to the home page
                
    1. Press the Happy Cooking logo on the upper left hand corner of the navbar.
    2. This will redirect you back to the home page.
    3. Press Home on the navbar from any of the three pages and it will bring you back to the homepage.
    

       
### Deployment of my project

My Deployment was done by opening a terminal and then by using the code git status first followed git add (I put in my file or image) git commit -m "message on what the update was" and the git push to the master branch followed by my username and password.

I deployed my page from github through github pages. I went to settings in my github repository and scrolled down to Github pages title and changed my source from disabled to master branch and clicked save. now my website has been deployed.

Heroku was used also to deploy my project i created an new application and called it happy cooking.

### Credit

To start bootstrap website where i got my template for my website.
I got the recipes from [Jamie Olivers website]( https://www.jamieoliver.com/) and the images too for my website.
I got my background images from [google images]( https://www.google.ie/)
I did my dataschema drawing in draw.io in [Holistics](https://www.holistics.io/blog/top-5-free-database-diagram-design-tools/) 

### Acknowledgements

I got inspiration on google Images I googled on google.com to see different websites and also for my colour scheme and background colour for my pages in my data-driven  web application.
I also got the recipes from Jamie Olivers website and the images too for my website.
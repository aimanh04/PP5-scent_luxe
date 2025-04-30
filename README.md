# PP5-scent_luxe

![ScentLuxe Am I Responsive Image](readme/features/responsive.png)

Link to the live project: [ScentLuxe](https://aimanh04-scentluxe-eb932135f6ed.herokuapp.com/)

Welcome to the **ScentLuxe**!
ScentLuxe is a Django-powered ecommerce application built to offer a seamless and elegant shopping experience for luxury candle and fragrance lovers. The platform features a curated collection of handcrafted candles made from repurposed champagne bottles, each with its own unique story and scent profile.

Users can browse products, leave reviews, manage their accounts, and complete purchases securely through a Stripe-integrated checkout system. Designed with performance and style in mind, ScentLuxe combines functionality and sophistication to deliver a premium online shopping experience.

## TABLE OF CONTENTS

- [USER EXPERIENCE](#user-experience)
- [DESIGN](#design)
- [FEATURES](#features)
- [WEB MARKETING](#web-marketing)
- [CODE TECHNOLOGIES USED](#code-technologies-used)
- [TESTING](#testing)
- [VALIDATION](#validation)
- [DEPLOYMENT](#deployment)
- [CREDITS](#credits)



## USER EXPERIENCE

#### Agile Methodology

<details>
<summary>Agile</summary>

<img src="readme/features//agile.png" alt="Agile Methodology">
</details>
The Healthy Recipes project followed Agile methodology, using iterative sprints to prioritize key features and improve based on user feedback. The MoSCoW method helped classify features, ensuring core functionalities like browsing, authentication, and recipe management were developed first. Continuous testing and refinements kept the platform user-friendly and responsive.

#### MoSCoW

<details>
<summary>MoSCoW</summary>


<img src="readme/features//moscow.png" alt="MoSCoW">
</details>
This project applied the MoSCoW prioritization technique to categorize its features and requirements based on their significance in achieving a minimum viable product (MVP). The MoSCoW method divides features into four groups: "Must have," "Should have," "Could have," and "Won't have," ensuring a structured approach to prioritization. By using this framework, the project focuses first on the most critical elements, guaranteeing that essential functionalities are addressed before less urgent ones.

#### First-Time User Goals
- Understand the website's purpose and luxury branding from the homepage
- Navigate the main menu with ease to explore the Shop, About, FAQ, and Contact pages
- Browse available Candles and view full product details without needing to register
- Learn about each candle's story, scent profile, and origin (e.g. Champagne bottle source)
- Trust the brand through visual cues of quality: elegant product image, and clear design
- Sign up for an account to access personalized features such as saved orders and review submissions
- View the cart and checkout process intuitively with no confusion or unnecessary steps
- Feel confident in the legitimacy and security of the store through visible payment and trust signals

#### Returning User Goals
- Log into their account effortlessly and resume shopping or managing orders
- Access their user profile to view past orders, submitted reviews, and saved details
- Leave new product reviews and edit or delete their previous reviews as needed
- Quickly browse best-sellers, new arrivals, or shop by scent category or collection
- Engage with other customers by reading shared reviews and product feedback
- Reorder previously purchased items directly from the profile or order history section
- Experience fast page load times and smooth navigation across all devices

#### As an Admin User
- Log into the admin panel securely using Django's authentication system
- Add, edit, or delete product listings including images, pricing, scent notes, and stock levels
- Manage user-submitted reviews with full CRUD permissions to maintain content quality
- Oversee all orders and update order statuses, refunds, or shipping notes when needed
- Edit core site content such as homepage text, FAQ answers content
- Maintain overall site cleanliness and performance to ensure consistent user satisfaction


## DESIGN

### Color Scheme

![Color Scheme](readme/features/palette.png)

### Database Models



## FEATURES

### Blog Features

<details> 
<summary><strong>Menu Bar</strong></summary>

![Menu Bar](readme/features/menu-loggedin.png)
</details>

- For a visiting user the menu bar consists of Home, All Products, FAQ, Contact, 
About Us, My Account with Sign-up and Log-in pages, and shopping bag.


## CODE TECHNOLOGIES USED

### Languages

- Python
- HTML
- JavaScript
- CSS

### Databases

- PostgreSQL from Code Institute was used as the PostgreSQL database for this project.

### Frameworks, Libraries and Programes used

- [GitHub](https://GitHub.com/) - To save and store files for the project
- [Gitpod](https://gitpod.io/) - To use as workspace to code project
- [VSCode](https://code.visualstudio.com) - Used as workspace for my project
- [Am I Responsive](https://techsini.com/multi-mockup/index.php) - Used to test responsivness
- [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) - Used to validate my python code.
- [Heroku](https://dashboard.heroku.com/) - Used to deploy project.
- [Chrome Devtools](https://developer.chrome.com/docs/devtools) - Used throughout the process to find bugs and test responsiveness on website
- [JSHint](https://jshint.com/) - To validate JavaScript code
- [W3C Markup Validation](https://validator.w3.org/) - To validate HTML code
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) - To validate CSS code
- [Pexels](https://www.pexels.com/) - For Hero image
- [Bootstrap](https://getbootstrap.com) - Used to style website and add better responsiveness and interactivity


### Installed Django Packages  

- **Gunicorn**: Used as the web server for deployment on Heroku.  
- **Cloudinary**: Hosts static and media files for efficient content delivery.  
- **dj-database-url**: Parses the database URL from Heroku's environment variables.  
- **psycopg2-binary**: Acts as a PostgreSQL adapter for Python to manage database connections.  
- **Django Summernote**: Provides a rich-text editor for the admin panel.  
- **Django Allauth**: Handles authentication, user registration, and account management.  
- **Crispy Forms**: Enhances form styling for a better user interface.  


## TESTING

### Manual Testing

#### Registration Testing

| Test Case | Status |
|-----------|--------|
| Account creation is successful | Passed |
| Login with created credentials | Passed |
| Logout functionality works correctly | Passed |


#### Navigation Testing

| Test Case | Status |
|-----------|--------|
| All pages are accessible | Passed |
| Navigation menu items are visible | Passed |
| Users can access posts successfully | Passed |


#### User Actions and Expected Outcomes

| Action Performed | Expected Result | Outcome |
|:---|:---|:---:|
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |


#### Layout and Functionality

| Test Action | Expected Result | Outcome |
|:---|:---|:---:|
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |
|  |  | Passed |


### Chrome Developer Tools  

Chrome Developer Tools were utilized throughout the development process to ensure responsiveness. The responsiveness of the webpage was tested by emulating various devices, including:

- Desktops  
- Laptops  
- Tablets  
- Mobile phones  

### Browser Testing  

During development, testing was conducted primarily on Google Chrome. In production, the website has been tested across multiple browsers, including:

- Google Chrome  
- Microsoft Edge  
- Mozilla Firefox  


## VALIDATION

### Validators

#### W3C HTML Validator

<details>
<summary><strong>HTML Validation</strong></summary>

HTML Validation
![HTML Test](readme/testing/htmltest.png)
</details>

#### W3C CSS Jigsaw Validator

<details>
<summary><strong>CSS Validation</strong></summary>

CSS Validation
![CSS Test](readme/testing/csstest.png)
</details>

#### JSHint

<details>
<summary><strong>JSHint Validation</strong></summary>

JSHint Validation
![JSHint Test](readme/testing/jshint.png)
</details>

#### CI Python Linter

<details>
<summary><strong>Python Linter Validation</strong></summary>

Python Linter Validation
![Python Linter Test](readme/testing/python-linter.png)
</details>


### Unsolved Bugs



## DEPLOYMENT

### Steps for deployment on Heroku
1. Go to the [Heroku](https://dashboard.heroku.com/) website.
2. Click on the "Create new app" option on the dashboard.
3. Give it your project name, select your region and go on the "Create app" option.
4. Click the settings tab.
5. Go to "Reveal Config Vars" and store all your sensitive data such as creds.json & port data.
6. Set the buildbacks to Python & Nodejs in that order.
7. Click on the deploy tab.
8. Select Github as a deployment method.
9. Connect it to your Github.
10. Authorize the correct repo to connect.
11. Choose to either "Enable Automatic" or on "Deploy Branch" to deploy the project.
12. Go on "View" to see your live project.


### Stripe API


### Gmail API


### Amazon S3


### Amazon IAM


### Forking the Github Repository
The steps to fork the github repository are:
1. Log in to your [GitHub](https://github.com/).
2. Go to the repository for your project.
3. Click fork on the right hand side of the screen.

### Making a local clone
To clone this repository, do the following steps:
1. Log in to your [GitHub](https://github.com/).
2. Go to the repository for this project []
().
3. Click on the code button and select whether you would like to clone with HTTPS, SSH or GitHub CLI and then copy the URL to your clipboard.
4. Open the terminal in your selected code editor and change the current working directory to the location of where you want the cloned directory.
5. Type "git clone" into the terminal, paste the link you copied and press enter.


## CREDITS

### Imagery

### Special Thanks To

- **Boutique Ado** This walkthrough was heavily relied upon my project due to time constraint and was extremily helpful. However, I did remake the design and made it my own.

- **Code Institute** for providing the foundational python knowledge.

- **Stack Overflow** for helpful solutions regarding python code and error handling.

- **W3Schools** for helpful solutions regarding python code and error handling.

- **Slack Community** for guidance and help

- Special thanks to all the tutors who has helped me in this project with troubleshooting assistance


### Other students projects

I took inspiration from other students who made a similar project to mine

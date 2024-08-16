# Heritage Housing Price Predictor

Welcome,

This is the Heritage Housing Price Predictor which predicts property prices within the region of Ames, Iowa.

## Table Of Contents

- [Business Requirements](#business-requirements)




## How to use this repo

1. Use this template to create your GitHub project repo

2. Log into the cloud-based IDE with your GitHub account.

3. On your Dashboard, click on the Create button

4. Paste in the URL you copied from GitHub earlier

5. Click Create

6. Wait for the workspace to open. This can take a few minutes.

7. Open a new terminal and `pip3 install -r requirements.txt`

11. Open the jupyter_notebooks directory and click on the notebook you want to open.

12. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.8.18 as it inherits from the workspace so it will be Python-3.8.18 as installed by our template. To confirm this you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In your Cloud IDE, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with *Regenerate API Key*.

## Business Requirements

The client has received an inheritance from a deceased great-grandfather located in Ames, Iowa, and is looking for help in maximising the sales price for the inherited properties.

Although the client has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and provided that.

* Business Requirement 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* Business Requirement 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).
* The dataset has almost 1500 rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## CRISP-DM

CRISP-DM (Cross-Industry Standard Process for Data Mining) is a widely used data mining methodology that provides a structured approach to planning and executing data analysis projects. It consists of six phases:

1. **Business Understanding**: Define the project objectives and requirements from a business perspective.
2. **Data Understanding**: Collect, explore, and understand the data to identify quality issues and initial insights.
3. **Data Preparation**: Clean, transform, and structure the data for analysis.
4. **Modeling**: Apply various modeling techniques and select the best model based on the data.
5. **Evaluation**: Assess the model's performance to ensure it meets the business objectives.
6. **Deployment**: Implement the model in a real-world environment for decision-making or other applications.

CRISP-DM is flexible, iterative, and helps ensure that data mining projects are aligned with business goals.

## Hypothesis and how to validate?

* Hypothesis 1: The higher the overall quality ("OverallQual") of a property, the higher the sale price.
    - How to validate: by performing a correlation study on the dataset
    - The correlation study confirms this hypothesis

* Hypothesis 2: The higher the size of a property ("TotalBsmtSF"), the higher the sale price.
    - How to validate: by performing a correlation study on the dataset
    - The correlation study confirms this hypothesis

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

* Business Requirement 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
    - Data Visualization and Correlation Study:
        - Data is collected and inspected from kaggle
        - Using Pearson and Spearman method, correlations are explored
        - Data is visualized to improve ease of use and help make quick deductions about which attributes have the most effect on sale price

* Business Requirement 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.
    - Regression Study and Data Analysis
        - In order to predict a sale price for properties in Ames, Iowa, a regression model is built, using "SalePrice" as target value
        - The best regression model is chosen
        - A dashboard for easy customer use is created

## ML Business Case

1. What are the business requirements?
* The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
* The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.

2. Is there any business requirement that can be answered with conventional data analysis?
* Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

3. Does the client need a dashboard or an API endpoint?
* The client needs a dashboard

4. What does the client consider as a successful project outcome?
* A study showing the most relevant variables correlated to sale price.
* Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.

5. Can you break down the project into Epics and User Stories?
* Information gathering and data collection.
* Data visualization, cleaning, and preparation.
* Model training, optimization and validation.
* Dashboard planning, designing, and development.
* Dashboard deployment and release.

6. Ethical or Privacy concerns?
* No. The client found a public dataset.

7. Does the data suggest a particular model?
* The data suggests a regressor where the target is the sale price.

8. What are the model's inputs and intended outputs?
* The inputs are house attribute information and the output is the predicted sale price.

9. What are the criteria for the performance goal of the predictions?
* We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.

10. How will the client benefit?
* The client will maximize the sales price for the inherited properties.

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

The dashboard has five pages:

* Page 1 shows the Business Requirements and describes the dataset to answer the Business Requirements
* Page 2 answers the first Business Requirement: visualizations of how individual house attributes relate to the target variable of SalePrice.
    * A table shows a dataset sample
    * Pearson and Spearman correlation plots
    * PPS analysis
* Page 3 answers the second Business Requirement: what should be the sale price of a given property.
    * Input fields for select property features
    * Display field for predicted sale price
* Page 4 shows the underlying hypothesis and validation
* Page 5 explains the ML Model
    * Information on the ML pipeline used to train the model
    * Demonstration of feature importance
    * Review of the pipeline performance

## Unfixed Bugs

* Not an unfixed bug but not the ideal solution: for an unknown reason, the packages from the requirements.txt file seem not to be recognized in the individual jupyter_notebooks. The initial instructions in the CI template were followed. The topic was discussed and tried to solve at length with my mentor. Tutor support was contacted on the issue. The friendly tutor advised, that he had encountered the same issue in his own projects and not found a solution either. He advised to install the necessary packages each time in the individual notebook and not get held up by that topic further - which I did.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.


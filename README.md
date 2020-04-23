# Reddit Flair Detector

Reddit Flair Detector web application is used to detect flairs of reddit posts using Machine Learning algorithms. The application can be found live at [Reddit Flair Detector](https://flair-predictor-app.herokuapp.com). 

### Directory Structure
The dscription of the files and folders in the directory is as follows:
1) [Data Extraction.ipynb](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/Data%20Extraction.ipynb) - Jupter notebook for web scrapping reddit data.
2) [Data Analysis.ipynb](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/Data%20Analysis.ipynb) - Jupyter notebook for analysing the reddit data collected.
3) [Predicting the Reddit Flair.ipynb](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/Predicting%20the%20Reddit%20Flair.ipynb) - Jupyter notebook to train various machine learning models on the data extracted and check the accuracy by taking into account different features.
4) [Gradient Boosting.pkl](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/Gradient%20Boosting.pkl) - Machine Learning model trained on our data.
5) [Final Reddit India Data.csv](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/Final%20Reddit%20India%20Data.csv) - csv file which consists of the data scraped from Reddit India.
6) [app.py](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/app.py) - The main Flask application which powers the whole UI. Uses html as frontend and Python in the backend.
7) [Procfile](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/Procfile) - Used for initiating Heroku app.
8) [templates](https://github.com/Shaurya-L/Reddit-Flair-Detector/tree/master/templates) - Consists of html files which form the frontend.


### Codebase
The entire code has been developed using Python programming language, utilizing it's powerful text processing and machine learning modules. The application has been developed using Flask web framework and hosted on Heroku web server.


### How to run the project:

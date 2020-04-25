# Reddit Flair Detector

Reddit Flair Detector web application is used to detect flairs of reddit posts using Machine Learning algorithms. The application can be found live at [Reddit Flair Detector](https://flair-classify.herokuapp.com). 

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
9) [requirements.txt](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/requirements.txt) - Containing all Python dependencies of the project.
10) [Plots](https://github.com/Shaurya-L/Reddit-Flair-Detector/tree/master/Plots) - Consists all the plots drawn as a part of data analysis


### Codebase
The entire code has been developed using Python programming language, utilizing it's powerful text processing and machine learning modules. The application has been developed using Flask web framework and hosted on Heroku web server.


### How to run the project:
Just follow the below steps in order to run this web app offline on your computer.
1) Clone the repository on the system and download the .zip file of the repositry and unzip the file
2) Open the terminal. Ensure that Python3 and pip is installed on the system. 
3) Type cd **'directory in which the app.py file is stored'**. **DO NOT** forget to enclose the directory within the quotation marks. 
4) Enter "**pip install -r requirements.txt**" to install all the libraries used in the project.
5) Enter "**python app.py**" from the terminal.
6) The application is running on your terminal. Just open the displayed URL (on terminal) on your web browser.


### Part 1: Reddit Data Collection
The data consists of 2218 unique reddit posts from the [r/india](https://www.reddit.com/r/india/) subreddit. The [R]eddiquette flair consisted of mere 18 posts while the others have 200 posts per flair. Data collection was the longest part of the whole process, and took about 4 hours for complete retrieval. The data scraped was divided into 12 different types of flairs:
1) AMA (Ask Me Anything)
2) Policy/Economy 
3) Non Political 
4) Science/Technology
5) Politics 
6) Coronavirus 
7) AskIndia
8) Business/Finance
9) Food 
10) Photography
11) Sports
12) [R]eddiquette

The data was stored into a CSV file for further usage. 

2 approaches were used for data extraction which are given as follows:

**Approach 1**<br>
Parsed through the **Top**, **Hot**, **New**, **Controversial** of [r/india](https://www.reddit.com/r/india/). Checked if I had already parsed through the data of the posts. If not then I would append the post data to the original data. Following attributes of data were collected:
* Title of the Post
* Score of the Post(Difference b/w the upvotes and downvotes of a post)
* Unique ID of the Post
* URL of the Post
* Number of Comments on the Post
* Body of the Post
* Flair of the Post

I was able to collect data from 2827 posts. However, there were quite a few problems with the data collected. Following are the problems encountered:
* A lot of random flairs were encountered. 
* Second problem was that data was very unevenly divided. Some flairs have more than 800 data instances while some flairs have negligible number of data instances

Following bar plot highlights the issues faced where x-axis denotes the Flair and y-axis denotes the number of data instances for each flair.

![Bar Plot](https://user-images.githubusercontent.com/57843558/80099977-ee691080-858c-11ea-9a12-0de6ff9fd28a.png)

To resolve the first problem some flairs were completely removed or 2 or more flairs were combined with each other. The following bar plot shows the same where x-axis denotes the Flair and y-axis denotes the number of data instances for each flair.

![Screen Shot 2020-04-23 at 6 08 20 PM](https://user-images.githubusercontent.com/57843558/80100336-751ded80-858d-11ea-9797-7b31678b3ffe.png)

This data was saved in [posts_data.csv](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/posts_data.csv) file

However, the second problem of data being unevenly divided still persists. To remove this problem a second approach of data collection was tried.

**Approach 2**<br>
Collected 200 posts for each of the 12 flairs from [r/india](https://www.reddit.com/r/india/) on Reddit using **praw**(Python Reddit API Wrapper) module.
The data includes the following attributes:
* Flair of the Post
* Title of the Post
* Unique ID of the Post
* Score of the Post(Difference b/w the upvotes and downvotes of a post)
* URL of the Post
* Body of the Post
* Number of Comments on the Post
* Post Comments

For comments, only top 10 comments were considered in dataset and no sub-comments are present.

This data was saved in [Final Reddit India Data.csv](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/Final%20Reddit%20India%20Data.csv) file

Following bar plot shows the distribution of data where x-axis denotes the Flair and y-axis denotes the number of data instances for each flair.

![Screen Shot 2020-04-23 at 6 22 38 PM](https://user-images.githubusercontent.com/57843558/80101907-ae575d00-858f-11ea-8aa2-ab8cb583a4b9.png)


### Part 2: Exploratory Data Analysis
Data analysis was performed on the data collected. All the plots have been saved in the [Plots](https://github.com/Shaurya-L/Reddit-Flair-Detector/tree/master/Plots) folder given in the repositry.

![Flairs vs Number of Data Points per Flair Bar Chart](https://user-images.githubusercontent.com/57843558/80102781-e57a3e00-8590-11ea-9f92-42a8c196fb4e.png)

![Distribution of Number of Words in Title Histogram](https://user-images.githubusercontent.com/57843558/80102773-e3b07a80-8590-11ea-9f49-854cf0edcad3.png)

![Word in Body v:s Number of Posts Histogram](https://user-images.githubusercontent.com/57843558/80102796-ea3ef200-8590-11ea-86d0-90b2388e7c51.png)

![Post Score v:s Number of Posts Histogram](https://user-images.githubusercontent.com/57843558/80102795-e9a65b80-8590-11ea-990d-93aaebc84362.png)

![Number of Comments v:s Number of Posts Histogram](https://user-images.githubusercontent.com/57843558/80102785-e612d480-8590-11ea-8d15-741d27e0a1b2.png)

![Number of Comments v:s Post Score Plot](https://user-images.githubusercontent.com/57843558/80102786-e7440180-8590-11ea-9419-af4e56ad0afd.png)

![Number of Comments v:s Post Score Scatter Plot 1](https://user-images.githubusercontent.com/57843558/80102789-e7dc9800-8590-11ea-851c-d0ff18297ca7.png)

![Number of Comments v:s Post Score Scatter Plot 2](https://user-images.githubusercontent.com/57843558/80102790-e8752e80-8590-11ea-9f57-0bc956e8d017.png)

![Number of Comments w r t Each Flair Histogram 1](https://user-images.githubusercontent.com/57843558/80102791-e90dc500-8590-11ea-962c-fda3a23e7fa9.png)

![Number of Comments w r t Each Flair Histogram 2](https://user-images.githubusercontent.com/57843558/80102794-e90dc500-8590-11ea-81c8-af3ebec5d6ff.png)


### Part 3: Building a Flair Detector/Classifier
The data collected in part 1 was loaded. The flair detector has been created in 2 steps as follows.

**Step 1 - Data Cleaning and Pre-processing**

We cannot apply machine learning or deep learning models directly on raw text. Data needs to be pre-processed that is data should be converted to a cleaner form so that it can be fed to our model. 

For **cleaning and pre-processing the data** we did the following five steps:
1) Converting entire text to lower case
2) Replacing symbols like these /, (), {}, \, etc with space
3) Deleting certain symbols like #, _, ^, etc
4) Removing STOPWORDS from text (STOPWORD is a commonly used word such as “the”, “a”, “an”, “in” that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query)
5) We'll also combine the post title, body, URL and the post comments to create a new feature which would be used for predicting flair of the data.

**Step 2 - Applying Machine Learning Algorithms**

We'll be implementing the following Machine Learning algorithms

* Logistic Regression
* Naive Bayes
* Linear SVM
* SGDC
* Random Forest
* MLP Classifier
* ADA Boost
* Gradient Boost
* K Nearest Neightbours(KNN)

We first trained these models using the Post **Title**, **Body**, **URL**, **Comments** feature and then combined these features to create a new feature **Combined_Features** and trained the machine learning models.

Following results were obtained

**Title as a Feature**

|   Machine Learning Algorithm  | Test Accuracy |
| ------------- | ------------- |
| Naive Bayes  | 67.75  |
| Linear SVM  | 71.00  |
| SGDC  | 70.27  |
| Logistic Regression  | 69.91  |
| **Random Forest**  | **71.71**  |
| MLP Classifier  | 52.79  |
| ADA Boost | 55.85  |
| Gradient Boosting  | 65.77  |
| KNN | 49.91 |


**Body as a Feature**

|   Machine Learning Algorithm  | Test Accuracy |
| ------------- | ------------- |
| Naive Bayes  | 32.43  |
| Linear SVM  | 37.66  |
| SGDC  | 39.82  |
| Logistic Regression  | 40  |
| Random Forest  | 40.72 |
| MLP Classifier  | 29.73  |
| ADA Boost | 28.65  |
| **Gradient Boosting**  | **41.26**  |
| KNN | 27.57 |


**URL as a Feature**

|   Machine Learning Algorithm  | Test Accuracy |
| ------------- | ------------- |
| Naive Bayes  | 29.55  |
| Linear SVM  | 33.87  |
| **SGDC**  | **36.94**  |
| Logistic Regression  | 34.23  |
| Random Forest  | 31.35  |
| MLP Classifier  | 25.59  |
| ADA Boost | 26.85  |
| Gradient Boosting  | 33.15  |
| KNN | 27.20 |

**Comments as a Feature**

|   Machine Learning Algorithm  | Test Accuracy |
| ------------- | ------------- |
| Naive Bayes  | 41.62  |
| Linear SVM  | 51.35 |
| SGDC  | 52.25  |
| Logistic Regression  | 51.72  |
| **Random Forest**  | **52.61**  |
| MLP Classifier  | 41.98  |
| ADA Boost | 39.28 |
| Gradient Boosting  | 47.39  |
| KNN | 38.38 |

**Title + Body + URL + Comments as a Feature**

|   Machine Learning Algorithm  | Test Accuracy |
| ------------- | ------------- |
| Naive Bayes  | 62.52  |
| Linear SVM  | 75.68  |
| SGDC  | 79.82 |
| Logistic Regression  | 78.20  |
| Random Forest  | 81.44  |
| MLP Classifier  | 60.18  |
| ADA Boost | 61.98|
| **Gradient Boosting**  |**84.68**  |
| KNN | 53.15 |

Using URL and Body as the only features gives us the lowest testing accuracy. We get the highest testing accuracy of **84.68%** when we use **Gradient Boosting** as our algorithm and post title, body, URL and comments as a combined feature.

The [gradient boosting](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/Gradient%20Boosting.pkl) model and random forest model returned the highest testing accuracies with all the features combined. Those models were saved to the working directory. Random Forest model couldn't be uploaded to github due to its large size. It has been saved as a [google drive](https://drive.google.com/file/d/1FE4O_Xgk4KR_jtNE5CS8oNQYKNyfSM7P/view?usp=sharing) file.

### Part 4: Building a Web Application

The best model which is Gradient Boosting was deployed as a web app which uses Flask in the backend and HTML at the frontend. <br>Following are the screenshots for the web app running on local host.

![Screen Shot 2020-04-25 at 11 39 18 PM](https://user-images.githubusercontent.com/57843558/80287305-74808500-874e-11ea-8c92-916b422016b8.png)

![Screen Shot 2020-04-25 at 11 41 31 PM](https://user-images.githubusercontent.com/57843558/80287308-76e2df00-874e-11ea-857a-7390d5c3aaa1.png)


### Part 5: Deploying on Heroku

The web application has been deployed on Heroku. The live demo can be found [here](https://flair-classify.herokuapp.com). Following are the screenshots for the web app running on heroku web server.

![Screen Shot 2020-04-25 at 11 45 55 PM](https://user-images.githubusercontent.com/57843558/80287399-10aa8c00-874f-11ea-9203-29390b9bad0e.png)

![Screen Shot 2020-04-25 at 11 46 04 PM](https://user-images.githubusercontent.com/57843558/80287406-13a57c80-874f-11ea-8a3e-b8e57f2b378d.png)

Another feature of the web app is that we can upload a text(.txt) file consisting of the links of various Reddit posts. Once the file is submitted the predicted flairs of all the posts is returned. This helps in the bulk testing of several Reddit posts at one go. The live demo for the same can be found [here](https://flair-classify.herokuapp.com/automated_testing). <br><br>Following are the screenshots for the same.

![Screen Shot 2020-04-25 at 11 55 54 PM](https://user-images.githubusercontent.com/57843558/80287712-751a1b00-8750-11ea-8b84-d3db437764e2.png)
<br><br>
For bulk testing of flairs of Reddit posts we make a text file consisting of links from 12 Reddit posts such that we have 1 link in each line. [RedditFlair.txt](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/RedditFlair.txt) was uploaded and when the submit button is clicked, the result will be shared as a JSON object which contains the Reddit URL and its corresponding flair as shown by the below screenshot
<br><br>
![Screen Shot 2020-04-25 at 11 56 36 PM](https://user-images.githubusercontent.com/57843558/80287714-78150b80-8750-11ea-9d4b-9991d779bdcb.png)
<br>
We can also run the [Automated Testing URL](https://flair-classify.herokuapp.com/automated_testing) through a client script. <br>Following screenshot demonstrates the same.



### References

**For Data Collection**

1) https://www.youtube.com/watch?v=gIZJQmX-55U
2) https://www.youtube.com/watch?v=NRgfgtzIhBQ
3) https://www.youtube.com/watch?v=KX2jvnQ3u60
4) https://praw.readthedocs.io/en/latest/

**For Flair Classification**

1) https://machinelearningmastery.com/clean-text-machine-learning-python/
2) https://towardsdatascience.com/nlp-for-beginners-cleaning-preprocessing-text-data-ae8e306bef0f
3) https://towardsdatascience.com/the-ultimate-guide-to-adaboost-random-forests-and-xgboost-7f9327061c4f
4) https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/

**For webapp and deployment on Heroku**

1) https://medium.com/techkylabs/getting-started-with-python-flask-framework-part-1-a4931ce0ea13
2) https://flask.palletsprojects.com/en/1.1.x/
3) https://www.youtube.com/watch?v=UbCWoMf80PY
4) https://www.youtube.com/watch?v=mrExsjcvF4o
5) https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

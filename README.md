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
9) [requirements.txt](https://github.com/Shaurya-L/Reddit-Flair-Detector/blob/master/requirements.txt) - Containing all Python dependencies of the project.


### Codebase
The entire code has been developed using Python programming language, utilizing it's powerful text processing and machine learning modules. The application has been developed using Flask web framework and hosted on Heroku web server.


### How to run the project:
Just follow the below steps in order to run this web app offline on your computer.
1) Clone the repository on the system and download the .zip file of the repositry and unzip the file
2) Open the terminal. Ensure that Python3 and pip is installed on the system. 
3) Type cd **'directory in which the app.py file is stored'**. **DO NOT** forget to encolse the directory within the quotation marks. 
4) Enter "**pip install -r requirements.txt**" to install all the libraries used in the project.
5) Enter "**python app.py**" from the terminal.
6) The application is running on your terminal. Just open the displayed URL (on terminal) on your web browser.


### Part 1: Reddit Data Collection
The data consists of 2218 unique reddit posts from the [r/india](https://www.reddit.com/r/india/) subreddit. The [R]eddiquette flair consisted of a mere 18 posts while the others had 200 posts per flair. Data collection was the longest part of the whole process, and took about 4 hourse for complete retrieval. The data scraped was divided into 12 different types of flairs:
1) AMA 
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
* Second problem was that data was very unevenly divided. Some flairs have more than 800 instances while some flairs have negligible number of instances

Following bar plot highlights the issues faced where x-axis denotes the Flair and y-axis denotes the number of data instances for each flair.

![Bar Plot](https://user-images.githubusercontent.com/57843558/80099977-ee691080-858c-11ea-9a12-0de6ff9fd28a.png)

To resolve the first problem some flairs were completely removed or 2 or more flairs were combined with each other. The following bar plot shows the same where x-axis denotes the Flair and y-axis denotes the number of data instances for each flair.

![Screen Shot 2020-04-23 at 6 08 20 PM](https://user-images.githubusercontent.com/57843558/80100336-751ded80-858d-11ea-9797-7b31678b3ffe.png)

This data was saved in **posts_data.csv** file

However, the second problem of data being unevenly divided still persisits. To remove this problem a second approach of data collection was tried.

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

This data was saved in **Final Reddit India Data.csv** file

Following bar plot shows the distribution of data where x-axis denotes the Flair and y-axis denotes the number of data instances for each flair.

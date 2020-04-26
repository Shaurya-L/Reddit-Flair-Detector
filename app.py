import pickle
import praw
import re
import nltk
from nltk.corpus import stopwords
from flask import Flask, render_template, request
from werkzeug import secure_filename
import json
#from flask_http_response import success, result, error


# Use pickle to load in the pre-trained model
model = pickle.load(open('Gradient Boosting.pkl','rb'))


reddit = praw.Reddit(client_id = '2d0GPjug_U7kaQ', client_secret = 'slwg95MGliJJAFwnh6kK7XziIY8', user_agent = 'Test_API', username = "Shaurya_L", password = "123456")


# Cleaning the data before giving it to the model
replace_by_space = re.compile('[/(){}\[\]\|@,;]')
replace_symbol = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()  # Converting text to lowercase
    text = replace_by_space.sub(' ', text)  # Replacing symbols mentioned in replace_by_space by space in text
    text = replace_symbol.sub('', text)  # Deleting symbols mentioned in replace_symbol from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)  # Removing STOPWORDS from text
    
    return text


# Combining Post title, URL, body and comments into one feature and making prediction on the reddit post
def prediction(url):
    submission = reddit.submission(url = url)
    data = {}
    data['Post_Title'] = str(submission.title)
    data['Post_URL'] = str(submission.url)
    data['Post_Body'] = str(submission.selftext)

    #submission.comments.replace_more(limit = None)
    #comment = ''
    #count = 0
    #for top_comment in submission.comments:
    #    comment = comment + ' ' + top_comment.body
    #    count += 1
    #    if(count > 10):
    #        break

    #data['Post_Comments'] = str(comment)

    data['Post_Title'] = clean_text(str(data['Post_Title']))
    data['Post_Body'] = clean_text(str(data['Post_Body']))
    #data['Post_Comments'] = clean_text(str(data['Post_Comments']))

    #combined_features = data['Post_Title'] + data['Post_Body'] + data['Post_URL'] + data['Post_Comments'] 
    combined_features = data['Post_Title'] + data['Post_Body'] + data['Post_URL']
    
    return model.predict([combined_features])


# Building the Flask app
app = Flask(__name__)
               
@app.route('/')
def index():                                                                                         
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
     if request.method == 'POST':
        link = request.form["email_name"]
        a = prediction(link)
        str_a = str(a[0])
        print(str_a)
        return render_template("success.html",str_a = str_a, link = link)

@app.route("/automated_testing")
def index2():                                                                                         
    return render_template("index2.html")

@app.route("/automated_testing", methods = ['POST', 'GET'])
def automated_testing():
    #print("Hello")
    #print(request.method)
    if request.method == 'POST':
        #print("Hello 2")
        myfile = request.files['upload_file']
        print("Hello")
        myfile.save(secure_filename(myfile.filename))
        lst = []
        with open(myfile.filename, 'r') as filein:
            for url in filein:
                lst.append(url)

        dic = {}
        for i in lst:
            i = i[:-1]
            pred = prediction(i)
            key = i
            value = pred[0]
            dic.update({key : value})

    d = json.dumps(dic)
    return json.dumps(d)


if __name__=='__main__':
    app.debug = True
    app.run()  # Run the app

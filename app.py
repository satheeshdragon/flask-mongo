from flask import Flask,render_template,jsonify

from flask_pymongo import PyMongo


# mongo = pymongo.MongoClient('mongodb+srv://sd:satheeshmongodb@sdcluster-6h2mn.mongodb.net/sample_training?retryWrites=true&w=majority', maxPoolSize=50, connect=False)



app=Flask(__name__)

# app.config["MONGO_URI"] = "mongodb+srv://sd:satheeshmongodb@sdcluster-6h2mn.mongodb.net/sample_training?retryWrites=true&w=majority"
app.config["MONGO_URI"] = "mongodb+srv://sd:satheeshmongodb@sdcluster-6h2mn.mongodb.net/test_two?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('About.html')

@app.route("/contact")
def contact():
    return render_template('Contact.html')


@app.route("/zip")
def home_page():
    online_users = mongo.db.exercises.find()
    return render_template("zip_data.html",online_users=online_users) 


@app.route("/zip_data")
def home_page_data():
    online_users = mongo.db.exercises.find().limit(2)
    return render_template("zip_data_two.html",online_users=online_users)     
       







if __name__ == "__main__":
	app.run( host='0.0.0.0', port=6000)
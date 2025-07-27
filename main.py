from flask import Flask,request,render_template
import pickle
import os
import firebase_admin
# from firebase_admin import credentials, db ,auth
from firebase_admin import credentials, initialize_app

app =Flask(__name__) #used to communicate between web server and web app
current_dir = os.path.dirname(os.path.abspath(__file__))
cred = credentials.Certificate("C:\\Users\\drkks\\Downloads\\online-fraud-firebase-adminsdk-zrf1l-2dc4be88fd.json")
firebase_admin.initialize_app(cred)
# firebase_admin.initialize_app(cred)


# Construct the absolute path to the model file
model_file_path = os.path.join(current_dir, 'lgmodel.pkl')

# Load the model
with open(model_file_path, 'rb') as model_file:
    model = pickle.load(model_file)
    



@app.route('/') 
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact", methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        Name=request.form.get('Name')
        # print(Name)
        Email= request.form.get('Email')
        Number=request.form.get('Number')
        Message=request.form.get('Message')
        entry = contact(fname=Name,email=Email,mobile=Number,message=Message )
        # db.session.add(entry)
        # db.session.commit()
    return render_template("contact.html")

@app.route('/predict_fraud', methods=['POST','GET'])
def predict_fraud():
    if request.method =='POST':
        print(request.form)
        # type = 2
        # print(type)
        # amount= 181
        # oldbalanceOrg = 181
        # newbalanceOrig = 0
        type1 = int(request.form.get("type1"))
        print(type1)
        amount= float(request.form.get('amount'))
        oldbalanceOrg = float(request.form.get('oldbalanceOrg'))
        newbalanceOrig = float(request.form.get('newbalanceOrig'))
       
        prediction = model.predict([[type1,amount,oldbalanceOrg,newbalanceOrig]])
        print(prediction)
        is_fraud=prediction[0]
        print(is_fraud)
        print(type(is_fraud))
        # return the prediction result
        return render_template('index.html', is_fraud=prediction[0])


if __name__=='__main__':
    app.run(debug=True)  # four parameter  1st is host,
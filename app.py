from flask import Flask,request,render_template
import pickle
app =Flask(__name__) #used to communicate between web server and web app
with open('C:/Users/lenovo/Desktop/online fraud detection/major1/major1/lgmodel.pkl','rb') as model_file:
    model = pickle.load(model_file)



@app.route('/') 
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")

def contact():
    return render_template("contact.html")
@app.route('/predict_fraud', methods=['POST','GET'])
def predict_fraud():
    if request.method =='POST':
        type = request.form.get("type")
        print(type)
        amount= float(request.form.get('amount'))
        oldbalanceOrg = float(request.form.get('oldbalanceOrg'))
        newbalanceOrig = float(request.form.get('newbalanceOrig'))
       
        prediction = model.predict([[type,amount,oldbalanceOrg,newbalanceOrig]])

        # return the prediction result
        return render_template('predict_fraud.html', is_fraud=prediction[0])


if __name__=='__main__':
    app.run(debug=True)  # four parameter  1st is host,
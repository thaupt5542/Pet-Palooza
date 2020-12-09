#This is where we are importing flask as well as the request library
from flask import Flask,request,jsonify,redirect,render_template
import requests

#allows the flask app to run and also connects the template and static folders
app = Flask(__name__,template_folder='templates', static_folder='static')

#this is the initial route which connects the index.html contains a form that submits a query to a dynamic route
@app.route('/')
def main():
    return render_template('index.html')

#this is a dynamic route which connects the randompet page and passes in the image from the api
@app.route('/dogAPI')
def dogAPI():
  """
  this is for the request which is sent to the dog api
  this tells the computer to make the request into a json object
  gets the key from the json called message
  """
  
  x = requests.get("https://dog.ceo/api/breeds/image/random")
  
  x = x.json()
  imageurl = x["message"]
  return render_template('image.html',image = imageurl)


@app.route('/contact')
def contact():
  """
  this is a static route which connects the contacts page for this I used Formspree.io
  """
  return render_template('contact.html')

#this is  static route which conects the petcare page
@app.route('/petcare')
def petcare():
  return render_template('petcare.html')

#this is  static route which conects the training page
@app.route('/training')
def training():
  return render_template('training.html')

#this is a dynamic route that takes in a query parameter and passes the parameter to the page and also displays a random dog image from the api
@app.route('/myname',methods = ['GET'])
def name():
  name = str(request.args['query'])
  x = requests.get("https://dog.ceo/api/breeds/image/random")
  #this tells the computer to make the request into a json object
  x = x.json()
  #gets the key from the json called message
  imageurl = x["message"]
  return render_template('name.html',image = imageurl,name = name)



#for future enpoints connect to firebase database which is a online nosql database or a sql database like mySQL 


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000,)

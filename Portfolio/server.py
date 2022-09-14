
from flask import Flask,render_template,url_for,redirect,request
import csv

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')

@app.route('/submit_form', methods=['GET',"POST"])
def submit():
    if request.method=="POST":
        try:
            data=request.form.to_dict()
            write_data_csv(data)
            message='Form Submitted, We will get in touch to you shortly!!'
            return render_template('thankyou.html',message=message)
        except:
            message= "Make sure you have placed the ""name"" attribute in all your form elements. Also, to prevent empty form submissions, see the ""required1"" property."
            return render_template('thankyou.html',message=message)
    else:
        return "Something went Wrong. Please Check your internet Connectivity and Resubmit the Contact Me form!"
        
def write_data_csv(data):
    name=data['name']
    email = data['email']
    subject=data['subject']
    message=data['message']
    with open('db.csv','a', newline="") as csvfile:
        db_writer=csv.writer(csvfile, delimiter= ",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([name,email,subject,message])


if __name__ == '__main__':
    app.run(debug=True)
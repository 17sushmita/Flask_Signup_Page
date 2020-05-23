from flask import Flask, render_template,url_for,request,flash,redirect
from flask_mail import Mail,Message
import sys

sending_email_address="youremailID@gmail.com"
sending_email_password="yourpassword"
receiving_email_address="admin@gmail.com"


app=Flask(__name__)
SECRET_KEY='1234'
app.config.update(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = sending_email_address,
	MAIL_PASSWORD = sending_email_password
	)
mail = Mail(app)



@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        username=request.form['username']
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        password=request.form['password']
        message = "USERNAME :"+username+"\nNAME :"+fname.title()+" "+lname.title()+"\nEMAIL ID :"+email+"\nPASSWORD :"+password
        name=fname.title()+" "+lname.title()
        try:
            msg = Message("New User Registered",sender=sending_email_address,recipients=[receiving_email_address])
            msg.body = message
            mail.send(msg)
            flash('Successfully Registered!!','success')
            return render_template('signup.html', name=name)
        except Exception :
            flash('Something went wrong!!','danger')
            return render_template('index.html')
        #return redirect(url_for('send_mail',details=details))
   
    return render_template('index.html')
'''
@app.route('/sign_up/<message>/<name>')
def sign_up(message,name):
    try:
        msg = Message("New User Registered",sender="7678sush@gmail.com",recipients=["17sushmita@gmail.com"])
        msg.body = message
        mail.send(msg)
        flash('Successfully Registered!!')
        return render_template('signup.html', name=name)
    except Exception :
        flash('Something went wrong!!')
        return render_template('index.html')
'''
app.secret_key = SECRET_KEY

if __name__=="__main__":
    app.debug=True
    app.run(debug=True)

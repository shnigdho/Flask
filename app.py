from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



ENV ='dev'
   
if ENV == 'dev':
    
     app.debug = True
     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresql:sabbir@localhost:5432/Berger'

else:
    app.debug == False
    app.confiq['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


db = SQLAlchemy(app)



class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    mobile = db.Column(db.Integer)
    HRN = db.Column(db.Integer)


    def __init__(self, customer, mobile, HRN):
        self.customer = customer
        self.mobile = mobile
        self.HRN = HRN




    # def __init__(self, customer_name, customer_mobile_number, customer_HRN_number):
    #     self.customer_name = customer_name
    #     self.customer_mobile_number = customer_mobile_number
    #     self.customer_HRN_number = customer_HRN_number




   




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        mobile = request.form['mobile']
        HRN = request.form['HRN']
        # print(customer, customer_mobile_Number, customer_HRN_Number)
        if customer == '' or mobile == '' or HRN == '':
            return render_template('index.html', message='Please fill all the fields')
        return render_template('success.html')
        


if __name__ == '__main__':
    app.debug = True
    app.run()
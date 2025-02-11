from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV ='dev'
   
if ENV == 'dev':
    
     app.debug = True
     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresql:XhSmart212213@#@localhost:5432/Berger'

else:
    app.debug == False
    app.confiq['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


db = SQLAlchemy(app)



# class Feedback(db.Model):
#     __tablename__ = 'feedback'
#     id = db.Column(db.Integer, primary_key=True)
#     customer = db.Column(db.String(200), unique=True)
#     customer_mobile_Number = db.Column(db.Integer)
#     customer_HRN_Number = db.Column(db.Integer)


#     def __init__(self, customer, customer_mobile_Number, customer_HRN_Number):
#         self.customer = customer
#         self.customer_mobile_Number = customer_mobile_Number
#         self.customer_HRN_Number = customer_HRN_Number


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(200), nullable=False)
    customer_mobile_number = db.Column(db.String(20), nullable=False) # Store phone number as string
    customer_HRN_number = db.Column(db.String(50), nullable=False) # Store HRN number as string

    def __init__(self, customer_name, customer_mobile_number, customer_HRN_number):
        self.customer_name = customer_name
        self.customer_mobile_number = customer_mobile_number
        self.customer_HRN_number = customer_HRN_number

# Example validation in a route function (not directly in the model)
def create_feedback(customer_name, mobile_num, hrn_num):
    if not all([customer_name.strip(), mobile_num.strip(), hrn_num.strip()]):
        return "All fields are required."
    
    try:
        feedback_obj = Feedback(customer_name=customer_name,
                                customer_mobile_number=mobile_num,
                                customer_HRN_number=hrn_num)
        
        with app.app_context():
            db.session.add(feedback_obj)
            db.session.commit()
            
            return "Feedback created successfully."
        
    except Exception as e:
        print(f"Error: {e}")
        return "Failed to create feedback."

# Initialize database tables if needed (call once during setup)
def init_db():
    with app.app_context():
        db.create_all()

init_db()

   




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        customer_mobile_Number = request.form['customer_1']
        customer_HRN_Number = request.form['customer_2']
        # print(customer, customer_mobile_Number, customer_HRN_Number)
        if customer == '' or customer_mobile_Number == '' or customer_HRN_Number == '':
            return render_template('index.html', message='Please fill all the fields')
        return render_template('success.html')
        


if __name__ == '__main__':
    app.debug = True
    app.run()
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



   




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
from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def web_page(page_name):
    return render_template(page_name)


def write_to_csv_file(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['text']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv_file(data)
            return redirect('/thank_you.html')
        except:
            return 'did not save to database'
    else:
        return "Something went wrong, try again!"
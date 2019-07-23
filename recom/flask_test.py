from flask import Flask, render_template, request
from distance import *

app = Flask(__name__)
app.secret_key = '2019'


@app.route('/', methods=['GET', 'POST'])
def LocationAPI():
    if request.method == 'POST':
        output = request.form.get('output')
        get_distance(output)
        print(output)
        return "success"

    return render_template('LocationAPI.html')


if __name__ == '__main__':
    app.run(debug=True)


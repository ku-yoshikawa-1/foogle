from flask import Flask, render_template, request


app = Flask(__name__)
app.secret_key = '2019'


@app.route('/', methods=['GET', 'POST'])
def LocationAPI():
    if request.method == 'POST':
        output = request.form.get('output')
        print(output)
        return "success"

    return render_template('LocationAPI.html')


if __name__ == '__main__':
    app.run(debug=True)


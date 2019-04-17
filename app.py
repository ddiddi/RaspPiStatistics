from flask import Flask
from datetime import datetime
from flask import render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    """.format(time=the_time)

@app.route('/energy')
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('charts.html', values=values, labels=labels)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/energy-bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Energy Usage', max=17000, labels=bar_labels, values=bar_values)

@app.route('/energy-line')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Energy Usage', max=17000, labels=line_labels, values=line_values)

@app.route('/energy-pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Energy Usage', max=17000, set=zip(values, labels, colors))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

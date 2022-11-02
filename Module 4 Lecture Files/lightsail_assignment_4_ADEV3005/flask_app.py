import numbers
from flask import Flask, render_template, request
from cal import MyMath

#creates the Flask web app object
#attaches a name to which the interpreter can identify the instance
app = Flask(__name__)

#@app.route('/') is a function decorator (decorators use @)
#Flask's route decorator lets you associate a URL with the python function
#In this case the URL is /results .  The decorator causes the Flask web
#server to call the functoin when a request for the specific url arrives
#at the server
@app.route('/results', methods=['POST'])
def generate_greeting()-> 'html':
    """Generates a greeting and displays to the user."""
    number_list = request.form['numbers']

    title = "Your math helper is here to help!!"
    text_input = number_list.split()
    number_list = []
    for i in text_input:
        int(i)
        number_list.append(i)
    input = number_list
    instance = MyMath(input)
    average = instance.average()
    standard_deviation = instance.StdDev()
    max = instance.Max()
    # ExampleClass = MyMath
    # sample_class.py = cal.py
    # results = instance.MyMath(numbers)
    # greeting(numbers)

    return render_template('results.html', the_title = title, input_value = input, average_value = average, standard_deviation_value = standard_deviation, max_value = max )



@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'Standard Deviation Generator')


#takes the Flask object assigned to the app variable and asks Flask
#to start running the web server
#note:  the debug=True, host='0.0.0.0' is needed to run on all ports when deployed to lightsail
app.run(debug=True, host = '0.0.0.0')


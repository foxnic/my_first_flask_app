from flask import Flask, request, jsonify, render_template

# create the flask app
app = Flask(__name__)

# what html should be loaded as the home page when the app loads?
@app.route('/')
def home():
    return render_template('app_frontend.html', prediction_text="")

# define the logic for reading the inputs from the WEB PAGE, 
# running the model, and displaying the prediction
@app.route('/predict', methods=['GET','POST'])
def predict():

    # get the description submitted on the web page
    a_description = request.form.get('description')
    return render_template('app_frontend.html', prediction_text=a_description)
    #return 'Description entered: {}'.format(a_description)

#@app.route('/prediction', methods=['GET', 'POST'])
#def prediction():
#    if request.method == 'POST':
#        prediction_data = request.json
#        print(prediction_data)
#    return jsonify({'result': prediction_data})

# boilerplate flask app code
if __name__ == "__main__":
    app.run(debug=True)

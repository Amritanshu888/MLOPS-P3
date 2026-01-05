from flask import Flask,request,render_template ## request so that any post request i will be able to capture through it
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler  ## The reason why i m doing it bcoz i will try to use that pickle file
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__) ## This will give us the entry point where we need to execute this

app = application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():  ## In index.html we have a form action, we are writing url_for and we are calling the same predict_datapoint function here and the method will be post, i.e. how when we do the post from that particular page the request will come over here
    if request.method == 'GET':
        return render_template('home.html') ## Returning a default home page, in home.html there will be simple input data fields that i need to provide to my model to do the prediction
    else: ## If its not 'GET' request it will be 'POST' --> In 'POST' part i have to capture the data do 'Standard Scaling' and 'Feature Scaling'
        data = CustomData(  ## This CustomData class will be created in predict_pipeline.py 
            ## Here we will try to read all the data we got from the frontend
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = float(request.form.get('reading_score')),
            writing_score = float(request.form.get('writing_score'))
        )
        ## Note: When we do the post this request will have the entire information
        pred_df = data.get_data_as_data_frame() ## Converting the data to DataFrame
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0]) ## As this will be in the list format
    
## To run this app.y
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
## Run : python app.py
# View ur app in: https://127.0.0.1:5000  
# Then go to : https://127.0.0.1:5000/predictdata     

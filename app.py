import joblib
from flask import Flask , render_template , request 
import Preprocess

app = Flask(__name__)


scaler = joblib.load("D:/Used Cars Pred/Used-Cars-Pred/Model/Scaler.h5")
model = joblib.load("D:/Used Cars Pred/Used-Cars-Pred/Model/Model.h5")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict' , methods=['POST'])
def get_prediction():
    if request.method == 'POST' :

        brand = request.form['brand']
        
        if brand == 'Hyundai':
            model_ = request.form['model']
        elif brand == 'Fiat':
            model_ = request.form['model1']
        else :
            model_ = request.form['model2']

        body = request.form['body']
        year = int(request.form['year'])
        color = request.form['Color']
        engine = request.form['engine']
        kilometers = request.form['Kilometers']
        gov = request.form ['Governament']
        trans = request.form['radio']
        fuel = request.form['radio1']
        


        data = {'Brand' : brand , 'Model' : model_ , 'Body' : body , 'Color' : color , 'Fuel' : fuel  ,
                'Kilometers': kilometers  , 'Engine': engine , 'Transmission' : trans , 'Gov' : gov , 'Year' : year }
    
    final_data = Preprocess.preprossecing(data)
    scaled_data = scaler.transform([final_data])
    prediction = int(model.predict(scaled_data))

    return render_template('index.html' , price = str(int(prediction)) +',000 EGP' )



if __name__ == '__main__':
    app.run(debug=True)


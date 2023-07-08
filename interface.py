from flask import Flask , jsonify , render_template , request ,redirect ,url_for
from utils import Wine
import config
import traceback

app = Flask(__name__)
@app.route('/')
def home():
    print('home page')
    # return jsonify({'result': ' home page created'})
    return render_template('wine.html')

@app.route('/predict', methods= ['POST'])
def test():
    try:
        if request.method == 'POST':
            data = request.form.get
            print('data:',data)

            fixed_acidity         = eval(data('fixed_acidity'))
            volatile_acidity      = eval(data('volatile_acidity'))
            citric_acid           = eval(data('citric_acid'))
            residual_sugar        = eval(data('residual_sugar'))
            chlorides             = eval(data('chlorides'))
            free_sulfur_dioxide   = eval(data('free_sulfur_dioxide'))
            total_sulfur_dioxide  = eval(data('total_sulfur_dioxide'))
            density               = eval(data('density'))
            pH                    = eval(data('pH'))
            sulphates             = eval(data('sulphates'))
            alcohol               = eval(data('alcohol'))

            obj = Wine(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,
                        chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol)
            quality = obj.predict_wine_quality()

            # return jsonify({'result': quality})
            return render_template('wine.html',prediction = quality)

    
    except:
        print(traceback.print_exc())
        return render_template('wine.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port= config.PORT_NUMBER, debug= False)

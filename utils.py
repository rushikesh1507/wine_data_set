import pickle
import json
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import config

class Wine():
    def __init__(self,fixed_acidity,volatile_acidity,citric_acid,residual_sugar,
                chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol):
        self.fixed_acidity        = fixed_acidity
        self.volatile_acidity     = volatile_acidity
        self.citric_acid          = citric_acid
        self.residual_sugar       = residual_sugar
        self.chlorides            = chlorides
        self.free_sulfur_dioxide  = free_sulfur_dioxide
        self.total_sulfur_dioxide = total_sulfur_dioxide
        self.density              = density
        self.pH                   = pH
        self.sulphates            = sulphates
        self.alcohol              = alcohol

    def __load_data(self):
        with open(config.PICKLE_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
        
    def predict_wine_quality(self):
        self.__load_data()

        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0][0]  = self.fixed_acidity 
        test_array[0][1]  = self.volatile_acidity
        test_array[0][2]  = self.citric_acid
        test_array[0][3]  = self.residual_sugar
        test_array[0][4]  = self.chlorides
        test_array[0][5]  = self.free_sulfur_dioxide
        test_array[0][6]  = self.total_sulfur_dioxide
        test_array[0][7]  = self.density
        test_array[0][8]  = self.pH
        test_array[0][9]  = self.sulphates
        test_array[0][10] = self.alcohol
    
        prediction = self.model.predict(test_array)[0]
        if prediction == 0 :
            return 'Bad Wine qaulity'
        else:
            return 'Good Wine Quality'


if __name__ == '__main__': 
    obj = Wine(7.0,100,0.47,3.6,0.067,100,42,0.47,3.39,0.66,50)
    result = obj.predict_wine_quality()
    print(result)
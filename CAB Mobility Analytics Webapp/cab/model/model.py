import numpy as np
import pandas as pd
import joblib

train_data = pd.read_csv('C:/Users/kishan/Desktop/cab1/cab/model/mobility_filter.csv')
X = train_data.drop(['Trip_ID','Var1','Var2','Var3','Confidence_Life_Style_Index','Type_of_Cab'],axis=1)
y = train_data['Type_of_Cab']

model = joblib.load('C:/Users/kishan/Desktop/cab1/cab/model/rf_mobility_model.pkl')

def predict_price(Trip_Distance,Customer_Since_Months,Life_Style_Index,Destination_Type, 
    Customer_Rating,Cancellation_Last_1Month,Gender,Surge_Pricing_Type):
    x=np.zeros(len(X.columns))
    x[0]=Trip_Distance
    x[1]=Customer_Since_Months
    x[2]=Life_Style_Index
    x[3]=Destination_Type
    x[4]=Customer_Rating
    x[5]=Cancellation_Last_1Month
    x[6]=Gender
    x[7]=Surge_Pricing_Type
        
    return model.predict([x])[0]

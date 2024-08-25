import pandas as pd
import pickle
import numpy as np
import copy
from math import radians, sin, cos, sqrt, atan2
from flask import Flask, request, jsonify




def haversine_distance(long1,lat1, long2, lat2):    
    # Convert latitude and longitude to radians
    lat1_rad = radians(lat1)
    long1_rad = radians(long1)
    lat2_rad = radians(lat2)
    long2_rad = radians(long2)

    # Haversine formula
    dlong = long2_rad - long1_rad
    dlat = lat2_rad - lat1_rad
    a = sin(dlat/2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlong/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6371 * c  # Earth radius in kilometers
    return distance


def data_processing(data):
    df = pd.DataFrame(data)
    df.pickup_datetime = pd.to_datetime(df.pickup_datetime)
    df['dayofyear'] = df.pickup_datetime.dt.dayofyear
    df['dayofweek'] = df.pickup_datetime.dt.weekday
    df['time'] = df.pickup_datetime.dt.time
    df['distance_km'] = df.apply(lambda x: haversine_distance(x.pickup_longitude, x.pickup_latitude, x.dropoff_longitude, x.dropoff_latitude) ,axis = 1 )
    df.drop(columns = ['pickup_datetime','pickup_longitude','pickup_latitude','dropoff_longitude', 'dropoff_latitude' ], inplace = True)
    df['dayofyear_sin'] = np.sin(2*np.pi*df['dayofyear']/366)
    df['dayofyear_cos'] = np.cos(2*np.pi*df['dayofyear']/366)
    df['dayofweek_sin'] = np.sin(2*np.pi*df['dayofweek']/6)
    df['dayofweek_cos'] = np.cos(2*np.pi*df['dayofweek']/6)
    df['total_seconds'] = df['time'].apply(lambda t: t.hour * 3600 + t.minute * 60 + t.second )
    df['time_sin'] = np.sin(2*np.pi*df['total_seconds']/86400)
    df['time_cos'] = np.cos(2*np.pi*df['total_seconds']/86400)
    final_df = df.drop(columns = ['dayofyear','dayofweek','time','total_seconds']).reset_index(drop = True)
    return final_df


with open('./production_model.bin' , 'rb') as f_in:
    model = pickle.load(f_in)

def predict(features):
    prediction = model.predict(features)
    return prediction

app = Flask('fare-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    raw_data = request.get_json()
    features = data_processing(raw_data)
    pred = predict(features)

    result = {
        "fare_amount": pred.tolist()[0]
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug = False, host='0.0.0.0', port = 9696)




import requests

data = {
    "pickup_datetime": ["2015-05-07 19:52:06 UTC"],
    "pickup_longitude": [-73.999817],	
	"pickup_latitude": [40.738354],
	"dropoff_longitude": [-73.999512]	,
	"dropoff_latitude" : [40.723217] ,	
	"passenger_count": [1] 
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=data)
print(response.json())
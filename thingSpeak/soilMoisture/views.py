from django.shortcuts import render
import requests
import json
from datetime import datetime
import io
import base64
import urllib
import matplotlib.pyplot as plt


def thingspeak_data_temperature(request):
    # set up API endpoint and parameters
    # url = 'https://api.thingspeak.com/channels/1970479/feeds.json'

    url='https://api.thingspeak.com/channels/1970479/fields/1.json'
    
    # make GET request to API endpoint
    response = requests.get(url, params=params)

    # check status code of response
    if response.status_code == 200:
        # extract data from response JSON
        data = response.json()
        s1=json.dumps(data)
        data=json.loads(s1)
        x=[]
        y=[]
        new_data=data['feeds']
        for i in range(len(new_data)):
            a=new_data[i]
            x.append(datetime.strptime(a['created_at'], '%Y-%m-%dT%H:%M:%SZ'))
            y.append(float(a['field1']))

        fig = plt.figure()
        plt.plot(x, sorted(y),color='red',linewidth=4,marker='o')
        plt.xlabel('Date',color='blue')
        plt.ylabel('FieldLabel1',color='blue')
        plt.title('Temperature',color='blue')
        # Save the figure to a PNG in memory
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        
        # Encode the PNG data in base64
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)

        return render(request, 'soilMoisture/temperature.html', {'graph': uri,'new_data':new_data})
    else:
        # handle error
        error_message = 'Error: status code ' + str(response.status_code)
        return render(request, 'error.html', {'message': error_message})

def thingspeak_data_humidity(request):
    # set up API endpoint and parameters
    # url = 'https://api.thingspeak.com/channels/1970479/feeds.json'

    url='https://api.thingspeak.com/channels/1970479/fields/2.json'
    # make GET request to API endpoint
    response = requests.get(url, params=params)

    # check status code of response
# check status code of response
    if response.status_code == 200:
        # extract data from response JSON
        data = response.json()
        s1=json.dumps(data)
        data=json.loads(s1)
        x=[]
        y=[]
        new_data=data['feeds']
        for i in range(len(new_data)):
            a=new_data[i]
            x.append(datetime.strptime(a['created_at'], '%Y-%m-%dT%H:%M:%SZ'))
            y.append(float(a['field2']))


        fig = plt.figure()
        plt.plot(x, y,color='red',linewidth=4,marker='o')
        plt.xlabel('Date',color='blue')
        plt.ylabel('FieldLabel2',color='blue')
        plt.title('Humidity',color='blue')
        
        
        # Save the figure to a PNG in memory
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        
        # Encode the PNG data in base64
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)

        return render(request, 'soilMoisture/humidity.html', {'graph': uri,'new_data':new_data})
    else:
        # handle error
        error_message = 'Error: status code ' + str(response.status_code)
        return render(request, 'error.html', {'message': error_message})

def thingspeak_data_soil_moisture(request):
    # set up API endpoint and parameters
    # url = 'https://api.thingspeak.com/channels/1970479/feeds.json'

    url='https://api.thingspeak.com/channels/1970479/fields/3.json'
    
    # make GET request to API endpoint
    response = requests.get(url, params=params)

    # check status code of response
    if response.status_code == 200:
        # extract data from response JSON
        data = response.json()
        s1=json.dumps(data)
        data=json.loads(s1)
        x=[]
        y=[]
        new_data=data['feeds']
        for i in range(len(new_data)):
            a=new_data[i]
            x.append(datetime.strptime(a['created_at'], '%Y-%m-%dT%H:%M:%SZ'))
            y.append(float(a['field3']))


        fig = plt.figure()
        plt.plot(x, y,color='red',linewidth=4,marker='o')
        plt.xlabel('Date',color='blue')
        plt.ylabel('FieldLabel3',color='blue')
        plt.title('Soil Moisture',color='blue')
        
        # Save the figure to a PNG in memory
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        
        # Encode the PNG data in base64
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)

        return render(request, 'soilMoisture/moisture.html', {'graph': uri,'new_data':new_data})
    else:
        # handle error
        error_message = 'Error: status code ' + str(response.status_code)
        return render(request, 'error.html', {'message': error_message})

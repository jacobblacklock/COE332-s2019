from requests import get, post
from flask import Flask, jsonify, request
import json
import sys

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


class dataHandler():
    data = []
    labels = []

    def __init__(self):
        self.readData()
        print("Loaded in " + str(len(self.data)) + " Records")
        print("Valid Methods: " + str(self.labels))

    def readData(self):
        with open("./UFOs_coord.csv", 'r') as f:
            self.labels = (f.readline())[:-1].split(",")
            for line in f:
                line = line[:-1]
                lineItem = {}
                info = line.split(",")
                for i in range(0, len(self.labels)):
                    lineItem[self.labels[i]] = info[i]
                #print(lineItem) #To test all output works as planned
                self.data.append(lineItem)
        return self.data

    def printData(self, data):
        if data == None:
            print("[]")
            return
        for i in data:
            print(i)

    @app.route('/')
    def getAllData(self):
        return self.data

    #Block for general method querying
    def getDatabyMethod(self, method, query):
        if method in self.labels:
            #Based on the method specified, run the right method (probably using a ladder)
            pass
        else:
            print("Invalid Method")
            return None

    #Convert [Day / Time] string into single ints for easy comparison
    def modifiedDayFormat(self, info):
        if info == 0: return [0, 0]
        infoDay = info.split(' ')
        try: infoTime = infoDay[1]
        except: infoTime = '0:0'
        infoDay = infoDay[0].split('/')
        infoTime = infoTime.split(':')
        modifiedInfo = []
        modifiedInfo.append(int(infoDay[2])*10000 + int(infoDay[0])*100 + int(infoDay[1]))
        modifiedInfo.append(int(infoTime[0])*100 + int(infoTime[1]))
        return modifiedInfo

    #Block for querying by the "Date / Time" field
    @app.route('/Date / Time/<string:start>/<string:end>')
    def getDatabyDate(self, start=0, end=0):
        modifiedStart = self.modifiedDayFormat(start)
        modifiedEnd = self.modifiedDayFormat(end)
        info = []
        for item in self.data:
            modifiedItem = self.modifiedDayFormat(item['Date / Time'])
            if modifiedItem[0] >= modifiedStart[0] and modifiedItem[0] <= modifiedEnd[0]:
                if modifiedItem[1] >= modifiedStart[1] and modifiedItem[1] <= modifiedEnd[1]:
                    info.append(item)

        return info
        
    #Block for querying by the "Country" field
    @app.route('/Country/<string:country>')
    def getDatabyCountry(self, country):
        info = []
        for item in self.data:
            if item['Country'] == country: info.append(item)
        return info

    #Block for querying by the "City" field
    @app.route('/City/<string:city>')
    def getDatabyCity(self, city):
        info = []
        for item in self.data:
            if item['City'] == city: info.append(item)
        return info

    #Block for querying by the "State" field
    @app.route('/State/<string:state>')
    def getDatabyState(self, state):
        info = []
        for item in self.data: 
            if item['State'] == state: info.append(item)
        return info

    #Block for querying by the "Shape" field
    @app.route('/Shape/<string:shape>')
    def getDatabyShape(self, shape):
        info = []
        for item in self.data:
            if item['Shape'] == shape: info.append(item)
        return info

    #Block for querying by the "lat"(Latitude) field
    @app.route('/Latitude/<string:start>/<string:end>')
    def getDatabyLAT(self, start=-90, end = 90):
        info = []
        for item in self.data:
            if item['lat'] >= start and item['lat'] <= end: info.append(item)
        return info

    #Block for querying by the "lng"(Longitude) field
    @app.route('/Longitude/<float:start>/<float:end>')
    def getDatabyLNG(self, start=-180, end=180):
        info = []
        for item in self.data:
            if item['lng'] >= start and item['lng'] <= end: info.append(item)
        return info

    #Block for querying by location using a latitude(lat) and longitude(lng) pair
    @app.route('/Location/<float:latStart>/<float:lngStart>/<float:latEnd>/<float:lngEnd>')
    def getDatabyLocation(self, latStart=-90, lngStart=-180, latEnd=90, lngEnd=180):
        info = []
        for item in self.data:
            if item['lat'] >= latStart and item['lng'] >= lngStart \
                and item['lat'] <= latEnd and item['lng'] <= lngEnd: info.append(item)
        return info



#Running Code for debugging
dataHandler()
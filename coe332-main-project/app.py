from flask import Flask, jsonify, request, render_template
import json, worker, urllib2
from plotter import plot_map

# The main Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def getData():
    #Browser Landing
    return render_template('index.html')


@app.route('/AllData', methods=['GET'])
def getUserFriendly():
    #gets all data
    return (worker.add_job("All=None") + "\n")


@app.route('/submitJSON', methods=['GET', 'POST'])
def executeWithJSON():
    try:
        inp = request.get_json(force=True)
        print(inp)
        if(inp == None):
            return ("No JSON was Provided\n")
        else:
            try:
                if(len(inp) == 1):
                    print (inp[u"command"].decode("utf-8"))
                    return executeCommand(inp[u"command"].decode("utf-8"))
                elif(len(inp) > 1):
                    if(inp[u"command"] == "Date"):
                        print (inp[u"command"].decode("utf-8") + "=" + inp[u"start"].decode("utf-8") + "-" + inp[u"end"].decode("utf-8"))
                        return executeCommand(inp[u"command"].decode("utf-8") + "=" + inp[u"start"].decode("utf-8") + "-" + inp[u"end"].decode("utf-8"))
                    else:
                        com = inp[u"command"].decode("utf-8") + "="
                        for i in inp.keys():
                            if i is not u"command":
                                com += inp[i] + " "
                        return executeCommand((com.decode('utf-8')).strip())
                else:
                    return ("Invalid JSON was provided. Valid Methods:\n\t{'command':'METHOD=PARM1 PARM2'}\n\t{'command':'METHOD', 'PARM1 NAME':'PARM VAL', 'PARM2 NAME':'PARM VAL'}\n")
            except:
                return ("Invalid JSON was provided. Valid Methods:\n\t{'command':'METHOD=PARM1 PARM2'}\n\t{'command':'METHOD', 'PARM1 NAME':'PARM VAL', 'PARM2 NAME':'PARM VAL'}\n")
    except:
        return ("No or Invalid JSON was provided. Valid Methods:\n\t{'command':'METHOD=PARM1 PARM2'}\n\t{'command':'METHOD', 'PARM1 NAME':'PARM VAL', 'PARM2 NAME':'PARM VAL'}\n")
    return ("If you see this, please contact the the server admin\n")


@app.route('/submit/<string:command>', methods=['GET'])
def executeCommand(command):
    try:
        if "%" in command:
            command = urllib2.unquote(command)
        vals = command.split("=")
        methods = ["All", "Date", "Country", "City", "State", "Shape", "LAT", "LNG", "LAT-LNG"]
        if vals[0] in methods:
            return (worker.add_job(command) + "\t Sent\n")
    except:
        return ("Invalid Command\n")
    return ("If you see this, please contact the the server admin\n")


@app.route('/data/<string:job_key>', methods=['GET'])
def getJobData(job_key):
    return (worker.get_output(job_key) + "\n")


@app.route('/status/<string:job_key>', methods=['GET'])
def getJobStatus(job_key):
    return (worker.get_status(job_key) + "\n")


@app.route('/add', methods=['GET', 'POST'])
def addWithJSON():
    try:
        inp = request.get_json(force=True)
        print(inp)
        if(inp == None):
            return ("No JSON was Provided\n")
        else:
            try:
                if(len(inp) == 7):
                    [str(inp[i]).decode('utf-8') for i in inp.keys()]
                    try:
                        return (worker.add_data(inp) + "\n")
                    except:
                        return ("Nope\n")
                else:
                    return ("Invalid JSON was provided. Valid Form: {'Date / Time': '4/1/2016 17:45', 'Country': 'USA', 'City': 'Suffolk', 'State': 'VA', 'Shape': 'Light', 'lat': '36.7282096', 'lng': '-76.5835702'}\n")
            except:
                return ("Invalid JSON was provided. Valid Form: {'Date / Time': '4/1/2016 17:45', 'Country': 'USA', 'City': 'Suffolk', 'State': 'VA', 'Shape': 'Light', 'lat': '36.7282096', 'lng': '-76.5835702'}\n")
            return ("If you see this, please contact the the server admin\n")        
    except:
        return ("No or Invalid JSON was provided. Valid Form: {'Date / Time': '4/1/2016 17:45', 'Country': 'USA', 'City': 'Suffolk', 'State': 'VA', 'Shape': 'Light', 'lat': '36.7282096', 'lng': '-76.5835702'}\n")
    return ("If you see this, please contact the the server admin\n")







@app.route('/QueryByDate', methods = ['GET'])
def findDates():
    try:
        start = request.args.get('start', type=str)
        end = request.args.get('end', type=str)
        if "%" in start:
            start = urllib2.unquote(start)
        if "\'" in start:
            start = start.strip("\'")
            print(start)
        if "%" in end:
            end = urllib2.unquote(end)
        if "\'" in end:
            end = end.strip("\'")
        return(worker.add_job("Date="+start+"-"+end) + "\n")
    except:
        return ("Incorrect URL\n")
    return ("If you see this, please contact the the server admin\n")

@app.route('/QueryByCountry', methods=['GET'])
def findCountries():
    try:
        country = request.args.get('country', type=str)
        return(worker.add_job("Country="+country) + "\n")
    except:
        return ("Incorrect URL\n")
    return ("If you see this, please contact the the server admin\n")

@app.route('/QueryByCity', methods=['GET'])
def findCities():
    try:
        city = request.args.get('city', type=str)
        return(worker.add_job("City="+city) + "\n")
    except:
        return ("Incorrect URL\n")
    return ("If you see this, please contact the the server admin\n")

@app.route('/QueryByState', methods=['GET'])
def findStates():
    try:
        state = request.args.get('state', type=str)
        return(worker.add_job("State="+state) + "\n")
    except:
        return ("Incorrect URL\n")
    return ("If you see this, please contact the the server admin\n")

@app.route('/QueryByShape', methods=['GET'])
def findShapes():
    try:
        shape = request.args.get('shape', type=str)
        return(worker.add_job("Shape="+shape) + "\n")
    except:
        return ("Incorrect URL\n")
    return ("If you see this, please contact the the server admin\n")

@app.route('/QueryByLAT', methods=['GET'])
def findLATs():
    try:
        lat = request.args.get('LAT')
        return(worker.add_job("LAT="+lat) + "\n")
    except:
        return ("Incorrect URL\n")
    return ("If you see this, please contact the the server admin\n")

@app.route('/QueryByLNG', methods=['GET'])
def findLNGs():
    try:
        lng = request.args.get('LNG')
        return(worker.add_job("LNG="+lng) + "\n")
    except:
        return ("Incorrect URL\n")
    return ("If you see this, please contact the the server admin\n")

@app.route('/QueryByLocation', methods=['GET'])
def findLocations():
    try:
        lat_lng = request.args.get('LAT-LNG')
        return(worker.add_job("LAT-LNG="+lat_lng) + "\n")
    except:
        return ("Incorrect URL\n")
    return ("If you see this, please contact the the server admin\n")


@app.route('/plot/<string:job_key>', methods=['GET'])
def getPlot(job_key):
    try:
        data = worker.get_output(job_key)
        plt = plot_map(data)
        plt.show()
        return ("This is a WIP")
    except:
        print("FAILURE TO RETRIEVE PLOT")
        return ("Plot Retrivement failed. Please contact a server admin if this persists.")
    return ("If you see this, please contact the the server admin\n")

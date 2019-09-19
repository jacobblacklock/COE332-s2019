from datetime import datetime
import json

class datahandler():
    data = []
    labels = []

    def __init__(self):
        self.__readData()
        print("Loaded in " + str(len(self.data)) + " Records")
        print("Valid Methods: " + str(self.labels))

    def __readData(self):
        with open("./UFOs_coord.csv", 'r') as f:
            self.labels = (f.readline())[:-1].split(",")
            for line in f:
                line = line[:-1]
                lineItem = {}
                info = line.split(",")
                for i in range(0, len(self.labels)):
                    lineItem[self.labels[i]] = info[i]
                #print(lineItem)    #To test all output works as planned
                self.data.append(lineItem)

            for record in self.data:
                #print(record)
                record["lat"] = float(record["lat"])
                record["lng"] = float(record["lng"])
                if(len(record["Date / Time"]) > 10):
                    record["Date / Time"] = datetime.strptime(record["Date / Time"], "%m/%d/%Y %H:%M")
                else:
                    record["Date / Time"] = datetime.strptime((record["Date / Time"] + " 0:00"), "%m/%d/%Y %H:%M")
        return self.data


    def addData(self, data_dict):
        if data_dict is not None and len(data_dict) == 7:
            try:
                if(len(data_dict["Date / Time"]) > 10):
                    data_dict["Date / Time"] = datetime.strptime(data_dict["Date / Time"], "%m/%d/%Y %H:%M")
                else:
                    data_dict["Date / Time"] = datetime.strptime((data_dict["Date / Time"] + " 0:00"), "%m/%d/%Y %H:%M")
                self.data += data_dict;
                return True;
            except:
                return False;
        else:
            return False;
        




    def getQuery(self, method, query):
        commands = ["All", "Date", "Country", "City", "State", "Shape", "LAT", "LNG", "LAT-LNG"]
        try:
            if(method not in commands):
                return ("Invalid Query Method")
            if(method == "All"):
                return self.getAllData()

            if(query == None):
                return ("Invalid Query Parameters")
            if(method == "Date"):
                query = query.split("-")
                return self.__getDatabyDate(query[0], query[1])
            elif(method == "Country"):
                return self.__getDatabyCountry(query)
            elif(method == "City"):
                return self.__getDatabyCity(query)
            elif(method == "State"):
                return self.__getDatabyState(query)
            elif(method == "Shape"):
                return self.__getDatabyShape(query)
            elif(method == "LAT"):
                query = query.split(',')
                return self.__getDatabyLAT(query[0], query[1])
            elif(method == "LNG"):
                query = query.split(',')
                return self.__getDatabyLNG(query[0], query[1])
            elif(method == "LAT-LNG"):
                query = query.split(',')
                return self.__getDatabyLocation(query[0], query[1], query[2], query[3])
        except:
            return ("Invalid Query Method")


    def getAllData(self):
        return self.data


    def printData(self, output):
        if output == None:
            print("[]")
            return
        for i in output:
            temp = i["Date / Time"]
            i["Date / Time"] = str(i["Date / Time"])
            print(i)
            i["Date / Time"] = temp


    def toString(self, output):
        outStr = "["
        if output == None:
            return ("[]")
        for i in output:
            i["Date / Time"] = str(i["Date / Time"])
            outStr += str(i) + "\n"
        return (outStr + "]\n")





    def __getDatabyDate(self, start, end):
        if self.data == None or start == None or end == None:
            print("[]")
            return
        try:
            start = datetime.strptime(start, "%m/%d/%Y %H:%M")
            end = datetime.strptime(end, "%m/%d/%Y %H:%M")
        except:
            return ("Invalid Input")

        output = []
        for record in self.data:
            if type(record["Date / Time"]) is str:
                record["Date / Time"] = datetime.strptime(record["Date / Time"], "%Y-%m-%d %H:%M:%S")
            if(record["Date / Time"] > start and record["Date / Time"] < end):
                output.append(record)
        return output

    def __getDatabyCountry(self, specifiedCountry):
        if self.data == None or specifiedCountry == None:
            print("[]")
            return
        specifiedCountry.upper()
        output = []
        for record in self.data:
            if(record["Country"] == specifiedCountry):
                output.append(record)
        return output


    def __getDatabyState(self, specifiedState):
        if self.data == None or specifiedState == None:
            print("[]")
            return
        specifiedState.upper()
        output = []
        for record in self.data:
            if(record["State"] == specifiedState):
                output.append(record)
        return output

    def __getDatabyCity(self, specifiedCity):
        if self.data == None or specifiedCity == None:
            print("[]")
            return
        output = []
        for record in self.data:
            if(record["City"] == specifiedCity):
                output.append(record)
        return output

    def __getDatabyShape(self, specifiedShape):
        if self.data == None or specifiedShape == None:
            print("[]")
            return
        output = []
        for record in self.data:
            if(record["Shape"] == specifiedShape):
                output.append(record)
        return output

    def __getDatabyLAT(self, startLAT, endLAT):
        if self.data == None or startLAT == None or endLAT == None:
            print("[]")
            return
        output = []
        for record in self.data:
            if(record["lat"] > float(startLAT) and record["lat"] < float(startLAT)):
                output.append(record)
        return output

    def __getDatabyLNG(self, startLNG, endLNG):
        if self.data == None or startLNG == None or endLNG == None:
            print("[]")
            return
        output = []
        for record in self.data:
            if(record["lng"] > float(startLNG) and record["lng"] < float(endLNG)):
                output.append(record)
        return output

    def __getDatabyLocation(self, startLat, startLNG, endLat, endLNG):
        if self.data == None or startLat == None or startLNG == None or endLat == None or endLNG == None:
            print("[]")
            return
        output = []
        for record in self.data:
            if(record["lng"] > float(startLNG) and record["lng"] < float(endLNG) and record["lat"] > float(startLat) and record["lat"] < float(endLat)):
                output.append(record)
        return output



#Debugging Statments that show usage
#d = datahandler()
#hg = d.getQuery("All", "None")
#print(len(hg[0]))

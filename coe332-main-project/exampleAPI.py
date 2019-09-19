### Task 3: Provide examples of how to use code with:
#-Curl
#-Python
#-Examples including JSON output

#Import the dataHandler object from the main.py file
from datahandler import datahandler

portal = datahandler()

#Gets all the records
portal.printData(portal.getAllData())
#Output: 5177 records of type: {'Date / Time': '1/2/2016 0:00', 'Country': 'USA', 'City': 'Paradise Valley', 'State': 'AZ', 'Shape': 'Disk', 'lat': '33.5428006', 'lng': '-111.9556'}



#Gets only the records that fall between the provided start and end times
start = "4/1/2016 7:05"
end = "4/1/2016 21:45"
portal.printData(portal.getDatabyDate(start, end))
#Output: pertinet records of type:
#{'Date / Time': '4/1/2016 17:45', 'Country': 'USA', 'City': 'Suffolk', 'State': 'VA', 'Shape': 'Light', 'lat': '36.7282096', 'lng': '-76.5835702'}



#Gets only the records that occurred in the given country(all caps)
specifiedCountry = "CANADA"
portal.printData(portal.getDatabyCountry(specifiedCountry))
#Output: pertinet records of type:
#{'Date / Time': '4/1/2016 6:30', 'Country': 'CANADA', 'City': 'Fort St. John', 'State': 'BC', 'Shape': 'Light', 'lat': '56.250094', 'lng': '-120.8334656'}



#Gets only the records that occured in the given city
specifiedCity = "Austin"
portal.printData(portal.getDatabyCity(specifiedCity))
#Output: pertinet records of type:
#{'Date / Time': '5/2/2016 19:49', 'Country': 'USA', 'City': 'Austin', 'State': 'TX', 'Shape': 'Fireball', 'lat': '30.2711286', 'lng': '-97.7436994'}



#Gets only the records that occured in the given state by state code
specifiedState = "TX"
portal.printData(portal.getDatabyState(specifiedState))
#Output: pertinet records of type:
#{'Date / Time': '3/2/2016 17:00', 'Country': 'USA', 'City': 'Cypress', 'State': 'TX', 'Shape': 'Unknown', 'lat': '29.9691116', 'lng': '-95.6971685'}



#Gets only the records that occured and had the described shape
specifiedShape = "Rectangle"
portal.printData(portal.getDatabyShape(specifiedShape))
#Output: pertinet records of type:
#{'Date / Time': '1/29/2016 14:10', 'Country': 'USA', 'City': 'Springfield', 'State': 'MO', 'Shape': 'Rectangle', 'lat': '37.2153307', 'lng': '-93.298252'}



#Gets the record(s) that conform to the given Latitude
startLAT = "30"
endLAT = "45"
portal.printData(portal.getDatabyShape(startLAT, endLAT))
#Output: pertinet records of type:
#{'Date / Time': '1/28/2016 20:15', 'Country': 'USA', 'City': 'Waukesha', 'State': 'WI', 'Shape': 'Fireball', 'lat': '43.0116784', 'lng': '-88.2314812'}



#Gets the record(s) that conform to the given Longitude
startLNG = "-100"
endLNG = "-70"
portal.printData(portal.getDatabyLAT(startLNG, endLNG))
#Output: pertinet records of type:
#{'Date / Time': '1/28/2016 20:15', 'Country': 'USA', 'City': 'Waukesha', 'State': 'WI', 'Shape': 'Fireball', 'lat': '43.0116784', 'lng': '-88.2314812'}



#Gets the record(s) that conform to both the given Longitude and Latitude
startLAT = "30"
endLAT = "45"
startLNG = "-100"
endLNG = "-70"
portal.printData(portal.getDatabyLocation(startLAT, startLNG, endLAT, endLNG))
#Output: pertinet records of type:
#{'Date / Time': '1/28/2016 20:15', 'Country': 'USA', 'City': 'Waukesha', 'State': 'WI', 'Shape': 'Fireball', 'lat': '43.0116784', 'lng': '-88.2314812'}

 
# Curl Examples

### All Data
 - curl localhost:5000/AllData
    - Output : 5177 records of type: {'Date / Time': '1/2/2016 0:00', 'Country': 'USA', 'City': 'Paradise Valley', 'State': 'AZ', 'Shape': 'Disk', 'lat': '33.5428006', 'lng': '-111.9556'}

___

### Gets only the records that fall between the provided Start and End Times
 - curl localhost:5000/QueryByDate?start="4/1/2016 7:05"&end="4/1/2016 21:45"
    - Output Type : {'Date / Time': '4/1/2016 17:45', 'Country': 'USA', 'City': 'Suffolk', 'State': 'VA', 'Shape': 'Light', 'lat': '36.7282096', 'lng': '-76.5835702'}

___

### Gets only the records that occurred in the given Country
 - curl localhost:5000/QuerybyCountry?country=CANADA
   - Output Type : {'Date / Time': '4/1/2016 6:30', 'Country': 'CANADA', 'City': 'Fort St. John', 'State': 'BC', 'Shape': 'Light', 'lat': '56.250094', 'lng': '-120.8334656'}

___

### Gets only the records that occured in the given City
 - curl localhost:5000/QuerybyCity?city=Austin
   - Output Type : {'Date / Time': '5/2/2016 19:49', 'Country': 'USA', 'City': 'Austin', 'State': 'TX', 'Shape': 'Fireball', 'lat': '30.2711286', 'lng': '-97.7436994'}

___

### Gets only the records that occured in the given State by State Code
 - curl localhost:5000/QuerybyState?state="TX"
   - Output Type : {'Date / Time': '3/2/2016 17:00', 'Country': 'USA', 'City': 'Cypress', 'State': 'TX', 'Shape': 'Unknown', 'lat': '29.9691116', 'lng': '-95.6971685'}

___

### Gets the record(s) that conform to the given Shape
 - curl localhost:5000/QuerybyShape?shape="Rectangle"
   - Output Type : {'Date / Time': '1/29/2016 14:10', 'Country': 'USA', 'City': 'Springfield', 'State': 'MO', 'Shape': 'Rectangle', 'lat': '37.2153307', 'lng': '-93.298252'}

___

### Gets the record(s) that conform to the given Latitude Range
 - curl localhost:5000/QuerybyLAT?LAT=[30, 45]
   - Output Type : {'Date / Time': '1/28/2016 20:15', 'Country': 'USA', 'City': 'Waukesha', 'State': 'WI', 'Shape': 'Fireball', 'lat': '43.0116784', 'lng': '-88.2314812'}

___

### Gets the record(s) that conform to the given Longitude Range
 - curl localhost:5000/QuerybyLNG?LNG=[-100, -70]
   - Output Type : {'Date / Time': '1/28/2016 20:15', 'Country': 'USA', 'City': 'Waukesha', 'State': 'WI', 'Shape': 'Fireball', 'lat': '43.0116784', 'lng': '-88.2314812'}

___

### Gets the record(s) that conform to both the given Longitude and Latitude Ranges
 - curl localhost:5000/QuerybyLocation?LAT=[30, 45]&LNG=[-100, -70]
   - Output Type : {'Date / Time': '1/28/2016 20:15', 'Country': 'USA', 'City': 'Waukesha', 'State': 'WI', 'Shape': 'Fireball', 'lat': '43.0116784', 'lng': '-88.2314812'}
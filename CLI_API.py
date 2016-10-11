import httplib
import json
from datetime import datetime


print "\n\nWelcome to this simple Commandline Weather App\n", "-"*46
print

city = raw_input("Enter the name of the City you want to query weather information: ")
# Creating the connection to a Public Weather API

connection = httplib.HTTPConnection('api.openweathermap.org')
connection.request("GET", "/data/2.5/weather?q=" + city + ",uk&appid=71f9a304a9de94c5138766c35fd48b30")
response = connection.getresponse()
print "\n", response.status, response.reason, "- The Connection was successful!\n"
data = json.loads(response.read())

print "ID:", data['id'], "\nCity:", data['name'], "\nCountry Code:", data['sys']['country'], "\nCoordinates: ", str(data['coord']['lon']) + ", " + str(data['coord']['lat']), "\nDate:", data['dt'], "\nDescription:", data['weather'][0]['description'],  "\nTemperature:", str(data['main']['temp'] - 273) + u"\N{DEGREE SIGN}C"    

connection.close()
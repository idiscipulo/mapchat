import googlemaps as gm
import pyowm

#set googlemaps api key
k = 'YOUR API KEY'

#class for users
class User():
	snd = ''
	addr = ''

#init list of active users
active = []
	
#check if message sender is active
def Check(snd):
	for i in range(0, len(active)):
		if snd == active[i].snd:
			return 1
	return 0

#if new user get address
def Hello(snd):
	try:
		u = User()
		u.snd = snd
		active.append(u)
		return('Hello and thank you for using MapChat. To begin, please enter your current location using \"Address..<Location>\".')
	except (TypeError, IndexError, Exception):
		return('I am sorry, there seems to be an issue processing your request. Enter \"List\" to view available functions.')

#adds address to active user
def Address(snd, addr):
	try:
		for i in range(0, len(active)):
			print(active[i].addr)
			if active[i].snd == snd:
				if active[i].addr == '':
					active[i].addr = addr
					return('Thank you. Enter \"List\" to view available functions.')
				else:
					active[i].addr = addr
					return('Current location updated.')
	except (TypeError, IndexError, Exception):
		return('I am sorry, there seems to be an issue processing your request. Enter \"List\" to view available functions.')

#determine directions
def Directions(snd, ad2):
	try:
		#create googlemaps client
		gmaps = gm.Client(key = k)

		#create return string
		ret = ""

		#get location of user
		for i in range(0, len(active)):
			if active[i].snd == snd:
				ad1 = active[i].addr

		#get directions
		directions = gmaps.directions(ad1, ad2)

		#calculate distance
		dist = round(directions[0]['legs'][0]['distance']['value'] / 1000)
		ret = ret + 'That location is ' + str(dist) + 'km away.\n'

		for i in range(0, len(directions[0]['legs'][0]['steps'])):
			dir = directions[0]['legs'][0]['steps'][i]['html_instructions'].split('<b>')
			dirString = ''.join(dir)
			dir = dirString.split('</b>')

			for s in dir:
				if s.find('<') != -1:
					dir.remove(s)

			ret = ret + '\n' + str(i + 1) + '. ' + ''.join(dir)
	
		return(ret)
	except (TypeError, IndexError, Exception):
		return('I am sorry, there seems to be an issue processing your request. Enter \"List\" to view available functions.')

#determine user elevation
def Elevation(ad1):
	try:
		#create googlemaps client
		gmaps = gm.Client(key = k)

		#get lat and long
		data = gmaps.geocode(ad1);
		lat = data[0]['geometry']['location']['lat']
		lng = data[0]['geometry']['location']['lng']

		data = gmaps.elevation((lat, lng))

		#convert to km
		el = round(data[0]['elevation'] / 1000)

		return('That location is ' + str(el) + 'km above sea level.')
	except (TypeError, IndexError, Exception):
		return('I am sorry, there seems to be an issue processing your request. Enter \"List\" to view available functions.')

#weather function
def Weather(ad1):
	#try:
		#create googlemaps client
		gmaps = gm.Client(key = k)

		#create owm client
		owm = pyowm.OWM('YOUR OWM KEY')

		#get lat and long
		data = gmaps.geocode(ad1);
		lat = data[0]['geometry']['location']['lat']
		lng = data[0]['geometry']['location']['lng']

		#get weather data
		obs = owm.weather_around_coords(lat, lng, 1)
		w = obs[0].get_weather();

		temp = w.get_temperature(unit = 'celsius')

		return('The weather at that location is ' + str(w.get_status()) + '. The temperature is ' + str(temp['temp']) + '*C.')
	#except (TypeError, IndexError, Exception):
		#return('I am sorry, there seems to be an issue processing your request. Enter \"List\" to view available functions.')


#list function
def List():
	return('Address..<Location>\nDirections..<Location>\nElevation..<Location>\nWeather..<Location>\nList\nExit')

#remove user from active
def Exit(snd):
	try:
		for i in range(0, len(active)):
			if active[i].snd == snd:
				index = i;
		active.pop(i);
		return('Thank you for using our service today.')
	except (TypeError, IndexError, Exception):
		return('I am sorry, there seems to be an issue processing your request. Enter \"List\" to view available function.')

#determine request
def InterMap(snd, request):
	#if new user call hello
	if Check(snd) == 0:
		return(Hello(snd))
	#if active user parse request
	elif Check(snd) == 1:
		rval = request.split('..')

		#call request behavior
		if rval[0].lower() == 'address':
			return(Address(snd, rval[1]))
		elif rval[0].lower() == 'directions':
			return(Directions(snd, rval[1]))
		elif rval[0].lower() == 'elevation':
			return(Elevation(rval[1]))
		elif rval[0].lower() == 'weather':
			return(Weather(rval[1]))
		elif rval[0].lower() == 'list':
			return(List())
		elif rval[0].lower() == 'exit':
			return(Exit(snd))






	

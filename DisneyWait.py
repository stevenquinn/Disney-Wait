from urllib2 import Request, urlopen, URLError
import json
from threading import Thread, Event
import serial

selectedRide = 'Space Mountain'

# Gets the wait time for a particular ride
class WaitTime(object):
	
	def __init__(self, ride):
		self.ride = ride
		self.DLurl = 'http://dlwait.zingled.com/dlp'
		self.DCAurl = 'http://dlwait.zingled.com/dca'
		self.baseline = 92
		self.benchmark = 90
		self.multiplier = 1
		
	def getRideData(self):
		request = Request(self.DLurl)
		data = ''
		
		try:
			# Get the JSON Data from the API
			response = urlopen(request)
			data = response.read()
		except URLError, e:
			print "error", e
			
		dl_data = json.loads(data)
		
		request = Request(self.DCAurl)
		data = ''
		
		try:
			# Get the JSON Data from the API
			response = urlopen(request)
			data = response.read()
		except URLError, e:
			print "error", e
			
		dca_data = json.loads(data)
		
		return dl_data + dca_data

	def getWaitTime(self):
		ride_data = self.getRideData()
			
		#Iterate through
		for ride in ride_data:
			# Grab only the appropriate ride
			if ride['name'] == self.ride:
				if ride['waitTime'] != '':
					rideTime = ride['waitTime'].split()
					rideMin = rideTime[0]
					if (rideMin == 'Closed'):
						rideMin = 180
					return int(rideMin)

	def getSpeed(self):
		time = self.getWaitTime()
		return (self.benchmark / time) * self.multiplier + self.baseline

ser = serial.Serial('/dev/cu.usbmodem1421', 9600, timeout=0)
ser.close()
ser.open()

class WaitThread(Thread):
	def __init__(self, event):
		Thread.__init__(self)
		self.stopped = event
		
	def run(self):
		while not self.stopped.wait(3):
			waitTime = WaitTime(selectedRide)
			speedString = str(waitTime.getSpeed())
			ser.write(speedString)

stopFlag = Event()
thread = WaitThread(stopFlag)
thread.start()

while 1:
	
	waitTime = WaitTime('Space Mountain')
	rideData = waitTime.getRideData()
	numRides = len(rideData)
	count = 1
	
	for item in rideData:
		print("[%d]: %s" % (count, item['name']))
		count += 1
	
	print("Selected: %s" % selectedRide)
	ride = raw_input("Enter Ride: ")
	
	count = 1
	for item in rideData:
		if count == int(ride):
			selectedRide = item['name']
		count += 1
		

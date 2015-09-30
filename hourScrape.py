import urllib2, re



	
def hasDay(s):
	days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
	for day in days:
		tmp = s.find(day)
		if tmp != -1:
			return True
	return False

def hasTime(s):
	reg = '[012]{0,1}[0-9]:[0-5][0-9]'
	if re.match(reg,s):
		return True
	return False 


def main():
	urlBase = "https://housing.colorado.edu"
	out = {}
	places = [
		#("/center-community", 'Center for Community Dining'), #C4C is "special"
		("/dining/locations-hours/cu-run-grab-n-go","CU on the Run Grab-n-Go"),
		("/dining/locations-hours/farrandmarket","Farrand Market"),
		("/dining/locations-hours/go-fresh-farrand-grab-n-go",'Go Fresh @ farrand Grab-n-Go'),
		("/kittredgemarket",'Kittredge Market'),
		("/dining/locations-hours/libby-dining-center" ,'Libby'),
		("/dining/locations-hours/sewall-dining-center" ,'Sewall'),
		("/dining/locations-hours/sewall-market",'Sewall Market' ),
		("/dining/locations-hours/village-express-grab-n-go" ,'Village grab-n-go'),
		("/dining/locations-hours/village-market" ,'Village market'),
		("/dining/locations-hours/weathertech-cafe" ,'Weathertech'),
		("/dining/locations-hours/zellers-grab-n-go" ,'Zellers Grab-n-Go'),
	]
	for url,name in places:
		source = urllib2.urlopen(urlBase+url).read()
		ind = source.find("Academic Year 2015-16")
		source = source[ind:]
		lis = source.split('\n')
		#data = '\n'.join(lis[3:12])
		data =[]
		for i in lis[3:12]:
			data.append(re.sub('<.+?>','',i))
		out[name] =  filter(lambda s: hasDay(s) or hasTime(s),data)
	print out

main()

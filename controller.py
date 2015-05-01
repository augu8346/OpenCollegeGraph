import web
import ocgnlp


urls = (
	'/StudentLogin', 'sLogin',
	'/TeacherLogin', 'tLogin',
	'/Dash', 'dash',
	'/search','search',
	'/(.*)', 'index',
	
)


render = web.template.render('templates/')
app = web.application(urls,globals())
db= web.database(dbn='mysql',user='ocgadmin',pw='mecocg',db='OpenCollege')
session = web.session.Session(app, web.session.DiskStore('/var/www/sessions'))  
regnumber = 0

class index:
	def GET(self , name):
		output = ocgnlp.get_query(name)
		return output

class sLogin:
	def GET(self):
		return render.sLogin()
	def POST(self):
		global regnumber
		data = web.input()
		regno = data.regno
		ofclass = data.ofclass
		result = db.select("Students", 
			vars = dict(regno=regno, ofclass=ofclass),
			what = 'RegNo',
			where = "RegNo=$regno and Class=$ofclass"
			)
		if len(result) == 0:
			return web.seeother('/StudentLogin')
		else: 
			regnumber = result[0].RegNo
			session.user = 'student'
			return web.seeother('/Dash')
		
class tLogin:
	def GET(self):
		return render.tLogin()
		
class dash:
	def GET(self):
		global regnumber
		if session.get('user','student'):
			print 'student'
		print regnumber
		result = db.select("Students", 
			vars = dict(regno=regnumber),
			what = '`First Name`,`Last Name`, Sex, `Date Of Birth`, `Email ID`, Class,Area,`PIN Code`',
			where = "RegNo=$regno"
			)
		var=result[0]
		area = var.get('Area')
		sex = var.get('Sex')
		name=var.get('First Name') +' ' + var.get('Last Name')
		Class=var.get('Class')
		email=var.get('Email ID')
		dob=var.get('Date Of Birth')
		pin=var.get('PIN Code')

		return render.dash(area,name,sex,Class,email,dob,pin)

class search:
	def GET(self):
		name = web.input()
		name = name.question
		output = ocgnlp.get_query(name)
		return output

if __name__ == "__main__":
	app.run()	

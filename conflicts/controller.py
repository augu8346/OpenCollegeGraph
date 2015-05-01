import web
web.__file__
import ocgnlp


urls = (
	'/', 'sLogin'
)


render = web.template.render('templates/')

app = web.application(urls,globals())


class index:
	def GET(self , name):
		output = ocgnlp.get_query(name)
		return output

class sLogin:
	def GET(self):
		name = 'Bob'    
		return render.index(name)
		



if __name__ == "__main__":
	app.run()	

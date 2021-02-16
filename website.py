import bottle
from bottle import get, post, request
from bot import start

@get('/')
def index():
	return '''
		<form action="/sendBots" method="post">
			Game Code: <input name="idd" type="text" /><br/>
			Basename: <input name="basename" type="text" /><br/>
			Number Of Bots: <input name="amount" type="text" /><br/>
			<input value="Login" type="submit" /><br/>
		</form>
	'''

@post('/sendBots')
def do_login():
	idd = request.forms.get('idd')
	basename = request.forms.get('basename')
	amount = request.forms.get('amount')
	try:
		amount = int(amount)
		idd = int(idd)
	except:
		return "<h1>Error</h1>"
	if len(basename) < 3 and len(basename) > 8:
		return "<h1> Basename cant be longer than 8 characters, and shorten than 3</h1>"
	try:
		if amount > 15:
			start(idd, basename, 15)
			return "<h1> Max bots sent at once is 15, so we sent 15</h1>"
		start(idd, basename, amount)
		return "<h1>Bots sent</h1>"
	except:
		return "<h1>Error</h1>"

bottle.run(host='localhost', port=5555, debug=True)
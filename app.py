from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

links = {'BS6SSngNsJ0':"Euronews English Live", 'X7Ktabhd8a4':"Aaj Tak LIVE TV", 'iL3Bg-ChVqw':"BEST POP SONGS WORLD 2018 - LIVE 24/7", 'NH-r7Psb34w':"Goodbye - Julian Martel", 'y2xQzzXngJo':"Maroon 5 GRANDES EXITOS 2017", 'AqcT8uYM0c4':"Charlie Puth - Songs You Might Not Have Heard", 'xS6pwQ1Gs2s':"ChillYourMind Radio • 24/7 Music Live Stream", 'Z-2khcTHIgs':"5 Biggest Tsunami Caught On Camera", 'mArSMOz8VZM':"A Tour of IIT Madras - Campus Life 2018", 'ALiqSY-8JQY':"Owl City - This Isn't The End"}

hashed_password = "sha256$92JKMNxV$5917dfdecacc822c2e3c311bb466b1cbb7cf04df3167cda9110a54a4a0504b8b"

@app.route('/')
def index():
	#pass1 = ""
	#hashed_password = generate_password_hash(pass1, method='sha256')
	#print(pass1)
	#print(hashed_password)
	return render_template('index.html', links=links)
	
@app.route('/player')
def player():
	address = request.args.get('address')
	i = address.find('youtube.com/watch?v=')
	videoID = address[i+20:]
	j = videoID.find('&')
	if j!=-1 :
		videoID = videoID[:j]
	return render_template('player.html', add = videoID)

@app.route('/directplay')
def directplay():
	return render_template('directplay.html')

@app.route('/addyoutubestreams')
def addyoutubestreams():
	return render_template('addyoutubestreams.html')

@app.route('/streamadded')
def streamadded():
	password_entered = request.args.get('password')
	if check_password_hash(hashed_password, password_entered):
		print("inside")
		address = request.args.get('address')
		description = request.args.get('description')
		i = address.find('youtube.com/watch?v=')
		videoID = address[i+20:]
		j = videoID.find('&')
		if j!=-1 :
			videoID = videoID[:j]
		#videoID, description
		links[videoID] = description
	return addyoutubestreams()

@app.route('/removeyoutubestreams')
def removeyoutubestreams():
	return render_template('removeyoutubestreams.html')

@app.route('/streamremoved')
def streamremoved():
	password_entered = request.args.get('password')
	if check_password_hash(hashed_password, password_entered):
		print("inside")
		address = request.args.get('address')
		i = address.find('youtube.com/watch?v=')
		videoID = address[i+20:]
		j = videoID.find('&')
		if j!=-1 :
			videoID = videoID[:j]
		if videoID in links:
			del links[videoID]
	return removeyoutubestreams()


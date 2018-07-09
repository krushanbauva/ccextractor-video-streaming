from flask import Flask, render_template, request
app = Flask(__name__)

links = {'BS6SSngNsJ0':"Euronews English Live", 'X7Ktabhd8a4':"Aaj Tak LIVE TV", 'iL3Bg-ChVqw':"BEST POP SONGS WORLD 2018 (ED SHEERAN CHARLIE PUTH BRUNO MARS) THE BEST SPOTIFY PLAYLIST - LIVE 24/7", 'NH-r7Psb34w':"Goodbye - Julian Martel", 'y2xQzzXngJo':"Maroon 5 GRANDES EXITOS Cubierta completa 2017 - Lo Mejor De Maroon 5 2017", 'AqcT8uYM0c4':"Charlie Puth - Songs You Might Not Have Heard", 'xS6pwQ1Gs2s':"ChillYourMind Radio • 24/7 Music Live Stream | Deep & Tropical House | Chill Music, Dance Music, EDM", 'Z-2khcTHIgs':"5 Biggest Tsunami Caught On Camera", 'mArSMOz8VZM':"A Tour of IIT Madras - Campus Life 2018", 'ALiqSY-8JQY':"Owl City - This Isn't The End"}

@app.route('/')
def index():
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
	address = request.args.get('address')
	description = request.args.get('description')
	i = address.find('youtube.com/watch?v=')
	videoID = address[i+20:]
	j = videoID.find('&')
	if j!=-1 :
		videoID = videoID[:j]
	#videoID, description
	links[videoID] = description
	return render_template('addyoutubestreams.html')
	
	
	
	
	

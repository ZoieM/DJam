from flask import Flask
from flask import render_template
app = Flask(__name__)
from pyspot.examples import show_artist_top_tracks
from pyspot.examples import search

global username

@app.route("/")
def index():
    data = []
    artists = ['Drake', 'Rihanna', 'Flume', 'Ed Sheeran']
    
    for artist in artists: 
        artist_info = {}
        artist_info['artist'] = artist
        artist_url = search.get_artist_url(artist)
        print(artist_url)
        artist_tracks = show_artist_top_tracks.get_top_track_by_artist(artist_url)
        artist_info['songs'] = artist_tracks 

        data.append(artist_info)


    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
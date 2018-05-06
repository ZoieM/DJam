# shows artist info for a URN or URL

import spotipy
import sys
import pprint
import os
import spotipy.util as util
from json.decoder import JSONDecodeError


def search(artist):
    scope = None

    username = 'priyankvars'
    client_id = '0281577f5b0c498f85bfcd13e3687aff'
    client_secret = 'c497ede7ddfa413bb050ba00d00a1222'
    redirect_uri = 'http://localhost:8888/callback'
    try:
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    #if len(sys.argv) > 1:
        #search_str = sys.argv[1]
    #else:
        #search_str = 'Radiohead'

    search_str = artist
    sp = spotipy.Spotify(auth = token)
    result = sp.search(search_str)
    #pprint.pprint(result)

    return dict(result)

def get_artist_url(artist): 
    results = search(artist)

    artist_url = results['tracks']['items'][0]['artists'][0]['id']
     
    
    return artist_url
        
def get_popularity_rating(artist, song_name): 
    results = search(artist)

    info = results['tracks']['items']

    for data in info:
        if data['name'] == song_name:
            popularity_rating = data['popularity']
    
    return popularity_rating
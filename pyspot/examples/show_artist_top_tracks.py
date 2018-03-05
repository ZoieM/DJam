# shows artist info for a URN or URL

import spotipy
import sys
import pprint
import spotipy.util as util
import os

from json.decoder import JSONDecodeError

def get_top_track_by_artist(artist_urn):
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
        #urn = sys.argv[1]
    #else:
        #urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

    urn = artist_urn
    sp = spotipy.Spotify(auth = token)
    response = sp.artist_top_tracks(urn)
    tracks = []
    for track in response['tracks']:
        tracks.append(track['name'])

    return tracks

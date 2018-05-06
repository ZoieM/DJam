# Creates a playlist for a user

import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util


#if len(sys.argv) > 2:
    #username = sys.argv[1]
    #playlist_name = sys.argv[2]
    #playlist_description = sys.argv[3]
#else:
    #print("Usage: %s username playlist-name playlist-description" % (sys.argv[0],))
    #sys.exit()

client_id = '0281577f5b0c498f85bfcd13e3687aff'
client_secret = 'c497ede7ddfa413bb050ba00d00a1222'
redirect_uri = 'http://localhost:8888/callback'
username = 'priyankvars'
playlist_name = 'new_playlist'
playlist_description = 'test using spotipy'

import os
from json.decoder import JSONDecodeError

scope = 'playlist-modify-public'
try:
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

#token = util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name,
                                        playlist_description)
    pprint.pprint(playlists)
else:
    print("Can't get token for", username)

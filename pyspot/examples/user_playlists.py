# shows a user's playlists (need to be authenticated via oauth)

import pprint
import sys
import os
import subprocess

import spotipy

import spotipy.util as util

from json.decoder import JSONDecodeError
scope = 'playlist-read-collaborative'

client_id = '0281577f5b0c498f85bfcd13e3687aff'
client_secret = 'c497ede7ddfa413bb050ba00d00a1222'
redirect_uri = 'http://localhost:8888/callback'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python user_playlists.py [username]")
    sys.exit()

#token = util.prompt_for_user_token(username)
try:
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'])
else:
    print("Can't get token for", username)

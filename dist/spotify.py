# print("spotify external file loading")
import requests
from urllib import parse

import os


SPOTIFY_CLIENT_ID = "0477e88f92c641fda1fb6e5fdbe5af37";
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:5500/index.html";
# SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']




#document.body.style.backgroundColor = "green"


def authorizeUser(e):
    # scopes
    # scopesList = ['ugc-image-upload',
    #             'user-read-recently-played',
    #             'user-top-read',
    #             'user-read-playback-position',
    #             'user-read-playback-state',
    #             'user-modify-playback-state',
    #             'user-read-currently-playing',
    #             'app-remote-control',
    #             'streaming',
    #             'playlist-modify-public',
    #             'playlist-modify-private',
    #             'playlist-read-private',
    #             'playlist-read-collaborative',
    #             'user-follow-modify',
    #             'user-follow-read',
    #             'user-library-modify',
    #             'user-library-read',
    #             'user-read-email',
    #             'user-read-private'];
    scopesList = ['user-read-currently-playing',
                'app-remote-control',
                'streaming'];
    url = ("https://accounts.spotify.com/authorize?client_id=" + SPOTIFY_CLIENT_ID
        + "&response_type=token"
        + "&scope=" + parse.quote(' '.join(scopesList))
        + "&redirect_uri=" + SPOTIFY_REDIRECT_URI)
    
    document.location = url

def parseArgs():
    split = document.location.hash.replace("#", "").split("&")
    #print(split)
    args = {}
    for arg in split:
        kv = arg.split("=")
        if len(kv) > 1:
            args[kv[0]] = kv[1]
    return args





# pa = parseArgs()
# for arg in pa:
#     print(arg + " - " + pa[arg])

parsedArgs = parseArgs()
if 'access_token' in parsedArgs:
    # User is authenticated!
    print("You're authenticated!")

    x = requests.get('https://w3schools.com')   # not sure 
    print(x.status_code)
else:
    print("User is not yet authenticated")



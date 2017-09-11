#!/usr/local/bin/python
# goto developer.spotify.com to create client id, secret, and redirect URI

#import pdb
#
#if __name__ == '__main__':
#  pdb.set_trace()
#  #main()

def get_creds():
  with open('/users/smittapalli/.creds/spotify','r') as credfile:
    lines = credfile.readlines()
    return { 'client_id': lines[0][0:-1], 'client_secret': lines[1][0:-1] }

# shows a user's playlists (need to be authenticated via oauth)

import sys, pdb
import spotipy
import spotipy.util as util

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print "   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name'])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print "Whoops, need your username!"
        print "usage: python user_playlists.py [username]"
        sys.exit()

    creds = get_creds()
    dascope = 'user-library-read'
    #pdb.set_trace()
    try:
      token = util.prompt_for_user_token('ramrom23', client_id=creds['client_id'], scope=dascope,
                  client_secret=creds['client_secret'], redirect_uri='http://github.com/ramrom')
                  #client_secret='blah', redirect_uri='http://github.com/ramrom')
    except spotipy.oauth2.SpotifyOauthError:
      print 'Oauth error!'
      sys.exit(1)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print
                print playlist['name']
                print '  total tracks', playlist['tracks']['total']
                results = sp.user_playlist(username, playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print "Can't get token for", username

#!/usr/local/bin/python
# goto developer.spotify.com to create client id, secret, and redirect URI

import sys, pdb
import spotipy
import spotipy.util as util

def get_creds():
  with open('/users/smittapalli/.creds/spotify','r') as credfile:
    lines = credfile.readlines()
    return { 'client_id': lines[0][0:-1], 'client_secret': lines[1][0:-1] }

def auth_flow(user_scope):
  creds = get_creds()
  try:
    token = util.prompt_for_user_token('ramrom23', client_id=creds['client_id'], scope=user_scope,
                client_secret=creds['client_secret'], redirect_uri='http://github.com/ramrom')
                #client_secret='blah', redirect_uri='http://github.com/ramrom')
  except spotipy.oauth2.SpotifyOauthError:
    print 'Oauth error!'
    sys.exit(1)
  return token

# shows a user's playlists (need to be authenticated via oauth)
def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print "   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name'])

def print_pl_name_and_owner(playlists):
  for pl in playlists:
    print pl['name'], pl['owner']['id']

def print_users_playlists(username, token):
  sp = spotipy.Spotify(auth=token)
  playlists = sp.user_playlists(username)
  #pdb.set_trace()
  for playlist in playlists['items']:
    if playlist['owner']['id'] == username:
      print
      print playlist['name']
      print '  total tracks', playlist['tracks']['total']
      results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
      tracks = results['tracks']
      show_tracks(tracks)
      while tracks['next']:
        tracks = sp.next(tracks)
        show_tracks(tracks)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    username = sys.argv[1]
    token = auth_flow('user-library-read')
    print_users_playlists('ramrom23', token)
  else:
    pdb.set_trace()

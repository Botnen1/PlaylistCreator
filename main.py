import requests
import spotipy

from koder import k_client_ID, k_client_secret, k_redirect_URI

from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = k_client_ID, 
                                               client_secret = k_client_secret, 
                                               redirect_uri = k_redirect_URI, 
                                               scope = "playlist-modify-public"))




print('Welcome to this playlist generator...\nLet us create your personalized playlist!')

valg1 = input('What do you want to base the playlist on?:\n (G) = genre\n (A) = artist\n (M) = mood\n (Y) = year\n>>>')
valg2 = input('How many songs do you want in your playlist? (max = 50)\n>>>')

if valg1.lower() == 'g':
    genre_pick = input('Enter your genre of choice: ')
    result = sp.search(q = f'genre:{genre_pick}', type = 'track', limit = valg2)
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, f"Playlist based on {genre_pick} - Playlist Creator", public=True)
    track_ids = [track['id'] for track in result['tracks']['items']]
    sp.playlist_add_items(playlist['id'], track_ids)
    print(f"Success!\nHere is your playlist:\n{playlist['external_urls']['spotify']}\nENJOY")

elif valg1.lower() == 'a':
    
    artist_pick = input('Enter your artist of choice, its IMPORTANT that you write the name correctly \n>>>')
    result = sp.search(q = f'artist:{artist_pick}', type = 'track', limit = valg2)
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, f"Playlist based on {artist_pick} - Playlist Creator", public=True)
    track_ids = [track['id'] for track in result['tracks']['items']]
    sp.playlist_add_items(playlist['id'], track_ids)
    print(f"Success!\nHere is your playlist:\n{playlist['external_urls']['spotify']}\nENJOY")
    
elif valg1.lower() == 'm':
    mood_pick = input('Enter your mood of choice: ')
    result = sp.search(q = f'mood:{mood_pick}', type = 'track', limit = valg2)
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, f"Playlist based on {mood_pick} - Playlist Creator", public=True)
    track_ids = [track['id'] for track in result['tracks']['items']]
    sp.playlist_add_items(playlist['id'], track_ids)
    print(f"Success!\nHere is your playlist:\n{playlist['external_urls']['spotify']}\nENJOY")    
    
elif valg1.lower() == 'y':
    year_pick = input('Enter your year of choice: ')
    result = sp.search(q = f'year:{year_pick}', type = 'track', limit = valg2)
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, f"Playlist based on {year_pick} - Playlist Creator", public=True)
    track_ids = [track['id'] for track in result['tracks']['items']]
    sp.playlist_add_items(playlist['id'], track_ids)
    print(f"Success!\nHere is your playlist:\n{playlist['external_urls']['spotify']}\nENJOY")
    
else:
    print('Invalid Choice, get your shit together man')





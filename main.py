import tkinter as tk
from tkinter import messagebox
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from koder import k_client_ID, k_client_secret, k_redirect_URI

def on_entry_click(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.insert(0, '')
        entry.config(fg='black')

def on_focusout(entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')

def create_playlist():
    valg1 = choice_var.get().lower()
    valg2 = entry_songs.get()

    if not valg2.isdigit() or not (1 <= int(valg2) <= 50):
        messagebox.showerror("Error", "Please enter a valid number of songs (1-50)")
        return

    if valg1 == 'g':
        genre_pick = entry_genre.get()
        create_and_add_playlist(f'genre:{genre_pick}', f"Playlist based on {genre_pick}")

    elif valg1 == 'a':
        artist_pick = entry_artist.get()
        create_and_add_playlist(f'artist:{artist_pick}', f"Playlist based on {artist_pick}")

    elif valg1 == 'm':
        mood_pick = entry_mood.get()
        create_and_add_playlist(f'mood:{mood_pick}', f"Playlist based on {mood_pick}")

    elif valg1 == 'y':
        year_pick = entry_year.get()
        create_and_add_playlist(f'year:{year_pick}', f"Playlist based on {year_pick}")

    elif valg1 == 'gy':
        genre_pick = entry_genre.get()
        year_pick = entry_year.get()
        create_and_add_playlist(f'genre:{genre_pick} year:{year_pick}', f"Playlist based on {genre_pick} and {year_pick}")

    elif valg1 == 'ay':
        artist_pick = entry_artist.get()
        year_pick = entry_year.get()
        create_and_add_playlist(f'artist:{artist_pick} year:{year_pick}', f"Playlist based on {artist_pick} and {year_pick}")

    else:
        messagebox.showerror("Error", "Invalid Choice. Please select a valid option.")

def create_and_add_playlist(query, playlist_name):
    result = sp.search(q=query, type='track', limit=entry_songs.get())
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, playlist_name + " - Playlist Creator", public=True)
    track_ids = [track['id'] for track in result['tracks']['items']]
    sp.playlist_add_items(playlist['id'], track_ids)
    messagebox.showinfo("Success", f"Playlist created!\nHere is your playlist:\n{playlist['external_urls']['spotify']}\nENJOY")

# Initialize Spotipy with SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=k_client_ID,
                                               client_secret=k_client_secret,
                                               redirect_uri=k_redirect_URI,
                                               scope="playlist-modify-public"))

# Tkinter GUI setup
root = tk.Tk()
root.title("Playlist Generator")

# Frame 1
frame1 = tk.Frame(root)
frame1.pack(padx=10, pady=10)

label1 = tk.Label(frame1, text="Select the basis for your playlist:")
label1.grid(row=0, column=0, columnspan=3, pady=5)

choice_var = tk.StringVar(value="G")

choices = [("Genre", "G"), ("Artist", "A"), ("Mood", "M"), ("Year", "Y"), ("Genre & Year", "GY"), ("Artist & Year", "AY")]
for i, (text, val) in enumerate(choices):
    btn = tk.Radiobutton(frame1, text=text, variable=choice_var, value=val)
    btn.grid(row=1, column=i, padx=5, pady=5)

# Frame 2
frame2 = tk.Frame(root)
frame2.pack(padx=10, pady=10)

label2 = tk.Label(frame2, text="Number of songs in the playlist (max = 50):")
label2.grid(row=0, column=0, pady=5)

entry_songs = tk.Entry(frame2)
entry_songs.grid(row=0, column=1, padx=5, pady=5)

# Frame 3
frame3 = tk.Frame(root)
frame3.pack(padx=10, pady=10)

# Entry fields based on the choice
entry_labels = {"G": "Enter your preferred genre: ",
                "A": "Enter your favorite artist: ",
                "M": "Enter your current mood: ",
                "Y": "Enter the desired year: ",
                "GY": "Enter your preferred genre: \nEnter the desired year: ",
                "AY": "Enter your favorite artist: \nEnter the desired year: "}

label3 = tk.Label(frame3, text=entry_labels[choice_var.get()])
label3.grid(row=0, column=0, pady=5)

entry_genre = tk.Entry(frame3, fg='grey')
entry_artist = tk.Entry(frame3, fg='grey')
entry_mood = tk.Entry(frame3, fg='grey')
entry_year = tk.Entry(frame3, fg='grey')

# Placeholder text and events for the entry boxes
placeholders = {"G": "Genre", "A": "Artist", "M": "Mood", "Y": "Year", "GY": "Genre\nYear", "AY": "Artist\nYear"}

entry_genre.insert(0, placeholders["G"])
entry_artist.insert(0, placeholders["A"])
entry_mood.insert(0, placeholders["M"])
entry_year.insert(0, placeholders["Y"])

entry_genre.bind('<FocusIn>', lambda event: on_entry_click(entry_genre, placeholders["G"]))
entry_genre.bind('<FocusOut>', lambda event: on_focusout(entry_genre, placeholders["G"]))

entry_artist.bind('<FocusIn>', lambda event: on_entry_click(entry_artist, placeholders["A"]))
entry_artist.bind('<FocusOut>', lambda event: on_focusout(entry_artist, placeholders["A"]))

entry_mood.bind('<FocusIn>', lambda event: on_entry_click(entry_mood, placeholders["M"]))
entry_mood.bind('<FocusOut>', lambda event: on_focusout(entry_mood, placeholders["M"]))

entry_year.bind('<FocusIn>', lambda event: on_entry_click(entry_year, placeholders["Y"]))
entry_year.bind('<FocusOut>', lambda event: on_focusout(entry_year, placeholders["Y"]))

entry_genre.grid(row=1, column=0, padx=5, pady=5)
entry_artist.grid(row=1, column=1, padx=5, pady=5)
entry_mood.grid(row=1, column=2, padx=5, pady=5)
entry_year.grid(row=1, column=3, padx=5, pady=5)

# Frame 4
frame4 = tk.Frame(root)
frame4.pack(padx=10, pady=10)

create_button = tk.Button(frame4, text="Create Playlist", command=create_playlist)
create_button.pack()

root.mainloop()

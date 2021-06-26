from config import *
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import re

ccm = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
sp = spotipy.Spotify(client_credentials_manager=ccm)



def manager():
        temp = get_start_data()
        spotify_link, save_method = temp[0], temp[1]

        temp = SpotifyParser(spotify_link=spotify_link, save_method=save_method).get_api_answer()
        api_answer, spotify_method = temp[0], temp[1]

        temp = SpotifyParser(spotify_method=spotify_method, api_answer=api_answer).get_tracks_data()
        tracks_name, tracks_authors, preview_urls, tracks_urls = temp[0], temp[1], temp[2], temp[3]

        temp = save_data(save_method=save_method, tracks_name=tracks_name, tracks_authors=tracks_authors, preview_urls=preview_urls, tracks_urls=tracks_urls)
        print()
        print(temp)



def get_start_data():
    spotify_link = input("Enter the spotify link: ")
    print()
    print("Select the method of processing the result:")
    print("1) Output to the terminal")
    print("2) Save to file (result.txt)")
    save_method = int(input("You have chosen the method: "))
    print()

    return (spotify_link, save_method)



def save_data(save_method=None, tracks_name=None, tracks_authors=None, preview_urls=None, tracks_urls=None):
    
    if save_method == 1:
        for i, track in enumerate(tracks_name):
            temp_print = "=====================\n\n"
            temp_print += f"Full name: {track} - {tracks_authors[i]}\n"
            temp_print += f"Name: {track}\n"
            temp_print += f"Author: {tracks_authors[i]}\n"
            temp_print += f"Preview: {preview_urls[i]}\n"
            temp_print += f"Track url: {tracks_urls[i]}\n"
            print(temp_print)
        print("=====================")


    elif save_method == 2:
        with open("result.txt", "w", encoding="utf-8") as file:
            for i, track in enumerate(tracks_name):
                temp_print = "=====================\n\n"
                temp_print += f"Full name: {track} - {tracks_authors[i]}\n"
                temp_print += f"Name: {track}\n"
                temp_print += f"Author: {tracks_authors[i]}\n"
                temp_print += f"Preview: {preview_urls[i]}\n"
                temp_print += f"Track url: {tracks_urls[i]}\n\n"
                file.write(temp_print)
            file.write("=====================")
            file.close()
            print()
            print("Write done!")

    else: 
        return "no save method found! stoped!"
    
    return "done"



class SpotifyParser:

    def __init__(self, spotify_link=None, api_answer=None, save_method=None, 
                    spotify_method=None, spotify_track_id=None, tracks_urls=None) -> None:

        self.spotify_link = spotify_link
        self.api_answer = api_answer
        self.save_method = save_method
        self.spotify_method = spotify_method
        self.spotify_track_id = spotify_track_id
        self.tracks_urls = tracks_urls



    def get_api_answer(self):

        if "playlist" in self.spotify_link:
            api_answer = sp.playlist_items(self.spotify_link)
            spotify_method = "playlist"
        elif "album" in self.spotify_link:
            api_answer = sp.album_tracks(self.spotify_link)
            spotify_method = "album"
        elif "track" in self.spotify_link:
            api_answer = sp.track(self.spotify_link)
            spotify_method = "track"
        else:
            return "no keywords found in the link"
        
        return (api_answer, spotify_method)



    def get_tracks_data(self):

        if self.spotify_method == "playlist":
            preview_urls = list()
            tracks_name = list()
            tracks_authors = list()
            tracks_urls = list()
            for item in self.api_answer.get('items'):
                artists_name = list()
                tracks_urls.append(item.get('track').get('external_urls').get('spotify'))
                track_name = item.get('track').get('name')
                for artists in item.get('track').get('artists'):
                    artists_name.append(artists.get('name'))
                preview_urls.append(item.get('track').get('album').get('images')[0].get('url'))
                tracks_name.append(track_name)
                tracks_authors.append(', '.join(artists_name))



        elif self.spotify_method == "album":
            preview_urls = list()
            tracks_name = list()
            tracks_authors = list()
            tracks_urls = list()
            for item in self.api_answer.get('items'):
                artists_name = list()
                tracks_urls.append(item.get('external_urls').get('spotify'))
                track_name = item.get('name')
                for artists in item.get('artists'):
                    artists_name.append(artists.get('name'))
                tracks_name.append(track_name)
                tracks_authors.append(', '.join(artists_name))
                preview_urls.append(SpotifyParser(spotify_track_id=self.api_answer.get('items')[0].get('id')).get_preview())



        elif self.spotify_method == "track":
            preview_urls = list()
            tracks_name = list()
            tracks_authors = list()
            tracks_urls = list()
            artists_name = list()
            tracks_name.append(self.api_answer.get('name'))
            tracks_urls.append(self.api_answer.get('external_urls').get('spotify'))
            for artists in self.api_answer.get('artists'):
                artists_name.append(artists.get('name'))
                tracks_authors.append(', '.join(artists_name))
            preview_urls.append(self.api_answer.get('album').get('images')[0].get('url'))

        return (tracks_name, tracks_authors, preview_urls, tracks_urls)



    def get_preview(self):
        local_method = sp.track(self.spotify_track_id)
        return local_method.get('album').get('images')[0].get('url')



if __name__ == "__main__":
    manager()
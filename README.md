# Spotify-data-parser
Simple Spotify parser on spotify link 

**Distributed by MIT correspondence**
## Content
- [Appointment](#Appointment)
- [Installation](#Installation)
- [Technical information](#Technical-information)
- [From the author](#From-the-author)


## Appointment
This script can parse data on the spotify link. This can help those who need to copy the name of the song or the author in the application, but can't do it. You just need to put a link in the script and it will give a list of track data (in the terminal or in txt). It also gives a link to the image of the track (album) in high resolution, and a full https:/ / link to this track!

## Installation
+ `git clone https://github.com/AleksZavg/spotify-data-parser`
+ `cd spotify-data-parser`
+ `pip install -r requirements.txt`
+ Then open `.env` file and paste your `spotify client id` and `spotify client secret`
+ `python main.py`


## Technical information
+ The `spotipy` library was used
+ The script uses environment variables
+ To use this script, you need a `client id` and `client secret`. You can get them at this [link](https://developer.spotify.com/dashboard/applications). You need to create your own application and take these variables

## Images
*You can find all the images in the `for_readme` folder in the repository of this project*

## From the author
Written in a hurry, mistakes are possible! During processing, lists with the received data appear, they can be taken from the class functions (this is if you will use these developments)

**Good luck to everyone and goodbye!**


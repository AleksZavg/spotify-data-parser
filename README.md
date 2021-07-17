# Spotify-data-parser
Simple Spotify parser on spotify link 

**Distributed by MIT correspondence**
## Content
- [Appointment](#Appointment)
- [Example](#Example)
- [Installation](#Installation)
- [Technical information](#Technical-information)
- [From the author](#From-the-author)


## Appointment
This script can parse data on the spotify link. This can help those who need to copy the name of the song or the author in the application, but can't do it. You just need to put a link in the script and it will give a list of track data (in the terminal or in txt). It also gives a link to the image of the track (album) in high resolution, and a full `https://` link to this track!

## Example
+ Sample data you get
```
Full name: Fashion Week - cry, Blackbear gg
Name: Fashion Week
Author: cry, Blackbear gg
Preview: https://i.scdn.co/image/ab67616d0000b273d33e9719ece26fe8dfd477a1
Track url: https://open.spotify.com/track/2lbv1Xcy06X4a0jRwlGgo1
```
*Track image (Preview) in 640x640 resolution*

*You can find more the images and gif in the `for_readme` folder in the repository*
### Animated process
![example](https://github.com/AleksZavg/spotify-data-parser/blob/main/for_readme/bandicam-2021-07-07-11-35-44-113.gif)

## Installation
+ `git clone https://github.com/alekszavg/spotify-data-parser.git`
+ `cd spotify-data-parser`
+ `pip install -r requirements.txt`
+ Create `.env`
+ Then open `.env` file and paste your `spotify_client_id` and `spotify_client_secret` ([get-this-data](https://developer.spotify.com/dashboard/applications))
  ```
  spotify_client_id = fa9bede2000000f15ab9d8ea000000
  spotify_client_secret = 74c6f0000045b5818a00000
  ```

+ `python main.py`


## Technical information
+ The `spotipy` library was used
+ The script uses environment variables
+ To use this script, you need a `client id` and `client secret`. You can get them at this [link](https://developer.spotify.com/dashboard/applications). You need to create your own application and take these variables

## From the author
Written in a hurry, mistakes are possible! During processing, lists with the received data appear, they can be taken from the class functions (this is if you will use these developments)

**Good luck to everyone and goodbye!**


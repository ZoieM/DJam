## What is DJam?

DJam is a playlist maker for individuals or groups who want to listen to music they like.
DJam is unique from popular music-streaming products and playlist creators because our playlist-maker allows you to create a playlist from 10 artists, considers how much you like each artist, will only play songs from those artists, and provides an *optimized shuffle*.

DJam was created as a class for SJSU's CMPE 130 (Advanced Algorithm Design) course in May 2018. 

## Screenshots
View [screenshots of DJam](https://drive.google.com/open?id=1IJF1vtW0gZK29yjdATwMqLA02eoJ9oma) on Google Drive.


## How to use DJam? 

### User Interaction

DJam is your personal DJ! Top Hits or Shuffle? No Problem! 
Just specify ten artists that you want to listen to and rate them on a scale from 1 to 10. 

When you are done, hit submit and DJam will create two playlists for you: 
+ **"Top Hits" Playlist:** Orders songs by general popularity and the ratings you provided for each artist.
+ **Optimally Shuffled Playlist:** Shuffles songs using an original "shuffle sort" which makes sure that each artist is spread throughout the playlist, yet still provides a random order. This is done by making sure that, until you reach the end of the playlist, no artist will repeat until at least 3 songs by 3 different artists have played.

### Technical Details

Behind the scenes DJam utilizes the last.fm music API to get popular song names from the artists you want to listen. DJam was written using Python, Bootstrap HTML/CSS, Flask, and Jinja. DJam also utilizes stacks, queues, quick sort, and shuffle sort to order your songs for the final playlist (and to meet the original class project criteria). 


## References
For more information about DJam and how it works, see our [project report](https://docs.google.com/document/d/1t4lra4Y8d6ZxTvt9qrVTB1N2tIzRZsWfOKWSUc7s10A/edit?usp=sharing) and [presentation](https://docs.google.com/presentation/d/1bSaVDmS7Xv7JTu0Q2g2tChNnQPSuKaIFrv2RCTo1Yyk/edit?usp=sharing).

Developed in May 2018 by Navina Mathew • Priyank Varshney • Zoie MacDougall

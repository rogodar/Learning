To export your own Library.xml from iTunes 

File -> Library -> Export Library

Make sure it is in the correct folder.   Of course iTUnes might change
UI and/or export format any time - so good luck :)

---- Worked Example: Tracks.py -----------------------------------
SELECT Track.title,Album.title,Artist.name from Track join Album join Artist on Track.album_id=Album.id and Album.artist_id=Artist.id
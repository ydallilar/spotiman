# spotiman

A high level wrapper around spotipy. The projects is in early stages so the functionality is very limited for now.

Also, includes spotiman_simple_curses executable, a simple experiment for a curses spotify player. It only manages Spotify Connect devices, doesn't do anything by itself. The curses application uses ncmpcpp keybindings.

![Screenshot](https://github.com/pssncp142/spotiman/blob/master/screenshot.png)

I have no ambitious objectives for this project. It is mostly a playground for me. But, if you have suggestions or comments, fell free to let me know. 

TODO:

- Release curses app as a module so others can contribute for new tabs.
- Event based kill on the threads

# Log

2018-10-02 : 

	- Added playlist window. 
	- Fix resizing terminal window
	- Enable scrolling for long lists

2018-10-08 :

	- Solved refreshing token

2018-10-15

	- SpotifyObject class and inherited classes. Now, revised version of spotipy.Spotify returns objects. (ongoing)



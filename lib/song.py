class Song:
    count = 0
    genres =set()
    artists =set()
    genre_count={}
    artist_count={}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count +=1
        Song.add_to_genre(genre)
        Song.add_to_artists(artist)
        Song.add_genre_count(genre)
        Song.add_artist_count(artist)

    # @classmethod
    # def add_song_to_count(cls):
       
    #    cls.count +=1
    
    
    @classmethod
    def add_to_genre(cls, genre):
        # checks genres list if genre is unique then append to genres list
        # for genres in genre if genres
        # x for x in genre if 
        Song.genres.add(genre)
        pass
    @classmethod
    def add_to_artists(cls, artist):
        Song.artists.add(artist)

    @classmethod 
    def add_genre_count(cls, genre):
        # each key of gengre name should point to the number of songs in that value
        # so when 
       if cls.genre_count.get(genre)== None:
           cls.genre_count.update({genre: 1})
       else:
           cls.genre_count[genre]+=1

    @classmethod
    def add_artist_count(cls, artist):
        if cls.artist_count.get(artist) ==None:
            cls.artist_count.update({artist: 1})
        else:
            cls.artist_count[artist]+=1



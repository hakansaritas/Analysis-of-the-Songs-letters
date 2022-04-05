# ######################################################################
# ##########   NUMBER OF THE LETTERS IN THE LYRIC ! ####################

# This work is about calculation of frequency of the unique letters in band lyrics
# using basic python commands. 

# important: lyric input should be written as English Language.

# I have written this function to improve myself,give useful
# ideas to python users and get fun.

# for much more information how to use this function, visit my Medium page

# I would want to dedicate this my first public function to "Ronnie James DIO" and "Rainbow"...
# which are the one the best rock vocals and music band in the universe.

# I am opening to suggestions and corrections
# Thanks
# ######################################################################
# ############# HOW TO EXECUTE ! ############
### to run lyric_letter function uncomment below command
# artist_list =["DIO","Whitesnake"]
# exam: letters_of_songs(artist_list, 5)
# ######################################################################

# Contact Detailed:
# ======================================================================
# Hakan SARITAŞ
# linkedin : www.linkedin.com/in/hakansaritas
# Mediuum: https://hakansaritas.medium.com/
# GitHub: https://github.com/hakansaritas
# kaggle: https://www.kaggle.com/hakansaritas
# ======================================================================

# pip install lyricsgenius


import pandas as pd
from lyricsgenius import Genius
pd.set_option('display.max_columns', None)

api_key = "CPZ6u-zmCHAckkq_AvhlQPTdVQwM01UF44JIKOJiwT4TlrAngggD_HXpmY3tk9XZ"


def letters_of_songs(list_of_bands=["Rainbow"], num_of_song=2):
    """
    calculation of frequency of the unique letters in lyrics writing in english.

    Args:
        List_of_bands : Artist names you want to analyze, list
        num_of_song: number of songs requested for each artist, int 
        
    Returns:
        artist_name: artist name,str
        artist_id: groups ID, int
        song_name: song name, str
        song_id: song ID, int
        A : frequency of A letter,int
        …
        Z: frequency of Z letter,int
        
    Note:
        This function outputs both an excel and a csv

    """
    # Genius function with api key

    genius = Genius(api_key, timeout=120, remove_section_headers=True, verbose=False)
    
    df = pd.DataFrame()
    
    
    for band in list_of_bands:
    
        artist_all_lyrics = genius.search_artist(band, max_songs=num_of_song)
    
        for i in range(num_of_song):
            
    # getting songs,artists names and IDs                 
            try:
                lyric_before = artist_all_lyrics.songs[i].lyrics
                song_name = artist_all_lyrics.songs[i].title
                song_id = artist_all_lyrics.songs[i].id
                artist_id = artist_all_lyrics.id
                artist_name = artist_all_lyrics.songs[i].artist
    # upper case    
                lyric_after = lyric_before.split("\n", 1)[1]
                lyric_after = lyric_after.upper()

    # letters list to be searched   
                english_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
                                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                number_list = []
    
                for i in english_alphabet:
                    
                    number_list.append(lyric_after.count(i))
    
                zipped_dict = dict(zip(english_alphabet, number_list))
                
   # assignment to variables 
                info_dict = {"artist_name": artist_name,
                             "artist_id": artist_id,
                             "song_name": song_name,
                             "song_id": song_id}
    
                info_dict.update(zipped_dict)
    
                last_list = [info_dict]
    
                frame = pd.DataFrame(last_list, columns=info_dict.keys())
    
                df = df.append(frame, True)
    
            except (AttributeError, IndexError):
    
                continue

    # output             
    df.to_excel("all_songs_deneme.xlsx")
    df.to_csv("all_songs_deneme")
            




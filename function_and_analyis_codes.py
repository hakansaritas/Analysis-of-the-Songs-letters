import pandas as pd
from lyricsgenius import Genius

# set rows and cols display
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

pd.set_option('display.max_columns', None)

api_key = "ENTER YOUR API KEY"

# describe the function
def letters_of_songs(list_of_bands=["Rainbow"], num_of_song=2):
    """
    calculation of frequency of the unique letters in lyrics writing in english.

    Args:
        list_of_bands : Artist names you want to analyze, list
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
    df.to_excel("hard_rock_dataset.xlsx", index=False)

# create artist list
artist_list =['Judas Priest', 'AC/DC', 'Black Sabbath', 'Aerosmith',
       'Iron Maiden', 'Van Halen', 'Mr. Big', 'Guns N’ Roses', 'Kiss',
       'Motörhead', 'Def Leppard', 'Bon Jovi', 'Scorpions', 'Europe',
       'Damn Yankees', 'Accept', 'Saxon', 'Bad English', 'Foreigner',
       'Triumph', 'Boston', 'Nazareth', 'Bad Company',
       'Michael Schenker Group', 'Whitesnake', 'Quiet Riot', 'Extreme',
       'April Wine', 'Uriah Heep', 'Cinderella', 'Molly Hatchet',
       'Prince', 'Autograph', 'Twisted Sister', 'Rainbow', 'Vandenberg',
       'Loverboy', 'Gamma Ray', 'Survivor', 'Dokken', 'Hanoi Rocks',
       'Grim reaper', 'Loudness', 'Tora Tora', 'Poison', 'Great White',
       'White Lion', 'Danger Danger', 'Tesla', 'Baton Rouge', 'Lordi',
       'Saigon Kick', 'Firehouse', 'Dangerous Toys', 'A Salty Dog',
       'Vinnie Vincent Invasion', 'Night Ranger', 'Thundercat', 'Winger',
       'Stryper', 'L.A. Guns', 'Young the Giant', 'Tyketto',
       'Brooks & Dunn', 'Steelheart', 'W.A.S.P.', 'Tora', 'Mötley Crüe',
       'ZZ Top', 'Current Joys', 'Helix', 'Golden Earring', 'TNT Boys',
       'Skid Row', 'Whitecross', 'Steeler', 'BulletBoys', 'Vixen',
       'Danzig', 'Faster Pussycat', 'Lynch Mob', 'Shotgun Messiah',
       'Blue Murder', 'Trixter', 'King Cobra', 'Wrathchild America',
       'Hurricane', 'Babylon A.D.', 'Junkyard', 'House of Lords',
       'South Gang', 'Love/Hate', 'Fastway', 'Bang Tango', 'Rockhead',
       'Femme Fatale', 'Moxy', 'Lee Aaron', 'Krokus', 'Coney Hatch',
       'The Rods (Band)', 'Manilla Road', 'Leatherwolf', 'Rush', 'Asiana',
       '38 Special', 'Thin Lizzy', 'Badlands', 'Stone Fury',
       'Alice Cooper', 'Father',
       'Star-Lord Band, Steve Szczepkowski & Yohann Boudreault',
       'Kingdom Come', 'Ozzy Osbourne', 'Journey', 'Foo Fighters',
       'Kick Axe', 'Fiona Apple', 'Treat', 'Fifth Angel', 'Savatage',
       'Warlock', 'Bangalore Choir', 'Pretty Maids', 'Rock Goddess',
       'Blackfoot', 'Circus Of Power', 'Jetboy', 'Britny Fox',
       'Tygers of Pan Tang', 'Madam X', 'Killer Dwarfs', 'Girlschool',
       'Zebra', 'Giuffria', 'Phantom Blue', 'Lizzy Borden', 'Bonfire',
       'Pretty Boy Floyd', 'Chastain', 'Black ’N Blue', 'Ace Frehley',
       'Tublatanka', 'Rage N’ Rox', 'REO Speedwagon', 'Tokyo Blade',
       'Alcatrazz', 'Lillian Axe', 'Bitter:Sweet', 'Agent Steel',
       'Rose Tattoo', 'Jaded Heart', 'Rough Cutt', 'Afterhours',
       'Ray LaMontagne & the Pariah Dogs']

# call the function
letters_of_songs(artist_list,10)

# read excel
df_= pd.read_excel(r"F:\python_workspace\VBO\python\letter_analysis_hakan\hard_rock_dataset.xlsx")
df = df_.copy()

#discovering the dataset
df.shape
df.nunique()
df.isnull().sum()

# create new variable which shows total letter number of each song
df["song_sum"] = df.loc[:,"A":"Z"].apply(lambda x: x.sum(),axis=1)
df.head(2)

# how many song name are the same
(df.loc[df[["song_name"]].duplicated()]).count()

# find dublicated
df.loc[df.duplicated(["song_name","song_sum"])]

# describe the song_sum variable
df["song_sum"].describe()

# how many letters does each band has
df.groupby("artist_name"). agg({"song_sum":"mean"}).\
                    sort_values("song_sum",ascending=False).tail()

# which song has not been used letter of "A"
df.loc[df["A"] == 0, ["artist_name","song_name"]]



# calculate percentage of each letter and create new dataframe
each_letter = df.loc[:,"A":"Z"].apply(lambda x: x.sum(),axis=0)

df_perc = pd.DataFrame(each_letter, columns=["sum_each_letter"])

df_perc["percentage"]  = df_perc["sum_each_letter"]/df_perc["sum_each_letter"].sum()*100

df_perc.head()



# creta reference percentage variable
list_of_ref = [8.12, 1.49, 2.71, 4.32, 12.02, 2.30, 2.03, 5.92,
                7.31, 0.10, 0.69, 3.98, 2.61, 6.95, 7.68, 1.82,
                0.11, 6.02, 6.28, 9.10, 2.88, 1.11, 2.09, 0.17,
                2.11, 0.07  ]

df_perc["ref_percentage"] = list_of_dict
df_perc = df_perc.round({"percentage":2})
df_perc

# comparing the percentages
df_perc[["percentage"]].sort_values("percentage",ascending=False).head()
df_perc[["ref_percentage"]].sort_values("ref_percentage",ascending=False).head()


######################### Plot bar graphs ##########################

import matplotlib.pyplot as plt

plt.style.use('seaborn')

df1= df_perc.loc[:,"percentage"].sort_values()
df2 = df_perc.loc[:,"ref_percentage"].sort_values()

# BAR
fig, (ax, ax2)  = plt.subplots(nrows=1, ncols=2, figsize=(15,10))

ax.invert_xaxis()
ax.yaxis.tick_right()


df1.plot(kind='barh', x='LABEL',  legend=False, ax=ax)
df2.plot(kind='barh', x='LABEL', ax=ax2)


ax.set_xlabel('percentage [%]')
ax2.set_xlabel('percentage [%]')
ax.set_ylabel("LETTERS", fontweight='bold')

ax.set_title("Percentage of the Each Letter in lyrics ",fontweight='bold')
ax2.set_title("Reference Percentage of the Each Letter",fontweight='bold')
plt.show()


#################### Plot pie charts ##########################
import matplotlib.pyplot as plt
import numpy as np

np.zeros(26)

myexplode = [0.2, 0., 0., 0., 0.2, 0., 0., 0., 0., 0., 0., 0., 0., 0.2, 0.2, 0., 0., 0.,
       0., 0.2, 0., 0., 0., 0., 0., 0.]

myexplode2 = [0.2, 0., 0., 0., 0.2, 0., 0., 0., 0.2, 0., 0., 0., 0., 0., 0.2, 0., 0., 0.,
       0., 0.2, 0., 0., 0., 0., 0., 0.]


fig = plt.figure(figsize=(15,10))

ax1 = fig.add_subplot(121)
ax1.pie(df_perc.percentage, labels = df_perc.index, startangle = 90, explode = myexplode)

ax2 = fig.add_subplot(122)
ax2.pie(df_perc.ref_percentage, labels = df_perc.index, startangle = 90, explode = myexplode2)

ax1.set_title("Percentage of the Each Letter in lyrics\n ",fontweight='bold')
ax2.set_title("Reference Percentage of the Each Letter\n",fontweight='bold')

plt.show()
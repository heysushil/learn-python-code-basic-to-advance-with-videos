# Class: OOP's

'''
OPP's:

1. same code use multiple time
2. OPP's have 2 behaviours:
    Class:
        attributes : varaibel
        behavior : fucntion => mehtods

    Construcer method: __init__(): it's like wild card entry to all exising methods in class and by use construcet will will pass values as cureent instance to all methos


Example: attributes: singer, songName        
    behavior: singleDetail
'''

class Album:
    # pass
    # these 2 are attributes of class ALbum
    # creating constructer
    def __init__(self, singer, songName):
        # self is a current instance. and we are creating 2 instace for singer and song name
        self.s = singer
        self.sn = songName

    def newSongAlbumDetail(self):
        print('''
        -----------------------------       
            New Album name
        -----------------------------
        Singer Name: {}
        Songe Name: {}
        '''.format(self.s,self.sn))

    def oldSongAlbumDetail(self):
        print('''
        -----------------------------
            Old Albume Detial
        -----------------------------
        Singer Name: {}
        Song Name: {}            
        '''.format(self.s,self.sn))


# after creating class you will use the class by object
singerName = input('Enter singer name: ')
songName = input('Enter song name: ')
albumObject = Album(singerName, songName)
# accessing constru values
print('\nGet song name: ',albumObject.sn)

# calling album detail methos
# condtion to categrise the old and new song by singer name
if singerName == 'Mukesh' or singerName == 'Lata':
    albumObject.oldSongAlbumDetail()
elif singerName == 'Ajeet' or singerName == 'Shreya':
    albumObject.newSongAlbumDetail()
else:
    print('\nSorry to say that your song coulnt find.')    

# by object access album class arrtibute singer
# print('\nalbumObject.singer: ',albumObject.singer,' \nSong Name: ',albumObject.songName)

'''
1. creat a class of programming languages in which you get your input of program name and behalf of program name you have different methods which show all basic information about the programming langaue but remeber when user input the programm name then you will use right methods for that.
like as: if user input python then you have python mehtods to call and in whihc you will use multiline sting to show the basic info of python.

2. create a mobile class in which if use input mobile comany name and modal name if these details exists then use the right methods to shwo the model detils.
Like as user input comany name : samsung and model name: galaxy so by that you have to use your method to shwo the galaxy model details if detials not exists then show a default message.
'''

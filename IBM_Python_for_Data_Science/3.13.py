#function collecting arguments

def ArtistNames(*names):
    for name in names:
        print(name)
# * before the parameter name means that the function can receive a variable number of arguments.

ArtistNames("Michael Jackson", "AC/DC", "Pink Floyd", "Guns N' Roses")
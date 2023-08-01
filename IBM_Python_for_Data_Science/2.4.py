# sets are unordered collections of unique elements

Set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(Set1)
#duplicate elements are removed


album_list = ["Michael Jackson", "Thriller","Thriller", 1982]
album_set = set(album_list)
album_set
#convert list to set



A = {"Thriller", "Back in Black", "AC/DC"}

A.add("NSYNC")
#add element to set

A.remove("NSYNC")
#remove element from set

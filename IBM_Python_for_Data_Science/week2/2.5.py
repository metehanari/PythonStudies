#sets


album_set1 = {"AC/DC", "Back in Black", "Thriller"}

album_set2 = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}

album_set3 = album_set1 & album_set2
#intersection of sets. & is the intersection operator


album_set1.union(album_set2)
#union of sets. | is the union operator or use union method
album_set4 = album_set1 | album_set2



album_set3.issubset(album_set1)
#check if subset. issubset is the subset method. returns boolean
# while loops

squares = ["orange", "orange", "purple", "blue", "orange"]

newsquares = []

i = 0

while squares[i] == "orange":
    newsquares.append(squares[i])
    i = i + 1

print(newsquares)   




#############################################

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0 #initialize counter
Rating = PlayListRatings[0] #initialize Rating
while(i < len(PlayListRatings) and Rating >= 6): 
    print(Rating)
    i = i + 1 
    Rating = PlayListRatings[i] 
# this loop will print out all the elements in the list until it hits a number less than 6.    
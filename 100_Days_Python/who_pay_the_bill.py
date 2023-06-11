import random

names_str = input("Add names and seperated by a comma\n") #add names

names = names_str.split(",") #split with comma

names_len = len(names) #length of list

rand_int = random.randint(0,names_len-1) #pick a random number as long as list

pick_from_list = names[rand_int] #pick a random index

#print(f"{pick_from_list} is going to pay!")

print(names)

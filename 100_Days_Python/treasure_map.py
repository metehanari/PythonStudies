row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
 
map = [row1,row2,row3]
 
print(f"{row1}\n{row2}\n{row3}")
print(map)
position = input("Where do you want to put the treasure? ") ##💰##

new_list = list(position) #split numbers to a list

index1 = int(new_list[0]) - 1
index2 = int(new_list[1]) - 1

map[index2][index1] = "💰"

print(f"{row1}\n{row2}\n{row3}")

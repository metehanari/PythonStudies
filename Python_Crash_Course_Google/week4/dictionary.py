#definition of dictionary.
file_counts = {"jpeg":10, "txt":14, "csv":2, "py": 23}

print(file_counts)

print(file_counts["txt"])
#print value

file_counts["cfg"] = 4
#add key,value
print(file_counts)

del file_counts["txt"]
#delete key
print(file_counts)

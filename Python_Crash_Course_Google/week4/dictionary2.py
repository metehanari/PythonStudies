#dictionary .items() method
file_counts = {"jpeg":10, "txt":14, "csv":2, "py": 23}

for extension,amount in file_counts.items():
    print("There are {} files .{} extensions".format(amount,extension))
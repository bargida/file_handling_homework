def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    # large_row = 0
    # for i in data:
    #     if len(i)>large_row:
    #         large_row = len(i)
    # return large_row
    large_char = data[0]

    for i in range(len(data)):
        if len(data[i]) > len(large_char):
            large_char = data[i]
    return large_char[:-1]

# Read data from file
df = open('./data/data10.txt').readlines()
print(main(df))
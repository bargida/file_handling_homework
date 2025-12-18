def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    total = 0
    for char in data:
        if char.isdigit():
            total+=1
    return total
# Read data from file

df = open('./data/data07.txt').read()
print(main(df))
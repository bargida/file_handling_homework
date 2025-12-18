def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    length = []

    for i in data:
        length+=[len(i)-1]
    return [length]
    
# Read data from file
df = open('./data/data06.txt').readlines()
print(main(df))
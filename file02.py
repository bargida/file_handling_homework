def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    res = len(data)
    return res

# Read data from file
data = open('./data/data01.txt').read()
print(main(data))
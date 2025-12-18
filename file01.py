def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    return data.split(',')
# Read data from file
data = open('./data/data01.txt').read()

print(main(data))
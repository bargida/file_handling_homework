def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    non_digit =[]
    for char in data:
        if not char.isdigit():
            non_digit+=[char]
    return non_digit

    
# Read data from file
df = open('./data/data04.txt').read()

print(main(df))
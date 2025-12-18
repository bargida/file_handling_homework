def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    min_value=10
    for i in data:
        if i.isdigit():
            if int(i)<min_value:
                min_value=int(i)
    return min_value

df = open('./data/data09.txt').read()
print(main(df))


# Read data from file
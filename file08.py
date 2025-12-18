def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    max_value=-1
    for i in data:
        if i.isdigit():
            if int(i)>max_value:
                max_value=int(i)
    return max_value

# Read data from file
df = open('./data/data08.txt').read()
print(main(df))
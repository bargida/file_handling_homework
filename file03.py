def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    digits =[]
    for num in data:
        if num.isdigit():
            digits+=[num]
    return digits
# Read data from file
df = open('./data/data03.txt').read()

print(main(df))
def min_ind(x):
    y = int(x * 1_000_000)
    print("{:,}".format(y).replace(",", "_"))  # US format with _ instead of ,
    print(format_indian(y))

def format_indian(n):
    s = str(n)
    # First group: last 3 digits
    r = s[-3:]
    s = s[:-3]
    # Rest: group by 2 digits
    while len(s) > 0:
        r = s[-2:] + "," + r
        s = s[:-2]
    return r

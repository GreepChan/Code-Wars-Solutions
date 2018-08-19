def find_short(s):
    return len(min([x for x in s.split(' ')],key=len))
    
print(find_short('asda as is aaaa a'))
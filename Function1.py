a = 'AbC'
b = 'HiAbc'
str1 = a.lower()
str2 = b.lower()
def strbits(s1,s2):
    if len(s1) > len(s2):
        res = s1[slice((len(s1) - len(s2)),len(s1))]
        if(res == s2):
            return True
        else:
            return False
    else:
        res = s2[slice((len(s2) - len(s1)),len(s2))]
        if(res == s1):
            return True
        else:
            return False

print(strbits(str1, str2))

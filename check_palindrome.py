#回文であるか、判断する関数
#A function that determines whether or not it is a palindrome
def kaibun(str):
    if str == str[::-1]:
        return True
    return False

print(kaibun('noon'))
print(kaibun('level'))
print(kaibun('cat'))
print(kaibun('python'))
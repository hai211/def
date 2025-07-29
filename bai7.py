def kiem_tra_palindrome(s:str) -> bool:
    s = s.replace(" ","")
    s = s.lower()
    return s == s[::-1]
print(kiem_tra_palindrome("A man a plan a canal Panama"))
# print(kiem_tra_palindrome("hello world"))

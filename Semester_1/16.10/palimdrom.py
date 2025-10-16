
s = input("Gib ein Wort ein: ")

isPalindrome = True
idx = 0

while idx < len(s)//2:
    
    
    
    if s[idx] == s[len(s)-1-idx]:
        isPalindrome = False
    
    idx += 1
        
print("Das Wort ist ein Palindrom:", isPalindrome)
        
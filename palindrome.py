def checkPalindrome(list):
    i = 0
    while i < len(list):
        if list[i] == list[-i-1]:
            return True
        return False

print(checkPalindrome("Tamhid"))
import math

def findEncryptedWord(s):
    if len(s) <= 2: return s 
    middle_len = int(len(s)/2)
    middle = middle_len-1 if middle_len%2==0 else middle_len
    new_word = s[middle] + \
                findEncryptedWord(s[:middle]) + \
                findEncryptedWord(s[middle+1:])
    return new_word

if __name__ == '__main__':
    R = []
    R.append("abc") # bac
    R.append("abcd") # bacd
    R.append("abcxcba") # xbacbca
    R.append("facebook") # eafcobok
    for r in R:
        print(r,findEncryptedWord(r))
        

    
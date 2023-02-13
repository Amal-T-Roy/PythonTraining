def AnagramChecker(S1,S2) :
    """
    Function that checks if second string can be made by rearranging letters
    In first string
    """
    if(sorted(S1) == sorted(S2)) :
        print('Anagram Detected')
    else :
        print('Not Anagram')

def PalindromeChecker(P1) :
    if(P1 == P1[::-1]):
        return True
    else:
        return False
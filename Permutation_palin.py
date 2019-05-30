"""
Given a string, write a function to check if it is a permutation
of a palindrome. A palindrome is a word or phrase that is the same 
forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words
"""

palin_perm_1 = "cat oo cat" # cato otac
palin_perm_2 = "Taco Cat" # Taco cat
palin_perm_3 = "tttt" # crazy, but still!
not_palin_perm = "This is not a palindrome permutation"

def is_palin_perm(s):
    s = s.replace(" ","").lower()
    d = dict()

    for i in s:
        if i in d:
            d[i] += 1
        else: 
            d[i] = 1
    
    ct_1, ct_2 = 0, 0
    for _, v in d.items():
        if v==2:
            ct_2 += 1
        elif v==1:
            ct_1 += 1
        elif len(d)==1 and v%2==0:
            return True
        else:
            return False
                
    if ct_1 == 1 or ct_2 == len(s)/2:
        return True
    else:
        return False

# True
print(is_palin_perm(palin_perm_1))
print(is_palin_perm(palin_perm_2))
print(is_palin_perm(palin_perm_3))
# False
print(is_palin_perm(not_palin_perm))    
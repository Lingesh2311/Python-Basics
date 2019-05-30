"""
Function to find if the given pair of strings a permutation of each other.
"""

is_permutation_1 = "dog"
is_permutation_2 = "gof"

not_permutation_1 = "Pot cl e a r"
not_permutation_2 = "Top clear"

def is_perm_1(s1, s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if len(s1) != len(s2):
        return False
    
    # Sorting the strings
    s1 = ''.join(sorted(s1)) # general form to join a list of characters to a string
    s2 = ''.join(sorted(s2))
    
    return s1==s2

print(is_perm_1(is_permutation_1,is_permutation_2))
print(is_perm_1(not_permutation_1,not_permutation_2))
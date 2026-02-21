s1 = "RULES"
s2 = "LESRU"

def check_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    
    d1 = {}
    d2 = {}
    
    for i in s1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    
    for i in s2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
            
    for i in d1:
        if i in d2:
            if d1[i] != d2[i]:
                return False
        else:
            return False
    
    return True


def CheckAnagrams(str1, str2):
    # Case: when both of the strings have different lengths
    if len(str1) != len(str2):
        return False

    # Initialize a frequency array to store character counts
    freq = [0] * 26

    # Count frequency of each character in str1
    for char in str1:
        freq[ord(char) - ord('A')] += 1

    # Decrement frequency for each character in str2
    for char in str2:
        freq[ord(char) - ord('A')] -= 1

    # Check if all frequencies are zero
    for count in freq:
        if count != 0:
            return False

    return True


print(check_anagrams(s1, s2))
print(CheckAnagrams(s1, s2))

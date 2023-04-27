from collections import Counter


def canConstruct(ransomNote, magazine):
    note, maga = Counter(ransomNote), Counter(magazine)
    if note & maga == note:
        return True
    return False


print(canConstruct("aa", "aab"))

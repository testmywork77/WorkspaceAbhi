w = input("Enter a word")

s = set(w)

set1 = {"a", "e", "i", "o", "u"}

b = s.intersection(set1)

print(f"Vowels in {w} are {b}")
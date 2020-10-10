l=["A", "B", "C"]

x=len(l)

for i in range(x):
    print(f"{l[i]} is available at positive index {i} and at negative index {i-x}")
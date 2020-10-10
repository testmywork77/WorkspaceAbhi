cart = [10,20,30,40]
for item  in cart:
    if item>=100:
        print("Error")
        break
    print(item)
else:
    print(f"item ordered")
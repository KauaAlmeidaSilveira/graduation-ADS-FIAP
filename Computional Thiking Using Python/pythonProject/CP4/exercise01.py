listPrice = [100, 200, 300, 400, 500]
listUnit = [1, 2, 3, 4, 5]
listDiscount = [0.5, 0.5, 0.5, 0.5, 0.5]

listFinalPrice = list(map(lambda x, y, z: (x - (x*z))*y, listPrice, listUnit, listDiscount))

print(f"A) {listFinalPrice}")

listRandomValues = [10,10,11,11]

listResult = list(map(lambda x: x+5 if x%2 ==0 else x-2, listRandomValues))

print(f"B) {listResult}")

listWords = ["Hello", "World", "In", "Python", "Programming", "Language"]

listWordsToLowerCase = list(map(lambda x: x.lower(), listWords))

print(f"C) {listWordsToLowerCase}")



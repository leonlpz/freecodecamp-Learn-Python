lucky_numbers = [42, 88, 9, 60, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Jim", "Oscar", "Toby" ]
friends2 = friends.copy()
friends[1] = "Mike"
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove(42)
#friends.clear()
friends.pop()
print(friends.index(60))
print(friends.count("Jim"))
del friends[9:]
friends.sort()
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)

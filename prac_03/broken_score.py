score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("invalid score")
elif score >= 90:
    print("Excellent!")
elif score >= 50:
    print("Passable")
else:
    print("bad")

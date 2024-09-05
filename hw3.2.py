grade: int = int(input("Enter a grade and get it in a string (0-100):"))

if grade >= 0 and grade <= 40:
    print("try harder next time...")
elif grade >= 41 and grade <= 60:
    print("you're getting there, need some more work")
elif grade >= 41 and grade <= 60:
    print("pretty good!!")
elif grade >= 81 and grade <= 95:
    print("awesome!")
elif grade >= 96 and grade <= 100:
    print("excellent!!!, you are a star")
else:
    print("invalid grade!.")

# end

# start

grade: int = int(input("Enter a grade (0-100):"))

match grade:
    # if grade >= 0 and grade <= 40
    case 1:
        print ('try harder next time!')
    # elf grade >= 41 and grade <= 60
    case 2:
        print ("you're getting there, need some more work")
    # elf grade >= 41 and grade <= 60
    case 3:
        print (" pretty good!!")
    # elf grade >= 81 and grade <= 95
    case 4:
        print ("awesome")
    # elf grade >= 96 and grade <= 100
    case 5:
        print ("excellent!!!, you are a super star!!")
    # else
    case 6:
        print ('invalid grade')

# end




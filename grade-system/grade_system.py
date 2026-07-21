def grade(mark):
    try:
        if (mark >= 90 and mark <=100):
            return 'A'
        elif(mark >=80 and mark <=89):
            return 'B'
        elif(mark >=70 and mark <=79):
            return 'C'
        elif(mark >=60 and mark <=69):
            return 'D'
        elif(mark<=60 and mark>=50):
            return 'E'
        else:
            return 'F'
        
    except Exception as e:
        return print('Error:',e)
        
grade(33)
print(grade(33))

mark = int(input("Enter Your Mark: "))

print("Your Grade is:",grade(mark))

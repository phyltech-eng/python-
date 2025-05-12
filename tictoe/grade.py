import random

def get_marks():
    marks=int(input("Enter your marks: "))
    return marks

def grading(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C+"
    elif marks >= 40:
        return "C"
    else:
        return "F"
def show_results(name,marks ,grade):
        print("your name is: ",name)
        print("your marks are: ", marks)
        print("Your grade is: ", grade)
def main():
            name=input("Enter your name: ")
            marks=get_marks()
            grade=grading(marks)
            show_results(name,marks,grade)


main()

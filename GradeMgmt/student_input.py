def myInput(student) :
    name = input("Eneter your name : ")
    kor = int(input("Enter your Korean Grade : "))
    eng = int(input("Enter your English Grade : "))
    math = int(input("Enter your Math Grade : "))
    student["name"]=name
    student["kor"]=kor
    student["eng"]=eng
    student["math"]=math
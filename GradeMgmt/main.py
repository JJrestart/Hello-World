import student_input
import student_output
import student_calc

print('Prigram is Starting...')
student = {}
student_input.myInput(student) # Call by Reference
student_calc.calc(student)
student_output.output(student)

print('Program is Shutting down...')

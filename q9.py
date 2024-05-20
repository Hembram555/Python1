students = [50, 60, 70]
subjects = [80, 40, 90]
marks = [55, 85, 65]

element_wise_max = list(map(max, zip(students, subjects, marks)))
print(element_wise_max)

#Marks Obtain By Students Are Given In a List, Find The Student Who Stood Third In the Class.
marks = [85,86,78,88,89,90,87,65,76,56,98,95]
sorted_marks = sorted(marks, reverse=True)
third_highest_mark = sorted_marks[2]
print("The Student Who Stood 3rd in the class: ",third_highest_mark)


#***___Or___***

#marks.sort()
#print(marks)
#print("3rd student", marks[-3])
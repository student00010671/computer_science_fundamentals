# Task 10 => Calculate the average mark

myFinalMarks = {
    'CSF': 75,
    'FunPro': 80,
    'WT': 85
}


def overall_mark():
    sum_of_marks = 0
    for mark in myFinalMarks:
        sum_of_marks += myFinalMarks[mark]
    return sum_of_marks / len(myFinalMarks)


print(overall_mark())

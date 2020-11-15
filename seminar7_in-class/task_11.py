# Task 11 => Calculate the overall mark

csf = {
    'cw1-weight': 0.4,
    'cw1-mark': 79,
    'exam-weight': 0.6,
    'exam-mark': 65
}

cw1Weight = csf.get('cw1-weight') * csf.get('cw1-mark', 0)
examWeight = csf.get('exam-weight') * csf.get('exam-mark', 0)
overallMark = cw1Weight + examWeight
print(str(overallMark))   # prints 70.6

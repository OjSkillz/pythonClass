def grade_students(student_scores : dict):
    student_grades = {}
    for key, value in student_scores.items() :
        if value <= 70 :
            value = "Fail"
        elif value > 70 and value <= 80 :
            value = "Acceptable"
        elif value > 80 and value <= 90 :
            value = "Exceeds Expectations"
        else :
            value = "Outstanding"
        student_grades[key] = value
    return student_grades

import os

"""
Pseudocode for student grading application

Display Welcome Message
Prompt the teacher to enter their name
Read in the teacher's name
Prompt the teacher to enter their title
Read in the teacher's title
Prompt the teacher to enter the number of students
Read in the number of students
Prompt the teacher to enter the number of subjects
Read in the number of subjects
Prompt the teacher to enter the scores of each student per subject
Read in the scores of each student per subject 
If any score is lesser than 0 or greater than 100
	Print an error message
	Prompt the teacher to enter that score again
Display class summary after input collection
"""
students = []
subjects = []
scores_per_student = {}
totals = []
averages = []
merged_grades = []
positions = {}
positions_keys = []
header = {"STUDENT" : ["TOT", "AVE", "POS"]}
header_list = []
passes = []
fails = []

def update_students_list(number_of_students):
    for count in range(number_of_students):
        students.append(f"Student {count + 1}")
    return students

def update_subjects(number_of_subjects):
    for count in range(number_of_subjects):
        subjects.append(f"SUB {count+1}")
    return subjects
    
def update_scores_per_student():
    for value in scores_per_student.values():
        value.append(sum(value))
        value.append(float(f"{value[len(value) -1]/len(subjects):.2f}"))
    return scores_per_student
    
def update_totals():
    for value in scores_per_student.values():
        totals.append(sum(value))
    return totals
   
def update_averages():
    for value in scores_per_student.values():
        averages.append(float(f"{sum(value)/len(value):.2f}"))
    return averages

def update_positions():
    position = 0
    positions = dict(zip(students, totals))
    positions = {key: value for key,value in sorted(positions.items(), key = lambda item: item[1], reverse  = True)}
    
    for value in positions.values():
        for values in scores_per_student.values():
            if  value in values: 
                position = position + 1
                values.append(position)
    return scores_per_student


def display_subject_summary():
    print()
    print("SUBJECT SUMMARY")
    for count in range(len(subjects)):
        subject_scores = []
        cut_off_mark = 40
        number_of_passes = 0
        number_of_fails = 0
        
        for values in scores_per_student.values():
            subject_scores.append(values[count])
        print(f"Subject {count + 1}")
        print("=" * 100)
        print(f"Best peforming student in Subject {count + 1} is:   {students[subject_scores.index(max(subject_scores))]} scoring {max(subject_scores)}")
        print(f"Least performing student in Subject {count + 1} is: {students[subject_scores.index(min(subject_scores))]}  scoring {min(subject_scores)}")
        print(f"Total score is: {sum(subject_scores)}")
        print(f"Average score is: {sum(subject_scores)/len(students):.2f}")
      
        for element in subject_scores:
            if element >= cut_off_mark:
                number_of_passes += 1
            else:
                number_of_fails += 1
        passes.append(number_of_passes)
        fails.append(number_of_fails)
        
        print(f"Number of passes: {number_of_passes}")
        print(f"Number of fails: {number_of_fails}")
        print()

def print_subject_difficulty():
    print(f"{'=' * 100}\n{'=' * 100}")
    print(f"The hardest subject is Subject {subjects.index(subjects[fails.index(max(fails))]) + 1} with {max(fails)} failures")
    print(f"The easiest subject is Subject {subjects.index(subjects[passes.index(max(passes))]) + 1} with {max(passes)} passes")
    
    maximum_scores = []
    minimum_scores = []
    
    for values in scores_per_student.values():
        maximum_scores.append(max(values[ : len(students) - 1: ]))
        minimum_scores.append(min(values[ : len(students) - 1: ]))
        
    overall_highest_score = max(maximum_scores)
    overall_lowest_score = min(minimum_scores)
    
    for key,value in scores_per_student.items():
        if overall_lowest_score in value:
            print(f"The overall lowest score is {overall_lowest_score} scored by {key} in Subject  {subjects.index(subjects[value.index(overall_lowest_score)]) + 1}")
            
        if overall_highest_score in value: 
            print(f"The overall highest score is {overall_highest_score} scored by {key} in Subject {subjects.index(subjects[value.index(overall_highest_score)]) + 1}")
    print("=" * 100)

def display_class_summary():
    print()
    print("CLASS SUMMARY")
    print("=" * 100)
    print(f"Best Graduating Student is: {students[totals.index(max(totals))]} scoring {max(totals)}")
    print("=" * 100 + "\n\n" + "!" * 100)
    print(f"Worst Graduating Student is: {students[totals.index(min(totals))]} scoring {min(totals)}")
    print("!" * 100 + "\n\n" + "=" * 100)
    print(f"Class total score is: {sum(totals)}\nClass Average Score is: {sum(totals)/len(students):.2f}\n{'=' * 100}")
    
def update_merged_grades():
    for key,value in scores_per_student.items():
        merged_grades.append(key)
        merged_grades.extend(value)
    return merged_grades  
    
def display_results_header():
    print("=" * 100)
    for subject in subjects[: : -1]:
        header["STUDENT"].insert(0, subject)
    for key,value in header.items():
        header_list.append(key)
        header_list.extend(value)
    for index in range(len(header_list)):
        print(f"{header_list[index]:<9}",end=" ")
    print()
    print("=" * 100)

def display_results():
    for key, values in scores_per_student.items():
        print(f"{key:<9}", end=" ")
        for value in values:
            print(f"{value:<9}", end=" ")
        print()
    print("=" * 100)
    print()
    print("=" * 100)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
titles = {1: "Mr", 2: "Mrs", 3: "Miss"}
os.system("clear")
print("Welcome to The Lagbaja Schools Student Grading Application🎓")

teacher_name = input("Kindly provide your name >>  ")
teacher_title = int(input("""
Kindly provide your title: \n
Enter 1️⃣  for Mr
Enter 2️⃣  for Mrs
Enter 3️⃣  for Miss \n >>>  """))
os.system('clear')

while teacher_title != 1 and  teacher_title != 2 and teacher_title != 3:
    teacher_title= int(input("""
Invalid Entry. \n
Enter 1️⃣  for Mr
Enter 2️⃣  for Mrs
Enter 3️⃣  for Miss \n >>>  """))
    os.system("clear")
    
os.system("clear")

number_of_students = int(input(f"How many students do you have? >> "))
update_students_list(number_of_students)
print("Saved Successfully")
os.system("clear")

number_of_subjects = int(input("How many subjects do they offer? >> "))
update_subjects(number_of_subjects)
print("Saved Successfully")
os.system("clear")

for index in range(1, number_of_students + 1):
    print()
    print(f"You Are Now Entering Scores for Student {index}") 
    scores = []
    for count in range(1, number_of_subjects + 1):
        score = int(input(f"Enter score for Subject {count} >>  "))
        while score < 0 or score > 100 :
            print("\nInvalid entry. Enter scores between 0 and 100")
            score = int(input(f"Enter score for Subject {count} >>  "))
        scores.append(score)
        print("Saved Successfully")
        print()
        scores_per_student[students[index-1]] = scores
    os.system("clear")
        
response = input("All results have been captured. Press ↩️  to proceed to grading and results >>>  ")
response = "clear"
os.system(response)
    
update_totals()
update_averages()
update_scores_per_student()
display_results_header()
update_merged_grades()
update_positions()
display_results()

proceed = input("Press ↩️  to proceed to Summary per Subject >>  ")
display_subject_summary()

proceed = input("Press ↩️  to proceed to Difficulty Level per Subject >>  ")
print_subject_difficulty()

proceed = input("Press ↩️ to proceed to Class Summary >>  ")
display_class_summary()


for entry, title in titles.items():
    if teacher_title == entry:
        print(f"You have come to the end of this grading exercise, {title} {teacher_name}.\n")
response_two = input("Press ↩️  To Exit The Lagbaja Schools Student Grading Application🎓 >>> ")

response_two = "clear"
os.system(response_two)

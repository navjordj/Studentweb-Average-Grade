from studentweb_average_grade.fs_grade_avg import AverageGrade

avg_grader = AverageGrade('res.html')
avg_grader.calculate_average()
print(avg_grader.grade_avg)
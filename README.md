# Studentweb Average Grade Calculator
Uses BeautifulSoup to scrape Studentweb results page to output the weighted grade average

## Installation
`pip install git+https://github.com/navjordj/Studentweb-Average-Grade`

## How to use
1. Right click and download html from `https://fsweb.no/studentweb/resultater.jsf`
2. Navigate to download directory
3. ```python
   from studentweb_average_grade.fs_grade_avg import AverageGrade
   avg_grader = AverageGrade('filename.html')
   avg_grader.calculate_average()
   print(avg_grader.grade_avg)
   ```

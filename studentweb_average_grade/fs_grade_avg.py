from typing import List, Union
from pathlib import Path

from bs4 import BeautifulSoup # type: ignore

class AverageGrade:
    """
    Class to generate average grades using a html file from https://fsweb.no/studentweb/resultater.jsf
    """

    legal_grades: dict = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

    def __init__(self, file: str):
        """Initialize class

        Args:
            file (str): path to html file to be scraped
        """
        self.file = file
        self.lines = self._read_file()

        self.soup = BeautifulSoup(self.lines, "html.parser")

        self.grade_list: List[int] = []
        self.stp_list: List[int] = []

        self.grade_avg: Union[float, None] = None
    
    def _read_file(self) -> str:
        """Helper function to read html file

        Returns:
            str: string containing the whole webpage
        """
        with open(self.file, 'r') as page:
            return page.read()

    def calculate_average(self) -> float:
        """Calculates the average grade

        Returns:
            float: Weighted average grade
        """
        rows = self.soup.find_all('tr', {"class": ["none", "resultatTop"]})

        for row in rows:
            has_grade = False

            grades_col = row.find_all('td', {"class": "col6Resultat"})
            stp_cols = row.find_all('td', {"class": "col7Studiepoeng"})

            for grade_col in grades_col:
                grades = grade_col.find_all('div', {"class": "infoLinje"})
                for grade in grades:
                    grade_clean = grade.text.strip()
                    if grade_clean in self.legal_grades:
                        has_grade = True
                        self.grade_list.append(self.legal_grades[grade_clean])

            if has_grade:
                for stp_col in stp_cols:
                    self.stp_list.append(int(stp_col.text[12:]))

        num_stp = sum(self.stp_list)
        self.grade_avg = sum(list(x*y for x, y in zip(self.grade_list, self.stp_list))) / num_stp
        return self.grade_avg

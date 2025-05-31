"""
My solution for https://leetcode.com/problems/create-a-new-column/submissions/1649929746/
"""

import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees

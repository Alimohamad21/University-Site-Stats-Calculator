from helpers.csvHelpers import *
from services.siteServices import *

login()
grades = get_grades()
stats = get_stats(grades)
createCsvFromDict("gpa.csv", {"GPA": stats.total_gpa, "TOTAL CREDITS": stats.total_credit_hours})
createCsvFromDict("grade_counts.csv", stats.grade_counts)
createCsvFromDict("grade_credit_hours.csv", stats.grade_credits_counts)


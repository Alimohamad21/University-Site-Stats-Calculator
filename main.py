from helpers.csvHelpers import *
from services.siteServices import *

print('Logging in...')
login()
print('Getting grades...')
grades = get_grades()
print('Getting stats...')
stats = get_stats(grades)
print('Creating output files...')
createCsvFromDict("gpa.csv", {"GPA": stats.total_gpa, "TOTAL CREDITS": stats.total_credit_hours})
createCsvFromDict("grade_counts.csv", stats.grade_counts)
createCsvFromDict("grade_credit_hours.csv", stats.grade_credits_counts)
print('Stats ready to view in gpa.csv, grade_counts.csv & grade_credit_hours.csv')

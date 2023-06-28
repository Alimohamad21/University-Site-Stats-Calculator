import os

from dotenv import load_dotenv
from selenium import webdriver

from helpers.data import *
from helpers.seleniumHelpers import *
from models.Result import *
from models.Stats import *

load_dotenv()
driver = webdriver.Edge(os.getenv('DRIVER_PATH'))


def login():
    driver.get(SITE_URL)
    retryUntilElementFound(driver.find_element_by_xpath, USERNAME_FIELD_XPATH)
    driver.find_element_by_xpath(USERNAME_FIELD_XPATH).send_keys(os.getenv('SITE_USERNAME'))
    driver.find_element_by_xpath(PASSWORD_FIELD_XPATH).send_keys(os.getenv('SITE_PASSWORD'))
    driver.find_element_by_xpath(STUDENT_RADIO_BTN_XPATH).click()
    driver.find_element_by_xpath(LOGIN_BTN_XPATH).click()


def get_grades():
    grades = {}
    retryUntilElementFound(driver.find_element_by_id, COURSE_GRADES_ID)
    for i in range(3):
        driver.find_element_by_id(COURSE_GRADES_ID).click()
    retryUntilElementFound(driver.find_element_by_xpath, TABLES_LOADED_INDICATOR_XPATH)
    isMaxTerm = False
    for term in range(1, 30):
        course_name_xpath = COURSE_NAME_XPATH.replace("TERM", str(term))
        course_grade_xpath = GRADE_XPATH.replace("TERM", str(term))
        credit_hours_xpath = COURSE_CREDITS_XPATH.replace("TERM", str(term))
        for course_no in range(1, 30):
            course_name_xpath_new = course_name_xpath.replace("COURSE_NO", str(course_no))
            course_grade_xpath_new = course_grade_xpath.replace("COURSE_NO", str(course_no))
            credit_hours_xpath_new = credit_hours_xpath.replace("COURSE_NO", str(course_no))
            try:
                course_name = driver.find_element_by_xpath(course_name_xpath_new).text
                course_grade = driver.find_element_by_xpath(course_grade_xpath_new).text
                credit_hours = driver.find_element_by_xpath(credit_hours_xpath_new).text
                grades[course_name] = CourseResult(course_grade, int(credit_hours))
            except:
                if course_no == 1:
                    isMaxTerm = True
                break
        if isMaxTerm:
            break
    driver.close()
    return grades


def get_stats(grades):
    grade_credit_hours = {'A+': 0, 'A': 0, 'A-': 0, 'B+': 0, 'B': 0, 'B-': 0, 'C+': 0, 'C': 0, 'C-': 0, 'D+': 0, 'D': 0,
                          'F': 0}
    grade_count = {'A+': 0, 'A': 0, 'A-': 0, 'B+': 0, 'B': 0, 'B-': 0, 'C+': 0, 'C': 0, 'C-': 0, 'D+': 0, 'D': 0,
                   'F': 0}
    for result in grades.values():
        if result.grade in grade_count.keys():
            grade_credit_hours[result.grade] += result.credit_hours
            grade_count[result.grade] += 1
    total_score = 0
    total_hours = 0
    for grade, grade_chs in grade_credit_hours.items():
        total_score += grade_chs * GRADE_POINTS[grade]
        total_hours += grade_chs
    total_gpa = total_score / total_hours
    return Stats(total_gpa, total_hours, grade_count, grade_credit_hours)

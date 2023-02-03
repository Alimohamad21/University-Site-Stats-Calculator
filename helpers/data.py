SITE_URL = 'http://std.eng.alexu.edu.eg/static/index.html'
USERNAME_FIELD_XPATH = '/html/body/div/div/form/input[1]'
PASSWORD_FIELD_XPATH = '/html/body/div/div/form/input[2]'
STUDENT_RADIO_BTN_XPATH = '/html/body/div/div/form/div[1]/div[3]/input'
LOGIN_BTN_XPATH = '/html/body/div/div/form/input[3]'
COURSE_GRADES_ID = 'crsGrd'
TABLES_LOADED_INDICATOR_XPATH = '/html/body/div[1]/div/section[1]/div/span[1]'
GRADE_XPATH = '/html/body/div[1]/div/section[1]/div/table[TERM]/tbody/tr[COURSE_NO]/td[4]'
COURSE_NAME_XPATH = '/html/body/div[1]/div/section[1]/div/table[TERM]/tbody/tr[COURSE_NO]/td[2]'
COURSE_CREDITS_XPATH = '/html/body/div[1]/div/section[1]/div/table[TERM]/tbody/tr[COURSE_NO]/td[3]'
GRADE_POINTS = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7,
                'D+': 1.3,
                'D': 1.0,
                'F': 0.0}

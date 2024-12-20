# Exercise 1
def main():
    num_course_and_audience = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
    num_course_and_name_teacher = {'CS101': 'Hines', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke',
                                   'CM241': 'Lee'}
    num_course_and_time = {'CS101': '8:00', 'CS102': '9:00', 'CS103': '10:00', 'NT110': '11:00', 'CM241': '13:00'}

    print("Course numbers:")
    for key in num_course_and_audience:
        print(key)

    user_num_course = input("Enter the course number to get its information: ")
    if user_num_course.upper() in num_course_and_audience:
        print(f"Room number: {num_course_and_audience[user_num_course.upper()]}")
        print(f"Teacher's name: {num_course_and_name_teacher[user_num_course.upper()]}")
        print(f"Course start time: {num_course_and_time[user_num_course.upper()]}")
    else:
        print("This course is not in the database.")


main()


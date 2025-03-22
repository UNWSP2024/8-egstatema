# Eliya Statema
# 3/21/25
# Course Info

def main():
    course_dict = {}

    while True:
        course_id = input("Enter a course ID or 0 to finish: ")
        if course_id == "0":
            break
        else:
            course_name = input(f"Enter the name of {course_id}: ")
            course_dict[course_id] = course_name

    subject_search = input("Enter a subject to search for courses (e.g. COS): ")

    print(f"{subject_search} courses:")
    courses_found = False
    for course_id, course_name in course_dict.items():
        if course_id.startswith(subject_search):
            print(f"{course_id} - {course_name}")
            courses_found = True
    if not courses_found:
        print("No courses were found for this subject.")

if __name__ == '__main__':
    main()
# You are given a hash table where the key is a course code,
# and the value is a list of all the course codes that are prerequisites for the key.
# Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.
#
# Example:
# {
#   'CSC300': ['CSC100', 'CSC200'],
#   'CSC200': ['CSC100'],
#   'CSC100': []
# }
#
# This input should return the order that we need to take these courses:
#  ['CSC100', 'CSC200', 'CSCS300']

def visit(course_to_prereqs, course, temp_marks: set, perm_mark: set, result: list):
    if course not in perm_mark:
        return True
    elif course in temp_marks:
        return False

    temp_marks.add(course)

    for dep_course in course_to_prereqs[course]:
        if not visit(course_to_prereqs, dep_course, temp_marks, perm_mark, result):
            return False

    temp_marks.remove(course)
    perm_mark.remove(course)
    result.append(course)
    return True


def courses_to_take(course_to_prereqs: dict):
    temp_marks = set()
    perm_mark = set(course_to_prereqs.keys())
    result = []

    while len(perm_mark) != 0:
        if not visit(course_to_prereqs, next(iter(perm_mark)), temp_marks, perm_mark, result):
            return None
    return result

courses = {
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}

print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
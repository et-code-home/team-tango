AVOID = -1
NEUTRAL = 0
PREFERRED = 1

def separate_students(preferences, group_size, rating):
    students = list(preferences.keys())
    for student in preferences:
        if student not in placed:
            avoid = []
            for i, rating in enumerate(preferences[student]):
                if rating == -1:
                    avoid.append(students[i-1])
            if len(avoid):
                for person in avoid:
                    if person not in placed:
                        for group in groups:
                            if len(group) != group_size:
                                if person not in group:
                                    group.append(person)
                                    placed.append(person)
                                    break
                if student not in placed:
                    for group in groups:
                        if len(group) != group_size:
                            if student not in group and not any(dude in group for dude in avoid):
                                group.append(student)
                                placed.append(student)
                                break

def fill_students(preferences, group_size):
    students = list(preferences.keys())
    for student in preferences:
        if student not in placed:
            matches = []
            for i, rating in enumerate(preferences[student]):
                if rating == PREFERRED:
                    matches.append(students[i-1])
            for group in groups:
                if len(group) != group_size:
                    if student not in group and any(dude in group for dude in matches):
                        group.append(student)
                        placed.append(student)
                        break

    for student in preferences:
        if student not in placed:
            for group in groups:
                if len(group) != group_size:
                    group.append(student)
                    placed.append(student)
                    break
            

# Load preferences from the 'preferences.py' file
from preferences import pairing_preferences

group_size = 5
groups = [[] for _ in range(len(pairing_preferences) // group_size)]
placed = []

separate_students(pairing_preferences, group_size, AVOID)
fill_students(pairing_preferences, group_size)

for i, group in enumerate(groups):
    print(f"Group {i+1}: {group}")

import random

exercises = [
    {
        "topic": "Functions",
        "tasks": [
            {
                "description": "Write a function `get_student_group(student_name)` that takes a student's name and returns their group name.",
                "function": "get_student_group",
                "parameters": ["student_name"]
            },
            {
                "description": "Create a function `add_student(name, email, github, group, certificates, completed_sessions, demos)` that adds a new student dictionary to `data['students']`.",
                "function": "add_student",
                "parameters": ["name", "email", "github", "group", "certificates", "completed_sessions", "demos"]
            },
            {
                "description": "Write a function `count_certificates(student_name)` that returns the number of certificates a given student has.",
                "function": "count_certificates",
                "parameters": ["student_name"]
            },
            {
                "description": "Build a function `list_students_in_group(group_name)` that returns a list of students who belong to a specific group.",
                "function": "list_students_in_group",
                "parameters": ["group_name"]
            }
        ]
    },
    
    {
        "topic": "List Comprehension",
        "tasks": [
            {
                "description": "Use list comprehension to create a list of students who have more than 2 demos completed.",
                "method": "list_comprehension"
            },
            {
                "description": "Write a list comprehension that returns a list of student names who have completed the 'Linux' session.",
                "method": "list_comprehension"
            },
            {
                "description": "Create a list comprehension that extracts each student’s `github` username.",
                "method": "list_comprehension"
            }
        ]
    },

    {
        "topic": "Data Type Manipulation",
        "tasks": [
            {
                "description": "Write code to add a new entry to `data['certificates']` for 'Python Certificate' and update each student’s certificates list if they have completed the 'Python' session.",
                "method": "dictionary_update"
            },
            {
                "description": "Format each student’s details as a single string using f-strings and store in a new list.",
                "method": "f_string_formatting"
            },
            {
                "description": "Write code to convert the `demos` value for each student into a string and add ' demos completed' to it, for display purposes.",
                "method": "string_casting"
            }
        ]
    },
    {
        "topic": "Conditionals",
        "tasks": [
            {
                "description": "Write a program that checks if a student has completed all sessions and prints 'Certified' if they have all certificates, and 'Incomplete' otherwise.",
                "conditionals": "if_else"
            },
            {
                "description": "Create a program that checks if a student has both 'Linux Certificate' and 'Python Certificate' and prints a congratulatory message if they do.",
                "conditionals": "if_else"
            },
            {
                "description": "Write code to identify students who are in 'Group B' and have completed more than 2 sessions. Print each student’s name.",
                "conditionals": "if_else"
            }
        ]
    },
    {
        "topic": "Loops",
        "tasks": [
            {
                "description": "Write a for loop that iterates through all students and prints each student’s name and completed sessions.",
                "loop_type": "for"
            },
            {
                "description": "Loop over all students and print the names of students who are missing any certificates.",
                "loop_type": "for"
            },
            {
                "description": "Write a nested loop to print each student’s name and each session they have completed.",
                "loop_type": "nested_for"
            }
        ]
    },
    {
        "topic": "Range",
        "tasks": [
            {
                "description": "Use range to print 'Learning Python' 5 times.",
                "range_usage": "simple_range"
            },
            {
                "description": "Use range(len(data['students'])) to access each student and print out their demos count.",
                "range_usage": "range_with_len"
            },
            {
                "description": "Use range to print every second student’s name from data['students'].",
                "range_usage": "range_with_step"
            }
        ]
    },

    {
        "topic": "Try/Except",
        "tasks": [
            {
                "description": "Write a function `find_student_email(student_name)` that looks up a student’s email and handles the error if the student does not exist.",
                "function": "find_student_email",
                "parameters": ["student_name"]
            },
            {
                "description": "Write a program that tries to print each student’s 'LinkedIn' profile from data['students']. If the key does not exist, it should print 'LinkedIn profile not available'.",
                "try_except": "key_error"
            },
            {
                "description": "Write a program that attempts to retrieve each student's number of demos and certificates. Use a TypeError exception handler to catch cases where the values are not integers and print an error message.",
                "try_except": "type_error"
            }
        ]
    },

    {
        "topic": "Project",
        "tasks": [
            {
                "description": "Write a program `generate_student_report(student_name)` that:\n"
                               "1. Checks if the student exists and handles errors if they don’t.\n"
                               "2. Retrieves the student’s details: `group`, `certificates`, `demos`.\n"
                               "3. Formats the details nicely and lists completed sessions in a readable list format.\n"
                               "4. Uses a loop to display each detail in the final report with appropriate formatting.",
                "function": "generate_student_report",
                "parameters": ["student_name"]
            }
        ]
    }
]

with open("august/tasks.txt","r") as file:
    content = file.read().split('\n')

for task in content:
    if task == '':
        break
    name, topic, task = task.split()
    exercises[int(topic)]['tasks'].pop(int(task))

task_seeker = input("Please enter your name: ")
for index, topic in enumerate(exercises):
    print(index, topic['topic'])

topic_num = int(input("Choose a topic (#): "))
task_num = random.randint(0, len(exercises[topic_num]['tasks']) -1)

with open("august/tasks.txt","a") as file:
   file.write(f"{task_seeker} {topic_num} {task_num}\n")

print("Your random task under the topic:", exercises[topic_num]['topic'], "is:")
print(exercises[topic_num]['tasks'][task_num]['description'])
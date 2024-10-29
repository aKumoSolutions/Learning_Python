from tokenize import group


data = {
        "students": [
            {
                "name": "Abdul S",
                "email": "john.smith@example.com",
                "github": "johnsmith123",
                "group": "Group A",
                "certificates": ["Linux Certificate", "Bash Certificate"],
                "completed_sessions": ["Linux", "Bash"],
                "demos": 3
            },
            {
                "name": "Abdullah H",
                "email": "john.smith@example.com",
                "github": "johnsmith123",
                "group": "Group A",
                "certificates": ["Linux Certificate", "Bash Certificate"],
                "completed_sessions": ["Linux", "Bash"],
                "demos": 3
            },
            {
                "name": "Mohammad",
                "email": "alice.johnson@example.com",
                "github": "alicejohnson",
                "group": "Group B",
                "certificates": ["Linux Certificate"],
                "completed_sessions": ["Linux"],
                "demos": 2
            },
            {
                "name": "Muhammad Amin",
                "email": "emma.davis@example.com",
                "github": "emmadavis89",
                "group": "Group A",
                "certificates": ["Linux Certificate", "Bash Certificate", "Python Certificate"],
                "completed_sessions": ["Linux", "Bash", "Python"],
                "demos": 4
            },
            {
                "name": "Shirin Z",
                "email": "michael.brown@example.com",
                "github": "michaelbrown",
                "group": "Group C",
                "certificates": ["Linux Certificate", "Bash Certificate", "Python Certificate", "AWS Certificate"],
                "completed_sessions": ["Linux", "Bash", "Python", "AWS"],
                "demos": 5
            },
            {
                "name": "Abdulhamid A",
                "email": "michael.brown@example.com",
                "github": "michaelbrown",
                "group": "Group C",
                "certificates": ["Linux Certificate", "Bash Certificate", "Python Certificate", "AWS Certificate"],
                "completed_sessions": ["Linux", "Bash", "Python", "AWS"],
                "demos": 5
            }
        ],
        "groups": [
            {
                "group_name": "January 2024",
                "students": ["John Smith", "Emma Davis"]
            },
            {
                "group_name": "May 2024",
                "students": ["John Smith", "Emma Davis"]
            },
            {
                "group_name": "August 2024",
                "students": ["Alice Johnson"]
            },
            {
                "group_name": "November 2024",
                "students": ["Michael Brown"]
            }
        ],
        "sessions": [
            {
                "name": "Linux",
                "prerequisite": None,
            },
            {
                "name": "Bash",
                "prerequisite": "Linux",
            },
            {
                "name": "Python",
                "prerequisite": "Bash",
            },
            {
                "name": "AWS",
                "prerequisite": "Python",
            },
            {
                "name": "Terraform",
                "prerequisite": "AWS",
            },
            {
                "name": "Docker",
                "prerequisite": "Terraform",
            },
            {
                "name": "Kubernetes",
                "prerequisite": "Docker",
            },
            {
                "name": "Jenkins",
                "prerequisite": "Kubernetes",
            }
        ], 
        "certificates": [
            "Linux Certificate",
            "Bash Certificate",
            "Python Certificate",
            "AWS Certificate",
            "Terraform Certificate",
            "Docker Certificate",
            "Kubernetes Certificate",
            "Jenkins Certificate"
        ]

}

def look_up_student_by_group():
    for group in data['groups']:
        print(group['group_name'])

    students = []
    group = input("Please enter a group: ")
    for st in data['students']:
        if st['group'] == group:
            students.append(st['name'])
    return students


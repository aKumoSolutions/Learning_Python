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

## 3. Function to print list of students with specific certificates
def students_with_specific_certificate():
    print("""
          Please choose one certificate from the list below:
                Linux Certificate
                Bash Certificate
                Python Certificate
                AWS Certificate
                Terraform Certificate
                Docker Certificate
                Kubernetes Certificate
                Jenkins Certificate
          """)
    
    ## Get user input
    certificate = input("Please enter certificate name: ")
    ## Empty list to hold student names with specific cetificate
    # student_list = []
    
    ## Loop through data and check which student has that specific certificate, 
    ## and add the student name to the list
    #============== First Method Using For Loop ==============#
    # for student in data["students"]:
    #     if certificate in student["certificates"]:
    #         student_list.append(student["name"])
    
    #============== Second Method Using list Comprehension ==============#
    student_list = [student["name"] for student in data["students"] if certificate in student["certificates"]]

    if len(student_list) == 0:
        return "No student have this certificate"
    
    return student_list
           
print(students_with_specific_certificate())    

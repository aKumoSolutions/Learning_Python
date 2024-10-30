data = {
        "students": [
            {
                "name": "Abdul Sharif",
                "email": "john.smith@example.com",
                "github": "johnsmith123",
                "group": "Group A",
                "certificates": ["Linux Certificate", "Bash Certificate"],
                "completed_sessions": ["Linux", "Bash"],
                "demos": 3
            },
            {
                "name": "Abdullah Hanifi",
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
                "name": "Shirin Ziyovuddinova",
                "email": "michael.brown@example.com",
                "github": "michaelbrown",
                "group": "Group C",
                "certificates": ["Linux Certificate", "Bash Certificate", "Python Certificate", "AWS Certificate"],
                "completed_sessions": ["Linux", "Bash", "Python", "AWS"],
                "demos": 5
            },
            {
                "name": "Abdulhamid Abdullajonov",
                "email": "michael.brown@example.com",
                "github": "michaelbrown",
                "group": "Group C",
                "certificates": ["Linux Certificate", "Bash Certificate", "Python Certificate", "AWS Certificate"],
                "completed_sessions": ["Linux", "Bash", "Python", "AWS"],
                "demos": 5
            }
        ],
        "groups": [
            "January 2024",
            "May 2024",
            "August 2024",
            "November 2024",
        ],
        "sessions": [
            {
                "name": "Linux",
                "prerequisite": []
            },
            {
                "name": "Bash",
                "prerequisite": ["Linux"]
            },
            {
                "name": "Python",
                "prerequisite": ["Linux", "Bash"]
            },
            {
                "name": "AWS",
                "prerequisite": ["Linux", "Bash", "Python", "GIT"]
            },
            {
                "name": "Terraform",
                "prerequisite": ["Linux", "Bash", "Python", "GIT", "AWS"]
            },
            {
                "name": "Docker",
                "prerequisite": ["Linux", "Bash", "Python", "GIT", "AWS", "Terraform"]
            },
            {
                "name": "Kubernetes",
                "prerequisite": ["Linux", "Bash", "Python", "GIT", "AWS", "Terraform", "Docker"]
            },
            {
                "name": "Jenkins",
                "prerequisite": ["Linux", "Bash", "Python", "GIT", "AWS", "Terraform", "Docker", "Kubernetes"]
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

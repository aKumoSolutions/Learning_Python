ef manage_students(students, action, student_name):
    """Adding or deleting students"""
    
    if action == "add":
        if student_name in students:
            return f"{student_name} is already in the list."
        students.append(student_name)
        return f"{student_name} has been added."

    elif action == "delete":
        if student_name not in students:
            return f"{student_name} is not in the list."
        students.remove(student_name)
        return f"{student_name} has been removed."

    return "Invalid action. Please use 'add' or 'delete'."




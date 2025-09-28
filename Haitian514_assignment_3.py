# Step 1: Foundation Setup
student_name = "Sean"
current_gpa = 3.2
study_hours = 25
social_points = 50
stress_level = 40

# Welcome message
print(f"Welcome, {student_name}!")
print(f"Starting GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

# Step 2: Course Planning
print("\nChoose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice (A/B/C): ")

if choice == "A":
    if current_gpa <= 2.5:
        study_hours += 5
        stress_level -= 5
        print("You chose Light load. Extra time to study and relax.")
    else:
        study_hours += 3
        stress_level -= 3
        print("You chose Light Load. Balanced approach")
if choice == "A":
    if current_gpa <= 2.5:
        study_hours += 5
        stress_level -= 5
        print("You chose Light load. Extra time to study and relax.")
    else:
        study_hours += 3
        stress_level -= 3
        print("You chose Light load. Balanced approach.")
elif choice == "B":
    if current_gpa >= 3.0:
        study_hours += 7
        stress_level += 5
        print("You chose Standard load. Manageable with effort.")
    else:
        study_hours += 10
        stress_level += 10
        print("You chose Standard load. Might be a stretch.")
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 12
        stress_level += 15
        print("You chose Heavy load. You're ready for the challenge!")
    else:
        study_hours += 15
        stress_level += 25
        print("You chose Heavy load. This could be overwhelming.")
else:
    print("Invalid input. Defaulting to Standard load.")
    study_hours += 7
    stress_level += 10

# Updated stats after decision:

print("\nUpdated Stats:")
print(f"Study Hours: {study_hours}")
print(f"Stress Level: {stress_level}")
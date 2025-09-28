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

# Step 3: Study Strategy Decision

study_options = ["Programming", "Math", "English", "History"]
print("\nChoose a subject to focus on:", study_options)
subject = input("Your choice: ")

if subject not in study_options:
    print("Invalid subject. No changes made.")
else:
    # Unique outcomes for each subject
    if subject == "Programming":
        if current_gpa < 3.0 or stress_level > 60:
            current_gpa += 0.15
            social_points -= 10
            print("Programming boosted your GPA, but drained your social energy.")
        else:
            current_gpa += 0.25
            social_points -= 5
            print("You thrived in Programming with minimal social cost.")
    
    elif subject == "Math":
        if study_hours > 30 and not stress_level > 70:
            current_gpa += 0.2
            social_points -= 8
            print("Math sharpened your skills, but required intense focus.")
        else:
            current_gpa += 0.1
            social_points -= 3
            print("Math helped a bit, but you struggled to stay consistent.")
    
    elif subject == "English":
        if stress_level < 50 and current_gpa >= 2.5:
            current_gpa += 0.1
            social_points += 5
            print("English gave you a creative outlet and boosted your social life.")
        else:
            current_gpa += 0.05
            social_points += 2
            print("English was relaxing, but didn’t impact your GPA much.")
    
    elif subject == "History":
        if study_hours > 35 or current_gpa < 2.8:
            current_gpa += 0.12
            social_points += 3
            print("History helped you reflect and grow academically.")
        else:
            current_gpa += 0.08
            social_points += 1
            print("History was a steady choice with modest gains.")
            
# Step 4: Final Semester Assesment:

print("\nFinal Semester Decision: Join a club or take extra tutoring?")
final_choice = input("Type 'club' or 'tutoring': ")

# Identity operator usage
if type(final_choice) is not str:
    print("Unexpected input type. Ending simulation.")
else:
    if final_choice == "club":
        social_points += 10
        stress_level += 5
        if stress_level > 70:
            print("You burned out from too much socializing!")
        elif current_gpa >= 3.5:
            print("You balanced academics and social life brilliantly!")
        else:
            print("You had fun but your grades slipped.")
    
    elif final_choice == "tutoring":
        study_hours += 10
        stress_level += 10
        if current_gpa >= 3.8:
            print("You aced the semester with top honors!")
        elif current_gpa >= 3.0:
            print("Solid performance with noticeable improvement.")
        else:
            print("You tried hard but need more support.")
    
    else:
        print("Invalid final choice. Semester ends quietly.")

# Final stats
print("\nFinal Stats:")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")
# Copilot was used to debug this code, and explain and slightly modify my code to meet a missing requirement in zybooks assignment
student_heights = input("Enter a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = sum(student_heights)

average = round(total_height / len(student_heights))

print(f"Average height is {average}")
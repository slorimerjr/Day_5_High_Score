# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
# Cannot use max/min function
#Write your code below this row 👇
x = 0
for score in student_scores:
  if score > x:
    x = score

print(f"This highest score in the class is: {x}.")




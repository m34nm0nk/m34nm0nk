# Create a for loop in a for loop (nested loop)
classroom = []
# create a for loop using the range function to iterate the loop 7 times
for i in range(7):
    # Each iteration should append a new empty list to the classroom list7x
    classroom.append([])
    # Create a new for loop in the first loop that will iterate 1-10
    for students in range(1,11):
        # Populates the nested lists with the iterated range 1-11
        classroom[i].append(students)
        
print(classroom)

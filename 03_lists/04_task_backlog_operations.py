# Topic: Lists
# Example: Task backlog operations

tasks = ["Requirement analysis", "Design UI", "Build API"]

# append() adds a new task.
tasks.append("Write test cases")

# remove() deletes a matching task.
tasks.remove("Design UI")

# pop() removes and returns an item by index.
completed_task = tasks.pop(0)

print("Completed:", completed_task)
print("Pending:", tasks)

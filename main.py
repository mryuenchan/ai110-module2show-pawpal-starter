from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Alex")

dog = Pet("Biscuit", "Dog")
cat = Pet("Mochi", "Cat")

dog.add_task(Task("Feed breakfast", "9:00 AM", 10, "high", "daily"))
dog.add_task(Task("Morning walk", "8:00 AM", 30, "high", "daily"))
cat.add_task(Task("Play time", "6:00 PM", 20, "low", "daily"))
cat.add_task(Task("Clean litter box", "10:00 AM", 15, "medium", "weekly"))

# Same time as Biscuit's task, so this creates a conflict
cat.add_task(Task("Give medicine", "9:00 AM", 5, "high", "daily"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler(owner)

print("Sorted Schedule:")
scheduler.print_schedule()

print("Only Biscuit's Tasks:")
for pet_name, task in scheduler.filter_by_pet("Biscuit"):
    print(f"{task.time} - {pet_name}: {task.description}")

print()

print("Incomplete Tasks:")
for pet_name, task in scheduler.filter_by_status(False):
    print(f"{task.time} - {pet_name}: {task.description}")

print()

print("Conflicts:")
conflicts = scheduler.detect_conflicts()

if conflicts:
    for first, second in conflicts:
        pet1, task1 = first
        pet2, task2 = second
        print(f"Warning: {pet1}'s '{task1.description}' and {pet2}'s '{task2.description}' are both at {task1.time}.")
else:
    print("No conflicts found.")

print()

print("Marking Morning walk complete...")
scheduler.mark_task_complete("Biscuit", "Morning walk")

print()

print("Updated Biscuit Tasks:")
for pet_name, task in scheduler.filter_by_pet("Biscuit"):
    print(f"{task.time} - {pet_name}: {task.description} | Due: {task.due_date} | Done: {task.completed}")
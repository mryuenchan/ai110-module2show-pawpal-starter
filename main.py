from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Alex")

dog = Pet("Biscuit", "Dog")
cat = Pet("Mochi", "Cat")

dog.add_task(Task("Feed breakfast", "9:00 AM", 10, "high"))
dog.add_task(Task("Morning walk", "8:00 AM", 30, "high"))
cat.add_task(Task("Play time", "6:00 PM", 20, "low"))
cat.add_task(Task("Clean litter box", "10:00 AM", 15, "medium"))

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
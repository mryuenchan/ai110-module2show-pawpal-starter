from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Alex")

dog = Pet("Biscuit", "Dog")
cat = Pet("Mochi", "Cat")

dog.add_task(Task("Morning walk", "8:00 AM", 30, "high"))
dog.add_task(Task("Feed breakfast", "9:00 AM", 10, "high"))
cat.add_task(Task("Clean litter box", "10:00 AM", 15, "medium"))
cat.add_task(Task("Play time", "6:00 PM", 20, "low"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler(owner)
scheduler.print_schedule()
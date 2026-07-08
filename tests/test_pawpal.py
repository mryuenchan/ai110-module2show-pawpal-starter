from datetime import timedelta

from pawpal_system import Owner, Pet, Task, Scheduler


def test_mark_complete_changes_status():
    task = Task("Morning walk", "8:00 AM", 30, "high")

    assert task.completed == False

    task.mark_complete()

    assert task.completed == True


def test_adding_task_increases_pet_task_count():
    pet = Pet("Biscuit", "Dog")
    task = Task("Feed breakfast", "9:00 AM", 10, "high")

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_scheduler_sorts_tasks_by_time():
    owner = Owner("Alex")
    pet = Pet("Biscuit", "Dog")

    pet.add_task(Task("Dinner", "6:00 PM", 10, "medium"))
    pet.add_task(Task("Morning walk", "8:00 AM", 30, "high"))
    pet.add_task(Task("Lunch", "12:00 PM", 10, "low"))

    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    schedule = scheduler.sort_by_time()

    times = [task.time for pet_name, task in schedule]

    assert times == ["8:00 AM", "12:00 PM", "6:00 PM"]


def test_daily_task_creates_next_occurrence():
    task = Task("Morning walk", "8:00 AM", 30, "high", "daily")

    next_task = task.mark_complete()

    assert task.completed == True
    assert next_task is not None
    assert next_task.description == "Morning walk"
    assert next_task.due_date == task.due_date + timedelta(days=1)
    assert next_task.completed == False


def test_scheduler_detects_conflicts():
    owner = Owner("Alex")

    dog = Pet("Biscuit", "Dog")
    cat = Pet("Mochi", "Cat")

    dog.add_task(Task("Feed breakfast", "9:00 AM", 10, "high"))
    cat.add_task(Task("Give medicine", "9:00 AM", 5, "high"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
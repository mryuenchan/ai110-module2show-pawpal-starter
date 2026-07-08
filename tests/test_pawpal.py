from pawpal_system import Task, Pet


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
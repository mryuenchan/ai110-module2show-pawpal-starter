from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    time: str
    duration: int
    priority: str
    frequency: str = "daily"
    completed: bool = False

    def mark_complete(self):
    """Mark the task as completed."""
    self.completed = True

    def mark_incomplete(self):
        self.completed = False


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        all_tasks = []
        for pet in self.pets:
            for task in pet.get_tasks():
                all_tasks.append((pet.name, task))
        return all_tasks


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def generate_schedule(self):
        tasks = self.owner.get_all_tasks()

        priority_order = {
            "high": 1,
            "medium": 2,
            "low": 3
        }

        tasks.sort(key=lambda item: priority_order.get(item[1].priority.lower(), 4))
        return tasks

    def print_schedule(self):
        schedule = self.generate_schedule()

        print("Today's Schedule")
        print("----------------")

        for pet_name, task in schedule:
            status = "Done" if task.completed else "Not done"
            print(f"{task.time} - {pet_name}: {task.description}")
            print(f"  Duration: {task.duration} minutes")
            print(f"  Priority: {task.priority}")
            print(f"  Frequency: {task.frequency}")
            print(f"  Status: {status}")
            print()
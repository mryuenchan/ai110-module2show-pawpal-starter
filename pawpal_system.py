from dataclasses import dataclass, field
from datetime import date, timedelta

@dataclass
class Task:
    description: str
    time: str
    duration: int
    priority: str
    frequency: str = "daily"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True
        return self.create_next_occurrence()

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False

    def create_next_occurrence(self):
        """Create the next daily or weekly version of a task."""
        if self.frequency.lower() == "daily":
            next_date = self.due_date + timedelta(days=1)
        elif self.frequency.lower() == "weekly":
            next_date = self.due_date + timedelta(days=7)
        else:
            return None

        return Task(
            self.description,
            self.time,
            self.duration,
            self.priority,
            self.frequency,
            False,
            next_date
        )

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
        """Store the owner so the scheduler can access all pet tasks."""
        self.owner = owner

    def time_to_minutes(self, time_string):
        """Convert a time like '8:00 AM' into minutes for sorting."""
        time_string = time_string.strip()
        time_part, period = time_string.split()
        hour, minute = time_part.split(":")

        hour = int(hour)
        minute = int(minute)

        if period.upper() == "PM" and hour != 12:
            hour += 12
        if period.upper() == "AM" and hour == 12:
            hour = 0

        return hour * 60 + minute

    def sort_by_time(self):
        """Sort all tasks by their time."""
        tasks = self.owner.get_all_tasks()
        return sorted(tasks, key=lambda item: self.time_to_minutes(item[1].time))

    def filter_by_pet(self, pet_name):
        """Return only tasks for one pet, sorted by time."""
        tasks = self.sort_by_time()
        return [item for item in tasks if item[0].lower() == pet_name.lower()]

    def filter_by_status(self, completed=False):
        """Return tasks based on completion status, sorted by time."""
        tasks = self.sort_by_time()
        return [item for item in tasks if item[1].completed == completed]

    def detect_conflicts(self):
        """Find tasks that are scheduled at the same time."""
        tasks = self.sort_by_time()
        conflicts = []

        seen_times = {}

        for pet_name, task in tasks:
            if task.time in seen_times:
                conflicts.append((seen_times[task.time], (pet_name, task)))
            else:
                seen_times[task.time] = (pet_name, task)

        return conflicts

    def mark_task_complete(self, pet_name, task_description):
        """Mark a task complete and add the next recurring task if needed."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                for task in pet.tasks:
                    if task.description.lower() == task_description.lower():
                        next_task = task.mark_complete()

                        if next_task:
                            pet.add_task(next_task)

                        return True

        return False

    def generate_schedule(self):
        """Generate the schedule sorted by time."""
        return self.sort_by_time()

    def print_schedule(self):
        """Print the daily schedule in a readable format."""
        schedule = self.generate_schedule()

        print("Today's Schedule")
        print("----------------")

        for pet_name, task in schedule:
            status = "Done" if task.completed else "Not done"
            print(f"{task.time} - {pet_name}: {task.description}")
            print(f"  Duration: {task.duration} minutes")
            print(f"  Priority: {task.priority}")
            print(f"  Frequency: {task.frequency}")
            print(f"  Due date: {task.due_date}")
            print(f"  Status: {status}")
            print()
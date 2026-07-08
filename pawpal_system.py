from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration: int
    priority: str

    def update_task(self, name=None, duration=None, priority=None):
        pass

    def get_priority(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass

    def remove_task(self, task_name):
        pass


@dataclass
class Owner:
    name: str
    available_minutes: int
    pet: Pet = None

    def add_pet(self, pet):
        pass

    def set_available_time(self, minutes):
        pass


class Scheduler:
    def __init__(self, tasks, available_minutes):
        self.tasks = tasks
        self.available_minutes = available_minutes

    def sort_tasks(self):
        pass

    def generate_plan(self):
        pass
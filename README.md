# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

classDiagram
    class Owner {
        +string name
        +list pets
        +add_pet(pet)
        +get_all_tasks()
    }

    class Pet {
        +string name
        +string species
        +list tasks
        +add_task(task)
        +get_tasks()
    }

    class Task {
        +string description
        +string time
        +int duration
        +string priority
        +string frequency
        +bool completed
        +date due_date
        +mark_complete()
        +mark_incomplete()
        +create_next_occurrence()
    }

    class Scheduler {
        +Owner owner
        +time_to_minutes(time_string)
        +sort_by_time()
        +filter_by_pet(pet_name)
        +filter_by_status(completed)
        +detect_conflicts()
        +mark_task_complete(pet_name, task_description)
        +generate_schedule()
        +print_schedule()
    }

    Owner "1" --> "*" Pet
    Pet "1" --> "*" Task
    Scheduler --> Owner

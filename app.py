import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("User")

owner = st.session_state.owner

st.header("Add a Pet")

pet_name = st.text_input("Pet name")
pet_species = st.text_input("Pet species")

if st.button("Add Pet"):
    if pet_name and pet_species:
        new_pet = Pet(pet_name, pet_species)
        owner.add_pet(new_pet)
        st.success(f"Added {pet_name}!")
    else:
        st.warning("Please enter both a pet name and species.")

if owner.pets:
    st.subheader("Current Pets")
    pet_table = []
    for pet in owner.pets:
        pet_table.append(
            {
                "Pet": pet.name,
                "Species": pet.species,
                "Number of Tasks": len(pet.tasks),
            }
        )
    st.table(pet_table)

st.divider()

st.header("Add a Task")

if owner.pets:
    pet_options = [pet.name for pet in owner.pets]
    selected_pet_name = st.selectbox("Choose a pet", pet_options)

    task_description = st.text_input("Task description")
    task_time = st.text_input("Task time", "8:00 AM")
    task_duration = st.number_input("Duration in minutes", min_value=1, value=10)
    task_priority = st.selectbox("Priority", ["high", "medium", "low"])
    task_frequency = st.selectbox("Frequency", ["daily", "weekly", "once"])

    if st.button("Add Task"):
        if task_description:
            for pet in owner.pets:
                if pet.name == selected_pet_name:
                    new_task = Task(
                        task_description,
                        task_time,
                        int(task_duration),
                        task_priority,
                        task_frequency,
                    )
                    pet.add_task(new_task)
                    st.success(f"Task added for {selected_pet_name}!")
        else:
            st.warning("Please enter a task description.")
else:
    st.info("Add a pet first before adding tasks.")

st.divider()

st.header("Today's Schedule")

scheduler = Scheduler(owner)

if owner.pets:
    try:
        schedule = scheduler.generate_schedule()

        if schedule:
            schedule_table = []

            for pet_name, task in schedule:
                schedule_table.append(
                    {
                        "Time": task.time,
                        "Pet": pet_name,
                        "Task": task.description,
                        "Duration": task.duration,
                        "Priority": task.priority,
                        "Frequency": task.frequency,
                        "Due Date": task.due_date,
                        "Completed": task.completed,
                    }
                )

            st.table(schedule_table)

            conflicts = scheduler.detect_conflicts()

            if conflicts:
                for first, second in conflicts:
                    pet1, task1 = first
                    pet2, task2 = second

                    st.warning(
                        f"Conflict warning: {pet1}'s '{task1.description}' and "
                        f"{pet2}'s '{task2.description}' are both scheduled at {task1.time}."
                    )
            else:
                st.success("No schedule conflicts found.")

        else:
            st.info("No tasks yet. Add a task above.")

    except ValueError:
        st.error("Please enter task times in this format: 8:00 AM")
else:
    st.info("Add pets and tasks to build a schedule.")

st.divider()

st.header("Complete a Task")

if owner.pets:
    pet_options = [pet.name for pet in owner.pets]
    complete_pet_name = st.selectbox("Choose pet to complete task for", pet_options)

    selected_pet = None
    for pet in owner.pets:
        if pet.name == complete_pet_name:
            selected_pet = pet

    if selected_pet and selected_pet.tasks:
        task_options = [task.description for task in selected_pet.tasks]
        complete_task_description = st.selectbox("Choose task to complete", task_options)

        if st.button("Mark Task Complete"):
            scheduler.mark_task_complete(complete_pet_name, complete_task_description)
            st.success(
                "Task marked complete. If it was daily or weekly, a new future task was created."
            )
    else:
        st.info("This pet has no tasks yet.")
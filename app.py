import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.title("PawPal+")

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

st.header("Add a Task")

if owner.pets:
    pet_options = [pet.name for pet in owner.pets]
    selected_pet_name = st.selectbox("Choose a pet", pet_options)

    task_description = st.text_input("Task description")
    task_time = st.text_input("Task time", "8:00 AM")
    task_duration = st.number_input("Duration in minutes", min_value=1, value=10)
    task_priority = st.selectbox("Priority", ["high", "medium", "low"])

    if st.button("Add Task"):
        for pet in owner.pets:
            if pet.name == selected_pet_name:
                new_task = Task(task_description, task_time, task_duration, task_priority)
                pet.add_task(new_task)
                st.success("Task added!")
else:
    st.info("Add a pet first before adding tasks.")

st.header("Today's Schedule")

if st.button("Generate Schedule"):
    scheduler = Scheduler(owner)
    schedule = scheduler.generate_schedule()

    if schedule:
        for pet_name, task in schedule:
            st.write(f"**{task.time} - {pet_name}: {task.description}**")
            st.write(f"Duration: {task.duration} minutes")
            st.write(f"Priority: {task.priority}")
            st.write("---")
    else:
        st.write("No tasks yet.")
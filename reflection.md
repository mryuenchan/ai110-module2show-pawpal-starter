# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
My initial UML design used four main classes: Owner, Pet, Task, and Scheduler.
- What classes did you include, and what responsibilities did you assign to each?
- Owner: stores owner information.
- Pet: stores pet information.
- CareTask: stores each task’s name, duration, and priority.
- Scheduler: chooses and organizes the tasks.
- DailyPlan: stores the final schedule for the day

**b. Design changes**

- Did your design change during implementation?
Yes, my design changed a little during implementation.  information.
- If yes, describe at least one change and why you made it.
At first, I thought about making separate classes for different tasks like walking, feeding, and medicine. I changed it to one general CareTask class because the tasks all used similar.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
My scheduler considers the time of each task, the pet the task belongs to, the task's completion status, and whether tasks have the same scheduled time. It can sort tasks by time, filter tasks by pet name or completion status, and detect simple conflicts when two tasks are scheduled at the same exact time.

- How did you decide which constraints mattered most?
The most important constraint was time because a daily schedule needs to be in the correct order. After that, filtering by pet and completion status was useful because it helps the owner focus on specific tasks.


**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff my scheduler makes is that the conflict detection only checks for exact matching times. For example, it can detect if two tasks both start at 9:00 AM, but it does not check if one task overlaps another based on duration.
- Why is that tradeoff reasonable for this scenario?
This is reasonable for this project because it keeps the code simple and easier to understand. A full calendar-style conflict checker would be more realistic, but it would also make the project more complicated.
---

## 3. AI Collaboration

**a. How you used AI**

I used AI to help brainstorm the class design, write the first version of the UML, create class skeletons, debug errors, and improve the scheduling logic. AI was also helpful when I needed short examples for tests and README documentation.

The most helpful prompts were specific questions, such as asking how the Scheduler should sort tasks by time, how to detect conflicts, or why an indentation error was happening. These prompts worked better than asking AI to do the whole project at once.

**b. Judgment and verification**

One moment where I did not accept the AI suggestion as-is was when the code did not match my actual files. I had to upload my real `app.py` and `pawpal_system.py` so the answer could be adjusted to my project.

I verified the suggestions by running `python main.py`, running `python -m pytest`, and checking whether the Streamlit app worked in the browser.

---

## 4. Testing and Verification

**a. What you tested**

I tested that a task can be marked complete, that adding a task to a pet increases the pet's task count, that the scheduler sorts tasks by time, that recurring daily tasks create the next task, and that conflicts are detected when two tasks have the same time.

These tests were important because they checked the main behaviors of the project. They helped confirm that the classes and scheduler logic worked before relying on the Streamlit app.

**b. Confidence**

I am about 4 out of 5 confident that my scheduler works correctly for the main requirements. The basic tests passed and the demo script showed the schedule working.

If I had more time, I would test invalid time formats, pets with no tasks, weekly recurring tasks, and overlapping tasks that start at different times but still conflict because of duration.

---

## 5. Reflection

**a. What went well**

The part I am most satisfied with is connecting the backend classes to the schedule logic. The Owner, Pet, Task, and Scheduler classes work together, and the app can show a real schedule instead of just placeholder UI.

**b. What you would improve**

If I had another iteration, I would improve the conflict detection. Right now, it only checks if two tasks start at the exact same time. A better version would also check whether tasks overlap based on duration.

**c. Key takeaway**

One important thing I learned is that system design makes coding easier. Starting with classes and responsibilities helped me understand how the app should be organized before writing all the logic.
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

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

"""
This code is a possible answer to: create a spreadsheet to track students and milestone rewards. What should the rows and columns be?
"""


class Student:
    """
    the most important class in this system. The student class handles the logic for the student object.
    Each instance have a name and id, a list of open task, that the student should be handling now and a list of
    finished tasks containing each task that is marked as complete. It also has a list of all rewards the student
    already got and a list of pending rewards, so those steps can be separated.
    """
    class_id_number: int = 0
    all_students: list = []

    def __init__(self, name):
        self.name = name
        Student.class_id_number += 1
        self.student_id = self.class_id_number
        self.open_tasks: list = []
        self.finished_tasks: list = []
        self.rewards_student_got: list = []
        self.pending_rewards: list = []

        Student.all_students.append(self)

    def student_gain_reward(self, reward):
        """
        this method add a reward to the student object. it removes the reward from the pending list
        and adds it to the rewards_student_got list.
        :param reward: the reward to be gained by the student
        """
        if reward is not None:
            if reward in self.pending_rewards and reward not in self.rewards_student_got:
                self.pending_rewards.remove(reward)
                self.rewards_student_got.append(reward)
                if self not in reward.students_who_got_reward:
                    reward.add_reward_to_student(self)
            reward.add_reward_to_student(self)

    def remove_reward(self, reward):
        """
        in cases where the reward must be withdrawn from a student.
        :param reward: the reward to be taken
        """
        if reward not in self.rewards_student_got:
            return "student dont have that reward"
        self.rewards_student_got.remove(reward)

    def update_pending_rewards(self, reward, automatic_update: bool = False):
        """ usually the mark task as complete method only appends the reward to the
        pending reward list, so it can be manually updated by a human later. But there
        is this automatic_update boolean that when set to True, will do everything
        automatically."""

        if reward not in self.pending_rewards and reward not in self.rewards_student_got:
            self.pending_rewards.append(reward)
            if automatic_update:
                self.student_gain_reward(reward)

    def update_tasks(self):
        """
        This method is intended to update the open_tasks list with new tasks, depending on the
        requirements level of the task
        """
        level = len(self.finished_tasks)
        print(f"Level for {self.name} is {level}")
        for task in Task.all_tasks:
            if task not in self.finished_tasks: # and task not in self.open_tasks:
                if task.requirements <= level:
                    print(f"New Task Unlocked: \n {self.name} unlocked {task.name}")
                    self.open_tasks.append(task)

    def mark_task_as_complete(self, task, automatic_update: bool = False):
        """
        This method marks the task as completed by this student instance.
        it appends the task to the finished task list and removes it from the open_task list.
        It also updates the open_task list with new tasks.
        It also triggers reward logic, updating pending rewards.
        :param task: the task that was completed and now needs to be marked as such
        """

        print(f"{self.name} completed {task.name}")
        self.finished_tasks.append(task)
        self.open_tasks.remove(task)
        if task.reward is not None:
            print(f"{self.name} gained reward {task.reward.name}")
        self.update_pending_rewards(task.reward, automatic_update)
        self.update_tasks()

    @classmethod
    def get_all_students(cls):
        return cls.all_students


class Reward:
    """
    The Reward class handles all the logic involving rewards. Each reward object has an id and a list
    of all the students who got that reward.
    """
    class_id_number: int = 0
    all_rewards: list = []

    def __init__(self, name):
        self.name = name
        Reward.class_id_number += 1
        self.reward_id = self.class_id_number
        self.students_who_got_reward: list = []
        Reward.all_rewards.append(self)

    def __str__(self):
        return f"Reward: {self.name}; ID: {self.reward_id}"

    def add_reward_to_student(self, student):
        """

        :param student: the student to receive the reward
        :return: appends the student to the list of all students who got this same reward
        """
        if student not in self.students_who_got_reward:
            self.students_who_got_reward.append(student)

    @classmethod
    def get_all_rewards(cls):
        """

        :return: a list of all rewards instantiated with this class
        """
        return cls.all_rewards


class Task:
    """
    The task class handles the properties of task, as assigned to each student.
    Each task has a reward but the default value is None for those task that gives no rewards.
    """
    class_id_number: int = 0
    all_tasks: list = []

    def __init__(self, name, reward=None):
        self.name: str = name
        Task.class_id_number += 1
        self.task_id = self.class_id_number
        self.complete: bool = False
        self.requirements: int = 0
        self.reward = reward
        Task.all_tasks.append(self)

    @classmethod
    def get_all_tasks(cls):
        """

        :return: retrieve a list of all the task instantiated with this class.
        """
        return cls.all_tasks

    @classmethod
    def find_task_by_id(cls, task_id: int):
        """
        runs thru all_tasks class attribute and returns the instance with the referenced id
        :param task_id: an Integer referencing the task.id attribute
        :return: task if task is found or None if no task is found
        """
        for task in cls.all_tasks:
            if task.task_id == task_id:
                return task
        return None  # If returns None, task not found

    def set_requirements(self, level: int):
        """
        number of tasks that need to be completed before unlocking this task
        this number will be compared to the len(finished_tasks) attribute of student

        :param level: an integer that represent how many tasks must be completed before unlocking this.
        :return: updates the requirement level of the task. Default is 0.
        """

        self.requirements = level

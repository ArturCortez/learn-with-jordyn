"""
This code is a possible answer to: create a spreadsheet to track students and milestone rewards. What should the rows and columns be?
"""


class Student:
    # I hope this is a class variable. If it works, we'll increment this  on every instance
    # to create kinda unique ids
    class_id_number: int = 0
    all_students: list = []

    def __init__(self, name):
        self.name = name
        self.class_id_number += 1
        self.student_id = self.class_id_number
        self.rewards_student_got: list = []
        Student.all_students.append(self)

    def student_gain_reward(self, reward):
        if reward not in self.rewards_student_got:
            self.rewards_student_got.append(reward)
        reward.add_reward_to_student(reward, self)

    def remove_reward(self, reward):
        if reward not in self.rewards_student_got:
            return "student dont have that reward"
        self.rewards_student_got.remove(reward)

    @classmethod
    def get_all_students(cls):
        return cls.all_students


class Reward:
    class_id_number: int = 0
    all_rewards: list = []

    def __init__(self, name):
        self.name = name
        self.class_id_number += 1
        self.reward_id = self.class_id_number
        self.students_who_got_reward: list = []
        Reward.all_rewards.append(self)

    def add_reward_to_student(self, student):
        if student not in self.students_who_got_reward:
            self.students_who_got_reward.append(student)

    @classmethod
    def get_all_rewards(cls):
        return cls.all_rewards
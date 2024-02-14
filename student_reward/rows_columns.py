"""
This code is a possible answer to: create a spreadsheet to track students and milestone rewards. What should the rows
and columns be?
There is supposed to be a lot more students than rewards, so rows should be students and columns should be rewards.
"""

from student_rewards_classes import Student, Reward


def create_table_dict():
    students = Student.get_all_students()
    rewards = Reward.get_all_rewards()
    dict_student_reward = {}

    for student in students:
        for reward in rewards:
            if reward in student.rewards_student_got:
                dict_student_reward[(student.name, reward.name)] = 'Yes'
            else:
                dict_student_reward[(student.name, reward.name)] = 'No'

    return dict_student_reward


table_dict = create_table_dict()

# Example: Accessing whether a specific student received a specific reward
student_name = "Alice"
reward_name = "Math Excellence"
print(f"{student_name} received {reward_name}: {table_dict.get((student_name, reward_name), 'No')}")

"""
This code is a possible answer to: create a spreadsheet to track students and milestone rewards. What should the rows
and columns be?
There is supposed to be a lot more students than rewards, so rows should be students and columns should be rewards.
"""

from student_rewards_classes import Student, Reward, Task


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


def list_of_rewards_to_send() -> list:
    list_to_send = []
    for student in Student.get_all_students():
        list_to_send.append(student.pending_rewards)

    return list_to_send


def dict_of_rewards_to_send() -> dict:
    """
    creates a dictionary with key student and value list of rewards
    :return: dictionary
    """
    dict_to_send = {}

    for student in Student.get_all_students():
        reward_dict = {}
        for reward in student.rewards_student_got:
            if reward is not None:
                print(reward.name)
                reward_dict.update({reward.reward_id: reward.name})
        dict_to_send.update({student.name: reward_dict})

    return dict_to_send


def create_reward_example():
    rewards = [
        "Rome", "Milan", "Naples", "Turin", "Palermo",
        "Genoa", "Bologna", "Florence", "Bari", "Catania",
        "Venice", "Verona", "Messina", "Padua", "Trieste",
        "Taranto", "Brescia", "Prato", "Modena", "Reggio Emilia"
    ]
    for reward in rewards:
        yield Reward(reward)


def create_task_example():
    task_list = [
        "Push-ups", "Squats", "Lunges", "Planks", "Burpees",
        "Sit-ups", "Jumping Jacks", "Mountain Climbers", "Leg Raises", "High Knees",
        "Russian Twists", "Pull-ups", "Dips", "Wall Sit", "Step-ups",
        "Bear Crawls", "Bicycle Crunches", "Inchworms", "Skaters", "Arm Circles"
    ]
    reward_generator = create_reward_example()
    for task in task_list:
        reward = next(reward_generator)
        yield Task(task, reward)


def create_example_student():
    names = [
        "Alice", "Bob", "Charlie", "Emma", "Liam", "Olivia", "Noah", "Ava",
        "Ethan", "Isabella", "Mason", "Sophia", "Mia",
        "Logan", "Amelia", "Lucas", "Harper", "Charlotte",
        "Alexander", "Evelyn", "Benjamin", "Abigail", "Emily"
    ]
    for name in names:
        yield Student(name)


if __name__ == "__main__":

    task_generator = create_task_example()
    task1 = next(task_generator)
    task1.set_requirements(0)
    task2 = next(task_generator)
    task2.set_requirements(1)
    task3 = next(task_generator)
    task3.set_requirements(1)
    task4 = next(task_generator)
    task4.set_requirements(2)
    task5 = next(task_generator)
    task5.set_requirements(3)

    student_list = []
    student_generator = create_example_student()

    for i in range(5):
        student_list.append(next(student_generator))


    for student in Student.get_all_students():
        student.update_tasks()


    for student in Student.get_all_students():
        student.mark_task_as_complete(task1, automatic_update=True)

    for sublist in list_of_rewards_to_send():
        for item in sublist:
            print(str(item))

    dict_to_print = dict_of_rewards_to_send()
    print(dict_to_print)

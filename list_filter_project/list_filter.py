def list_filter(list_of_strings: list, substring: str) -> list:

    new_list = [element for element in list_of_strings if substring in element]

    return new_list


if __name__ == "__main__":
    phrases = [
        "And now",
        "the end is near",
        "and so I face",
        "the final curtain",
        "My friend",
        "I'll make it clear",
        "I'll state my case",
        "of which I'm certain",
    ]

    key = "tain"

    sublist = list_filter(phrases, key)

    print(sublist)

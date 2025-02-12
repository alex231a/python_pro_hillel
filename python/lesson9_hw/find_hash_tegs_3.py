"""Module with function that finds hashtags in text"""

import re


def find_tags(inp_text):
    """Function that finds hashtags in text"""
    pattern = r"#[0-9a-zA-Zа-яА-Яі]+"
    return re.findall(pattern, inp_text)


if __name__ == "__main__":
    TEXT = """
        #Програмування
        #Python3
        #AI2025
        #ВчимоРегулярніВирази
        #НовиниТехнологій
        #MachineLearning
        #TechNews2025
        #ChatGPT
        #Вибори2025
        #РозробкаПрограм
        something else
        One more example
    """
    print(find_tags(TEXT))

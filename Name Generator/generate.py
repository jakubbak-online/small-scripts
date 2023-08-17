import random


def random_line(filename="names.txt", word_count=2):
    words = list()

    with open(filename, "r") as f_inner:
        all_lines = f_inner.readlines()
        for count in range(word_count):
            line = random.choice(all_lines)
            words.append(line)

    to_return = str()
    for word in words:
        word = word.strip("\n")
        word += " "
        to_return += word

    return to_return


with open("output.txt", "w+") as f:
    for _ in range(100):
        print(random_line(), file=f)

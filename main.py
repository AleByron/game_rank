import json


def calculate_rank(score):

    while True:
        if score.isdigit():
            score = float(score)
            if -17.8 <= score <= 90:
                break
            else:
                score = input("Invalid score, enter your score: ")
        else:
            score = input("Invalid score, enter your score: ")

    with open('ranks.json', 'r') as file:
        json_file = json.load(file)

    ranks = []

    for rank in json_file:
        ranks.append(rank)

    for rank in ranks:
        if rank["score_start"] <= score <= rank["score_end"]:
            return rank["name"]


def main():
    score = input("Enter your score: ")
    print(calculate_rank(score))


if __name__ == '__main__':
    main()

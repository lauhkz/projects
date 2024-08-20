dict1 = { "first_quarter": 24, "second_quarter": 31}
dict2 = { "third_quarter": 29, "fourth_quarter": 40}

score_dict = ({
    "first_quarter": 24, "second_quarter": 31}, {
    "third_quarter": 29, "fourth_quarter": 40
})
"""
The merge function accepts two scores dictionaries as input and returns a single /merged/ dictionary
that contains all of the keys and values from the input dictionaries.
"""
def merge(dict1, dict2):
    score_dict = {}

    for key in dict1:
        score_dict[key] = dict1[key]

    for key in dict2:
        score_dict[key] = dict2[key]
    print(score_dict)
    #return score_dict

def totalScore(score_dict):
    total = 0
    for key in score_dict:
        total += score_dict[key]
    print(total)

merge(dict1, dict2)
totalScore(score_dict)

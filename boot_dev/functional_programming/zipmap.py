keys = ["The Grand Budapest Hotel", "Fantastic Mr. Fox", "Moonrise Kingdom"]
values = [8.1, 7.9, 7.8]

"""
2. Recursively call zipmap on all but the first elements from keys and values
3. Add the first element of keys to the resulting dictionary, and set its value to the first element in values
4. Return the updated dictionary
"""


def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return dict()
    rec = dict(zipmap(keys[1:], values[1:]))
    rec[keys[0]] = values[0]
    return rec


print(zipmap(keys, values))

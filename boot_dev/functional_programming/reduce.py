import functools

joined = [
    "This is the first sentence",
    "This is the second sentence",
    "This is the third sentence",
]

# This is the first sentence. This is the second sentence.


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_setences(sentences, n=input("enter 'n':")):
    if n != 0:
        return "".join(functools.reduce(join, sentences[: int(n)])) + "."
    return ""


print(
    join_first_setences(
        joined,
    )
)

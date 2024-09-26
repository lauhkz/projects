documents = ("hello there", "sonny", "how ya doing")


def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = (prefix + document,)
    new_tuple = documents + new_doc
    return new_tuple

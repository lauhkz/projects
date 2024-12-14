
def new_collection(initial_docs):
    def inner_func(string):
        list_copy = initial_docs.copy()
        if isinstance(string, list):
            for str in string:
                list_copy.append(str)
            return list_copy
        else:
            list_copy.append(string)
            return list_copy
    return inner_func


nw_collection = new_collection(["doc1", "doc2", "doc3", "doc4"])

print(nw_collection(["doc5", "doc6"]))

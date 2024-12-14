test = [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])]


def file_type_getter(file_extension_tuples):
    dic = {}
    for extension in file_extension_tuples:
        for k in extension[1]:
            dic[k] = extension[0]

    return lambda key: file_extension_tuples.get(key, "Unknown")


print(file_type_getter(test))

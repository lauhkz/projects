test = [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])]


def file_type_getter(file_extentions_tuples):
    extentions_dict = {}

    for file in file_extentions_tuples:
        for extension in file[1]:
            extentions_dict[extension] = file[0]

    return lambda file: extentions_dict.get(file, "Unknown")


print(file_type_getter(test))

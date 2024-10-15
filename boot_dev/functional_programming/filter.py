run_cases = "\n* We are the music makers\n- And we are the dreamers of dreams\n* Come with me and you'll be\n"


def remove_invalid_lines(document):
    striped = document.split("\n")
    new_doc = list(filter(lambda lines: not lines.startswith("-"), striped))
    "\n".join(new_doc)
    return "\n".join(
        (filter(lambda lines: not lines.startswith("-"), document.split("\n")))
    )
    # i did it

    print(striped)
    print(new_doc)


print(remove_invalid_lines(run_cases))

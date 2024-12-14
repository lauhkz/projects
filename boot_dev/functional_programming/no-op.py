test = "The **answer to the ultimate question** of life, the universe and everything is *42*\n"

#"The answer to the ultimate question of life, the universe and everything is 42\n"

def remove_emphasis_from_word(word):
    formated = "".join(list(map(lambda w: w.strip("*"), word)))
    return formated

def remove_emphasis_from_line(line):
    formated = " ".join(list(map(remove_emphasis_from_word, line.split(" "))))
    return formated

def remove_emphasis(document):
    if len(document) == 0:
        return
    formated = list(map(remove_emphasis_from_line, document.split("\n")))
    return formated

    

print(remove_emphasis(test))
print(remove_emphasis_from_line(test))

test = """###
@##
$$$
###"""
# The inputs of this function are, the character that we want to "search",
# the sequence length of our character, and the document to search.

def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            counter = 0
            lines = doc.split("\n")
            for line in lines:
                if sequence in line:
                    counter += 1
            return counter
        return with_length
    return with_char


print(lines_with_sequence("#")(3)(test))

messages = ['darn it', "this dang thing won't work", 'lets fight one on one']

def filter_messages(messages):
    filtered_list = []
    count_of_dangs = []
    final_list = []

    for message in messages:
        counter = 0

        if ("dang" in message):
            counter += 1
            count_of_dangs.append(counter)

        filtered_list += message.split("dang")

    for word in filtered_list:
        final_list += word.split()

    final_list = " ".join(final_list)
    del filtered_list[:]
    filtered_list.append(final_list)


    print(filtered_list)
    print(f"and these are the total of bad words sayed {count_of_dangs}")

"""
that code transform all the elements in one string (without the "dang") and returns a list with the string
almost ;-;
"""

#filter_messages(messages)

# this is the solution that accidentaly the bot gave me (i only wanted to know how to remove the whitespace left in the string)

def working_filter_messages(messages):
    filtered_list = []
    count_of_dangs = []

    for message in messages:
        counter = 0
        words = message.split()
        cleaned_words = []

        for word in words:
            if (word == "dang"):
                counter += 1
            else:
                cleaned_words.append(word)

        filtered_list.append(" ".join(cleaned_words))
        count_of_dangs.append(counter)

    print(filtered_list, count_of_dangs)
    #return filtered_list, count_of_dangs



working_filter_messages(messages)

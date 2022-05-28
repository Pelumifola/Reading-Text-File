def read_file_content(filename):
    with open(filename) as data:
        data_file = data.read()
        return data_file

def count_words():
    text = read_file_content("./story.txt").lower()
    split_text = text.split()
    strip_text = [txt.strip(", . ?") for txt in split_text]
    set_text = set(strip_text)
    dict_word = {}
    for word in set_text:
        count = strip_text.count(word)
        dict_word[word] = count
    return dict_word

print(count_words())


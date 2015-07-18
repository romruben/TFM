import os

PROCESSED_CORPUS_PATH = os.getcwd() + "/processed_corpus/"

def readfile(path):
    return open(path, 'r').read()

def get_tags(text):
    tokens = text.replace("\n", "").split(" ")
    del tokens[-1]
    tags = []

    for token in tokens:
        tokensplitted = token.split("_")
        if token!="" and len(tokensplitted)> 1 and tokensplitted[1] not in tags:
            tags.append(tokensplitted[1])

    return tags

def get_cleaned_text(text, detected_tags):
    for tag in detected_tags: text = text.replace("_"+tag, "")
    return text


def write_tags_files(detected_tags):
    f = open(PROCESSED_CORPUS_PATH + 'tags.txt', 'wb+')
    for tag in detected_tags: f.write(tag+"\n")
    f.close()

def write_clean_content(text):
    f = open(PROCESSED_CORPUS_PATH + 'processed_text.txt', 'wb+')
    f.write(text)
    f.close()


content = readfile("detroit.txt")

tags = get_tags(content)
write_tags_files(tags)

cleaned_text = get_cleaned_text(content, tags)
write_clean_content(cleaned_text)





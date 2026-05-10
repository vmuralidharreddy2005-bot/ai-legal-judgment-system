def extract_entities(text):

    words = text.split()

    entities = []

    for word in words:

        if word.istitle():

            entities.append(word)

    return list(set(entities))
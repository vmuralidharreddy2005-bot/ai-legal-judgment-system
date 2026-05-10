def legal_chatbot(question, text):

    question = question.lower()

    text = text.lower()

    # Fraud detection
    if "fraud" in question:

        if "fraud" in text or "cheating" in text:

            return "Yes, the document mentions fraud or cheating related activities."

        else:

            return "No fraud-related content was found."

    # IPC detection
    elif "ipc" in question:

        if "420" in text:

            return "IPC 420 is mentioned in the document."

        else:

            return "No IPC section was identified."

    # Punishment detection
    elif "punishment" in question or "sentence" in question:

        if "imprisonment" in text:

            return "The document mentions imprisonment as punishment."

        else:

            return "Punishment information was not found."

    # Summary request
    elif "summary" in question:

        return "This legal case discusses criminal activities and court judgment."

    else:

        return "Sorry, I could not understand the legal question."
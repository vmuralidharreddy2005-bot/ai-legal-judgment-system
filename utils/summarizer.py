from transformers import pipeline

def generate_summary(text):

    # Load summarization pipeline
    summarizer = pipeline(
        task="summarization",
        model="facebook/bart-large-cnn"
    )

    # Reduce large text
    text = text[:2000]

    # Generate summary
    result = summarizer(
        text,
        max_length=120,
        min_length=40,
        do_sample=False
    )

    return result[0]["summary_text"]
import streamlit as st
import plotly.express as px

from utils.pdf_reader import extract_text
from utils.preprocess import preprocess_text
from utils.entity_extractor import extract_entities
from utils.similarity import find_similar_cases
from utils.summarizer import generate_summary
from utils.predictor import predict_case
from utils.chatbot import legal_chatbot
from utils.report_generator import generate_pdf_report

# Page settings
st.set_page_config(
    page_title="AI Legal Judgment Prediction System",
    page_icon="⚖",
    layout="wide"
)

# Sidebar
st.sidebar.title("⚖ Legal AI Dashboard")

st.sidebar.info(
    "AI-powered legal document analysis using NLP, Machine Learning, and Transformers."
)

st.sidebar.markdown("---")

st.sidebar.write("Features:")
st.sidebar.write("✔ PDF Analysis")
st.sidebar.write("✔ AI Summarization")
st.sidebar.write("✔ Fraud Prediction")
st.sidebar.write("✔ Semantic Search")
st.sidebar.write("✔ AI Legal Chatbot")
st.sidebar.write("✔ Analytics Dashboard")
st.sidebar.write("✔ PDF Report Download")

# Main title
st.title("⚖ AI Legal Judgment Prediction System")

st.markdown(
    "Upload a legal PDF document and analyze it using Artificial Intelligence."
)

# Upload PDF
uploaded_file = st.file_uploader(
    "📂 Upload Legal PDF File",
    type=["pdf"]
)

if uploaded_file is not None:

    # Save uploaded PDF
    with open("temp_case.pdf", "wb") as f:

        f.write(uploaded_file.read())

    # Extract text
    text = extract_text("temp_case.pdf")

    # NLP preprocessing
    cleaned_text = preprocess_text(text)

    # Entity extraction
    entities = extract_entities(text)

    # Similarity search
    similarities = find_similar_cases(cleaned_text)

    # Prediction
    prediction, probability = predict_case(cleaned_text)

    # Generate summary
    with st.spinner("Generating AI Summary..."):

        summary = generate_summary(text)

    # Prediction label
    if prediction == 1:

        prediction_label = "Fraud Case"

    else:

        prediction_label = "Non-Fraud Case"

    confidence_score = max(probability) * 100

    # Generate PDF report
    report_path = generate_pdf_report(

        summary,
        prediction_label,
        confidence_score
    )

    # Top metrics
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            label="Document Length",
            value=f"{len(text.split())} words"
        )

    with col2:

        st.metric(
            label="Entities Found",
            value=len(entities)
        )

    with col3:

        st.metric(
            label="Prediction Confidence",
            value=f"{confidence_score:.2f}%"
        )

    st.markdown("---")

    # Prediction section
    st.subheader("⚖ AI Judgment Prediction")

    if prediction == 1:

        st.error("🚨 Predicted Result: Fraud Case")

    else:

        st.success("✅ Predicted Result: Non-Fraud Case")

    # AI Summary
    st.subheader("🧠 AI Generated Summary")

    st.info(summary)

    # Download PDF report
    st.subheader("📥 Download AI Report")

    with open(report_path, "rb") as pdf_file:

        st.download_button(
            label="Download PDF Report",
            data=pdf_file,
            file_name="AI_Legal_Report.pdf",
            mime="application/pdf"
        )

    # Original extracted text
    st.subheader("📄 Extracted PDF Text")

    st.write(text)

    # Cleaned NLP text
    st.subheader("🧹 Cleaned NLP Text")

    st.write(cleaned_text)

    # Entities
    st.subheader("🏷 Extracted Legal Entities")

    if entities:

        for entity in entities:

            st.write(f"• {entity}")

    else:

        st.write("No entities found.")

    # Similar cases
    st.subheader("⚡ Similar Legal Cases")

    for i, score in enumerate(similarities):

        st.progress(float(score))

        st.write(f"Case {i+1} Similarity Score: {score:.2f}")

    # Analytics dashboard
    st.subheader("📊 Legal Analytics Dashboard")

    case_names = [
        "Case 1",
        "Case 2",
        "Case 3",
        "Case 4"
    ]

    scores = similarities.tolist()

    fig = px.bar(

        x=case_names,
        y=scores,

        labels={
            "x": "Legal Cases",
            "y": "Similarity Score"
        },

        title="Legal Case Similarity Analysis"
    )

    st.plotly_chart(fig, use_container_width=True)

    # AI chatbot
    st.subheader("🤖 AI Legal Chatbot")

    user_question = st.text_input(
        "Ask a question about the uploaded legal document"
    )

    if user_question:

        answer = legal_chatbot(user_question, text)

        st.success(answer)
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
import matplotlib.pyplot as plt
import random
import time

st.set_page_config(page_title="AI Sentiment Analyzer", layout="centered")

MODEL_PATH = "tiny_model"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

st.title("🧠 AI Review Sentiment Analyzer")

# ---------------- SAMPLE GENERATION ---------------- #

def generate_samples():
    samples = random.sample([
        # Product reviews
        "The product quality is amazing and exceeded expectations",
        "Battery drains too fast and overheats frequently",
        "Fantastic experience, would definitely buy again",
        "Completely disappointed with the build quality",
        "Delivery was quick and packaging was neat",
        "Highly recommended for everyone",
        "Not worth the price at all",

        # Movie reviews added
        "The movie was absolutely fantastic with brilliant acting",
        "Terrible storyline and poor direction ruined the film",
        "An emotional masterpiece and beautifully shot scenes",
        "Worst movie I have watched this year",
        "The plot was weak but performances were decent",
        "A complete waste of time and money",
        "The cinematography and music were outstanding"
    ], 5)
    return "\n".join(samples)

# ---------------- INPUT ---------------- #

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

user_input = st.text_area(
    "Enter review(s)",
    value=st.session_state.input_text,
    height=200,
    placeholder="Write one or multiple reviews (one per line)"
)

col1, col2 = st.columns(2)

with col1:
    analyze_clicked = st.button("Analyze Reviews", use_container_width=True)

with col2:
    if st.button("Generate Example Reviews", use_container_width=True):
        st.session_state.input_text = generate_samples()
        st.rerun()

# ---------------- MODEL PREDICT ---------------- #

def predict(text):

    # ---------- rule-based negative guard ----------
    negative_keywords = ["worst", "not worth", "waste", "bad", "poor", "terrible", "awful"]

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        pred = torch.argmax(probs).item()
        confidence = probs[0][pred].item()

    sentiment = "Positive" if pred == 1 else "Negative"

    # override ONLY when obvious negative phrase appears
    if any(word in text.lower() for word in negative_keywords):
        sentiment = "Negative"
        confidence = max(confidence, 0.90)

    return sentiment, confidence


# ---------------- ANALYSIS ---------------- #

if analyze_clicked:

    if not user_input.strip():
        st.warning("Enter at least one review.")
        st.stop()

    reviews = [r.strip() for r in user_input.split("\n") if r.strip()]

    positive, negative = 0, 0
    pos_reviews, neg_reviews = [], []

    # 🔄 Loading animation
    loading = st.empty()
    progress = st.progress(0)

    loading.markdown("### 🔍 Running sentiment inference...")

    for i, review in enumerate(reviews):
        sentiment, conf = predict(review)

        if sentiment == "Positive":
            positive += 1
            pos_reviews.append((review, conf))
        else:
            negative += 1
            neg_reviews.append((review, conf))

        progress.progress((i + 1) / len(reviews))
        time.sleep(0.05)

    loading.empty()
    progress.empty()

    st.divider()
    st.subheader("📊 Analyzed Reviews")

    pos_col, neg_col = st.columns(2)

    with pos_col:
        st.markdown("#### 🟦 Positive Reviews")
        for review, conf in pos_reviews:
            st.markdown(
                f"""
                <div style="
                    background-color:#e8f6ff;
                    padding:14px;
                    border-radius:12px;
                    margin-bottom:12px;
                    border-left:8px solid #007acc;
                    box-shadow:0px 2px 6px rgba(0,0,0,0.08);
                    color:#00324d;">
                    <span style="font-size:15px; font-weight:500;">{review}</span><br>
                    <span style="font-weight:700;">
                        Confidence: {conf*100:.1f}%
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    with neg_col:
        st.markdown("#### 🟥 Negative Reviews")
        for review, conf in neg_reviews:
            st.markdown(
                f"""
                <div style="
                    background-color:#ffe9e9;
                    padding:14px;
                    border-radius:12px;
                    margin-bottom:12px;
                    border-left:8px solid #cc0000;
                    box-shadow:0px 2px 6px rgba(0,0,0,0.08);
                    color:#4d0000;">
                    <span style="font-size:15px; font-weight:500;">{review}</span><br>
                    <span style="font-weight:700;">
                        Confidence: {conf*100:.1f}%
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    total = positive + negative

    if total > 0:
        st.divider()
        st.subheader("📉 Overall Sentiment")

        fig, ax = plt.subplots(figsize=(3,3))
        ax.pie(
            [positive, negative],
            labels=["Positive", "Negative"],
            autopct="%1.1f%%",
            textprops={'fontsize':9}
        )
        plt.tight_layout()
        st.pyplot(fig)

# ---------------- FOOTER ---------------- #

st.divider()
st.markdown(
    """
    <div style='text-align:center; padding:15px; color:gray; font-size:13px'>
        TinyBERT Sentiment Engine with Streamlit UI 
    </div>
    """,
    unsafe_allow_html=True
)
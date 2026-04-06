# 🧠 Review Sentiment Analysis using BERT

A lightweight NLP web application that classifies product and movie reviews as **Positive** or **Negative** using a fine-tuned **TinyBERT** model.

Built with **Streamlit · HuggingFace Transformers · PyTorch · Render**, this project demonstrates how to train, optimize, and deploy a compact transformer model into a fully functional real-time inference system.

---

# 🚀 Live Demo

🔗 **https://review-sentiment-analysis-using-tiny.onrender.com**

This hosted application allows users to:

* Input one or multiple reviews
* Run real-time sentiment classification
* Visualize results instantly
* Analyze aggregated sentiment trends

---

# 📌 Project Motivation

Modern sentiment analysis systems often rely on large transformer models that are computationally expensive and slow to deploy.

This project was designed to:

* Demonstrate **efficient transformer deployment**
* Use **lightweight models suitable for free cloud hosting**
* Showcase **end-to-end ML workflow**
* Provide **interactive real-time inference**
* Simulate production-grade NLP pipeline design

Instead of using large models like BERT-base, this project uses:

```text
TinyBERT — lightweight, fast, deployable
```

---

# 🧠 Model Architecture

## Base Model

```text
prajjwal1/bert-tiny
```

This is a compressed version of BERT designed for:

* Faster inference
* Lower memory footprint
* Lightweight deployment
* Edge-compatible inference

---

## Model Specifications

| Property           | Value                        |
| ------------------ | ---------------------------- |
| Base Model         | prajjwal1/bert-tiny          |
| Layers             | 2 Transformer Encoder Layers |
| Hidden Size        | 128                          |
| Attention Heads    | 2                            |
| Parameters         | ~4 Million                   |
| Model Size         | ~17 MB                       |
| Output Classes     | Positive / Negative          |
| Framework          | PyTorch                      |
| Tokenizer          | WordPiece Tokenizer          |
| Training Framework | HuggingFace Transformers     |

---

## Why TinyBERT Was Chosen

Key reasons:

* Small memory footprint
* Fast inference time
* Ideal for free-tier deployment
* Reduced cold-start latency
* Suitable for production demos

Compared to BERT-base:

| Model     | Size   |
| --------- | ------ |
| BERT-base | ~420MB |
| TinyBERT  | ~17MB  |

That difference makes deployment practical.

---

# 🏗️ System Architecture

The system follows a **single-service inference architecture**.

```text
User Input
     ↓
Streamlit UI
     ↓
Tokenizer
     ↓
TinyBERT Model
     ↓
Prediction Logic
     ↓
Rule-Based Override
     ↓
Visualization Engine
     ↓
Final Output
```

---

# ⚙️ Application Workflow

## Step-by-Step Flow

1. User enters review text
2. Text is tokenized using WordPiece tokenizer
3. Input tokens passed into TinyBERT model
4. Model produces probability scores
5. Confidence calculated
6. Rule-based overrides applied (if needed)
7. Results displayed visually
8. Aggregate statistics generated

---

# 🧪 Hybrid Inference Design

This project uses:

```text
Model-based inference + Rule-based override
```

This improves reliability.

---

## Why Hybrid Inference?

Pure ML models sometimes misclassify:

```text
Worst product ever → incorrectly predicted Positive
```

To fix edge cases, rule-based logic detects:

```text
worst
terrible
waste
broken
refund
useless
```

These trigger **forced Negative classification**.

---

## Hybrid Logic Flow

```text
Model predicts sentiment
        ↓
Check negative keyword list
        ↓
Override if strong negative keyword detected
```

---

# 📊 Visualization System

The UI displays:

* Individual predictions
* Confidence scores
* Sentiment distribution
* Summary statistics

Visualization components:

```text
Positive Review Cards
Negative Review Cards
Pie Chart Summary
Progress Indicator
Confidence Metrics
```

---

# 🎯 Key Features

## Multi-review Input

Users can analyze:

```text
One review
Multiple reviews
Batch review sets
```

Each line = one review.

---

## Real-time Inference

The system performs:

```text
Live prediction
Immediate rendering
Incremental progress tracking
```

---

## Confidence Scoring

Each review produces:

```text
Sentiment label
Confidence percentage
```

Confidence derived from:

```text
Softmax probability
```

---

## Demo Review Generator

One-click demo feature generates:

```text
Random realistic review samples
```

Useful for:

* Testing
* Demonstrations
* UI validation

---

# 🏗️ Tech Stack

## Frontend

```text
Streamlit
```

Used for:

* UI rendering
* Input handling
* Visualization
* Interactive workflow

---

## Machine Learning

```text
HuggingFace Transformers
PyTorch
```

Used for:

* Model loading
* Tokenization
* Inference
* Probability scoring

---

## Visualization

```text
Matplotlib
```

Used for:

```text
Pie chart generation
Sentiment distribution display
```

---

## Deployment Platform

```text
Render Web Service
```

Used for:

```text
Cloud hosting
Automatic deployment
Web accessibility
```

---

# 📁 Detailed Project Structure

```text
Review_Sentiment_Analysis_using_tiny-BERT/
│
├── app.py
│   Streamlit UI logic
│   Model inference pipeline
│   Visualization rendering
│
├── requirements.txt
│   Python dependencies
│   Version-pinned libraries
│
├── render.yaml
│   Deployment configuration
│   Runtime specification
│
├── .streamlit/
│   └── config.toml
│       Theme settings
│       Server configuration
│
├── tiny_model/
│   Pretrained model artifacts
│
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── tokenizer_config.json
│
└── README.md
```

---

# 🔧 Model Training Pipeline (Conceptual)

Although deployed as inference-only, the training process followed:

```text
Dataset loading
Text preprocessing
Tokenization
Model fine-tuning
Validation
Model saving
Deployment preparation
```

---

## Training Dataset

Dataset:

```text
IMDb Movie Reviews Dataset (subset)
```

Used for:

```text
Binary sentiment classification
```

---

## Training Steps

1. Load dataset
2. Clean text
3. Tokenize using WordPiece
4. Train TinyBERT
5. Evaluate accuracy
6. Save trained model

---

# 📈 Performance Considerations

TinyBERT advantages:

```text
Fast inference
Low latency
Low memory usage
Suitable for free hosting
```

---

## Estimated Runtime Metrics

| Metric          | Value        |
| --------------- | ------------ |
| Model Load Time | ~2–4 seconds |
| Inference Time  | < 200 ms     |
| Memory Usage    | ~200–300MB   |
| Deployment Size | ~17MB        |

---

# 🛠️ Local Setup

```bash
git clone https://github.com/Vinayak45541/Review_Sentiment_Analysis_using_tiny-BERT.git

cd Review_Sentiment_Analysis_using_tiny-BERT

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

# ☁️ Deployment Configuration

Platform:

```text
Render
```

Deployment Details:

| Field         | Value                                                             |
| ------------- | ----------------------------------------------------------------- |
| Runtime       | Python 3                                                          |
| Build Command | pip install -r requirements.txt                                   |
| Start Command | streamlit run app.py --server.port $PORT --server.address 0.0.0.0 |
| Instance Type | Free Tier                                                         |

---

# 🧪 Example Inputs

## Positive

```text
The product quality is amazing
Fantastic experience overall
Loved the performance
```

## Negative

```text
Worst purchase ever
Battery drains quickly
Complete waste of money
```

---

# 🧠 Engineering Highlights

This project demonstrates:

```text
Transformer model deployment
Hybrid inference design
Real-time NLP UI integration
Cloud deployment workflow
Memory-efficient ML engineering
```

---

# 🎯 Use Cases

This system can be used for:

```text
Product review analysis
Customer feedback analysis
Movie review sentiment detection
Market sentiment monitoring
User feedback classification
```

---

# 🚧 Future Improvements

Potential upgrades:

```text
Multi-class sentiment detection
Emotion classification
Model quantization
Batch inference optimization
REST API integration
Database logging
User authentication
Dashboard analytics
```

---

# 📄 License

MIT License

This project is open-source and available for educational and professional use.

---

# 👨‍💻 Author

**Vinayak**

Engineering Student — Machine Learning & Full-Stack Development

Focus Areas:

```text
Natural Language Processing
Model Deployment
Full Stack ML Applications
Production ML Engineering
```

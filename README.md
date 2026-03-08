# 🧠 TinyBERT Sentiment Analysis Web App

A lightweight web application that performs **binary sentiment classification** (Positive / Negative) using a fine-tuned **TinyBERT** model.  
Built with **Streamlit** and **HuggingFace Transformers**, the app provides real-time predictions with confidence scores and visual summaries.

---

## 🚀 Live Demo

🔗 [https://reviewsentimentanalysisusingtiny-bert-85nhkqhr6fkgr6dopd7wgc.streamlit.app/](https://reviewsentimentanalysisusingtiny-bert-85nhkqhr6fkgr6dopd7wgc.streamlit.app/)

---

## 📌 Project Summary

This project demonstrates:

- Fine-tuning a compact Transformer model for sentiment analysis  
- Optimizing model size for cloud deployment  
- Building an interactive NLP web interface  
- Deploying a production-ready app using Streamlit Cloud  

---

## 🧠 Model Details

| Property | Details |
|---|---|
| Base Model | `prajjwal1/bert-tiny` |
| Architecture | 2-layer Transformer encoder |
| Parameters | ~4M |
| Task | Binary sentiment classification |
| Training Data | IMDb movie reviews (subset) |
| Framework | PyTorch + HuggingFace Transformers |
| Model Size | ~17 MB |

> TinyBERT was chosen to ensure fast inference and stable cloud deployment while maintaining reasonable accuracy.

---

## ⚙️ Features

### 🔍 Sentiment Prediction
- Supports single and multi-line reviews  
- Displays confidence score per review  
- Real-time inference with progress bar  

### 🎨 Visualization
- Side-by-side display of positive and negative reviews  
- Pie chart showing overall sentiment distribution  

### 🤖 Hybrid Inference Logic
In addition to model predictions, rule-based checks handle clearly negative phrases (e.g., *worst*, *not worth*, *waste*, *terrible*) to improve short-text reliability.

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| ML Model | HuggingFace Transformers + PyTorch |
| Visualization | Matplotlib |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure

```
Review_Sentiment_Analysis_using_tiny-BERT/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Pinned Python dependencies
├── packages.txt              # System-level apt packages (for Linux/Cloud)
├── .gitignore
│
├── .streamlit/
│   └── config.toml           # Theme and server configuration
│
├── tiny_model/               # Fine-tuned TinyBERT model files
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── tokenizer_config.json
│
└── README.md
```

---

## 🛠️ Local Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Vinayak45541/Review_Sentiment_Analysis_using_tiny-BERT.git
cd Review_Sentiment_Analysis_using_tiny-BERT
```

### 2️⃣ Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application
```bash
streamlit run app.py
```

---

## ☁️ Deploying to Streamlit Cloud

1. Push this repository to GitHub (ensure `tiny_model/` folder is committed)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New App** → select your repo → set **Main file path** to `app.py`
4. Click **Deploy**

> No environment variable setup is needed — the model loads from the local `tiny_model/` directory.

---

## 🧪 Example Inputs

**Positive**
- This movie was amazing and emotional  
- Excellent product quality and value for money  

**Negative**
- Worst purchase I have made this year  
- Not worth the price at all  

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

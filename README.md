# 🧠 TinyBERT Sentiment Analysis Web App

A lightweight web application that performs **binary sentiment classification** (Positive / Negative) using a fine-tuned **TinyBERT** model.  
Built with **Streamlit** and **HuggingFace Transformers**, the app provides real-time predictions with confidence scores and visual summaries.

---

## 🚀 Live Demo

🔗 https://reviewsentimentanalysisusingtiny-bert-85nhkqhr6fkgr6dopd7wgc.streamlit.app/

---

## 📌 Project Summary

This project demonstrates:

- Fine-tuning a compact Transformer model for sentiment analysis  
- Optimizing model size for cloud deployment  
- Building an interactive NLP web interface  
- Deploying a production-ready app using Streamlit Cloud  


---

## 🧠 Model Details

- Base Model: `prajjwal1/bert-tiny`  
- Architecture: 2-layer Transformer encoder  
- Parameters: ~4M  
- Task: Binary sentiment classification  
- Training Data: IMDb movie reviews (subset)  
- Framework: PyTorch + HuggingFace Transformers  
- Model Size: ~15–20 MB  

TinyBERT was chosen to ensure fast inference and stable cloud deployment while maintaining reasonable accuracy.

---

## ⚙️ Features

### 🔍 Sentiment Prediction
- Supports single and multi-line reviews  
- Displays confidence score  
- Real-time inference  

### 🎨 Visualization
- Separate display of positive and negative reviews  
- Pie chart showing overall sentiment distribution  

### 🤖 Hybrid Inference Logic
In addition to model predictions, basic rule-based checks handle clearly negative phrases (e.g., *worst*, *not worth*, *waste*, *terrible*) to improve short-text reliability.

---

## 🏗️ Tech Stack

- Python  
- Streamlit  
- PyTorch  
- HuggingFace Transformers  
- Matplotlib  

---

## 📁 Project Structure

```
Review_Sentiment_Analysis_using_tiny-BERT/
│
├── app.py
├── requirements.txt
│
├── tiny_model/
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
```
git clone https://github.com/Vinayak45541/Review_Sentiment_Analysis_using_tiny-BERT.git
cd Review_Sentiment_Analysis_using_tiny-BERT
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run Application
```
streamlit run app.py
```

---

## 🧪 Example Inputs

**Positive**
- This movie was amazing and emotional  
- Excellent product quality and value for money  

**Negative**
- Worst purchase I have made this year  
- Not worth the price at all  

---

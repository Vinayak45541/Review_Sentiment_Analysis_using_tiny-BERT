# 🧠 Review Sentiment Analysis using TinyBERT

A lightweight NLP web application that classifies product and movie reviews as **Positive** or **Negative** using a fine-tuned **TinyBERT** model.

Built with **Streamlit** · **HuggingFace Transformers** · **PyTorch** · Deployed on **Render**

---

## 🚀 Live Demo

🔗 **[https://review-sentiment-analysis-using-tiny.onrender.com](https://review-sentiment-analysis-using-tiny.onrender.com)**


---

## 📌 Overview

This project demonstrates:
- Fine-tuning a compact Transformer model (`prajjwal1/bert-tiny`) for binary sentiment classification
- Hybrid inference combining model predictions with rule-based keyword overrides for edge cases
- Building an interactive NLP web interface with real-time results and visualizations
- Cloud deployment using Render

---

## 🧠 Model Details

| Property | Value |
|---|---|
| Base Model | `prajjwal1/bert-tiny` |
| Architecture | 2-layer Transformer encoder |
| Parameters | ~4 Million |
| Task | Binary Sentiment Classification (Positive / Negative) |
| Training Data | IMDb movie reviews (subset) |
| Framework | PyTorch + HuggingFace Transformers |
| Model Size | ~17 MB |

---

## ⚙️ Features

- **Multi-review input** — analyze one or many reviews at once (one per line)
- **Confidence scores** — each review shows model confidence %
- **Hybrid inference** — rule-based keyword check for clearly negative phrases (*worst, terrible, waste*, etc.)
- **Visual summary** — side-by-side positive/negative cards + pie chart
- **Example generator** — one-click sample reviews for quick testing

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| UI Framework | Streamlit |
| ML Model | HuggingFace Transformers |
| Deep Learning | PyTorch |
| Visualization | Matplotlib |
| Deployment | Render (Web Service) |

---

## 📁 Project Structure

```
Review_Sentiment_Analysis_using_tiny-BERT/
│
├── app.py                    # Streamlit application
├── requirements.txt          # Python dependencies (pinned)
├── render.yaml               # Render deployment config
├── .gitignore
│
├── .streamlit/
│   └── config.toml           # Streamlit theme & server settings
│
├── tiny_model/               # Fine-tuned TinyBERT model
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── tokenizer_config.json
│
└── README.md
```

---

## 🛠️ Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/Vinayak45541/Review_Sentiment_Analysis_using_tiny-BERT.git
cd Review_Sentiment_Analysis_using_tiny-BERT

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

## ☁️ Deployment (Render)

| Field | Value |
|---|---|
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |
| Instance Type | Free |

The `render.yaml` in this repo auto-configures the above settings.

---

## 🧪 Example Inputs

**Positive Reviews**
```
The product quality is amazing and exceeded expectations
Fantastic experience, would definitely buy again
An emotional masterpiece and beautifully shot scenes
```

**Negative Reviews**
```
Worst purchase I have made this year
Battery drains too fast and overheats frequently
A complete waste of time and money
```

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

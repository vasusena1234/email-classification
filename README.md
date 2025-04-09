# 📧 Email Spam Detection using Machine Learning

This project builds, trains, and serves a machine learning model that detects whether a given email message is **spam** or **ham (not spam)**. It uses Python, Scikit-learn, and basic MLOps principles with Docker for reproducibility. The model is deployed as a REST API to serve predictions.

---

## 🗂️ Project Structure

```
email-spam-detection/
├── pipelines/
│   └── main.py # Training pipeline script
├── training/
│   └── spam.csv # Input dataset (SMS Spam Collection)
├── serving/
│   ├── app.py # FastAPI app to serve the trained model
│   └── Dockerfile # Dockerfile for containerizing the serving API
├── requirements.txt # Required Python dependencies
├── Dockerfile # Dockerfile for training (optional)
└── README.md # You're here!
```

---

## 📊 Dataset

**Name:** SMS Spam Collection
**Format:** CSV
**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)

**Columns:**
- `v1`: Label (`ham` or `spam`)
- `v2`: The text message

We rename:
- `v1` → `label`
- `v2` → `message`

We also map labels:
- `ham` → `0`
- `spam` → `1`

---

## 🔧 Model Training Pipeline

The training is handled via `pipelines/main.py`.

### 🔍 Steps Performed:

1. **Load Dataset**:
    ```python
    df = pd.read_csv("training/spam.csv", encoding='latin-1')
    ```
    **Clean Columns**: Only select and rename relevant columns.

    **Encode Labels**: Convert `ham` and `spam` labels to binary (0, 1).

    **Train-Test Split**:
    ```python
    train_test_split(df["message"], df["label"], test_size=0.2)
    ```

    **Build ML Pipeline**:
    - `CountVectorizer`: Transforms text into token count vectors.
    - `MultinomialNB`: A Naive Bayes classifier suitable for text classification.

    **Train Model**: The pipeline is trained using `.fit()`.

    **Evaluate Accuracy**: Uses `accuracy_score` and `classification_report` to assess performance.

    **Save Model**: Saved using `joblib` to `/app/model/spam_classifier.pkl`.

    **Log Metrics**: Accuracy and detailed classification report are stored in `/app/model/metrics.txt`.

```yaml
🧠 Example Accuracy Log:
Accuracy: 0.9823
Classification Report:
              precision    recall  f1-score   support

           0       0.98      0.99      0.99       966
           1       0.97      0.93      0.95       149

    accuracy                           0.98      1115
   macro avg       0.97      0.96      0.97      1115
weighted avg       0.98      0.98      0.98      1115
```

---

## 🚀 Model Serving (API)

Once trained, the model can be served using FastAPI. The REST API is hosted using the `serving/app.py` script and containerized using Docker.

### 📦 `app.py` Overview
- Loads the trained pipeline using `joblib`.
- Exposes a `/predict` endpoint to receive messages and return predictions.

### 🧪 API Contract

**POST /predict**

**Request Body**:
```json
{
  "message": "You won a free ticket!"
}
```

**Response**:
```json
{
  "prediction": "spam"
}
```

### 🐳 Serving via Docker
**Dockerfile** (`serving/`):
```dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app.py /app/
COPY ./spam_classifier.pkl /app/

RUN pip install joblib scikit-learn pandas

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
```

### 🧪 Build & Run the Container
```bash
# Step 1: Build
docker build -t spam-detector-api -f serving/Dockerfile .

# Step 2: Run
docker run -p 8080:8080 spam-detector-api
```

---

## ✅ End-to-End Pipeline

| Step                | Tool Used               | Output                           |
|---------------------|-------------------------|----------------------------------|
| Data Ingestion      | pandas                  | Cleaned DataFrame                |
| Text Vectorization  | CountVectorizer         | Bag of Words Matrix              |
| Model Training      | MultinomialNB           | Trained classifier model         |
| Evaluation          | sklearn.metrics         | Accuracy & classification report |
| Persistence         | joblib                  | Saved .pkl model                 |
| Serving             | FastAPI, Docker         | REST API for predictions         |

---

## 🧪 Testing the API

You can use `curl`, Postman, or Python `requests`:
```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "Congratulations! You won a free iPhone!"}'
```

---

## 📌 Future Improvements
- Add support for more preprocessing (stopwords, stemming).
- Model versioning & model registry integration.
- CI/CD integration with GitHub Actions.
- Streamlit or UI5 front-end for predictions.
- OAuth authentication for secure API access.
- Deploy via SAP BTP or Azure App Services.

---
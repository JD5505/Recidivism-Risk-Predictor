# ⚖️ Recidivism Risk Predictor

A machine learning web application that predicts the likelihood of a defendant reoffending (recidivism), built with a **FastAPI** backend and a **Streamlit** frontend.

---

## 📌 Overview

This project uses the [COMPAS dataset](https://github.com/propublica/compas-analysis) to train a classification model that assesses recidivism risk based on defendant demographics and criminal history. The system mirrors the kind of risk-scoring used in the real criminal justice system — but with full transparency into the model and its inputs.

---

## 🗂️ Project Structure

```
Recidivism-Risk-Predictor/
├── backend/
│   ├── app.py                  # FastAPI application & prediction endpoint
│   ├── Model/
│   │   ├── model.pkl           # Trained ML model
│   │   ├── Model_Training.ipynb
│   │   └── cox-violent-parsed_filt.csv   # Training dataset
│   └── Schema/
│       └── user_input.py       # Pydantic input schema with computed fields
└── frontend/
    └── index.py                # Streamlit UI
```

---

## ⚙️ How It Works

1. The user enters defendant information in the **Streamlit** frontend.
2. The frontend sends a `POST` request to the **FastAPI** backend at `/predict`.
3. The backend validates the input via a **Pydantic schema**, computes derived features (`age_cat`, `c_charge_degree`), and passes them to the model.
4. The trained model returns a **probability of reoffending**. If ≥ 0.50, the prediction is flagged as high risk.

---

## 🧠 Input Features

| Feature | Description |
|---|---|
| `age` | Age of the defendant |
| `juv_fel_count` | Felonies committed as a juvenile |
| `juv_misd_count` | Misdemeanors committed as a juvenile |
| `juv_other_count` | Other juvenile offenses |
| `priors_count` | Total prior adult criminal charges |
| `charge_degree` | Severity of current charge (e.g. F1, M2, CT) |
| `c_days_from_compas` | Days between arrest and COMPAS screening |

### Computed Features (auto-derived in backend)

| Feature | Logic |
|---|---|
| `age_cat` | `Young` (< 25), `Adult` (25–45), `Senior` (> 45) |
| `c_charge_degree` | Ordinal encoding of charge severity (0–13) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/JD5505/Recidivism-Risk-Predictor.git
cd Recidivism-Risk-Predictor
pip install fastapi uvicorn streamlit requests pandas scikit-learn joblib pydantic
```

### Running the App

**1. Start the FastAPI backend** (from the `backend/` directory):
```bash
cd backend
uvicorn app:app --host 127.0.0.1 --port 8000
```

**2. Start the Streamlit frontend** (from the `frontend/` directory, in a new terminal):
```bash
cd frontend
streamlit run index.py
```

**3. Open your browser** at `http://localhost:8501`

---

## 🔌 API Reference

### `GET /`
Returns a welcome message.

### `POST /predict`
Accepts defendant data and returns a risk prediction.

**Request Body:**
```json
{
  "age": 28,
  "juv_fel_count": 0,
  "juv_misd_count": 1,
  "juv_other_count": 0,
  "priors_count": 3,
  "charge_degree": "F3",
  "c_days_from_compas": 5
}
```

**Response:**
```json
{
  "prediction": 1
}
```
`1` = High risk of reoffending | `0` = Low risk

---

## ⚠️ Ethical Disclaimer

This tool is built for **educational purposes only**. Automated recidivism scoring systems have well-documented biases and should never be used as the sole basis for real-world legal or judicial decisions. See ProPublica's [Machine Bias](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) investigation for important context on the COMPAS dataset.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **ML / Data:** scikit-learn, pandas, joblib
- **Validation:** Pydantic v2
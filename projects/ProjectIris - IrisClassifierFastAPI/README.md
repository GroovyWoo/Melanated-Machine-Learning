


# 🪴 Project Iris — Iris Classifier FastAPI

## 📌 Overview

This project is a Machine Learning web service that classifies iris flower species using the famous Iris dataset.
It trains a Random Forest model with scikit-learn, then serves predictions through a FastAPI app.


*The project demonstrates:* 

	•	Training and saving a machine learning model (joblib)
	•	Serving predictions via an API (FastAPI + Uvicorn)
	•	Testing the API locally with curl or other tools

---

## ⚙️ Tech Stack
	•	Python 3.13+
	•	scikit-learn (ML model)
	•	FastAPI (web framework)
	•	Uvicorn (ASGI server)
	•	Joblib (model serialization)

---

## 📂 Project Structure 
```bash
ProjectIrisFastAPI/
│── venv/                  # virtual environment (ignored in git)
│── app/
│   ├── main.py             # FastAPI app serving predictions
│── train_iris.py           # script to train and save the model
│── model.joblib            # saved model file (created after training)
│── requirements.txt        # dependencies
│── README.md               # project documentation

```

---

## 💻 How to Run Locally 

1.	Clone repo & navigate to project
```bash 
git clone <your-repo-link>
cd ProjectIrisFastAPI
```

2.	Create & activate virtual environment
```bash 
python3 -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows 
```

3.	Install dependencies
```bash 
pip install -r requirements.txt 
```

4.	Train the model (creates model.joblib)
```bash 
python train_iris.py
```

5.	Run FastAPI app
```bash 
uvicorn app.main:app --reload 
```

6.	Test the API (example with curl)
```bash 
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"features":[5.1, 3.5, 1.4, 0.2]}'
```

### ✅ Example Response:
```json
{"prediction": "setosa"}
```


## 🧑🏽‍💻 Example Prediction Inputs 

 •	[5.1, 3.5, 1.4, 0.2] → setosa ; 
 
 •	[6.7, 3.1, 4.7, 1.5] → versicolor ;
 
 •	[7.2, 3.0, 5.8, 1.6] → virginica ;

---

## 📊 Skills Learned
•	Setting up Python virtual environments 

•	Installing dependencies with requirements.txt 

•	Training and saving a model with scikit-learn 

•	Serving predictions with FastAPI and Uvicorn 

•	Testing APIs with curl 

•	Understanding project structure for ML + API integration 

---

## 📌 Project Status

## ✅ Completed (Local Demo Ready)
 🔜 Next Steps: 
 
 •	Add frontend (simple form or landing page) 
 
 •	Deploy to a cloud service (Heroku, Render, or OCI)

---

## 📜 License

MIT License ( https://choosealicense.com/licenses/mit/ ).

---

## 👤 Author

Created by Q/GroovyWoo (Melanated Machine Learning) 🧠⚙️




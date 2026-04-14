# 🏡 California Housing Price Prediction App

## 🚀 Overview

This project is an **end-to-end Machine Learning web application** that predicts housing prices in California based on various socio-economic and geographic features.

The model is deployed as a live web application where users can input housing parameters and receive real-time predictions.

---

## 🌐 Live Demo

👉 **Access the deployed app here:**
**https://california-house-pricing-vegb.onrender.com**

---

## 🧠 Problem Statement

Accurately predicting housing prices is essential for:

* Real estate investment decisions
* Market analysis
* Financial planning

This project aims to build a robust regression model that estimates housing prices based on district-level data.

---

## 📊 Dataset

The model is trained on the **California Housing Dataset**, which contains:

* **20,640 samples**
* **8 input features**

### 🔑 Features:

* `MedInc` – Median income
* `HouseAge` – Median house age
* `AveRooms` – Average rooms per household
* `AveBedrms` – Average bedrooms per household
* `Population` – Total population
* `AveOccup` – Average household occupancy
* `Latitude` – Geographic latitude
* `Longitude` – Geographic longitude

### 🎯 Target:

* `MedHouseVal` – Median house value

---

## ⚙️ Tech Stack

### 🧠 Machine Learning

* Scikit-learn
* NumPy
* Pandas

### 🌐 Backend

* Flask
* Gunicorn

### 🎨 Frontend

* HTML
* CSS
* JavaScript

### ☁️ Deployment

* Render

---

## 🔄 Project Workflow

1. Data preprocessing & cleaning
2. Feature scaling using StandardScaler
3. Model training (Regression model)
4. Model serialization using Pickle
5. Flask API development
6. Frontend integration
7. Deployment on Render

---

## 🧪 Model Performance

The model was evaluated using standard regression metrics such as:

* R² Score
* RMSE

---

## 📁 Project Structure

```
project/
│
├── app.py
├── regmodel.pkl
├── scaling.pkl
├── requirements.txt
├── Procfile
├── templates/
│   └── home.html
```

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/yourusername/yourrepo.git
```

2. Navigate into the folder:

```
cd yourrepo
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
python app.py
```

5. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🔥 Key Features

* Real-time prediction
* Interactive UI dashboard
* Scaled input preprocessing
* End-to-end ML pipeline
* Deployed and accessible online

---

## 🚀 Future Improvements

* Add ensemble models (Voting Regressor)
* Feature importance visualization
* User authentication system
* Prediction history storage
* Advanced UI/UX improvements

---

## 👤 Author

**Gideon Oyegbami**

---

## ⭐ Acknowledgements

* Scikit-learn for dataset and ML tools
* Open-source community

---

## 📌 Final Note

This project demonstrates the full lifecycle of a Machine Learning system — from data preprocessing to deployment 

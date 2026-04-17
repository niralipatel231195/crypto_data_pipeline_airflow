# 🚀 Crypto Data Pipeline using Apache Airflow

## 📌 Project Overview
This project implements an end-to-end ETL pipeline that extracts cryptocurrency data from an API, transforms it using Python, and loads it into a PostgreSQL database. The workflow is orchestrated using Apache Airflow.

---

## 🧠 Architecture

API → Extract → Transform → Load → PostgreSQL  
                ↑  
           Airflow DAG  

---

## 🛠️ Tech Stack

- Python  
- Apache Airflow  
- Pandas  
- PostgreSQL  
- WSL (Linux)

---

## ⚙️ Workflow

### 🔹 Extract
- Fetch cryptocurrency data from API
- Store data using Airflow XCom

### 🔹 Transform
- Convert JSON to Pandas DataFrame
- Select and rename required columns

### 🔹 Load
- Insert data into PostgreSQL
- Handle duplicates using:
```sql
ON CONFLICT (id) DO NOTHING

## Install Dependencies

pip install -r requirements.txt \
  --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-3.12.txt
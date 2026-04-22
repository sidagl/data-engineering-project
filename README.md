# 📊 Data Engineering Pipeline — Product Insights API

## 🚀 Overview
This project demonstrates an end-to-end data engineering pipeline that collects, processes, and serves structured data for business use.

The system simulates a real-world B2B use case where organizations need structured insights from publicly available data.

---

## 🎯 Problem Statement
Businesses often lack structured, up-to-date data for decision-making (pricing trends, product insights, etc.).

This project solves that by:
- Collecting raw data from a public source
- Cleaning and standardizing it
- Storing it in a queryable database
- Exposing it via API endpoints and a lightweight dashboard

---

## 🧱 Architecture
Scraper → Raw Data → Cleaning → Database → API → Dashboard → User

---

## ⚙️ Tech Stack
- Python  
- BeautifulSoup (Web Scraping)  
- Pandas (Data Cleaning)  
- SQLite (Database)  
- Flask (API & Dashboard)  
- Render (Deployment)  

---

## 🔄 Pipeline Workflow

1. **Scraping**
   - Extracts product data (name, price, rating)
   - Handles pagination and missing values

2. **Data Cleaning**
   - Removes encoding issues and symbols
   - Converts data types (price → float, rating → numeric)
   - Handles missing values
   - Adds timestamp

3. **Storage**
   - Stores cleaned data in SQLite database

4. **API Layer**
   - Exposes endpoints for querying data

5. **Dashboard**
   - Displays product data in a simple UI
   - Fetches data dynamically from API

---

## 🌐 Live Demo

### 🔗 API Base URL:
https://data-engineering-project-qjlv.onrender.com/

### 📊 Dashboard (Recommended View):
https://data-engineering-project-qjlv.onrender.com/dashboard

---

## 📡 API Endpoints

- `/products` → Get all products  
- `/avg-price` → Get average price  
- `/top-rated` → Top-rated products  
- `/products/rating/<rating>` → Filter by rating  
- `/search?q=keyword` → Search products  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python run_pipeline.py
python api/app.py
```

## 🔁 Automation

Pipeline can be executed via:

```bash
python run_pipeline.py
```

Designed to support scheduling (cron / task scheduler).

## 📌 Key Highlights

- End-to-end ETL pipeline
- Automated workflow
- REST API for data access
- Lightweight dashboard for visualization
- Deployed and publicly accessible
- Handles real-world data issues
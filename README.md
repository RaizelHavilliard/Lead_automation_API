## Lead Processing Automation API

A lightweight FastAPI-based backend system that automates lead file cleaning and processing for small agencies and marketing teams.

### 🚀 What It Does

* Accepts CSV lead files
* Validates email addresses (RFC compliant)
* Removes duplicate emails
* Cleans and normalizes data
* Generates summary statistics
* Provides downloadable cleaned CSV

---

### 📊 Example Use Case

Marketing agencies often manually clean lead lists before reporting.

This API automates:

* Removing invalid emails
* Eliminating duplicates
* Structuring lead data
* Exporting clean lead files

---

### 🛠 Tech Stack

* FastAPI
* Pandas
* Email-validator
* Uvicorn

---

### 📂 CSV Format

```
name,email,company
```

---

### 🔌 Endpoints

**POST /upload**

Upload CSV file and receive processing statistics.

Response:

```json
{
  "total_leads": 10,
  "duplicates_removed": 2,
  "invalid_emails": 3,
  "clean_leads": 5
}
```

**GET /download**

Download cleaned CSV file.

---

### ▶ Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then visit:

```
http://127.0.0.1:8000/docs
```

---

### 🎯 Target Users

* Lead generation agencies
* Real estate teams
* B2B sales teams
* Consultants managing inbound leads


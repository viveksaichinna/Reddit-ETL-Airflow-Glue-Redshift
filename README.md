# Reddit ETL Pipeline with Airflow, AWS Glue, Athena, and Redshift

This project demonstrates a modular ETL workflow where Reddit data is extracted using Python and orchestrated via Apache Airflow until it's loaded into Amazon S3. Subsequent transformation and analytics steps are carried out using AWS Glue, Athena, and Redshift.

---

## 🚀 Project Overview

### 🔹 Steps Involved & Architecture:
![Reddit ETL Architecture](ETL_Arch_img.png)

1. **Data Extraction & Load to S3 (Orchestrated by Airflow)**

   * Extracts Reddit posts using Reddit API (via PRAW).
   * Uploads raw data to Amazon S3 in `.csv` format.
   * Orchestrated using Apache Airflow.

2. **Data Transformation (Manual Trigger or Scheduled via AWS Console)**

   * AWS Glue cleans and normalizes raw Reddit data.
   * Transformed dataset is stored back into S3.

3. **Schema Cataloging & Querying**

   * AWS Glue Crawler catalogs the transformed dataset.
   * Amazon Athena used for ad-hoc queries on curated data.

4. **Loading to Redshift**

   * Final, curated dataset is loaded into Amazon Redshift for analytics.

---

## 🛠️ Tech Stack

* **Python** (with `praw` for Reddit API)
* **Apache Airflow** – Orchestrates extraction and S3 upload
* **Amazon S3** – Data lake (raw & transformed zones)
* **AWS Glue** – Serverless ETL job for transformation
* **Glue Crawler** – For schema discovery
* **Amazon Athena** – SQL-like queries over S3
* **Amazon Redshift** – Analytics and BI-ready storage
* **IAM** – Secure, role-based access between services


## ✅ Prerequisites

* AWS account with:

  * S3 bucket (raw and curated zones)
  * IAM roles for S3, Glue, Athena, Redshift
  * Redshift cluster + table
* Reddit API credentials from [Reddit Developer Console](https://www.reddit.com/prefs/apps)
* Airflow installed and running locally or in the cloud

---

## 🔧 Setup Instructions

1. **Clone the repo:**

   ```bash
   git clone https://github.com/yourusername/Reddit-ETL-Airflow-Glue-Redshift.git
   cd Reddit-ETL-Airflow-Glue-Redshift
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Reddit API keys and AWS credentials**

4. **Start Airflow and trigger the DAG:**

   * Extracts Reddit data and uploads it to S3.

5. **Run AWS Glue job** via the console to transform the raw data.

6. **Run Glue Crawler** to catalog the transformed data.

7. **Query the data via Athena or load into Redshift** for downstream analytics.

---

## 📊 Example Use Cases

* Text mining and topic modeling on Reddit posts
* Detecting trending topics across subreddits
* Pushing Reddit data into BI dashboards via Redshift

---

## 👤 Author

**Vivek Sai Chinna Burada**
Data Engineer | AWS | ETL | Analytics | GenAI
[LinkedIn](https://www.linkedin.com/in/viveksaichinna) • [GitHub](https://github.com/viveksaichinna)

---

## 📋 License

This project is licensed under the MIT License.

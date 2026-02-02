# Homework 02 – Workflow Orchestration

## Project Overview
This repository contains my solutions for the Data Engineering Zoomcamp 2026 Module 2 homework. The assignment involves analyzing NYC Yellow and Green Taxi data for 2020-2021 and extending existing Kestra flows to include 2021 data.

## Project Structure
```
Homework/
├── Data/                              # Data files (if any)
├── docker-compose.yml                 # Docker setup for PostgreSQL + pgAdmin
├── flows/                             # Kestra workflow definitions
│   └── question1.yaml                 # Kestra flow for data ingestion
├── nyc-taxi/                          # Python analysis scripts
│   ├── Green_Taxi_2020.ipynb          # Green Taxi 2020 analysis
│   ├── main.py                        # Main data ingestion script
│   ├── pyproject.toml                 # Python dependencies (UV)
│   ├── README.md                      # Local README
│   ├── uv.lock                        # UV lock file
│   ├── Yellow_Taxi_2020.ipynb         # Yellow Taxi 2020 analysis
│   └── Yellow_Taxi_2021_03.ipynb      # Yellow Taxi March 2021 analysis
├── README.md                          # This file
├── screenshots/                       # Screenshots of results
│   ├── Question1.png                  # Question 1 screenshot
│   ├── Question2.png                  # Question 2 screenshot
│   ├── Question3.png                  # Question 3 screenshot
│   ├── Question4.png                  # Question 4 screenshot
│   └── Question5.png                  # Question 5 screenshot
└── sql/                               # SQL queries
    └── queries.sql                    # SQL queries used for analysis
```

## Setup Instructions

### 1. Start Docker Services
```bash
docker-compose up -d
```
**Services started:**
- **PostgreSQL:** localhost:5432 (user: root, password: root, database: ny_taxi)
- **pgAdmin:** http://localhost:8085 (admin@admin.com / root)

### 2. Install Python Dependencies
```bash
cd nyc-taxi
uv sync  # Installs pandas, sqlalchemy, psycopg2, etc.
```

### 3. Run Analysis
Open the Jupyter notebooks in the `nyc-taxi/` directory to see the complete analysis.

## Question 1: File Size for December 2020 Yellow Taxi Data
**Method:** Used Kestra flow (`flows/question1.yaml`) to download and extract the file. The Kestra execution output shows the uncompressed file size.

**Result:** File size matches one of the provided options. See screenshot in `screenshots/Question1.png`.

## Question 2: Variable Rendering in Kestra
**Method:** Created a Kestra flow with template variables.

**Kestra Flow (`flows/question1.yaml`):**
```yaml
inputs:
  - name: taxi
    type: STRING
  - name: year  
    type: STRING
  - name: month
    type: STRING

tasks:
  - id: render
    type: io.kestra.core.tasks.log.Log
    message: "{{ inputs.taxi }}_tripdata_{{ inputs.year }}-{{ inputs.month }}.csv"
```

**Test Configuration:**
- **Inputs:** `taxi: green`, `year: 2020`, `month: 04`
- **Output:** `green_tripdata_2020-04.csv`

**Verification:** See screenshot in `screenshots/Question2.png`.

## Question 3: Total Rows for Yellow Taxi 2020
**Method:** Loaded all 12 months of 2020 Yellow Taxi data into PostgreSQL.

**Code (`nyc-taxi/Yellow_Taxi_2020.ipynb`):** Python script using pandas to load data in chunks.

**SQL Verification:**
```sql
SELECT COUNT(*) FROM yellow_taxi;
```

**Result:** See screenshot in `screenshots/Question3.png`.

## Question 4: Total Rows for Green Taxi 2020
**Method:** Loaded all 12 months of 2020 Green Taxi data.

**Note:** Green Taxi has different column names (`lpep_*` instead of `tpep_*`).

**Code (`nyc-taxi/Green_Taxi_2020.ipynb`):** Adjusted for Green Taxi column structure.

**SQL Verification:**
```sql
SELECT COUNT(*) FROM green_taxi;
```

**Result:** See screenshot in `screenshots/Question4.png`.

## Question 5: Rows for Yellow Taxi March 2021
**Method:** Loaded only March 2021 Yellow Taxi data.

**Code (`nyc-taxi/Yellow_Taxi_2021_03.ipynb`):** Single month data loading script.

**SQL Verification:**
```sql
SELECT COUNT(*) FROM yellow_taxi_march_2021;
```

**Result:** See screenshot in `screenshots/Question5.png`.

## Question 6: Kestra Timezone Configuration
**Correct Configuration:**
```yaml
triggers:
  - id: schedule
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "@daily"
    timezone: "America/New_York"
```

**Reason:** According to Kestra documentation, the `timezone` property accepts IANA timezone identifiers. Using `America/New_York` properly handles both Eastern Standard Time (EST) and Eastern Daylight Time (EDT) with automatic Daylight Saving Time adjustments.

**Documentation Reference:** Kestra documentation specifies using IANA timezone format for the `timezone` property in Schedule triggers.
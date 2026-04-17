# ⚡ India Electricity Consumption Analysis (2019-2020)

![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5/CSS3](https://img.shields.io/badge/UI%2FUX-Modern_Dark_Theme-blueviolet?style=for-the-badge)

## 📌 Project Overview & Problem Statement
The goal of this project is to analyze the electricity consumption patterns across various states and regions in India for the years 2019 and 2020. 

The year 2020 saw unprecedented changes due to the COVID-19 pandemic and the subsequent nationwide lockdowns. This project aims to visually answer critical questions:
* How did the lockdown impact overall power consumption?
* Which states and regions are the highest consumers of electricity?
* What does the month-by-month consumption trend look like before, during, and after the lockdown?

To solve this, I built an end-to-end data pipeline: utilizing **Python** for data preprocessing (bypassing traditional database overhead for speed and efficiency), **Tableau** for building an interactive visualization dashboard, and **Flask** to serve the final product on a custom, modern web interface.

---

## 🏗️ Architecture & Data Flow

```mermaid
graph TD
    A[Raw Data CSV] -->|Data Cleaning & Feature Engineering| B(Python / Pandas)
    B -->|Export| C[Cleaned Tableau-Ready CSV]
    C -->|Import & Visualize| D{Tableau Public}
    D -->|Generate Embed URL| E[Flask Web App backend]
    E -->|Render Modern UI| F((End User Dashboard))
    
    style B fill:#306998,stroke:#FFD43B,stroke-width:2px,color:#fff
    style D fill:#E97627,stroke:#fff,stroke-width:2px,color:#fff
    style E fill:#000000,stroke:#fff,stroke-width:2px,color:#fff

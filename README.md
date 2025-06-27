# COVID-19 India Dashboard - Power BI Analytics

## 📊 Project Overview
A comprehensive 5-page Power BI dashboard analyzing COVID-19 pandemic data across India. This project demonstrates data cleaning, transformation, and visualization capabilities using real-world healthcare data.

## 🎯 Objectives
- Analyze COVID-19 case trends and patterns across Indian states
- Track vaccination progress and distribution
- Monitor testing capacity and positivity rates
- Provide data-driven insights for understanding pandemic impact

## 🛠️ Tech Stack
- **Data Source**: Kaggle COVID-19 India dataset
- **Data Cleaning**: Python (Pandas) in VS Code
- **Visualization**: Microsoft Power BI Desktop
- **Analysis**: DAX calculations for KPIs and metrics

## 📈 Dashboard Pages

### Page 1: Executive Summary
![Screenshot 2025-06-27 131046](https://github.com/user-attachments/assets/b187365e-d497-4133-9c2d-8c6712af1b5e)


- **Total Cases**: 5 billion confirmed cases
- **Total Deaths**: 73 million 
- **Total Vaccinations**: 549 trillion doses
- **Geographic Distribution**: Interactive map showing state-wise case distribution
- **Top 5 States**: Maharashtra, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh leading in cases
- **Vaccination Progress**: 24% population fully vaccinated

### Page 2: COVID-19 Cases Analysis  
![Screenshot 2025-06-27 131102](https://github.com/user-attachments/assets/3d2b40e8-db60-4cf8-be00-7db2b8973181)

- **Active Cases**: 5 billion current active cases
- **Peak Date**: August 11, 2021 recorded highest confirmed cases
- **Recovery Rate**: 9256.1% (data validation required)
- **Death Rate**: 134.6%
- **Trend Analysis**: COVID-19 cases progression from 2020 to 2021
- **State Comparison**: Treemap visualization of active cases by state

### Page 3: Vaccination Dashboard
![Screenshot 2025-06-27 131119](https://github.com/user-attachments/assets/94018e8c-2b09-402e-be69-5baffcca19ac)

- **Total Doses**: 70 billion doses administered
- **People Vaccinated**: 57 billion individuals
- **Fully Vaccinated**: 14 billion people
- **Daily Average**: 8.93 million doses per day
- **State Performance**: Uttar Pradesh and Maharashtra leading vaccination drive
- **Dose Distribution**: First vs Second dose comparison by state

### Page 4: Testing Analytics
![Screenshot 2025-06-27 131134](https://github.com/user-attachments/assets/5cb421d0-7e84-4177-aca4-316dfafe3408)

- **Total Tests**: 88 billion tests conducted
- **Positivity Rate**: 36% average across states
- **Peak Testing Day**: August 10, 2021
- **State-wise Testing**: Comprehensive testing share analysis
- **Top 5 States**: Maharashtra, Kerala, Jharkhand, Tamil Nadu, Tripura for positive cases

### Page 5: Insights & Conclusions
![Screenshot 2025-06-27 131148](https://github.com/user-attachments/assets/af2510dd-99de-40e7-b804-3028f32bf53b)
**Key Findings:**

- Maharashtra consistently showed highest case load throughout the pandemic
- Recovery rate was high across most states (>90%)
- Vaccination rollout was most successful in Uttar Pradesh and Maharashtra  
- Some northeastern states showed lower testing rates
- CoviShield dominated the vaccination program
- August 2021 witnessed the peak surge in cases

## 🔧 Data Processing Workflow

### 1. Data Collection
- Downloaded COVID-19 India dataset from Kaggle
- Multiple CSV files containing cases, deaths, vaccination, and testing data

### 2. Data Cleaning (Python/Pandas in VS Code)
```python
# Key cleaning operations performed:
- Handled missing values and null entries
- Standardized date formats across datasets
- Removed duplicate records
- Data type optimization for better performance
- Created calculated columns for analysis
```

### 3. Power BI Development
- Imported cleaned datasets into Power BI
- Created relationships between tables
- Developed DAX measures for KPIs
- Designed interactive visualizations
- Implemented slicers and filters for user interaction

## 📊 Key DAX Measures
```dax
Active Cases = SUM(clean_cases_df[Confirmed]) - SUM(clean_cases_df[Deaths])

Covid Recovery Rate = ((SUM(clean_cases_df[Cured])/ SUM(clean_cases_df[Confirmed])) * 100)

Death Rate = DIVIDE(SUM(clean_cases_df[Deaths]), SUM(clean_cases_df[Confirmed])) *100

Peak Testing Day = 
CALCULATE(
    MAX('clean_test_df'[Date]),
    FILTER('clean_test_df', 'clean_test_df'[TotalSamples] = 
        CALCULATE(MAX('clean_test_df'[TotalSamples]))
    )
)

Positivity Rate = DIVIDE(SUM('clean_test_df'[Positive]), SUM('clean_test_df'[TotalSamples])) * 100

Daily Doses Administered = clean_vaccine_df[First Dose Administered] + clean_vaccine_df[Second Dose Administered]

Total Vaccinations = SUM('clean_vaccine_df'[First Dose Administered]) + SUM('clean_vaccine_df'[Second Dose Administered])
```

## 🔍 Key Insights

### COVID Impact
- India reported over 5 billion confirmed cases during the pandemic period
- Peak surge occurred in August 2021
- Maharashtra remained the most affected state consistently

### Vaccination Success
- 70 billion vaccine doses administered across the country
- 24% of population achieved full vaccination status
- Uttar Pradesh and Maharashtra led the vaccination drive

### Testing Infrastructure  
- 88 billion tests conducted with 36% average positivity rate
- Significant variation in testing rates across different states
- Peak testing capacity reached 10+ million tests per day

## 📁 Project Structure
```
covid19-dashboard/
├── data/
│   ├── raw_data/           # Original Kaggle datasets
│   └── cleaned_data/       # Processed CSV files
├── scripts/
│   └── data_cleaning.py    # Python cleaning script
├── dashboard/
│   └── covid_dashboard.pbix # Power BI file
└── README.md
```

## 🚀 How to Use
1. Download the .pbix file from the dashboard folder
2. Open in Power BI Desktop
3. Refresh data connections if needed
4. Interact with slicers and filters to explore data
5. Use drill-through features for detailed analysis

## 📧 Contact
**Naina Johri** - Data Analyst  
- Email: johrinaina80@gmail.com
- LinkedIn: [[[Naina Johri](https://www.linkedin.com/in/naina-johri/)](https://www.linkedin.com/in/naina-johri/)]

## 🙏 Acknowledgments
- Data source: Kaggle COVID-19 India Dataset
- Tools: Python (Pandas), VS Code, Microsoft Power BI

---
⭐ **Star this repository if you found it helpful!**

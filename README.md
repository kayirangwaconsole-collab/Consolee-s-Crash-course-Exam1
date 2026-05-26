# Emerging Education Access Risk Corridors in DRC

An interactive dashboard mapping education access challenges in the Democratic Republic of Congo (DRC).

## 📊 Dashboard Features

- **Interactive Leaflet Map**: Visualize education access across DRC regions
- **Risk Level Indicators**: Color-coded by risk (Very High, High, Medium, Low)
- **Data Table**: Quick reference statistics
- **Statistics Panel**: Overall summary metrics

## 📍 View the Dashboard

**Live Link:** https://kayirangwaconsole-collab.github.io/Consolee-s-Crash-course-Exam1/

## 📚 Data Sources

### Primary Data Sources:
1. **UNESCO Institute for Statistics (UIS)**
   - URL: http://data.uis.unesco.org/
   - Coverage: Education statistics for DRC and African regions
   - Topics: Education access, enrollment rates, infrastructure

2. **World Bank Education Data**
   - URL: https://data.worldbank.org/topic/education
   - Coverage: DRC education indicators, access barriers
   - Topics: Education access, gender parity, school attendance

3. **UNHCR - Refugee Data Finder**
   - URL: https://data.unhcr.org/
   - Coverage: Impact on education in conflict-affected regions
   - Topics: Displacement, education disruption in DRC

4. **United Nations Development Programme (UNDP) - HDR**
   - URL: http://hdr.undp.org/
   - Coverage: Human development in DRC
   - Topics: Education quality, access inequality

5. **DRC Ministry of Education**
   - Coverage: National education statistics
   - Topics: School distribution, access corridors, regional data

6. **ReliefWeb - Situation Reports**
   - URL: https://reliefweb.int/
   - Coverage: DRC education crisis reports
   - Topics: Education disruption in conflict zones

7. **ACLED - Armed Conflict Location Data**
   - URL: https://acleddata.com/
   - Coverage: Conflict-affected regions in DRC
   - Topics: Areas with access barriers

## 🛠️ How to Use the Data

1. Open `sample_education_data.csv` to see the data structure
2. Use `filter_drc_data.py` to filter data for DRC
3. View the interactive dashboard at the link above

## 📁 Files in This Repository

- `index.html` - Interactive dashboard (main file)
- `filter_drc_data.py` - Python script to filter DRC data
- `sample_education_data.csv` - Sample education data
- `DRC_education_corridors.csv` - Filtered DRC data

## 🚀 Getting Started

### View Online (Easiest)
Just visit: https://kayirangwaconsole-collab.github.io/Consolee-s-Crash-course-Exam1/

### Run Locally
1. Clone the repository
2. Open `index.html` in your browser
3. No installation needed!

### Use the Python Script
```bash
python filter_drc_data.py
```
This creates `DRC_education_corridors.csv` with filtered data.

## 📖 Understanding the Data

**Columns:**
- **Country**: Nation (DRC in this case)
- **Region**: Geographic area within DRC
- **Risk_Level**: Education access difficulty (Very High, High, Medium, Low)
- **Education_Access**: Percentage of population with access (%)
- **Year**: Year of data collection

**Risk Levels Explained:**
- 🔴 **Very High**: Severe barriers to education access
- 🟠 **High**: Significant access challenges
- 🟡 **Medium**: Moderate access issues
- 🟢 **Low**: Minimal access barriers

## 📝 License

This project is for educational purposes.

## 👤 Author

Created as part of a beginner programming course.

Building an Adaptive Education Intelligence System for Conflict-Affected Regions

# 🏦 Financial Performance Dashboard — Apex Bank

![Dashboard Preview](![Uploading Screenshot 2026-04-16 105948.png…])

> A complete, end-to-end Financial Performance Dashboard project demonstrating KPI tracking, data visualization, and financial analysis for a banking institution. Built with **Python**, **Excel (openpyxl)**, and an interactive **HTML/Chart.js dashboard** — suitable for showcasing Data Analytics, Business Intelligence, and Banking domain skills on GitHub.

---

## 📌 Project Overview

This project simulates a real-world Financial Performance Dashboard for **Apex Bank**, a hypothetical commercial bank. It covers:

- **Revenue, Expenses, and Net Income** tracking across 5 years (2020–2024)
- **Key profitability KPIs**: Net Profit Margin, ROE, ROA, EPS, Cost-to-Income Ratio
- **Asset Quality Metrics**: Total Assets, Loans, Deposits, NPL Ratio, Capital Adequacy, Liquidity
- **Business Segment Revenue** across 5 divisions: Retail Banking, Corporate Banking, Wealth Management, Investment Banking, and Treasury
- **Monthly and Quarterly breakdowns** for granular trend analysis

---

## 🗂️ Project Structure

```
financial-dashboard/
│
├── 📁 data/                        # Generated CSV and JSON datasets
│   ├── annual_pnl.csv              # Annual P&L: 2020–2024
│   ├── monthly_revenue.csv         # Month-by-month FY2024 revenue
│   ├── asset_quality.csv           # Balance sheet & asset quality KPIs
│   ├── segment_revenue.csv         # Revenue by business segment per year
│   ├── quarterly_kpis.csv          # Quarterly KPI scorecard FY2024
│   └── dashboard_data.json         # Consolidated JSON (used by HTML dashboard)
│
├── 📁 scripts/                     # Python scripts
│   ├── generate_data.py            # Generates all synthetic financial data
│   ├── build_excel.py              # Builds the multi-sheet Excel workbook
│   └── kpi_analysis.py             # Text-based KPI analysis & insights report
│
├── 📁 dashboard/                   # Interactive web dashboard
│   └── index.html                  # Standalone HTML dashboard (Chart.js)
│
├── Financial_Dashboard.xlsx        # ⭐ Excel workbook with charts & formulas
└── README.md                       # This file
```

---

## 🚀 Quick Start

### Prerequisites

```bash
pip install pandas numpy openpyxl
```

### Step 1 — Generate Data

```bash
python scripts/generate_data.py
```

Produces all CSV files and the `dashboard_data.json` in the `/data` folder.

### Step 2 — Build the Excel Workbook

```bash
python scripts/build_excel.py
```

Creates `Financial_Dashboard.xlsx` with **6 formatted sheets**, color-coded cells, Excel formulas, and embedded charts.

### Step 3 — Run the KPI Analysis Report

```bash
python scripts/kpi_analysis.py
```

Prints a full text-based executive KPI analysis with insights, benchmarks, and management commentary.

### Step 4 — Open the Interactive Dashboard

Simply open `dashboard/index.html` in any modern browser:

```bash
open dashboard/index.html        # macOS
start dashboard/index.html       # Windows
xdg-open dashboard/index.html    # Linux
```

No server required — it's fully self-contained.

---

## 📊 Excel Workbook — Sheet Summary

| Sheet | Contents |
|-------|----------|
| **Executive Summary** | Full 5-year P&L table + Revenue bar chart + Margin line chart |
| **Monthly Revenue 2024** | Month-by-month breakdown with MoM % changes + charts |
| **Asset Quality** | Balance sheet KPIs with NPL/Capital Adequacy benchmarks + trend chart |
| **Business Segments** | Pivot table of 5 segments × 5 years + 2024 pie chart |
| **Quarterly KPIs** | Q1–Q4 2024 scorecard with EPS, ROE, expense ratio + bar chart |
| **Assumptions & Notes** | Color coding legend, model assumptions, data sources |

### Color Coding (Industry Standard)

| Color | Meaning |
|-------|---------|
| 🔵 Blue text | Hardcoded input assumptions |
| ⚫ Black text | Excel formulas & calculated values |
| 🟢 Green text | Links from other worksheets |
| 🔴 Red text | External file links |
| 🟡 Yellow background | Key cells requiring attention |

---

## 🌐 Interactive HTML Dashboard — Features

The `dashboard/index.html` is a **single-file interactive dashboard** with:

- **5 tabs**: Overview · Monthly P&L · Asset Quality · Business Segments · Quarterly KPIs
- **KPI Cards** with YoY delta indicators (▲/▼)
- **12 Chart.js charts**: Bar, Line, Doughnut, and Stacked Bar charts
- **Sortable data tables** with conditional color formatting (green/amber/red)
- **Traffic-light badges** for NPL Ratio and risk indicators
- Fully **responsive** for mobile and desktop
- Zero dependencies — runs offline in any browser

---

## 📈 Key KPIs Tracked

### Profitability
| KPI | FY2024 | FY2023 | Trend |
|-----|--------|--------|-------|
| Total Revenue | $6,678M | $6,770M | ▼ 1.4% |
| Net Income | $1,790M | $1,848M | ▼ 3.1% |
| Net Profit Margin | 26.8% | 27.3% | ▼ |
| Cost-to-Income Ratio | 58.9% | 57.1% | ▼ |
| ROE | 10.6% | 10.3% | ▲ |
| ROA | 1.55% | 1.49% | ▲ |
| EPS | $4.34 | $3.64 | ▲ |

### Asset Quality
| KPI | FY2024 | Benchmark | Status |
|-----|--------|-----------|--------|
| NPL Ratio | 2.37% | < 2.5% | ✅ OK |
| Capital Adequacy | 16.7% | > 10.5% (Basel III) | ✅ Compliant |
| Liquidity Ratio | 126.2% | > 100% | ✅ Healthy |

---

## 🛠️ Skills Demonstrated

| Skill | Tool / Method |
|-------|---------------|
| Data Generation & Simulation | Python (NumPy, Pandas) |
| KPI Analysis & Reporting | Python tabular reports |
| Excel Dashboard Creation | openpyxl (charts, formulas, formatting) |
| Interactive Data Visualization | Chart.js (8 chart types) |
| Financial Modeling | Industry-standard color coding, CAGR, ratios |
| Dashboard Design (IBM Cognos-style) | HTML/CSS, KPI cards, tab navigation |
| Banking Domain Knowledge | NPL, Capital Adequacy, C/I Ratio, ROE, ROA |

---

## 📌 IBM Cognos / Power BI Equivalent

This dashboard replicates the kind of reporting typically done in **IBM Cognos Analytics** or **Microsoft Power BI**:

- **KPI scorecards** with traffic light indicators
- **Drill-down** from annual → quarterly → monthly
- **Business segment** breakdowns
- **Balance sheet** health monitoring
- **Time-series trend analysis**

The HTML dashboard can be imported as a custom visual or the CSVs can be loaded directly into Power BI / IBM Cognos / Tableau for production deployment.

---

## 📁 Data Dictionary

### `annual_pnl.csv`
| Column | Description |
|--------|-------------|
| Year | Fiscal year |
| Total_Revenue_M | Total revenue in USD millions |
| Interest_Income_M | Revenue from interest |
| Fee_Income_M | Fee-based revenue |
| Operating_Expenses_M | Total operating costs |
| Provision_Losses_M | Loan loss provisions |
| EBIT_M | Earnings before interest & tax |
| Net_Income_M | Bottom-line profit |
| Net_Profit_Margin_Pct | Net income / Revenue × 100 |
| Cost_Income_Ratio_Pct | OpEx / Revenue × 100 |
| ROE_Pct | Return on Equity |
| ROA_Pct | Return on Assets |
| EPS | Earnings per share |

---

## 🤝 Contributing

Pull requests welcome! To add a new KPI or visualization:

1. Add the metric to `generate_data.py`
2. Re-run `python scripts/generate_data.py`
3. Update `build_excel.py` for the Excel sheet
4. Update `dashboard/index.html` for the web dashboard

---

## 📄 License

MIT License — free for personal, educational, and portfolio use.

---

## 👤 Author

Built as a portfolio project demonstrating **Financial Analytics**, **Data Visualization**, and **Banking KPI Dashboard** skills.

> 💡 *All financial data is synthetic and generated for demonstration purposes only. It does not represent any real institution.*


## 📸 Dashboard Preview




### Overview
![Overview 1](screenshots/Screenshot%202026-04-15%20023103.png)
![Overview 2](screenshots/Screenshot%202026-04-15%20023327.png)

### Monthly P&L
![Monthly P&L 1](screenshots/Screenshot%202026-04-15%20023400.png)
![Monthly P&L 2](screenshots/Screenshot%202026-04-15%20023424.png)
![Monthly P&L 3](screenshots/Screenshot%202026-04-15%20023430.png)
![Monthly P&L 4](screenshots/Screenshot%202026-04-15%20023445.png)
![Monthly P&L 5](screenshots/Screenshot%202026-04-15%20023504.png)

### Asset Quality
![Asset Quality 1](screenshots/Screenshot%202026-04-15%20023522.png)
![Asset Quality 2](screenshots/Screenshot%202026-04-15%20023542.png)

### Business Segments
![Business Segment 1](screenshots/Screenshot%202026-04-15%20023557.png)
![Business Segment 2](screenshots/Screenshot%202026-04-15%20023613.png)
![Business Segment 3](screenshots/Screenshot%202026-04-15%20023628.png)



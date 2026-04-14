"""
Financial Performance Dashboard - Data Generator
Generates realistic synthetic bank/business financial KPI data
"""

import pandas as pd
import numpy as np
import json
import os

np.random.seed(42)

YEARS = [2020, 2021, 2022, 2023, 2024]
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
QUARTERS = ["Q1","Q2","Q3","Q4"]

# ── Annual P&L ────────────────────────────────────────────────────────────────
base_revenue = 5200  # $M
annual_rows = []
for i, yr in enumerate(YEARS):
    growth = np.random.uniform(0.06, 0.13)
    revenue = base_revenue * ((1 + growth) ** i)
    interest_income   = revenue * np.random.uniform(0.52, 0.58)
    fee_income        = revenue * np.random.uniform(0.18, 0.22)
    other_income      = revenue - interest_income - fee_income
    operating_exp     = revenue * np.random.uniform(0.54, 0.60)
    provision_losses  = revenue * np.random.uniform(0.06, 0.10)
    ebit              = revenue - operating_exp - provision_losses
    tax               = ebit * 0.21
    net_income        = ebit - tax
    annual_rows.append({
        "Year": yr,
        "Total_Revenue_M":    round(revenue, 2),
        "Interest_Income_M":  round(interest_income, 2),
        "Fee_Income_M":       round(fee_income, 2),
        "Other_Income_M":     round(other_income, 2),
        "Operating_Expenses_M": round(operating_exp, 2),
        "Provision_Losses_M": round(provision_losses, 2),
        "EBIT_M":             round(ebit, 2),
        "Net_Income_M":       round(net_income, 2),
        "Tax_M":              round(tax, 2),
        "Net_Profit_Margin_Pct": round((net_income / revenue) * 100, 2),
        "Cost_Income_Ratio_Pct": round((operating_exp / revenue) * 100, 2),
        "ROE_Pct":            round(np.random.uniform(10, 16), 2),
        "ROA_Pct":            round(np.random.uniform(1.0, 1.8), 2),
        "EPS":                round(np.random.uniform(3.2, 5.8), 2),
    })
df_annual = pd.DataFrame(annual_rows)

# ── Monthly Revenue 2024 ──────────────────────────────────────────────────────
base_monthly = df_annual.loc[df_annual.Year==2024, "Total_Revenue_M"].values[0] / 12
monthly_rows = []
for m in MONTHS:
    seasonal = 1 + np.random.uniform(-0.06, 0.10)
    rev = base_monthly * seasonal
    exp = rev * np.random.uniform(0.54, 0.60)
    prov = rev * np.random.uniform(0.06, 0.09)
    ni = (rev - exp - prov) * 0.79
    monthly_rows.append({
        "Month": m, "Year": 2024,
        "Revenue_M":      round(rev, 2),
        "Expenses_M":     round(exp, 2),
        "Provision_M":    round(prov, 2),
        "Net_Income_M":   round(ni, 2),
        "Net_Margin_Pct": round((ni/rev)*100, 2),
    })
df_monthly = pd.DataFrame(monthly_rows)

# ── Asset Quality ─────────────────────────────────────────────────────────────
asset_rows = []
for i, yr in enumerate(YEARS):
    total_assets = 85000 + i * np.random.uniform(4000, 7000)
    loans = total_assets * np.random.uniform(0.60, 0.66)
    deposits = total_assets * np.random.uniform(0.70, 0.76)
    npl_ratio = np.random.uniform(1.2, 3.5)
    asset_rows.append({
        "Year": yr,
        "Total_Assets_M":  round(total_assets, 2),
        "Total_Loans_M":   round(loans, 2),
        "Total_Deposits_M": round(deposits, 2),
        "NPL_Ratio_Pct":   round(npl_ratio, 2),
        "Capital_Adequacy_Pct": round(np.random.uniform(13.5, 17.0), 2),
        "Liquidity_Ratio_Pct":  round(np.random.uniform(120, 145), 2),
        "Loan_to_Deposit_Pct":  round((loans/deposits)*100, 2),
    })
df_assets = pd.DataFrame(asset_rows)

# ── Business Segment Revenue ──────────────────────────────────────────────────
segments = ["Retail Banking","Corporate Banking","Wealth Management","Investment Banking","Treasury"]
seg_rows = []
for yr in YEARS:
    yr_rev = df_annual.loc[df_annual.Year==yr,"Total_Revenue_M"].values[0]
    shares = np.random.dirichlet(np.ones(5)*3)
    for seg, share in zip(segments, shares):
        seg_rows.append({
            "Year": yr, "Segment": seg,
            "Revenue_M": round(yr_rev * share, 2),
            "Growth_Pct": round(np.random.uniform(-2, 18), 2),
        })
df_segments = pd.DataFrame(seg_rows)

# ── Quarterly KPIs 2024 ───────────────────────────────────────────────────────
q_rows = []
for q in QUARTERS:
    base = df_annual.loc[df_annual.Year==2024,"Total_Revenue_M"].values[0] / 4
    rev = base * np.random.uniform(0.93, 1.08)
    exp = rev * np.random.uniform(0.54, 0.59)
    ni  = (rev - exp) * 0.79
    q_rows.append({
        "Quarter": q,
        "Revenue_M":    round(rev, 2),
        "Expenses_M":   round(exp, 2),
        "Net_Income_M": round(ni, 2),
        "EPS":          round(np.random.uniform(1.1, 1.6), 2),
        "ROE_Pct":      round(np.random.uniform(11, 15), 2),
    })
df_quarterly = pd.DataFrame(q_rows)

# ── Export ────────────────────────────────────────────────────────────────────
out = "/home/claude/financial-dashboard/data"
df_annual.to_csv(f"{out}/annual_pnl.csv", index=False)
df_monthly.to_csv(f"{out}/monthly_revenue.csv", index=False)
df_assets.to_csv(f"{out}/asset_quality.csv", index=False)
df_segments.to_csv(f"{out}/segment_revenue.csv", index=False)
df_quarterly.to_csv(f"{out}/quarterly_kpis.csv", index=False)

# Export JSON for dashboard
summary = {
    "annual": df_annual.to_dict(orient="records"),
    "monthly": df_monthly.to_dict(orient="records"),
    "assets": df_assets.to_dict(orient="records"),
    "segments": df_segments.to_dict(orient="records"),
    "quarterly": df_quarterly.to_dict(orient="records"),
}
with open(f"{out}/dashboard_data.json", "w") as f:
    json.dump(summary, f, indent=2)

print("✅ Data generated successfully")
print(f"   Annual P&L rows: {len(df_annual)}")
print(f"   Monthly rows: {len(df_monthly)}")
print(f"   Asset rows: {len(df_assets)}")
print(f"   Segment rows: {len(df_segments)}")
print(f"   Quarterly rows: {len(df_quarterly)}")

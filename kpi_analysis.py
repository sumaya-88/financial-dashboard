"""
Financial Performance Dashboard — KPI Analysis Report
Generates a full text-based KPI analysis with insights
"""

import pandas as pd
import numpy as np

DATA_DIR = "/home/claude/financial-dashboard/data"

df_a  = pd.read_csv(f"{DATA_DIR}/annual_pnl.csv")
df_m  = pd.read_csv(f"{DATA_DIR}/monthly_revenue.csv")
df_as = pd.read_csv(f"{DATA_DIR}/asset_quality.csv")
df_s  = pd.read_csv(f"{DATA_DIR}/segment_revenue.csv")
df_q  = pd.read_csv(f"{DATA_DIR}/quarterly_kpis.csv")

SEP  = "═" * 70
SEP2 = "─" * 70
UP   = "▲"
DOWN = "▼"

def pct_change(new, old):
    return ((new - old) / abs(old)) * 100

def arrow(val):
    return UP if val >= 0 else DOWN

def section(title):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)

def subsection(title):
    print(f"\n{SEP2}")
    print(f"  {title}")
    print(SEP2)

# ── HEADER ────────────────────────────────────────────────────────────────────
print(SEP)
print("  APEX BANK — FINANCIAL PERFORMANCE KPI ANALYSIS REPORT")
print("  Reporting Period: FY 2020 – FY 2024")
print("  All figures in USD Millions unless noted")
print(SEP)

# ── 1. ANNUAL P&L ─────────────────────────────────────────────────────────────
section("1. ANNUAL PROFIT & LOSS SUMMARY")
print(f"\n{'Year':<6}{'Revenue':>12}{'Expenses':>12}{'Net Income':>12}{'NP Margin':>12}{'C/I Ratio':>12}{'YoY Rev%':>10}")
print(SEP2)
for i, row in df_a.iterrows():
    yoy = ""
    if i > 0:
        prev = df_a.iloc[i-1]
        ch = pct_change(row.Total_Revenue_M, prev.Total_Revenue_M)
        yoy = f"{arrow(ch)} {abs(ch):.1f}%"
    print(f"{int(row.Year):<6}"
          f"${row.Total_Revenue_M:>10,.1f}"
          f"${row.Operating_Expenses_M:>10,.1f}"
          f"${row.Net_Income_M:>10,.1f}"
          f"{row.Net_Profit_Margin_Pct:>11.1f}%"
          f"{row.Cost_Income_Ratio_Pct:>11.1f}%"
          f"{yoy:>12}")

last  = df_a.iloc[-1]
first = df_a.iloc[0]
cagr_rev = (last.Total_Revenue_M / first.Total_Revenue_M) ** (1/4) - 1
cagr_ni  = (last.Net_Income_M    / first.Net_Income_M)    ** (1/4) - 1
print(f"\n  5-Year CAGR — Revenue: {cagr_rev*100:.1f}%  |  Net Income: {cagr_ni*100:.1f}%")
print(f"  EPS FY2024: ${last.EPS:.2f}  |  ROE: {last.ROE_Pct:.1f}%  |  ROA: {last.ROA_Pct:.2f}%")

# ── 2. MONTHLY ANALYSIS ───────────────────────────────────────────────────────
section("2. MONTHLY REVENUE ANALYSIS — FY 2024")
print(f"\n{'Month':<6}{'Revenue':>12}{'Expenses':>12}{'Net Income':>12}{'Margin':>10}{'MoM Δ':>10}")
print(SEP2)
for i, row in df_m.iterrows():
    mom = ""
    if i > 0:
        prev = df_m.iloc[i-1]
        ch = pct_change(row.Revenue_M, prev.Revenue_M)
        mom = f"{arrow(ch)} {abs(ch):.1f}%"
    print(f"{row.Month:<6}"
          f"${row.Revenue_M:>10,.1f}"
          f"${row.Expenses_M:>10,.1f}"
          f"${row.Net_Income_M:>10,.1f}"
          f"{row.Net_Margin_Pct:>9.1f}%"
          f"{mom:>12}")

best  = df_m.loc[df_m.Net_Income_M.idxmax()]
worst = df_m.loc[df_m.Net_Income_M.idxmin()]
print(f"\n  Best Month:  {best.Month} — Net Income ${best.Net_Income_M:.1f}M ({best.Net_Margin_Pct:.1f}% margin)")
print(f"  Worst Month: {worst.Month} — Net Income ${worst.Net_Income_M:.1f}M ({worst.Net_Margin_Pct:.1f}% margin)")
print(f"  FY2024 Total Revenue:    ${df_m.Revenue_M.sum():,.1f}M")
print(f"  FY2024 Total Net Income: ${df_m.Net_Income_M.sum():,.1f}M")

# ── 3. ASSET QUALITY ─────────────────────────────────────────────────────────
section("3. ASSET QUALITY & BALANCE SHEET")
print(f"\n{'Year':<6}{'Total Assets':>14}{'Total Loans':>13}{'Deposits':>12}{'NPL%':>8}{'Cap.Adq%':>10}{'Liq%':>8}")
print(SEP2)
for _, row in df_as.iterrows():
    npl_flag = " ⚠" if row.NPL_Ratio_Pct > 2.5 else "  "
    print(f"{int(row.Year):<6}"
          f"${row.Total_Assets_M:>12,.1f}"
          f"${row.Total_Loans_M:>11,.1f}"
          f"${row.Total_Deposits_M:>10,.1f}"
          f"{row.NPL_Ratio_Pct:>7.2f}%{npl_flag}"
          f"{row.Capital_Adequacy_Pct:>8.1f}%"
          f"{row.Liquidity_Ratio_Pct:>7.1f}%")

latest_a = df_as.iloc[-1]
asset_cagr = (latest_a.Total_Assets_M / df_as.iloc[0].Total_Assets_M) ** (1/4) - 1
print(f"\n  Asset CAGR: {asset_cagr*100:.1f}%")
print(f"  FY2024 Loan-to-Deposit Ratio: {latest_a.Loan_to_Deposit_Pct:.1f}%")
npl_status = "ABOVE THRESHOLD ⚠" if latest_a.NPL_Ratio_Pct > 2.5 else "Within acceptable range ✓"
print(f"  FY2024 NPL Status: {npl_status}")
print(f"  FY2024 Capital Adequacy vs Basel III min (10.5%): {'COMPLIANT ✓' if latest_a.Capital_Adequacy_Pct > 10.5 else 'NON-COMPLIANT ✗'}")

# ── 4. SEGMENT ANALYSIS ───────────────────────────────────────────────────────
section("4. BUSINESS SEGMENT REVENUE (USD MILLIONS)")
segs = df_s.Segment.unique()
years_list = sorted(df_s.Year.unique())
print(f"\n{'Segment':<22}" + "".join(f"{y:>10}" for y in years_list) + f"{'5Y Total':>12}{'FY24 Share':>12}")
print(SEP2)
total_24 = df_s[df_s.Year==2024].Revenue_M.sum()
for seg in segs:
    row_data = [df_s[(df_s.Segment==seg) & (df_s.Year==yr)].Revenue_M.values[0]
                if len(df_s[(df_s.Segment==seg) & (df_s.Year==yr)]) > 0 else 0
                for yr in years_list]
    total = sum(row_data)
    share = row_data[-1] / total_24 * 100
    print(f"{seg:<22}" + "".join(f"{v:>10,.0f}" for v in row_data) + f"{total:>11,.0f}" + f"{share:>10.1f}%")

top_seg_24 = df_s[df_s.Year==2024].sort_values("Revenue_M", ascending=False).iloc[0]
print(f"\n  Top Segment FY2024: {top_seg_24.Segment} (${top_seg_24.Revenue_M:,.1f}M, {top_seg_24.Revenue_M/total_24*100:.1f}% share)")

# ── 5. QUARTERLY KPIs ─────────────────────────────────────────────────────────
section("5. QUARTERLY KPI SCORECARD — FY 2024")
print(f"\n{'Quarter':<10}{'Revenue':>12}{'Expenses':>12}{'Net Income':>12}{'EPS':>8}{'ROE%':>8}{'Exp.Ratio':>12}")
print(SEP2)
for _, row in df_q.iterrows():
    exp_ratio = row.Expenses_M / row.Revenue_M * 100
    flag = " ⚠" if exp_ratio > 59 else "  "
    print(f"{row.Quarter:<10}"
          f"${row.Revenue_M:>10,.1f}"
          f"${row.Expenses_M:>10,.1f}"
          f"${row.Net_Income_M:>10,.1f}"
          f"${row.EPS:>6.2f}"
          f"{row.ROE_Pct:>7.1f}%"
          f"{exp_ratio:>9.1f}%{flag}")

print(f"\n  Full Year EPS: ${df_q.EPS.sum():.2f}  |  Avg ROE: {df_q.ROE_Pct.mean():.1f}%")
print(f"  Best Quarter by Net Income: {df_q.loc[df_q.Net_Income_M.idxmax(),'Quarter']} (${df_q.Net_Income_M.max():,.1f}M)")

# ── 6. KEY INSIGHTS ───────────────────────────────────────────────────────────
section("6. KEY INSIGHTS & MANAGEMENT COMMENTARY")
print(f"""
  REVENUE & PROFITABILITY
  ─────────────────────────────────────────────────────────────────────
  • Revenue grew from ${first.Total_Revenue_M/1e3:.1f}B (FY20) to ${last.Total_Revenue_M/1e3:.1f}B (FY24),
    representing a {cagr_rev*100:.1f}% CAGR over 5 years.
  • Net profit margin contracted slightly from {first.Net_Profit_Margin_Pct:.1f}% to {last.Net_Profit_Margin_Pct:.1f}%,
    suggesting rising cost pressure.
  • Cost-to-Income ratio of {last.Cost_Income_Ratio_Pct:.1f}% in FY24; target is below 55%.

  ASSET QUALITY
  ─────────────────────────────────────────────────────────────────────
  • Total assets grew to ${latest_a.Total_Assets_M/1e3:.1f}B with a healthy loan book of
    ${latest_a.Total_Loans_M/1e3:.1f}B.
  • NPL ratio of {latest_a.NPL_Ratio_Pct:.2f}% in FY24 requires monitoring (spiked in FY22).
  • Capital adequacy at {latest_a.Capital_Adequacy_Pct:.1f}% — well above Basel III minimum of 10.5%.

  SEGMENT PERFORMANCE
  ─────────────────────────────────────────────────────────────────────
  • Treasury is the dominant revenue segment in FY2024 at ${df_s[(df_s.Year==2024)&(df_s.Segment=='Treasury')].Revenue_M.values[0]:,.0f}M.
  • Wealth Management posted the strongest FY2024 growth (+{df_s[(df_s.Year==2024)&(df_s.Segment=='Wealth Management')].Growth_Pct.values[0]:.1f}%).
  • Retail Banking remains a significant contributor at ${df_s[(df_s.Year==2024)&(df_s.Segment=='Retail Banking')].Revenue_M.values[0]:,.0f}M.

  QUARTERLY TRENDS
  ─────────────────────────────────────────────────────────────────────
  • Q3 2024 delivered the highest net income of ${df_q.Net_Income_M.max():,.1f}M.
  • Q2 showed the best cost efficiency with ROE at {df_q.ROE_Pct.max():.1f}%.
  • FY2024 full-year EPS: ${df_q.EPS.sum():.2f}.
""")
print(SEP)
print("  END OF REPORT — Apex Bank Financial Performance Dashboard")
print(SEP)

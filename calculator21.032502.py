import streamlit as st
import numpy_financial as npf

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🇨🇦 Mortgage & Financial Capacity Suite",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── GLOBAL CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=DM+Mono:wght@400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', system-ui, sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
.stApp { background-color: #f1f5f9; }

[data-testid="stSidebar"] { background: white !important; border-right: 1.5px solid #e2e8f0 !important; }
[data-testid="stSidebar"] .block-container { padding: 1.5rem 1rem !important; }
[data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    font-size: 10px !important; font-weight: 700 !important; color: #94a3b8 !important;
    text-transform: uppercase !important; letter-spacing: 0.08em !important;
    padding-bottom: 6px !important; border-bottom: 1px dashed #e2e8f0 !important; margin-bottom: 0.8rem !important;
}
[data-testid="stNumberInput"] input {
    font-family: 'DM Mono', monospace !important; font-size: 14px !important;
    background: #f8fafc !important; border: 1.5px solid #e2e8f0 !important;
    border-radius: 8px !important; color: #0f172a !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: #3b82f6 !important; box-shadow: 0 0 0 3px rgba(59,130,246,0.12) !important;
}
[data-testid="stNumberInput"] label {
    font-size: 11px !important; font-weight: 700 !important; color: #64748b !important;
    text-transform: uppercase !important; letter-spacing: 0.06em !important;
}
[data-testid="stTabs"] [role="tablist"] { border-bottom: 2px solid #e2e8f0 !important; gap: 4px !important; background: transparent !important; }
[data-testid="stTabs"] [role="tab"] {
    font-family: 'DM Sans', sans-serif !important; font-size: 13px !important; font-weight: 600 !important;
    color: #94a3b8 !important; border: none !important; border-bottom: 2.5px solid transparent !important;
    padding: 9px 16px !important; background: transparent !important; border-radius: 0 !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] { color: #3b82f6 !important; border-bottom: 2.5px solid #3b82f6 !important; }
[data-testid="stMetric"] { background: white !important; border: 1.5px solid #e2e8f0 !important; border-radius: 12px !important; padding: 16px 20px !important; }
[data-testid="stMetric"] label { font-size: 10px !important; font-weight: 700 !important; color: #94a3b8 !important; text-transform: uppercase !important; letter-spacing: 0.08em !important; }
[data-testid="stMetric"] [data-testid="stMetricValue"] { font-family: 'DM Mono', monospace !important; font-size: 22px !important; font-weight: 800 !important; color: #0f172a !important; letter-spacing: -0.02em !important; }
.stButton button { font-family: 'DM Sans', sans-serif !important; font-weight: 600 !important; border-radius: 8px !important; border: 1.5px solid #e2e8f0 !important; background: #f8fafc !important; color: #475569 !important; font-size: 13px !important; }
.stButton button:hover { background: #f1f5f9 !important; border-color: #cbd5e1 !important; }
hr { border-color: #e2e8f0 !important; margin: 1.2rem 0 !important; }
[data-testid="stExpander"] { border: 1.5px solid #e2e8f0 !important; border-radius: 10px !important; background: white !important; }
[data-testid="stExpander"] summary { font-size: 13px !important; font-weight: 700 !important; color: #0f172a !important; }
[data-testid="stAlert"] { border-radius: 8px !important; font-size: 13px !important; }
[data-testid="stCheckbox"] label { font-size: 13px !important; color: #475569 !important; }
[data-testid="stSlider"] label { font-size: 11px !important; font-weight: 700 !important; color: #64748b !important; text-transform: uppercase !important; letter-spacing: 0.06em !important; }
</style>
""", unsafe_allow_html=True)


# ─── HELPERS ──────────────────────────────────────────────────────────────────
def metric_card(label, value, color="#10b981", size=22):
    st.markdown(f"""
    <div style="background:white; border:1.5px solid #e2e8f0; border-top:3px solid {color};
                border-radius:12px; padding:16px 20px; text-align:center;">
        <div style="font-size:10px; font-weight:700; color:#94a3b8; text-transform:uppercase;
                    letter-spacing:0.08em; margin-bottom:8px;">{label}</div>
        <div style="font-size:{size}px; font-weight:800; color:{color};
                    font-family:'DM Mono',monospace; letter-spacing:-0.02em;">{value}</div>
    </div>
    """, unsafe_allow_html=True)

def section_header(text):
    st.markdown(f"""
    <div style="font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase;
                letter-spacing:0.08em; padding-bottom:8px; border-bottom:1px dashed #e2e8f0; margin:0 0 14px;">
        {text}
    </div>
    """, unsafe_allow_html=True)

def info_banner(html, color_bg="#eff6ff", color_border="#bfdbfe", color_text="#1e40af"):
    st.markdown(f"""
    <div style="background:{color_bg}; border:1px solid {color_border}; border-radius:8px;
                padding:10px 14px; font-size:13px; color:{color_text}; margin:10px 0;">
        {html}
    </div>
    """, unsafe_allow_html=True)

def ratio_badge(label, value, limit):
    pct = value * 100
    color = "#ef4444" if pct > limit else ("#f59e0b" if pct > limit * 0.9 else "#10b981")
    st.markdown(f"""
    <div style="background:white; border:2px solid {color}; border-radius:10px; padding:14px 16px; text-align:center;">
        <div style="font-size:10px; font-weight:700; color:#94a3b8; text-transform:uppercase;
                    letter-spacing:0.08em; margin-bottom:6px;">
            {label} <span style="color:#e2e8f0;">Limit: {limit}%</span>
        </div>
        <div style="font-size:28px; font-weight:800; color:{color}; font-family:'DM Mono',monospace;">{pct:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)


# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🇨🇦 Mortgage Suite")
    st.markdown("---")
    section_header("1. Personal Monthly Debts")
    auto_loan     = st.number_input("Auto Loan ($)",         value=400.0,  step=50.0,  key="s_auto")
    personal_loan = st.number_input("Personal Loan ($)",     value=0.0,    step=50.0,  key="s_pers")
    credit_card   = st.number_input("Credit Card Min. ($)",  value=0.0,    step=25.0,  key="s_cc")
    misc_debt     = st.number_input("Other Misc. Debts ($)", value=0.0,    step=25.0,  key="s_misc")
    total_other_debts = auto_loan + personal_loan + credit_card + misc_debt
    st.markdown(f"""
    <div style="background:#f8fafc; border-radius:8px; padding:8px 12px;
                font-family:'DM Mono',monospace; font-size:12px; margin:8px 0 16px;">
        Total: <strong style="color:#ef4444;">${total_other_debts:,.2f}</strong>/mo
    </div>
    """, unsafe_allow_html=True)
    section_header("Funds")
    down_payment = st.number_input("Down Payment ($)", value=30000.0, step=5000.0, key="s_down")
    min_down_pct = st.slider("Min. Required %", 5.0, 20.0, 5.0, step=1.0, key="s_pct")


# ─── MAIN HEADER ──────────────────────────────────────────────────────────────
st.markdown("""
<div style="display:flex; align-items:center; gap:12px; margin-bottom:4px;">
    <span style="font-size:24px;">🇨🇦</span>
    <span style="font-size:20px; font-weight:800; color:#0f172a; letter-spacing:-0.02em;">
        Complete Mortgage & Financial Capacity Suite
    </span>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "🏠 Buyer Financial Capacity",
    "💰 Minimum Income Calculation",
    "📊 GDS/TDS & TVM Solver",
    "🧮 Sharp EL-738XT Calculator"
])


# ─── TAB 1: BUYER FINANCIAL CAPACITY ─────────────────────────────────────────
with tab1:
    st.markdown("### Step-by-Step Financial Capacity")
    cap_inc = st.number_input("Gross Annual Household Income ($)", value=90000.0, step=5000.0, key="cap_inc")
    m_inc = cap_inc / 12
    c1, c2 = st.columns(2)
    with c1:
        c_tax   = st.number_input("Monthly Taxes ($)",      value=250.0, step=25.0, key="cap_tax")
        c_heat  = st.number_input("Monthly Heating ($)",    value=100.0, step=25.0, key="cap_heat")
        c_condo = st.number_input("Monthly Condo Fees ($)", value=0.0,   step=25.0, key="cap_condo")
    with c2:
        stress_r = st.number_input("Stress Test Rate (%)", value=7.25, step=0.25, key="cap_stress", help="Standard = Contract Rate + 2%")
        amort    = st.number_input("Amortization (Years)",  value=25,   step=1,    key="cap_amort")

    avail_gds = (m_inc * 0.39) - (c_tax + c_heat + 0.5 * c_condo)
    avail_tds = (m_inc * 0.44) - (c_tax + c_heat + 0.5 * c_condo + total_other_debts)
    final_pmt = max(0.0, min(avail_gds, avail_tds))
    binding   = "GDS" if avail_gds <= avail_tds else "TDS"

    r_p       = (1 + (stress_r / 100) / 2) ** (2 / 12) - 1
    n_periods = int(amort * 12)
    max_loan  = abs(npf.pv(r_p, n_periods, -final_pmt, 0))

    max_price_inc  = (max_loan / 1.04) + down_payment
    max_price_down = down_payment / (min_down_pct / 100)
    final_cap      = min(max_price_inc, max_price_down)

    st.markdown("---")
    r1, r2, r3 = st.columns(3)
    with r1: metric_card("Capacity via Income (A)",       f"${max_price_inc:,.2f}",  color="#3b82f6")
    with r2: metric_card("Capacity via Down Payment (B)", f"${max_price_down:,.2f}", color="#8b5cf6")
    with r3: metric_card("MAX PURCHASE CAPACITY",         f"${final_cap:,.2f}",      color="#10b981", size=20)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("📋 View Detailed Capacity Formula Breakdown", expanded=True):
        st.markdown("#### Step 1: Calculating Max Purchase Price Based on Income")
        st.markdown(f"""
        <div style="overflow-x:auto; border-radius:8px; border:1.5px solid #e2e8f0; margin:12px 0;">
        <table style="width:100%; border-collapse:collapse; font-family:'DM Sans',sans-serif;">
            <thead><tr style="background:#f8fafc; border-bottom:2px solid #e2e8f0;">
                <th style="padding:10px 12px; text-align:left; font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.06em; width:32px;"></th>
                <th style="padding:10px 12px; text-align:left; font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.06em;">Variable</th>
                <th style="padding:10px 12px; text-align:right; font-size:11px; font-weight:700; color:#3b82f6; text-transform:uppercase; letter-spacing:0.06em;">GDS (ABD) Logic</th>
                <th style="padding:10px 12px; text-align:right; font-size:11px; font-weight:700; color:#8b5cf6; text-transform:uppercase; letter-spacing:0.06em;">TDS (ATD) Logic</th>
            </tr></thead>
            <tbody>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">0</td><td style="padding:9px 12px; color:#475569; font-size:13px;">Gross Monthly Income</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">${m_inc:,.2f}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">${m_inc:,.2f}</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">1</td><td style="padding:9px 12px; color:#475569; font-size:13px;">Debt Service Ratio</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">× 39%</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">× 44%</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">2</td><td style="padding:9px 12px; color:#475569; font-size:13px;">Funds Available</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">= ${m_inc*0.39:,.2f}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">= ${m_inc*0.44:,.2f}</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">3</td><td style="padding:9px 12px; color:#475569; font-size:13px;">Monthly Taxes</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${c_tax:,.2f}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${c_tax:,.2f}</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">4</td><td style="padding:9px 12px; color:#475569; font-size:13px;">Monthly Heating</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${c_heat:,.2f}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${c_heat:,.2f}</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">5</td><td style="padding:9px 12px; color:#475569; font-size:13px;">50% Condo Fees</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${0.5*c_condo:,.2f}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${0.5*c_condo:,.2f}</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">6</td><td style="padding:9px 12px; color:#475569; font-size:13px;">Other Monthly Debts</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#94a3b8;">N/A</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${total_other_debts:,.2f}</td></tr>
                <tr style="background:#f8fafc;"><td style="padding:10px 12px; color:#cbd5e1; font-size:11px;">7</td><td style="padding:10px 12px; color:#0f172a; font-size:13px; font-weight:700;">Available Mortgage PMT</td><td style="padding:10px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; font-weight:700; color:#0f172a;">${avail_gds:,.2f}</td><td style="padding:10px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; font-weight:700; color:#0f172a;">${avail_tds:,.2f}</td></tr>
            </tbody>
        </table></div>
        """, unsafe_allow_html=True)
        info_banner(f"<strong>Selection:</strong> The lower amount is <strong>${final_pmt:,.2f}</strong>. Used as PMT for TVM. (Binding: <strong>{binding}</strong>)")
        st.markdown("---")
        st.markdown(f"""
        <div style="font-size:13px; font-weight:700; color:#0f172a; margin-bottom:8px;">Financial Calculator Settings used (CPT PV):</div>
        <div style="display:flex; flex-wrap:wrap; gap:20px; font-family:'DM Mono',monospace; font-size:12px; color:#475569; margin-bottom:8px;">
            <span>• P/Y = 12 | C/Y = 2</span>
            <span>• n = {n_periods} periods | I/Y = {stress_r}%</span>
            <span>• MAX MORTGAGE (incl. CMHC): <strong style="color:#0f172a;">${max_loan:,.2f}</strong></span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f"""
        <div style="font-size:13px; font-weight:700; color:#0f172a; margin-bottom:6px;">Final Step 1 Result:</div>
        <div style="font-family:'DM Mono',monospace; font-size:13px; color:#475569;">
            (Max Mortgage) ÷ 1.04 + Down Payment = <strong style="color:#10b981; font-size:15px;">${max_price_inc:,.2f}</strong>
        </div>
        """, unsafe_allow_html=True)
        st.warning("⚠️ If credit score is below 680, lenders typically use 32% GDS and 40% TDS limits.")


# ─── TAB 2: MINIMUM INCOME CALCULATION ───────────────────────────────────────
with tab2:
    st.markdown("### Minimum Income Calculation")
    st.markdown("<p style='color:#64748b; font-size:13px;'>Find the required salary to afford specific costs at a 39% GDS limit.</p>", unsafe_allow_html=True)
    m1, m2 = st.columns(2)
    with m1:
        min_pmt  = st.number_input("Monthly Mortgage PMT ($)",       value=2000.0, step=0.01, format="%.2f", key="min_pmt",
                                   help="Enter the Sharp-computed PMT rounded to 2 decimal places (e.g. 1593.12)")
        min_tax  = st.number_input("Taxes (Property & School) ($)",  value=300.0,  step=0.01, format="%.2f", key="min_tax")
    with m2:
        min_heat  = st.number_input("Monthly Heating ($)",    value=125.0, step=0.01, format="%.2f", key="min_heat")
        min_condo = st.number_input("Monthly Condo Fees ($)", value=0.0,   step=0.01, format="%.2f", key="min_condo")

    # Round PMT to 2dp to match Sharp EL-738XT cent-level rounding
    min_pmt_sharp = round(min_pmt, 2)
    housing_total = round(min_pmt_sharp + min_tax + min_heat + 0.5 * min_condo, 2)
    req_monthly   = round(housing_total / 0.39, 2)
    req_annual    = round(req_monthly * 12, 2)

    st.markdown("---")
    r1, r2 = st.columns(2)
    with r1: metric_card("Total Monthly Housing Costs",   f"${housing_total:,.2f}", color="#3b82f6")
    with r2: metric_card("Required Gross Annual Salary",  f"${req_annual:,.2f}",    color="#f59e0b", size=20)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:white; border:1.5px solid #e2e8f0; border-radius:12px; padding:20px 22px;">
        <div style="font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:12px;">Formula Breakdown</div>
        <div style="font-family:'DM Mono',monospace; font-size:13px; color:#475569; line-height:2;">
            PMT ${min_pmt_sharp:,.2f} + Taxes ${min_tax:,.2f} + Heat ${min_heat:,.2f} + ½ Condo ${0.5*min_condo:,.2f}
            = <strong style="color:#0f172a;">${housing_total:,.2f}</strong> / month<br>
            Required Monthly = ${housing_total:,.2f} ÷ 0.39 = <strong style="color:#0f172a;">${req_monthly:,.2f}</strong><br>
            Required Annual = ${req_monthly:,.2f} × 12 = <strong style="color:#f59e0b;">${req_annual:,.2f}</strong>
        </div>
        <div style="margin-top:10px; background:#f5f3ff; border:1px solid #ddd6fe; border-radius:8px;
                    padding:8px 12px; font-family:'DM Mono',monospace; font-size:11px; color:#4c1d95;">
            ✓ PMT rounded to 2 decimal places to match Sharp EL-738XT cent-level rounding
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── TAB 3: GDS/TDS & TVM SOLVER ─────────────────────────────────────────────
with tab3:
    st.markdown("### Ratio Calculator & Sharp TVM Solver")
    ratio_inc_annual = st.number_input("Gross Annual Income ($)", value=90000.0, step=5000.0, key="r_inc")
    m_inc_ratio = ratio_inc_annual / 12 if ratio_inc_annual > 0 else 1
    st.markdown("---")
    r_c1, r_c2 = st.columns(2)

    with r_c1:
        st.markdown("<div style='font-size:13px; font-weight:700; color:#0f172a; margin-bottom:14px;'>🧮 Sharp EL-738XT TVM</div>", unsafe_allow_html=True)
        py   = st.number_input("P/Y",     value=12.0,     step=1.0,    key="sharp_py")
        cy   = st.number_input("C/Y",     value=2.0,      step=1.0,    key="sharp_cy")
        i_y  = st.number_input("I/Y (%)", value=6.0,      step=0.25,   key="sharp_iy")
        pv_y = st.number_input("PV ($)",  value=300000.0, step=5000.0, key="sharp_pv")
        r_periodic = (1 + (i_y / 100) / cy) ** (cy / py) - 1
        sharp_pmt  = abs(npf.pmt(r_periodic, 25 * py, pv_y, 0))
        metric_card("Computed PMT", f"${sharp_pmt:,.2f}", color="#6366f1")
        st.markdown(f"""
        <div style="background:#f5f3ff; border:1px solid #ddd6fe; border-radius:8px;
                    padding:10px 14px; font-family:'DM Mono',monospace; font-size:12px; color:#4c1d95; margin-top:10px;">
            r = (1 + {i_y}% / {cy:.0f})^({cy:.0f}/{py:.0f}) − 1 = {r_periodic*100:.6f}%
        </div>
        """, unsafe_allow_html=True)

    with r_c2:
        st.markdown("<div style='font-size:13px; font-weight:700; color:#0f172a; margin-bottom:14px;'>📊 Current Debt Ratios</div>", unsafe_allow_html=True)
        use_sharp  = st.checkbox(f"Use Sharp PMT (${sharp_pmt:,.2f})?", value=True, key="use_sharp")
        manual_pmt = sharp_pmt
        if not use_sharp:
            manual_pmt = st.number_input("Manual PMT ($)", value=1500.0, key="manual_pmt")
        active_pmt = sharp_pmt if use_sharp else manual_pmt
        r_tax   = st.number_input("Monthly Tax ($)",        value=250.0, step=25.0, key="r_tax")
        r_heat  = st.number_input("Monthly Heating ($)",    value=100.0, step=25.0, key="r_heat")
        r_condo = st.number_input("Monthly Condo Fees ($)", value=0.0,   step=25.0, key="r_condo")
        total_h = active_pmt + r_tax + r_heat + 0.5 * r_condo
        total_d = total_h + total_other_debts
        gds_val = total_h / m_inc_ratio
        tds_val = total_d / m_inc_ratio
        st.markdown("---")
        rb1, rb2 = st.columns(2)
        with rb1: ratio_badge("GDS Ratio", gds_val, 39)
        with rb2: ratio_badge("TDS Ratio", tds_val, 44)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:white; border:1.5px solid #e2e8f0; border-radius:12px; padding:20px 22px;">
        <div style="font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:12px;">Ratio Breakdown</div>
        <div style="font-family:'DM Mono',monospace; font-size:12px; color:#475569; line-height:2.2;">
            PMT ${active_pmt:,.2f} + Tax ${r_tax:,.2f} + Heat ${r_heat:,.2f} + ½ Condo ${0.5*r_condo:,.2f} = Housing <strong style="color:#0f172a;">${total_h:,.2f}</strong><br>
            Housing ${total_h:,.2f} + Other Debts ${total_other_debts:,.2f} = Total <strong style="color:#0f172a;">${total_d:,.2f}</strong><br>
            GDS = ${total_h:,.2f} ÷ ${m_inc_ratio:,.2f} = <strong style="color:{'#ef4444' if gds_val*100 > 39 else '#10b981'};">{gds_val*100:.2f}%</strong> {"⚠️ EXCEEDS 39% LIMIT" if gds_val*100 > 39 else "✅ Within limit"}<br>
            TDS = ${total_d:,.2f} ÷ ${m_inc_ratio:,.2f} = <strong style="color:{'#ef4444' if tds_val*100 > 44 else '#10b981'};">{tds_val*100:.2f}%</strong> {"⚠️ EXCEEDS 44% LIMIT" if tds_val*100 > 44 else "✅ Within limit"}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── TAB 4: SHARP EL-738XT MORTGAGE CALCULATOR ───────────────────────────────
with tab4:
    st.markdown("### 🧮 Sharp EL-738XT Mortgage Calculator")
    st.markdown("<p style='color:#64748b; font-size:13px;'>Full TVM solver with amortization schedule — replicating Sharp financial calculator logic for Canadian mortgages.</p>", unsafe_allow_html=True)

    left_col, right_col = st.columns(2)

    with left_col:
        # ── Dark calculator panel ──
        st.markdown("""
        <div style="background:#1e293b; border-radius:16px; padding:20px; margin-bottom:14px; box-shadow:0 8px 32px rgba(15,23,42,0.35);">
            <div style="background:#0f172a; border-radius:10px; padding:14px 18px; margin-bottom:16px; border:1px solid #334155;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#334155; letter-spacing:0.15em; margin-bottom:4px;">SHARP EL-738XT  |  CANADIAN MORTGAGE MODE</div>
                <div style="font-family:'DM Mono',monospace; font-size:11px; color:#475569;">P/Y=12  C/Y=2  |  Set inputs below then click CPT</div>
            </div>
            <div style="font-size:10px; font-weight:700; color:#64748b; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:8px;">TVM Inputs</div>
        </div>
        """, unsafe_allow_html=True)

        # Solve-for radio
        solve_for = st.radio("Compute (CPT) — Solve for:", ["PMT", "PV", "N", "FV"],
                             horizontal=True, key="calc_solve")

        st.markdown("---")

        ca1, ca2 = st.columns(2)
        with ca1:
            calc_py = st.number_input("P/Y (Payments/Year)",     value=12.0,     step=1.0,    key="calc_py")
            calc_iy = st.number_input("I/Y — Annual Rate (%)",   value=5.5,      step=0.05,   key="calc_iy", help="e.g. 5.5 for 5.5%")
            calc_pv = st.number_input("PV — Mortgage Amount ($)", value=400000.0, step=5000.0, key="calc_pv",
                                      disabled=(solve_for == "PV"))
        with ca2:
            calc_cy = st.number_input("C/Y (Compounding/Year)",  value=2.0,      step=1.0,    key="calc_cy", help="2 = semi-annual (Canadian)")
            calc_n  = st.number_input("N — Total Periods",        value=300.0,    step=12.0,   key="calc_n",  help="25 yrs × 12 = 300",
                                      disabled=(solve_for == "N"))
            calc_pmt_input = st.number_input("PMT — Payment ($)", value=2400.0,  step=25.0,   key="calc_pmt",
                                             disabled=(solve_for == "PMT"))

        # ── Calculations ──
        calc_r = (1 + (calc_iy / 100) / calc_cy) ** (calc_cy / calc_py) - 1

        if solve_for == "PMT":
            result_pmt = abs(npf.pmt(calc_r, calc_n, calc_pv, 0))
            result_pv  = calc_pv
            result_n   = int(calc_n)
        elif solve_for == "PV":
            result_pmt = calc_pmt_input
            result_pv  = abs(npf.pv(calc_r, calc_n, -calc_pmt_input, 0))
            result_n   = int(calc_n)
        elif solve_for == "N":
            result_pmt = calc_pmt_input
            result_pv  = calc_pv
            if calc_pmt_input > 0 and calc_r > 0:
                result_n = int(abs(npf.nper(calc_r, -calc_pmt_input, calc_pv, 0)))
            else:
                result_n = 0
        else:  # FV
            result_pmt = calc_pmt_input
            result_pv  = calc_pv
            result_n   = int(calc_n)

        # ── Display screen result ──
        if solve_for == "PMT":
            screen_val = f"${result_pmt:,.2f}"
            screen_label = "CPT PMT ="
        elif solve_for == "PV":
            screen_val = f"${result_pv:,.2f}"
            screen_label = "CPT PV ="
        elif solve_for == "N":
            screen_val = f"{result_n} periods ({result_n/12:.1f} yrs)"
            screen_label = "CPT N ="
        else:
            fv_result = npf.fv(calc_r, result_n, -result_pmt, -result_pv)
            screen_val = f"${fv_result:,.2f}"
            screen_label = "CPT FV ="

        st.markdown(f"""
        <div style="background:#0f172a; border-radius:12px; padding:18px 20px; margin:14px 0; border:1px solid #334155;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#334155; letter-spacing:0.12em; margin-bottom:6px;">
                SHARP EL-738XT  |  {screen_label}
            </div>
            <div style="font-family:'DM Mono',monospace; font-size:28px; color:#10b981; font-weight:700; letter-spacing:-0.02em;">
                {screen_val}
            </div>
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#475569; margin-top:6px;">
                r = {calc_r*100:.7f}% per period  |  P/Y={calc_py:.0f}  C/Y={calc_cy:.0f}  I/Y={calc_iy}%  n={result_n}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Formula box
        st.markdown(f"""
        <div style="background:#f5f3ff; border:1px solid #ddd6fe; border-radius:10px; padding:12px 16px;
                    font-family:'DM Mono',monospace; font-size:11px; color:#4c1d95; line-height:1.9;">
            <div style="font-weight:700; font-size:12px; margin-bottom:4px;">🇨🇦 Canadian Mortgage Formula</div>
            r = (1 + I/Y ÷ C/Y) ^ (C/Y ÷ P/Y) − 1<br>
            r = (1 + {calc_iy}% ÷ {calc_cy:.0f}) ^ ({calc_cy:.0f} ÷ {calc_py:.0f}) − 1<br>
            <strong style="color:#6d28d9;">r = {calc_r*100:.8f}% per period</strong>
        </div>
        """, unsafe_allow_html=True)

    with right_col:
        # ── Summary metrics ──
        # Round PMT to 2dp to match how Sharp EL-738XT stores and uses it
        active_pmt_calc = round(result_pmt, 2)
        active_pv_calc  = result_pv
        active_n_calc   = result_n
        total_cost      = active_pmt_calc * active_n_calc
        total_interest  = max(0, total_cost - active_pv_calc)

        mc1, mc2 = st.columns(2)
        with mc1:
            metric_card("Monthly Payment (PMT)", f"${active_pmt_calc:,.2f}", color="#3b82f6", size=18)
            metric_card("Total Cost of Mortgage", f"${total_cost:,.2f}", color="#f59e0b", size=16)
        with mc2:
            metric_card("Mortgage Amount (PV)",  f"${active_pv_calc:,.2f}", color="#8b5cf6", size=18)
            metric_card("Total Interest Paid",   f"${total_interest:,.2f}",  color="#ef4444", size=16)

        # Principal vs Interest bar
        if active_pv_calc > 0 and total_cost > 0:
            prin_pct = min(100, (active_pv_calc / total_cost) * 100)
            int_pct  = max(0, 100 - prin_pct)
            st.markdown(f"""
            <div style="background:white; border:1.5px solid #e2e8f0; border-radius:12px; padding:16px 20px; margin:14px 0;">
                <div style="font-size:11px; font-weight:700; color:#64748b; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;">Principal vs Interest Split</div>
                <div style="height:16px; background:#f1f5f9; border-radius:99px; overflow:hidden; margin-bottom:8px;">
                    <div style="height:100%; width:{prin_pct:.1f}%; background:linear-gradient(90deg,#3b82f6,#6366f1); border-radius:99px;"></div>
                </div>
                <div style="display:flex; justify-content:space-between; font-family:'DM Mono',monospace; font-size:12px;">
                    <span style="color:#3b82f6; font-weight:600;">Principal {prin_pct:.1f}% = ${active_pv_calc:,.2f}</span>
                    <span style="color:#ef4444; font-weight:600;">Interest {int_pct:.1f}% = ${total_interest:,.2f}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ── P1 / P2 Payment Range Analysis (AMRT) ────────────────────────────
        st.markdown("""
        <div style="background:#1e293b; border-radius:12px; padding:16px 18px; margin:14px 0 10px;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#475569; letter-spacing:0.15em; margin-bottom:6px;">SHARP EL-738XT  |  AMRT  —  AMORTIZATION RANGE</div>
            <div style="font-size:13px; font-weight:700; color:#e2e8f0; margin-bottom:2px;">P1 / P2 Payment Range Analyzer</div>
            <div style="font-size:11px; color:#64748b;">Set a starting (P1) and ending (P2) payment to isolate interest, principal, and balance for any range.</div>
        </div>
        """, unsafe_allow_html=True)

        p_col1, p_col2 = st.columns(2)
        with p_col1:
            p1 = st.number_input(
                "P1 — Starting Payment #",
                min_value=1, max_value=max(1, active_n_calc),
                value=1, step=1, key="amrt_p1",
                help="First payment in the range to analyze (e.g. 1 = start of loan)"
            )
        with p_col2:
            p2 = st.number_input(
                "P2 — Ending Payment #",
                min_value=1, max_value=max(1, active_n_calc),
                value=min(12, max(1, active_n_calc)), step=1, key="amrt_p2",
                help="Last payment in the range to analyze (e.g. 12 = end of Year 1)"
            )

        # Clamp and validate
        p1 = int(max(1, p1))
        p2 = int(max(p1, p2))

        # ── Compute the full schedule up to p2 ──
        if active_pmt_calc > 0 and active_pv_calc > 0:
            # Round PMT to 2 decimal places to match Sharp EL-738XT behaviour
            # (the real calculator works in cents, accumulating exact cent-level interest)
            sharp_rounded_pmt = round(active_pmt_calc, 2)
            bal     = active_pv_calc
            sched   = []
            for i in range(1, min(active_n_calc, 360) + 1):
                int_i  = round(bal * calc_r, 2)
                prin_i = round(min(sharp_rounded_pmt - int_i, bal), 2)
                bal    = round(max(0.0, bal - prin_i), 2)
                sched.append({"period": i, "interest": int_i, "principal": prin_i, "balance": bal})
                if bal < 0.01:
                    break

            # Clamp p2 to actual schedule length
            p2 = min(p2, len(sched))
            p1 = min(p1, p2)

            # Balance just before p1 (end of period p1-1)
            bal_before = sched[p1 - 2]["balance"] if p1 > 1 else active_pv_calc
            bal_after  = sched[p2 - 1]["balance"]

            range_int  = sum(r["interest"]  for r in sched[p1 - 1 : p2])
            range_prin = sum(r["principal"] for r in sched[p1 - 1 : p2])
            num_pmts   = p2 - p1 + 1

            # ── AMRT Results panel ──
            st.markdown(f"""
            <div style="background:white; border:1.5px solid #e2e8f0; border-radius:12px; padding:18px 20px; margin:10px 0 14px;">
                <div style="font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:14px;">
                    AMRT Results — Payments {p1} to {p2} ({num_pmts} payment{"s" if num_pmts != 1 else ""})
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:14px;">
                    <div style="background:#eff6ff; border:1.5px solid #bfdbfe; border-radius:10px; padding:14px 16px; text-align:center;">
                        <div style="font-size:10px; font-weight:700; color:#3b82f6; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:6px;">Interest Paid (INT)</div>
                        <div style="font-size:22px; font-weight:800; color:#1d4ed8; font-family:'DM Mono',monospace;">${range_int:,.2f}</div>
                    </div>
                    <div style="background:#f0fdf4; border:1.5px solid #bbf7d0; border-radius:10px; padding:14px 16px; text-align:center;">
                        <div style="font-size:10px; font-weight:700; color:#10b981; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:6px;">Principal Paid (PRN)</div>
                        <div style="font-size:22px; font-weight:800; color:#065f46; font-family:'DM Mono',monospace;">${range_prin:,.2f}</div>
                    </div>
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:14px;">
                    <div style="background:#f8fafc; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 16px; text-align:center;">
                        <div style="font-size:10px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:6px;">Balance at Start of P1</div>
                        <div style="font-size:16px; font-weight:700; color:#475569; font-family:'DM Mono',monospace;">${bal_before:,.2f}</div>
                    </div>
                    <div style="background:#f8fafc; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 16px; text-align:center;">
                        <div style="font-size:10px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:6px;">Balance at End of P2 (BAL)</div>
                        <div style="font-size:16px; font-weight:700; color:#0f172a; font-family:'DM Mono',monospace;">${bal_after:,.2f}</div>
                    </div>
                </div>
                <div style="background:#f8fafc; border-radius:8px; padding:10px 14px; font-family:'DM Mono',monospace; font-size:11px; color:#64748b; line-height:1.8;">
                    <strong style="color:#0f172a;">Range breakdown:</strong>
                    &nbsp; INT ${range_int:,.2f} + PRN ${range_prin:,.2f} = Total paid ${range_int + range_prin:,.2f}
                    &nbsp;|&nbsp; BAL reduced by ${bal_before - bal_after:,.2f}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # ── Amortization Schedule (filtered to P1–P2 range, then full) ──
            st.markdown("**📅 Amortization Schedule** — Showing selected range (P1–P2) + annual snapshots")

            rows = []
            for r in sched:
                i = r["period"]
                in_range = p1 <= i <= p2
                is_annual = (i % 12 == 0)
                if in_range or is_annual or i <= 3:
                    rows.append({
                        "period":    i,
                        "label":     f"Mo {i}" if not is_annual else f"Year {i // 12}",
                        "payment":   active_pmt_calc,
                        "interest":  r["interest"],
                        "principal": r["principal"],
                        "balance":   r["balance"],
                        "in_range":  in_range,
                        "is_annual": is_annual,
                    })

            header_html = "".join([
                f'<th style="padding:8px 10px; text-align:{"left" if h=="Period" else "right"}; font-size:10px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.06em; border-bottom:2px solid #e2e8f0; background:#f8fafc; position:sticky; top:0;">{h}</th>'
                for h in ["Period", "Payment", "Interest", "Principal", "Balance"]
            ])

            rows_html = ""
            for row in rows:
                in_r  = row["in_range"]
                is_yr = row["is_annual"]
                bg    = "#fefce8" if in_r else ("#f8fafc" if is_yr else "white")
                fw    = "700" if in_r else ("600" if is_yr else "400")
                border_left = "border-left:3px solid #f59e0b;" if in_r else ""
                rows_html += f'<tr style="border-bottom:1px solid #f1f5f9; background:{bg}; {border_left}">'
                rows_html += f'<td style="padding:7px 10px; font-family:\'DM Mono\',monospace; color:{"#92400e" if in_r else "#64748b"}; font-size:11px; font-weight:{fw};">{row["label"]} {"◀" if in_r else ""}</td>'
                rows_html += f'<td style="padding:7px 10px; text-align:right; font-family:\'DM Mono\',monospace; color:#0f172a; font-size:12px; font-weight:{fw};">${row["payment"]:,.2f}</td>'
                rows_html += f'<td style="padding:7px 10px; text-align:right; font-family:\'DM Mono\',monospace; color:#ef4444; font-size:12px; font-weight:{fw};">${row["interest"]:,.2f}</td>'
                rows_html += f'<td style="padding:7px 10px; text-align:right; font-family:\'DM Mono\',monospace; color:#10b981; font-size:12px; font-weight:{fw};">${row["principal"]:,.2f}</td>'
                rows_html += f'<td style="padding:7px 10px; text-align:right; font-family:\'DM Mono\',monospace; color:#475569; font-size:12px; font-weight:{fw};">${row["balance"]:,.2f}</td>'
                rows_html += "</tr>"

            st.markdown(f"""
            <div style="overflow-x:auto; max-height:400px; overflow-y:auto; border-radius:8px; border:1.5px solid #e2e8f0;">
            <table style="width:100%; border-collapse:collapse;">
                <thead><tr>{header_html}</tr></thead>
                <tbody>{rows_html}</tbody>
            </table>
            </div>
            <div style="margin-top:8px; font-family:'DM Mono',monospace; font-size:11px; color:#94a3b8;">
                <span style="background:#fefce8; border:1px solid #fde68a; border-radius:4px; padding:2px 8px; color:#92400e; font-weight:700;">◀ highlighted rows</span>
                = selected P1–P2 range &nbsp;|&nbsp; Total schedule: <strong style="color:#0f172a;">{len(sched)} periods ({len(sched)/12:.1f} yrs)</strong>
                &nbsp;|&nbsp; Total interest: <strong style="color:#ef4444;">${sum(r["interest"] for r in sched):,.2f}</strong>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Enter valid PV and PMT values to generate the amortization schedule.")
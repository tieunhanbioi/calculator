import streamlit as st
import numpy_financial as npf

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🇨🇦 Suite Hypothécaire / Mortgage Suite",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── TRANSLATIONS ─────────────────────────────────────────────────────────────
LANG = {
    "en": {
        # General
        "app_title": "Complete Mortgage & Financial Capacity Suite",
        "language_toggle": "🇫🇷 Français",

        # Sidebar
        "sidebar_title": "🇨🇦 Mortgage Suite",
        "sidebar_debts": "1. Personal Monthly Debts",
        "sidebar_auto": "Auto Loan ($)",
        "sidebar_personal": "Personal Loan ($)",
        "sidebar_cc": "Credit Card Min. ($)",
        "sidebar_misc": "Other Misc. Debts ($)",
        "sidebar_total": "Total",
        "sidebar_per_month": "/mo",
        "sidebar_funds": "Funds",
        "sidebar_down": "Down Payment ($)",
        "sidebar_min_pct": "Min. Required %",

        # Tab names
        "tab1": "🏠 Buyer Financial Capacity",
        "tab2": "💰 Minimum Income Calculation",
        "tab3": "📊 GDS/TDS & TVM Solver",
        "tab4": "🧮 Sharp EL-738XT Calculator",

        # Tab 1
        "t1_title": "Step-by-Step Financial Capacity",
        "t1_income": "Gross Annual Household Income ($)",
        "t1_taxes": "Monthly Taxes ($)",
        "t1_heating": "Monthly Heating ($)",
        "t1_condo": "Monthly Condo Fees ($)",
        "t1_stress": "Stress Test Rate (%)",
        "t1_stress_help": "Standard = Contract Rate + 2%",
        "t1_amort": "Amortization (Years)",
        "t1_cap_income": "Capacity via Income (A)",
        "t1_cap_down": "Capacity via Down Payment (B)",
        "t1_max_cap": "MAX PURCHASE CAPACITY",
        "t1_expander": "📋 View Detailed Capacity Formula Breakdown",
        "t1_step1": "Step 1: Calculating Max Purchase Price Based on Income",
        "t1_col_variable": "Variable",
        "t1_col_gds": "GDS (ABD) Logic",
        "t1_col_tds": "TDS (ATD) Logic",
        "t1_row0": "Gross Monthly Income",
        "t1_row1": "Debt Service Ratio",
        "t1_row2": "Funds Available",
        "t1_row3": "Monthly Taxes",
        "t1_row4": "Monthly Heating",
        "t1_row5": "50% Condo Fees",
        "t1_row6": "Other Monthly Debts",
        "t1_row7": "Available Mortgage PMT",
        "t1_selection": "<strong>Selection:</strong> The lower amount is <strong>{pmt}</strong>. Used as PMT for TVM. (Binding: <strong>{binding}</strong>)",
        "t1_calc_settings": "Financial Calculator Settings used (CPT PV):",
        "t1_periods": "periods",
        "t1_max_mortgage": "MAX MORTGAGE (incl. CMHC)",
        "t1_final_result": "Final Step 1 Result:",
        "t1_formula": "(Max Mortgage) ÷ 1.04 + Down Payment =",
        "t1_warning": "⚠️ If credit score is below 680, lenders typically use 32% GDS and 40% TDS limits.",

        # Tab 2
        "t2_title": "Minimum Income Calculation",
        "t2_subtitle": "Find the required salary to afford specific costs at a 39% GDS limit.",
        "t2_pmt": "Monthly Mortgage PMT ($)",
        "t2_pmt_help": "Enter the Sharp-computed PMT rounded to 2 decimal places (e.g. 1593.12)",
        "t2_taxes": "Taxes (Property & School) ($)",
        "t2_heating": "Monthly Heating ($)",
        "t2_condo": "Monthly Condo Fees ($)",
        "t2_housing_total": "Total Monthly Housing Costs",
        "t2_req_salary": "Required Gross Annual Salary",
        "t2_formula_title": "Formula Breakdown",
        "t2_req_monthly": "Required Monthly",
        "t2_req_annual": "Required Annual",
        "t2_sharp_note": "✓ PMT rounded to 2 decimal places to match Sharp EL-738XT cent-level rounding",

        # Tab 3
        "t3_title": "Ratio Calculator & Sharp TVM Solver",
        "t3_income": "Gross Annual Income ($)",
        "t3_tvm_title": "🧮 Sharp EL-738XT TVM",
        "t3_ratio_title": "📊 Current Debt Ratios",
        "t3_use_sharp": "Use Sharp PMT ({pmt})?",
        "t3_manual_pmt": "Manual PMT ($)",
        "t3_tax": "Monthly Tax ($)",
        "t3_heat": "Monthly Heating ($)",
        "t3_condo": "Monthly Condo Fees ($)",
        "t3_gds": "GDS Ratio",
        "t3_tds": "TDS Ratio",
        "t3_limit": "Limit",
        "t3_breakdown_title": "Ratio Breakdown",
        "t3_housing": "Housing",
        "t3_other_debts": "Other Debts",
        "t3_total": "Total",
        "t3_exceeds_gds": "⚠️ EXCEEDS 39% LIMIT",
        "t3_exceeds_tds": "⚠️ EXCEEDS 44% LIMIT",
        "t3_within": "✅ Within limit",

        # Tab 4
        "t4_title": "🧮 Sharp EL-738XT Mortgage Calculator",
        "t4_subtitle": "Full TVM solver with amortization schedule — replicating Sharp financial calculator logic for Canadian mortgages.",
        "t4_screen_mode": "CANADIAN MORTGAGE MODE",
        "t4_set_inputs": "Set inputs below then click CPT",
        "t4_cpt_label": "Compute (CPT) — Solve for:",
        "t4_py_help": "e.g. 12 = monthly payments",
        "t4_cy_help": "2 = semi-annual (Canadian)",
        "t4_iy_help": "e.g. 5.5 for 5.5%",
        "t4_n_help": "25 yrs × 12 = 300",
        "t4_py": "P/Y (Payments/Year)",
        "t4_cy": "C/Y (Compounding/Year)",
        "t4_iy": "I/Y — Annual Rate (%)",
        "t4_n":  "N — Total Periods",
        "t4_pv": "PV — Mortgage Amount ($)",
        "t4_pmt": "PMT — Payment ($)",
        "t4_formula_title": "🇨🇦 Canadian Mortgage Formula",
        "t4_pmt_card": "Monthly Payment (PMT)",
        "t4_pv_card":  "Mortgage Amount (PV)",
        "t4_total_cost": "Total Cost of Mortgage",
        "t4_total_int": "Total Interest Paid",
        "t4_split_title": "Principal vs Interest Split",
        "t4_principal": "Principal",
        "t4_interest": "Interest",
        "t4_amrt_header": "AMRT  —  AMORTIZATION RANGE",
        "t4_amrt_title": "P1 / P2 Payment Range Analyzer",
        "t4_amrt_subtitle": "Set a starting (P1) and ending (P2) payment to isolate interest, principal, and balance for any range.",
        "t4_p1": "P1 — Starting Payment #",
        "t4_p1_help": "First payment in the range to analyze (e.g. 1 = start of loan)",
        "t4_p2": "P2 — Ending Payment #",
        "t4_p2_help": "Last payment in the range to analyze (e.g. 12 = end of Year 1)",
        "t4_amrt_results": "AMRT Results — Payments {p1} to {p2} ({n} payment{s})",
        "t4_int_paid": "Interest Paid (INT)",
        "t4_prin_paid": "Principal Paid (PRN)",
        "t4_bal_start": "Balance at Start of P1",
        "t4_bal_end": "Balance at End of P2 (BAL)",
        "t4_range_breakdown": "Range breakdown:",
        "t4_total_paid": "Total paid",
        "t4_bal_reduced": "BAL reduced by",
        "t4_sched_title": "**📅 Amortization Schedule** — Showing selected range (P1–P2) + annual snapshots",
        "t4_highlighted": "◀ highlighted rows",
        "t4_selected_range": "= selected P1–P2 range",
        "t4_total_sched": "Total schedule",
        "t4_total_interest": "Total interest",
        "t4_periods_yrs": "periods",
        "t4_yrs": "yrs",
        "t4_no_data": "Enter valid PV and PMT values to generate the amortization schedule.",
        "t4_period": "Period",
        "t4_payment": "Payment",
        "t4_year": "Year",
        "t4_month_abbr": "Mo",
        "t4_payment_s": "payments",
        "t4_payment_1": "payment",
        "t4_per_period": "per period",
    },
    "fr": {
        # General
        "app_title": "Suite complète hypothécaire et de capacité financière",
        "language_toggle": "🇬🇧 English",

        # Sidebar
        "sidebar_title": "🇨🇦 Suite Hypothécaire",
        "sidebar_debts": "1. Dettes mensuelles personnelles",
        "sidebar_auto": "Prêt auto ($)",
        "sidebar_personal": "Prêt personnel ($)",
        "sidebar_cc": "Carte de crédit min. ($)",
        "sidebar_misc": "Autres dettes diverses ($)",
        "sidebar_total": "Total",
        "sidebar_per_month": "/mois",
        "sidebar_funds": "Mise de fonds",
        "sidebar_down": "Mise de fonds ($)",
        "sidebar_min_pct": "% min. requis",

        # Tab names
        "tab1": "🏠 Capacité financière",
        "tab2": "💰 Revenu minimum",
        "tab3": "📊 RSD/RTD & TVM",
        "tab4": "🧮 Calculatrice Sharp EL-738XT",

        # Tab 1
        "t1_title": "Capacité financière étape par étape",
        "t1_income": "Revenu brut annuel du ménage ($)",
        "t1_taxes": "Taxes mensuelles ($)",
        "t1_heating": "Chauffage mensuel ($)",
        "t1_condo": "Frais de condo mensuels ($)",
        "t1_stress": "Taux de simulation de crise (%)",
        "t1_stress_help": "Standard = Taux contractuel + 2 %",
        "t1_amort": "Amortissement (années)",
        "t1_cap_income": "Capacité via le revenu (A)",
        "t1_cap_down": "Capacité via la mise de fonds (B)",
        "t1_max_cap": "CAPACITÉ D'ACHAT MAXIMALE",
        "t1_expander": "📋 Voir le détail de la formule",
        "t1_step1": "Étape 1 : Calcul du prix d'achat maximal basé sur le revenu",
        "t1_col_variable": "Variable",
        "t1_col_gds": "Logique RSD (ABD)",
        "t1_col_tds": "Logique RTD (ATD)",
        "t1_row0": "Revenu mensuel brut",
        "t1_row1": "Ratio du service de la dette",
        "t1_row2": "Fonds disponibles",
        "t1_row3": "Taxes mensuelles",
        "t1_row4": "Chauffage mensuel",
        "t1_row5": "50 % des frais de condo",
        "t1_row6": "Autres dettes mensuelles",
        "t1_row7": "PMT hypothécaire disponible",
        "t1_selection": "<strong>Sélection :</strong> Le montant le plus bas est <strong>{pmt}</strong>. Utilisé comme PMT pour le TVM. (Ratio contraignant : <strong>{binding}</strong>)",
        "t1_calc_settings": "Paramètres de la calculatrice financière utilisés (CPT VА) :",
        "t1_periods": "périodes",
        "t1_max_mortgage": "PRÊT MAX (incl. SCHL)",
        "t1_final_result": "Résultat final de l'étape 1 :",
        "t1_formula": "(Prêt max) ÷ 1,04 + Mise de fonds =",
        "t1_warning": "⚠️ Si la cote de crédit est inférieure à 680, les prêteurs utilisent généralement 32 % RSD et 40 % RTD.",

        # Tab 2
        "t2_title": "Calcul du revenu minimum",
        "t2_subtitle": "Trouvez le salaire requis pour couvrir des coûts spécifiques à une limite RSD de 39 %.",
        "t2_pmt": "PMT hypothécaire mensuel ($)",
        "t2_pmt_help": "Entrez le PMT calculé par la Sharp arrondi à 2 décimales (ex. 1593,12)",
        "t2_taxes": "Taxes (foncières et scolaires) ($)",
        "t2_heating": "Chauffage mensuel ($)",
        "t2_condo": "Frais de condo mensuels ($)",
        "t2_housing_total": "Total des coûts mensuels de logement",
        "t2_req_salary": "Salaire annuel brut requis",
        "t2_formula_title": "Détail de la formule",
        "t2_req_monthly": "Revenu mensuel requis",
        "t2_req_annual": "Revenu annuel requis",
        "t2_sharp_note": "✓ PMT arrondi à 2 décimales pour correspondre à l'arrondi au cent de la Sharp EL-738XT",

        # Tab 3
        "t3_title": "Calculateur de ratios & solveur TVM Sharp",
        "t3_income": "Revenu annuel brut ($)",
        "t3_tvm_title": "🧮 TVM Sharp EL-738XT",
        "t3_ratio_title": "📊 Ratios d'endettement actuels",
        "t3_use_sharp": "Utiliser le PMT Sharp ({pmt}) ?",
        "t3_manual_pmt": "PMT manuel ($)",
        "t3_tax": "Taxes mensuelles ($)",
        "t3_heat": "Chauffage mensuel ($)",
        "t3_condo": "Frais de condo mensuels ($)",
        "t3_gds": "Ratio RSD",
        "t3_tds": "Ratio RTD",
        "t3_limit": "Limite",
        "t3_breakdown_title": "Détail des ratios",
        "t3_housing": "Logement",
        "t3_other_debts": "Autres dettes",
        "t3_total": "Total",
        "t3_exceeds_gds": "⚠️ DÉPASSE LA LIMITE DE 39 %",
        "t3_exceeds_tds": "⚠️ DÉPASSE LA LIMITE DE 44 %",
        "t3_within": "✅ Dans les limites",

        # Tab 4
        "t4_title": "🧮 Calculatrice hypothécaire Sharp EL-738XT",
        "t4_subtitle": "Solveur TVM complet avec tableau d'amortissement — reproduisant la logique de la calculatrice financière Sharp pour les hypothèques canadiennes.",
        "t4_screen_mode": "MODE HYPOTHÈQUE CANADIENNE",
        "t4_set_inputs": "Entrez les valeurs ci-dessous puis cliquez sur CPT",
        "t4_cpt_label": "Calculer (CPT) — Résoudre pour :",
        "t4_py_help": "ex. 12 = paiements mensuels",
        "t4_cy_help": "2 = semestriel (standard canadien)",
        "t4_iy_help": "ex. 5,5 pour 5,5 %",
        "t4_n_help": "25 ans × 12 = 300",
        "t4_py": "P/A (Paiements/Année)",
        "t4_cy": "C/A (Composé/Année)",
        "t4_iy": "I/A — Taux annuel (%)",
        "t4_n":  "N — Nombre de périodes",
        "t4_pv": "VA — Montant de l'hypothèque ($)",
        "t4_pmt": "PMT — Versement ($)",
        "t4_formula_title": "🇨🇦 Formule hypothécaire canadienne",
        "t4_pmt_card": "Versement mensuel (PMT)",
        "t4_pv_card":  "Montant de l'hypothèque (VA)",
        "t4_total_cost": "Coût total de l'hypothèque",
        "t4_total_int": "Total des intérêts payés",
        "t4_split_title": "Répartition capital / intérêts",
        "t4_principal": "Capital",
        "t4_interest": "Intérêts",
        "t4_amrt_header": "AMRT  —  PLAGE D'AMORTISSEMENT",
        "t4_amrt_title": "Analyseur de plage P1 / P2",
        "t4_amrt_subtitle": "Définissez un paiement de départ (P1) et un paiement de fin (P2) pour isoler les intérêts, le capital et le solde pour n'importe quelle plage.",
        "t4_p1": "P1 — N° du paiement de départ",
        "t4_p1_help": "Premier paiement de la plage (ex. 1 = début du prêt)",
        "t4_p2": "P2 — N° du paiement de fin",
        "t4_p2_help": "Dernier paiement de la plage (ex. 12 = fin de la 1re année)",
        "t4_amrt_results": "Résultats AMRT — Paiements {p1} à {p2} ({n} paiement{s})",
        "t4_int_paid": "Intérêts payés (INT)",
        "t4_prin_paid": "Capital remboursé (PRN)",
        "t4_bal_start": "Solde au début de P1",
        "t4_bal_end": "Solde à la fin de P2 (SOL)",
        "t4_range_breakdown": "Détail de la plage :",
        "t4_total_paid": "Total payé",
        "t4_bal_reduced": "Solde réduit de",
        "t4_sched_title": "**📅 Tableau d'amortissement** — Plage P1–P2 sélectionnée + instantanés annuels",
        "t4_highlighted": "◀ rangées surlignées",
        "t4_selected_range": "= plage P1–P2 sélectionnée",
        "t4_total_sched": "Tableau total",
        "t4_total_interest": "Total intérêts",
        "t4_periods_yrs": "périodes",
        "t4_yrs": "ans",
        "t4_no_data": "Entrez des valeurs VA et PMT valides pour générer le tableau d'amortissement.",
        "t4_period": "Période",
        "t4_payment": "Versement",
        "t4_year": "An",
        "t4_month_abbr": "Mois",
        "t4_payment_s": "paiements",
        "t4_payment_1": "paiement",
        "t4_per_period": "par période",
    }
}

# ─── LANGUAGE SELECTION (persisted in session state) ──────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "en"

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
def t(key):
    """Shorthand: get translated string for current language."""
    return LANG[st.session_state.lang][key]

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
            {label} <span style="color:#e2e8f0;">{t('t3_limit')}: {limit}%</span>
        </div>
        <div style="font-size:28px; font-weight:800; color:{color}; font-family:'DM Mono',monospace;">{pct:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)


# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"## {t('sidebar_title')}")

    # Language toggle button
    if st.button(t("language_toggle"), key="lang_btn"):
        st.session_state.lang = "fr" if st.session_state.lang == "en" else "en"
        st.rerun()

    st.markdown("---")
    section_header(t("sidebar_debts"))
    auto_loan     = st.number_input(t("sidebar_auto"),     value=400.0,  step=50.0,  key="s_auto")
    personal_loan = st.number_input(t("sidebar_personal"), value=0.0,    step=50.0,  key="s_pers")
    credit_card   = st.number_input(t("sidebar_cc"),       value=0.0,    step=25.0,  key="s_cc")
    misc_debt     = st.number_input(t("sidebar_misc"),     value=0.0,    step=25.0,  key="s_misc")
    total_other_debts = auto_loan + personal_loan + credit_card + misc_debt
    st.markdown(f"""
    <div style="background:#f8fafc; border-radius:8px; padding:8px 12px;
                font-family:'DM Mono',monospace; font-size:12px; margin:8px 0 16px;">
        {t('sidebar_total')}: <strong style="color:#ef4444;">${total_other_debts:,.2f}</strong>{t('sidebar_per_month')}
    </div>
    """, unsafe_allow_html=True)
    section_header(t("sidebar_funds"))
    down_payment = st.number_input(t("sidebar_down"), value=30000.0, step=5000.0, key="s_down")
    min_down_pct = st.slider(t("sidebar_min_pct"), 5.0, 20.0, 5.0, step=1.0, key="s_pct")


# ─── MAIN HEADER ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="display:flex; align-items:center; gap:12px; margin-bottom:4px;">
    <span style="font-size:24px;">🇨🇦</span>
    <span style="font-size:20px; font-weight:800; color:#0f172a; letter-spacing:-0.02em;">
        {t('app_title')}
    </span>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    t("tab1"), t("tab2"), t("tab3"), t("tab4")
])


# ─── TAB 1: BUYER FINANCIAL CAPACITY ─────────────────────────────────────────
with tab1:
    st.markdown(f"### {t('t1_title')}")
    cap_inc = st.number_input(t("t1_income"), value=90000.0, step=5000.0, key="cap_inc")
    m_inc = cap_inc / 12
    c1, c2 = st.columns(2)
    with c1:
        c_tax   = st.number_input(t("t1_taxes"),   value=250.0, step=25.0, key="cap_tax")
        c_heat  = st.number_input(t("t1_heating"), value=100.0, step=25.0, key="cap_heat")
        c_condo = st.number_input(t("t1_condo"),   value=0.0,   step=25.0, key="cap_condo")
    with c2:
        stress_r = st.number_input(t("t1_stress"), value=7.25, step=0.25, key="cap_stress", help=t("t1_stress_help"))
        amort    = st.number_input(t("t1_amort"),  value=25,   step=1,    key="cap_amort")

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
    with r1: metric_card(t("t1_cap_income"), f"${max_price_inc:,.2f}",  color="#3b82f6")
    with r2: metric_card(t("t1_cap_down"),   f"${max_price_down:,.2f}", color="#8b5cf6")
    with r3: metric_card(t("t1_max_cap"),    f"${final_cap:,.2f}",      color="#10b981", size=20)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander(t("t1_expander"), expanded=True):
        st.markdown(f"#### {t('t1_step1')}")
        st.markdown(f"""
        <div style="overflow-x:auto; border-radius:8px; border:1.5px solid #e2e8f0; margin:12px 0;">
        <table style="width:100%; border-collapse:collapse; font-family:'DM Sans',sans-serif;">
            <thead><tr style="background:#f8fafc; border-bottom:2px solid #e2e8f0;">
                <th style="padding:10px 12px; text-align:left; font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.06em; width:32px;"></th>
                <th style="padding:10px 12px; text-align:left; font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.06em;">{t('t1_col_variable')}</th>
                <th style="padding:10px 12px; text-align:right; font-size:11px; font-weight:700; color:#3b82f6; text-transform:uppercase; letter-spacing:0.06em;">{t('t1_col_gds')}</th>
                <th style="padding:10px 12px; text-align:right; font-size:11px; font-weight:700; color:#8b5cf6; text-transform:uppercase; letter-spacing:0.06em;">{t('t1_col_tds')}</th>
            </tr></thead>
            <tbody>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">0</td><td style="padding:9px 12px; color:#475569; font-size:13px;">{t('t1_row0')}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">${m_inc:,.2f}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">${m_inc:,.2f}</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">1</td><td style="padding:9px 12px; color:#475569; font-size:13px;">{t('t1_row1')}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">× 39%</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">× 44%</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">2</td><td style="padding:9px 12px; color:#475569; font-size:13px;">{t('t1_row2')}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">= ${m_inc*0.39:,.2f}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">= ${m_inc*0.44:,.2f}</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">3</td><td style="padding:9px 12px; color:#475569; font-size:13px;">{t('t1_row3')}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${c_tax:,.2f}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${c_tax:,.2f}</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">4</td><td style="padding:9px 12px; color:#475569; font-size:13px;">{t('t1_row4')}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${c_heat:,.2f}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${c_heat:,.2f}</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">5</td><td style="padding:9px 12px; color:#475569; font-size:13px;">{t('t1_row5')}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${0.5*c_condo:,.2f}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${0.5*c_condo:,.2f}</td></tr>
                <tr style="border-bottom:1px solid #f1f5f9;"><td style="padding:9px 12px; color:#cbd5e1; font-size:11px;">6</td><td style="padding:9px 12px; color:#475569; font-size:13px;">{t('t1_row6')}</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#94a3b8;">N/A</td><td style="padding:9px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; color:#475569;">• ${total_other_debts:,.2f}</td></tr>
                <tr style="background:#f8fafc;"><td style="padding:10px 12px; color:#cbd5e1; font-size:11px;">7</td><td style="padding:10px 12px; color:#0f172a; font-size:13px; font-weight:700;">{t('t1_row7')}</td><td style="padding:10px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; font-weight:700; color:#0f172a;">${avail_gds:,.2f}</td><td style="padding:10px 12px; text-align:right; font-family:'DM Mono',monospace; font-size:13px; font-weight:700; color:#0f172a;">${avail_tds:,.2f}</td></tr>
            </tbody>
        </table></div>
        """, unsafe_allow_html=True)
        info_banner(t("t1_selection").format(pmt=f"${final_pmt:,.2f}", binding=binding))
        st.markdown("---")
        st.markdown(f"""
        <div style="font-size:13px; font-weight:700; color:#0f172a; margin-bottom:8px;">{t('t1_calc_settings')}</div>
        <div style="display:flex; flex-wrap:wrap; gap:20px; font-family:'DM Mono',monospace; font-size:12px; color:#475569; margin-bottom:8px;">
            <span>• P/Y = 12 | C/Y = 2</span>
            <span>• n = {n_periods} {t('t1_periods')} | I/Y = {stress_r}%</span>
            <span>• {t('t1_max_mortgage')}: <strong style="color:#0f172a;">${max_loan:,.2f}</strong></span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f"""
        <div style="font-size:13px; font-weight:700; color:#0f172a; margin-bottom:6px;">{t('t1_final_result')}</div>
        <div style="font-family:'DM Mono',monospace; font-size:13px; color:#475569;">
            {t('t1_formula')} <strong style="color:#10b981; font-size:15px;">${max_price_inc:,.2f}</strong>
        </div>
        """, unsafe_allow_html=True)
        st.warning(t("t1_warning"))


# ─── TAB 2: MINIMUM INCOME CALCULATION ───────────────────────────────────────
with tab2:
    st.markdown(f"### {t('t2_title')}")
    st.markdown(f"<p style='color:#64748b; font-size:13px;'>{t('t2_subtitle')}</p>", unsafe_allow_html=True)
    m1, m2 = st.columns(2)
    with m1:
        min_pmt = st.number_input(t("t2_pmt"), value=2000.0, step=0.01, format="%.2f", key="min_pmt",
                                  help=t("t2_pmt_help"))
        min_tax = st.number_input(t("t2_taxes"), value=300.0, step=0.01, format="%.2f", key="min_tax")
    with m2:
        min_heat  = st.number_input(t("t2_heating"), value=125.0, step=0.01, format="%.2f", key="min_heat")
        min_condo = st.number_input(t("t2_condo"),   value=0.0,   step=0.01, format="%.2f", key="min_condo")

    min_pmt_sharp = round(min_pmt, 2)
    housing_total = round(min_pmt_sharp + min_tax + min_heat + 0.5 * min_condo, 2)
    req_monthly   = round(housing_total / 0.39, 2)
    req_annual    = round(req_monthly * 12, 2)

    st.markdown("---")
    r1, r2 = st.columns(2)
    with r1: metric_card(t("t2_housing_total"), f"${housing_total:,.2f}", color="#3b82f6")
    with r2: metric_card(t("t2_req_salary"),    f"${req_annual:,.2f}",    color="#f59e0b", size=20)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:white; border:1.5px solid #e2e8f0; border-radius:12px; padding:20px 22px;">
        <div style="font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:12px;">{t('t2_formula_title')}</div>
        <div style="font-family:'DM Mono',monospace; font-size:13px; color:#475569; line-height:2;">
            PMT ${min_pmt_sharp:,.2f} + {t('t2_taxes').split(' ($)')[0]} ${min_tax:,.2f} + {t('t2_heating').split(' ($)')[0]} ${min_heat:,.2f} + ½ Condo ${0.5*min_condo:,.2f}
            = <strong style="color:#0f172a;">${housing_total:,.2f}</strong> / {t('sidebar_per_month').lstrip('/')}<br>
            {t('t2_req_monthly')} = ${housing_total:,.2f} ÷ 0.39 = <strong style="color:#0f172a;">${req_monthly:,.2f}</strong><br>
            {t('t2_req_annual')} = ${req_monthly:,.2f} × 12 = <strong style="color:#f59e0b;">${req_annual:,.2f}</strong>
        </div>
        <div style="margin-top:10px; background:#f5f3ff; border:1px solid #ddd6fe; border-radius:8px;
                    padding:8px 12px; font-family:'DM Mono',monospace; font-size:11px; color:#4c1d95;">
            {t('t2_sharp_note')}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── TAB 3: GDS/TDS & TVM SOLVER ─────────────────────────────────────────────
with tab3:
    st.markdown(f"### {t('t3_title')}")
    ratio_inc_annual = st.number_input(t("t3_income"), value=90000.0, step=5000.0, key="r_inc")
    m_inc_ratio = ratio_inc_annual / 12 if ratio_inc_annual > 0 else 1
    st.markdown("---")
    r_c1, r_c2 = st.columns(2)

    with r_c1:
        st.markdown(f"<div style='font-size:13px; font-weight:700; color:#0f172a; margin-bottom:14px;'>{t('t3_tvm_title')}</div>", unsafe_allow_html=True)
        py   = st.number_input("P/Y",     value=12.0,     step=1.0,    key="sharp_py")
        cy   = st.number_input("C/Y",     value=2.0,      step=1.0,    key="sharp_cy")
        i_y  = st.number_input("I/Y (%)", value=6.0,      step=0.25,   key="sharp_iy")
        pv_y = st.number_input("PV ($)",  value=300000.0, step=5000.0, key="sharp_pv")
        r_periodic = (1 + (i_y / 100) / cy) ** (cy / py) - 1
        sharp_pmt  = abs(npf.pmt(r_periodic, 25 * py, pv_y, 0))
        metric_card("PMT", f"${sharp_pmt:,.2f}", color="#6366f1")
        st.markdown(f"""
        <div style="background:#f5f3ff; border:1px solid #ddd6fe; border-radius:8px;
                    padding:10px 14px; font-family:'DM Mono',monospace; font-size:12px; color:#4c1d95; margin-top:10px;">
            r = (1 + {i_y}% / {cy:.0f})^({cy:.0f}/{py:.0f}) − 1 = {r_periodic*100:.6f}%
        </div>
        """, unsafe_allow_html=True)

    with r_c2:
        st.markdown(f"<div style='font-size:13px; font-weight:700; color:#0f172a; margin-bottom:14px;'>{t('t3_ratio_title')}</div>", unsafe_allow_html=True)
        use_sharp  = st.checkbox(t("t3_use_sharp").format(pmt=f"${sharp_pmt:,.2f}"), value=True, key="use_sharp")
        manual_pmt = sharp_pmt
        if not use_sharp:
            manual_pmt = st.number_input(t("t3_manual_pmt"), value=1500.0, key="manual_pmt")
        active_pmt = sharp_pmt if use_sharp else manual_pmt
        r_tax   = st.number_input(t("t3_tax"),   value=250.0, step=25.0, key="r_tax")
        r_heat  = st.number_input(t("t3_heat"),  value=100.0, step=25.0, key="r_heat")
        r_condo = st.number_input(t("t3_condo"), value=0.0,   step=25.0, key="r_condo")
        total_h = active_pmt + r_tax + r_heat + 0.5 * r_condo
        total_d = total_h + total_other_debts
        gds_val = total_h / m_inc_ratio
        tds_val = total_d / m_inc_ratio
        st.markdown("---")
        rb1, rb2 = st.columns(2)
        with rb1: ratio_badge(t("t3_gds"), gds_val, 39)
        with rb2: ratio_badge(t("t3_tds"), tds_val, 44)

    st.markdown("<br>", unsafe_allow_html=True)
    gds_status = t("t3_exceeds_gds") if gds_val*100 > 39 else t("t3_within")
    tds_status = t("t3_exceeds_tds") if tds_val*100 > 44 else t("t3_within")
    st.markdown(f"""
    <div style="background:white; border:1.5px solid #e2e8f0; border-radius:12px; padding:20px 22px;">
        <div style="font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:12px;">{t('t3_breakdown_title')}</div>
        <div style="font-family:'DM Mono',monospace; font-size:12px; color:#475569; line-height:2.2;">
            PMT ${active_pmt:,.2f} + {t('t3_tax').split(' ($)')[0]} ${r_tax:,.2f} + {t('t3_heat').split(' ($)')[0]} ${r_heat:,.2f} + ½ Condo ${0.5*r_condo:,.2f} = {t('t3_housing')} <strong style="color:#0f172a;">${total_h:,.2f}</strong><br>
            {t('t3_housing')} ${total_h:,.2f} + {t('t3_other_debts')} ${total_other_debts:,.2f} = {t('t3_total')} <strong style="color:#0f172a;">${total_d:,.2f}</strong><br>
            GDS = ${total_h:,.2f} ÷ ${m_inc_ratio:,.2f} = <strong style="color:{'#ef4444' if gds_val*100 > 39 else '#10b981'};">{gds_val*100:.2f}%</strong> {gds_status}<br>
            TDS = ${total_d:,.2f} ÷ ${m_inc_ratio:,.2f} = <strong style="color:{'#ef4444' if tds_val*100 > 44 else '#10b981'};">{tds_val*100:.2f}%</strong> {tds_status}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── TAB 4: SHARP EL-738XT MORTGAGE CALCULATOR ───────────────────────────────
with tab4:
    st.markdown(f"### {t('t4_title')}")
    st.markdown(f"<p style='color:#64748b; font-size:13px;'>{t('t4_subtitle')}</p>", unsafe_allow_html=True)

    left_col, right_col = st.columns(2)

    with left_col:
        st.markdown(f"""
        <div style="background:#1e293b; border-radius:16px; padding:20px; margin-bottom:14px; box-shadow:0 8px 32px rgba(15,23,42,0.35);">
            <div style="background:#0f172a; border-radius:10px; padding:14px 18px; margin-bottom:16px; border:1px solid #334155;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#334155; letter-spacing:0.15em; margin-bottom:4px;">SHARP EL-738XT  |  {t('t4_screen_mode')}</div>
                <div style="font-family:'DM Mono',monospace; font-size:11px; color:#475569;">P/Y=12  C/Y=2  |  {t('t4_set_inputs')}</div>
            </div>
            <div style="font-size:10px; font-weight:700; color:#64748b; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:8px;">TVM</div>
        </div>
        """, unsafe_allow_html=True)

        solve_for = st.radio(t("t4_cpt_label"), ["PMT", "PV", "N", "FV"], horizontal=True, key="calc_solve")
        st.markdown("---")

        ca1, ca2 = st.columns(2)
        with ca1:
            calc_py = st.number_input(t("t4_py"), value=12.0,     step=1.0,    key="calc_py", help=t("t4_py_help"))
            calc_iy = st.number_input(t("t4_iy"), value=5.5,      step=0.05,   key="calc_iy", help=t("t4_iy_help"))
            calc_pv = st.number_input(t("t4_pv"), value=400000.0, step=5000.0, key="calc_pv", disabled=(solve_for == "PV"))
        with ca2:
            calc_cy = st.number_input(t("t4_cy"), value=2.0,    step=1.0,  key="calc_cy", help=t("t4_cy_help"))
            calc_n  = st.number_input(t("t4_n"),  value=300.0,  step=12.0, key="calc_n",  help=t("t4_n_help"), disabled=(solve_for == "N"))
            calc_pmt_input = st.number_input(t("t4_pmt"), value=2400.0, step=25.0, key="calc_pmt", disabled=(solve_for == "PMT"))

        calc_r = (1 + (calc_iy / 100) / calc_cy) ** (calc_cy / calc_py) - 1

        if solve_for == "PMT":
            result_pmt = abs(npf.pmt(calc_r, calc_n, calc_pv, 0))
            result_pv  = calc_pv; result_n = int(calc_n)
        elif solve_for == "PV":
            result_pmt = calc_pmt_input
            result_pv  = abs(npf.pv(calc_r, calc_n, -calc_pmt_input, 0)); result_n = int(calc_n)
        elif solve_for == "N":
            result_pmt = calc_pmt_input; result_pv = calc_pv
            result_n = int(abs(npf.nper(calc_r, -calc_pmt_input, calc_pv, 0))) if calc_pmt_input > 0 and calc_r > 0 else 0
        else:
            result_pmt = calc_pmt_input; result_pv = calc_pv; result_n = int(calc_n)

        if solve_for == "PMT":
            screen_val = f"${result_pmt:,.2f}"; screen_label = "CPT PMT ="
        elif solve_for == "PV":
            screen_val = f"${result_pv:,.2f}"; screen_label = "CPT PV ="
        elif solve_for == "N":
            screen_val = f"{result_n} {t('t4_periods_yrs')} ({result_n/12:.1f} {t('t4_yrs')})"; screen_label = "CPT N ="
        else:
            fv_result  = npf.fv(calc_r, result_n, -result_pmt, -result_pv)
            screen_val = f"${fv_result:,.2f}"; screen_label = "CPT FV ="

        st.markdown(f"""
        <div style="background:#0f172a; border-radius:12px; padding:18px 20px; margin:14px 0; border:1px solid #334155;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#334155; letter-spacing:0.12em; margin-bottom:6px;">
                SHARP EL-738XT  |  {screen_label}
            </div>
            <div style="font-family:'DM Mono',monospace; font-size:28px; color:#10b981; font-weight:700; letter-spacing:-0.02em;">
                {screen_val}
            </div>
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#475569; margin-top:6px;">
                r = {calc_r*100:.7f}% {t('t4_per_period')}  |  P/Y={calc_py:.0f}  C/Y={calc_cy:.0f}  I/Y={calc_iy}%  n={result_n}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background:#f5f3ff; border:1px solid #ddd6fe; border-radius:10px; padding:12px 16px;
                    font-family:'DM Mono',monospace; font-size:11px; color:#4c1d95; line-height:1.9;">
            <div style="font-weight:700; font-size:12px; margin-bottom:4px;">{t('t4_formula_title')}</div>
            r = (1 + I/Y ÷ C/Y) ^ (C/Y ÷ P/Y) − 1<br>
            r = (1 + {calc_iy}% ÷ {calc_cy:.0f}) ^ ({calc_cy:.0f} ÷ {calc_py:.0f}) − 1<br>
            <strong style="color:#6d28d9;">r = {calc_r*100:.8f}% {t('t4_per_period')}</strong>
        </div>
        """, unsafe_allow_html=True)

    with right_col:
        active_pmt_calc = round(result_pmt, 2)
        active_pv_calc  = result_pv
        active_n_calc   = result_n
        total_cost      = active_pmt_calc * active_n_calc
        total_interest  = max(0, total_cost - active_pv_calc)

        mc1, mc2 = st.columns(2)
        with mc1:
            metric_card(t("t4_pmt_card"),    f"${active_pmt_calc:,.2f}", color="#3b82f6", size=18)
            metric_card(t("t4_total_cost"),  f"${total_cost:,.2f}",      color="#f59e0b", size=16)
        with mc2:
            metric_card(t("t4_pv_card"),     f"${active_pv_calc:,.2f}",  color="#8b5cf6", size=18)
            metric_card(t("t4_total_int"),   f"${total_interest:,.2f}",   color="#ef4444", size=16)

        if active_pv_calc > 0 and total_cost > 0:
            prin_pct = min(100, (active_pv_calc / total_cost) * 100)
            int_pct  = max(0, 100 - prin_pct)
            st.markdown(f"""
            <div style="background:white; border:1.5px solid #e2e8f0; border-radius:12px; padding:16px 20px; margin:14px 0;">
                <div style="font-size:11px; font-weight:700; color:#64748b; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;">{t('t4_split_title')}</div>
                <div style="height:16px; background:#f1f5f9; border-radius:99px; overflow:hidden; margin-bottom:8px;">
                    <div style="height:100%; width:{prin_pct:.1f}%; background:linear-gradient(90deg,#3b82f6,#6366f1); border-radius:99px;"></div>
                </div>
                <div style="display:flex; justify-content:space-between; font-family:'DM Mono',monospace; font-size:12px;">
                    <span style="color:#3b82f6; font-weight:600;">{t('t4_principal')} {prin_pct:.1f}% = ${active_pv_calc:,.2f}</span>
                    <span style="color:#ef4444; font-weight:600;">{t('t4_interest')} {int_pct:.1f}% = ${total_interest:,.2f}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ── P1 / P2 AMRT ──
        st.markdown(f"""
        <div style="background:#1e293b; border-radius:12px; padding:16px 18px; margin:14px 0 10px;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#475569; letter-spacing:0.15em; margin-bottom:6px;">SHARP EL-738XT  |  {t('t4_amrt_header')}</div>
            <div style="font-size:13px; font-weight:700; color:#e2e8f0; margin-bottom:2px;">{t('t4_amrt_title')}</div>
            <div style="font-size:11px; color:#64748b;">{t('t4_amrt_subtitle')}</div>
        </div>
        """, unsafe_allow_html=True)

        p_col1, p_col2 = st.columns(2)
        with p_col1:
            p1 = st.number_input(t("t4_p1"), min_value=1, max_value=max(1, active_n_calc),
                                 value=1, step=1, key="amrt_p1", help=t("t4_p1_help"))
        with p_col2:
            p2 = st.number_input(t("t4_p2"), min_value=1, max_value=max(1, active_n_calc),
                                 value=min(12, max(1, active_n_calc)), step=1, key="amrt_p2", help=t("t4_p2_help"))

        p1 = int(max(1, p1))
        p2 = int(max(p1, p2))

        if active_pmt_calc > 0 and active_pv_calc > 0:
            sharp_rounded_pmt = round(active_pmt_calc, 2)
            bal = active_pv_calc
            sched = []
            for i in range(1, min(active_n_calc, 360) + 1):
                int_i  = round(bal * calc_r, 2)
                prin_i = round(min(sharp_rounded_pmt - int_i, bal), 2)
                bal    = round(max(0.0, bal - prin_i), 2)
                sched.append({"period": i, "interest": int_i, "principal": prin_i, "balance": bal})
                if bal < 0.01:
                    break

            p2 = min(p2, len(sched))
            p1 = min(p1, p2)

            bal_before = sched[p1 - 2]["balance"] if p1 > 1 else active_pv_calc
            bal_after  = sched[p2 - 1]["balance"]
            range_int  = sum(r["interest"]  for r in sched[p1 - 1 : p2])
            range_prin = sum(r["principal"] for r in sched[p1 - 1 : p2])
            num_pmts   = p2 - p1 + 1
            pmt_word   = t("t4_payment_1") if num_pmts == 1 else t("t4_payment_s")

            st.markdown(f"""
            <div style="background:white; border:1.5px solid #e2e8f0; border-radius:12px; padding:18px 20px; margin:10px 0 14px;">
                <div style="font-size:11px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:14px;">
                    {t('t4_amrt_results').format(p1=p1, p2=p2, n=num_pmts, s='')}  ({num_pmts} {pmt_word})
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:14px;">
                    <div style="background:#eff6ff; border:1.5px solid #bfdbfe; border-radius:10px; padding:14px 16px; text-align:center;">
                        <div style="font-size:10px; font-weight:700; color:#3b82f6; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:6px;">{t('t4_int_paid')}</div>
                        <div style="font-size:22px; font-weight:800; color:#1d4ed8; font-family:'DM Mono',monospace;">${range_int:,.2f}</div>
                    </div>
                    <div style="background:#f0fdf4; border:1.5px solid #bbf7d0; border-radius:10px; padding:14px 16px; text-align:center;">
                        <div style="font-size:10px; font-weight:700; color:#10b981; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:6px;">{t('t4_prin_paid')}</div>
                        <div style="font-size:22px; font-weight:800; color:#065f46; font-family:'DM Mono',monospace;">${range_prin:,.2f}</div>
                    </div>
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:14px;">
                    <div style="background:#f8fafc; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 16px; text-align:center;">
                        <div style="font-size:10px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:6px;">{t('t4_bal_start')}</div>
                        <div style="font-size:16px; font-weight:700; color:#475569; font-family:'DM Mono',monospace;">${bal_before:,.2f}</div>
                    </div>
                    <div style="background:#f8fafc; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 16px; text-align:center;">
                        <div style="font-size:10px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:6px;">{t('t4_bal_end')}</div>
                        <div style="font-size:16px; font-weight:700; color:#0f172a; font-family:'DM Mono',monospace;">${bal_after:,.2f}</div>
                    </div>
                </div>
                <div style="background:#f8fafc; border-radius:8px; padding:10px 14px; font-family:'DM Mono',monospace; font-size:11px; color:#64748b; line-height:1.8;">
                    <strong style="color:#0f172a;">{t('t4_range_breakdown')}</strong>
                    &nbsp; INT ${range_int:,.2f} + PRN ${range_prin:,.2f} = {t('t4_total_paid')} ${range_int + range_prin:,.2f}
                    &nbsp;|&nbsp; {t('t4_bal_reduced')} ${bal_before - bal_after:,.2f}
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(t("t4_sched_title"))

            rows = []
            for r in sched:
                i = r["period"]
                in_range  = p1 <= i <= p2
                is_annual = (i % 12 == 0)
                if in_range or is_annual or i <= 3:
                    label = f"{t('t4_year')} {i // 12}" if is_annual else f"{t('t4_month_abbr')} {i}"
                    rows.append({"period": i, "label": label, "payment": active_pmt_calc,
                                 "interest": r["interest"], "principal": r["principal"],
                                 "balance": r["balance"], "in_range": in_range, "is_annual": is_annual})

            col_headers = [t("t4_period"), t("t4_payment"), t("t4_interest"), t("t4_principal"), "Balance"]
            header_html = "".join([
                f'<th style="padding:8px 10px; text-align:{"left" if h==t("t4_period") else "right"}; font-size:10px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.06em; border-bottom:2px solid #e2e8f0; background:#f8fafc; position:sticky; top:0;">{h}</th>'
                for h in col_headers
            ])

            rows_html = ""
            for row in rows:
                in_r  = row["in_range"]
                is_yr = row["is_annual"]
                bg    = "#fefce8" if in_r else ("#f8fafc" if is_yr else "white")
                fw    = "700" if in_r else ("600" if is_yr else "400")
                bl    = "border-left:3px solid #f59e0b;" if in_r else ""
                rows_html += f'<tr style="border-bottom:1px solid #f1f5f9; background:{bg}; {bl}">'
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
                <span style="background:#fefce8; border:1px solid #fde68a; border-radius:4px; padding:2px 8px; color:#92400e; font-weight:700;">{t('t4_highlighted')}</span>
                {t('t4_selected_range')} &nbsp;|&nbsp; {t('t4_total_sched')}: <strong style="color:#0f172a;">{len(sched)} {t('t4_periods_yrs')} ({len(sched)/12:.1f} {t('t4_yrs')})</strong>
                &nbsp;|&nbsp; {t('t4_total_interest')}: <strong style="color:#ef4444;">${sum(r["interest"] for r in sched):,.2f}</strong>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info(t("t4_no_data"))

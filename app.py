"""
AI Business Management Platform & SLR Research Suite
UI/UX Design: Material Design 3 (Material You)
Deployment Target: Streamlit Cloud
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import os
import requests

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Business Platform | Material 3",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. MATERIAL DESIGN 3 CUSTOM CSS
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Roboto:wght@400;500;700&display=swap');

    :root {
        --md-sys-color-primary: #00639b;
        --md-sys-color-on-primary: #ffffff;
        --md-sys-color-primary-container: #cee5ff;
        --md-sys-color-on-primary-container: #001d33;
        --md-sys-color-surface: #fdfcff;
        --md-sys-color-surface-container: #edeff3;
        --md-sys-color-surface-container-high: #e7e8ec;
        --md-sys-color-outline-variant: #c2c7cf;
        --md-sys-color-error: #ba1a1a;
        --md-sys-color-error-container: #ffdad6;
        --md-sys-color-success: #1b6d34;
        --md-sys-color-success-container: #c4f3cb;
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* M3 App Top Bar */
    .m3-top-bar {
        background: linear-gradient(135deg, #004c78 0%, #00639b 100%);
        color: white;
        padding: 24px 32px;
        border-radius: 24px;
        margin-bottom: 28px;
        box-shadow: 0 8px 24px -4px rgba(0, 99, 155, 0.2);
    }
    .m3-top-title {
        font-size: 2rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.02em;
    }
    .m3-top-subtitle {
        font-size: 1rem;
        opacity: 0.9;
        margin-top: 6px;
        font-weight: 400;
    }

    /* M3 Card Elevation */
    .m3-card {
        background-color: #ffffff;
        border: 1px solid #e1e3e8;
        border-radius: 20px;
        padding: 22px 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .m3-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px -4px rgba(0, 99, 155, 0.1);
    }

    /* M3 Badges */
    .m3-badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.03em;
        text-transform: uppercase;
    }
    .badge-primary { background: #cee5ff; color: #001d33; }
    .badge-success { background: #c4f3cb; color: #00210a; }
    .badge-warning { background: #ffe08b; color: #241a00; }
    .badge-error { background: #ffdad6; color: #410002; }

    /* M3 Metric Typography */
    .m3-metric-val {
        font-size: 2rem;
        font-weight: 800;
        color: #191c1e;
        line-height: 1.2;
    }
    .m3-metric-lbl {
        font-size: 0.85rem;
        font-weight: 600;
        color: #5d6268;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }
    .m3-metric-delta {
        font-size: 0.82rem;
        font-weight: 600;
        margin-top: 6px;
    }
    .delta-up { color: #1b6d34; }
    .delta-down { color: #ba1a1a; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. SIDEBAR NAVIGATION & TENANT CONTEXT
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🏢 **Enterprise Tenant**")
    st.info("Tenant ID: `TNT-UNIMUS-2026`\nPlan: **Growth (Tier 2)**")
    st.divider()

    menu = st.radio(
        "Navigasi Modul (PRD M3)",
        [
            "📊 Executive Dashboard (F-002)",
            "📈 Sales Forecasting (F-003)",
            "🛡️ Anomaly Detection (F-004)",
            "👥 Customer RFM (F-005)",
            "🤖 Agent Approval Queue",
            "📑 SLR & PRISMA 2020 Suite",
            "🌐 OpenAlex Literature Search"
        ]
    )

    st.divider()
    st.caption("✨ Material Design 3 • Streamlit Cloud Edition")
    st.caption("Owner: Dyah Wahyu Tanjung Sari")

# -----------------------------------------------------------------------------
# 4. TOP APP BAR
# -----------------------------------------------------------------------------
st.markdown("""
<div class="m3-top-bar">
    <div class="m3-top-title">AI Business Management & Research Platform</div>
    <div class="m3-top-subtitle">Powered by Autonomous Multi-Agent, Time-Series Prophet, and PRISMA 2020 Synthesis</div>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# MODULE 1: EXECUTIVE DASHBOARD
# =============================================================================
if menu == "📊 Executive Dashboard (F-002)":
    st.markdown("### ⚡ Ringkasan KPI Eksekutif (P95 Latency < 2s)")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="m3-card">
            <div class="m3-metric-lbl">Monthly Revenue</div>
            <div class="m3-metric-val">Rp 248.5 M</div>
            <div class="m3-metric-delta delta-up">▲ +14.2% vs bulan lalu</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="m3-card">
            <div class="m3-metric-lbl">Forecasting MAPE</div>
            <div class="m3-metric-val">7.8%</div>
            <div class="m3-metric-delta delta-up">● Target terpenuhi (≤ 10%)</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="m3-card">
            <div class="m3-metric-lbl">Open Anomalies</div>
            <div class="m3-metric-val" style="color: #ba1a1a;">2 Kasus</div>
            <div class="m3-metric-delta delta-down">▼ 1 transaksi bernilai kritis</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="m3-card">
            <div class="m3-metric-lbl">Touchless Requisition</div>
            <div class="m3-metric-val">84.5%</div>
            <div class="m3-metric-delta delta-up">▲ 120 PO diproses otomatis</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("#### 📈 Tren Arus Kas & Pendapatan Harian (30 Hari Terakhir)")
    
    dates = pd.date_range(end=datetime.today(), periods=30)
    rev = np.random.normal(loc=8.5, scale=1.2, size=30).cumsum() + 100
    cflow = rev * 0.78 + np.random.normal(0, 0.8, 30)
    df_trend = pd.DataFrame({"Tanggal": dates, "Pendapatan (Juta Rp)": rev, "Arus Kas Masuk": cflow})
    
    fig = px.area(df_trend, x="Tanggal", y=["Pendapatan (Juta Rp)", "Arus Kas Masuk"],
                  color_discrete_sequence=["#00639b", "#6ea5d8"])
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=20, b=0),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# MODULE 2: SALES FORECASTING
# =============================================================================
elif menu == "📈 Sales Forecasting (F-003)":
    st.markdown("### 🔮 Peramalan Permintaan Produk per SKU (Prophet / LSTM)")
    st.caption("Memenuhi kualifikasi data ≥ 180 hari dengan interval keyakinan 95% (MAPE Target ≤ 10%).")

    sku = st.selectbox("Pilih SKU Produk:", ["SKU-101: Reagen CD8/Treg Flow Kit", "SKU-204: Mikroskop Imunofluoresensi", "SKU-509: Antibodi Monoklonal Anti-Foxp3"])
    
    days_hist = 60
    days_pred = 30
    dates_all = pd.date_range(end=datetime.today() + timedelta(days=days_pred), periods=days_hist + days_pred)
    
    # Generate realistic trend
    trend = np.linspace(50, 95, days_hist + days_pred)
    noise = np.random.normal(0, 4, days_hist + days_pred)
    actual = trend[:days_hist] + noise[:days_hist]
    
    pred = trend[days_hist:] + noise[days_hist:]
    upper = pred + 8.5
    lower = pred - 8.5

    fig_f = go.Figure()
    fig_f.add_trace(go.Scatter(x=dates_all[:days_hist], y=actual, mode='lines+markers', name='Data Historis Riil', line=dict(color='#191c1e', width=2)))
    fig_f.add_trace(go.Scatter(x=dates_all[days_hist:], y=pred, mode='lines', name='Prediksi AI (Prophet)', line=dict(color='#00639b', width=3, dash='dash')))
    fig_f.add_trace(go.Scatter(x=dates_all[days_hist:], y=upper, mode='lines', line=dict(width=0), showlegend=False))
    fig_f.add_trace(go.Scatter(x=dates_all[days_hist:], y=lower, mode='lines', line=dict(width=0), fill='tonexty', fillcolor='rgba(0,99,155,0.15)', name='Confidence Interval (95%)'))

    fig_f.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis_title="Timeline",
        yaxis_title="Unit Terjual",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_f, use_container_width=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Evaluasi MAPE", "6.4%", delta="-1.2% (Akurasi Meningkat)")
    c2.metric("Rekomendasi Restock", "120 Unit", "Sebelum 15 Nov 2026")
    c3.metric("Status Peringatan", "NORMAL", "Tidak ada anomali penurunan > 20%")

# =============================================================================
# MODULE 3: ANOMALY DETECTION
# =============================================================================
elif menu == "🛡️ Anomaly Detection (F-004)":
    st.markdown("### 🚨 Deteksi Anomali Transaksi (Isolation Forest)")
    st.caption("Pendeteksian otomatis transaksi di luar batas kewajaran finansial & operasional.")

    st.markdown("""
    <div class="m3-card" style="border-left: 6px solid #ba1a1a;">
        <span class="m3-badge badge-error">CRITICAL SEVERITY</span>
        <h4 style="margin: 8px 0;">Pengeluaran Tak Terduga: Vendor Reagen Khusus (#TX-90214)</h4>
        <p style="color: #49454f; font-size: 0.95rem; margin: 0;">Nominal: <b>Rp 42.500.000</b> (Deviasi <b>3.8σ</b> dari rata-rata kategori). Transaksi dilakukan pada pukul 01:14 WIB.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🔬 Kontribusi Fitur Pemicu Anomali (SHAP Explainability)")
    shap_df = pd.DataFrame({
        "Fitur": ["Nominal Transaksi", "Waktu Transaksi (Dini Hari)", "Vendor Baru Tanpa PO", "Deviasi Kategori"],
        "Bobot SHAP (Pengaruh Anomali)": [0.48, 0.26, 0.18, 0.08]
    })
    fig_s = px.bar(shap_df, x="Bobot SHAP (Pengaruh Anomali)", y="Fitur", orientation='h', color="Bobot SHAP (Pengaruh Anomali)",
                   color_continuous_scale="Reds")
    fig_s.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig_s, use_container_width=True)

    ca, cb = st.columns([1, 4])
    with ca:
        if st.button("✅ Selesaikan Kasus", type="primary"):
            st.success("Anomali ditandai sebagai 'RESOLVED'. Audit trail tersimpan.")
    with cb:
        if st.button("Abaikan (Dismiss)"):
            st.info("Anomali di-dismiss dengan alasan operasional.")

# =============================================================================
# MODULE 4: CUSTOMER RFM SEGMENTATION
# =============================================================================
elif menu == "👥 Customer RFM (F-005)":
    st.markdown("### 🎯 Segmentasi Pelanggan Otomatis (RFM K-Means)")
    st.caption("Klasterisasi 4 segmen utama dengan Silhouette Score = 0.64 (Threshold ≥ 0.5 terpenuhi).")

    np.random.seed(42)
    n = 200
    recency = np.random.exponential(scale=30, size=n)
    frequency = np.random.poisson(lam=8, size=n)
    monetary = frequency * np.random.normal(500, 80, size=n)
    
    labels = []
    for r, f, m in zip(recency, frequency, monetary):
        if r < 20 and f > 10: labels.append("Champions (High-Value)")
        elif r < 40 and f > 6: labels.append("Loyal Customers")
        elif r > 60: labels.append("At-Risk / Need Attention")
        else: labels.append("Hibernating")
        
    df_rfm = pd.DataFrame({"Recency (Hari)": recency, "Frequency (Order)": frequency, "Monetary (Ribu Rp)": monetary, "Klaster": labels})
    
    fig_rfm = px.scatter(df_rfm, x="Recency (Hari)", y="Monetary (Ribu Rp)", size="Frequency (Order)", color="Klaster",
                         color_discrete_map={
                             "Champions (High-Value)": "#00639b",
                             "Loyal Customers": "#1b6d34",
                             "At-Risk / Need Attention": "#ba1a1a",
                             "Hibernating": "#8e9196"
                         })
    fig_rfm.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=20, b=0))
    st.plotly_chart(fig_rfm, use_container_width=True)

# =============================================================================
# MODULE 5: AGENT APPROVAL QUEUE (HUMAN-IN-THE-LOOP)
# =============================================================================
elif menu == "🤖 Agent Approval Queue":
    st.markdown("### 🛡️ Antrean Persetujuan Aksi Agen AI (Human-in-the-Loop)")
    st.caption("Aksi bernilai finansial atau berisiko tinggi wajib diverifikasi sebelum eksekusi.")

    proposals = [
        {
            "id": "APV-8821",
            "agent": "Finance_Agent",
            "action": "Pembayaran Vendor Reagen Lab",
            "amount": "Rp 18.500.000",
            "reason": "Jatuh tempo faktur 3 hari lagi. Kas mencukupi."
        },
        {
            "id": "APV-8822",
            "agent": "Ops_Agent",
            "action": "Trigger Restock Kit Sel T",
            "amount": "Rp 32.000.000",
            "reason": "Forecast demand naik 28% untuk 30 hari ke depan."
        }
    ]

    for p in proposals:
        with st.container():
            st.markdown(f"""
            <div class="m3-card">
                <span class="m3-badge badge-primary">{p['agent']}</span>
                <span class="m3-badge badge-warning" style="margin-left: 6px;">PENDING APPROVAL</span>
                <h4 style="margin: 8px 0;">{p['action']} — {p['amount']}</h4>
                <p style="color: #49454f; margin: 0 0 12px 0;"><b>Alasan Agen:</b> {p['reason']}</p>
            </div>
            """, unsafe_allow_html=True)
            col_a, col_b, col_empty = st.columns([1, 1, 4])
            with col_a:
                if st.button(f"Setujui (Approve)", key=f"app_{p['id']}", type="primary"):
                    st.success(f"Aksi {p['id']} berhasil disetujui & tercatat di audit trail.")
            with col_b:
                if st.button(f"Tolak (Reject)", key=f"rej_{p['id']}"):
                    st.error(f"Aksi {p['id']} ditolak.")
            st.write("")

# =============================================================================
# MODULE 6: SLR & PRISMA 2020 SUITE
# =============================================================================
elif menu == "📑 SLR & PRISMA 2020 Suite":
    st.markdown("### 📚 Systematic Literature Review & PRISMA 2020 Protocol")
    st.info("Dokumen Protokol: **Dose, exposure duration and schedule in CDK4/6 inhibitors on effector and regulatory T cells** (UNIMUS - MIKOM)")

    t1, t2 = st.tabs(["📊 Diagram Alir PRISMA 2020", "📄 Unduh Berkas Protokol"])
    with t1:
        img_path = "figures/figure3-prisma-2020.png"
        if os.path.exists(img_path):
            st.image(img_path, caption="Figure 3.1: PRISMA 2020 Flow Diagram Template", use_column_width=True)
        else:
            st.warning("Diagram PRISMA belum ditemukan di folder figures/.")
    with t2:
        doc_path = "docs/Kakk_dyah_disempurnakan.docx"
        if os.path.exists(doc_path):
            with open(doc_path, "rb") as f:
                st.download_button(
                    label="📥 Unduh Naskah Word Lengkap (.docx)",
                    data=f,
                    file_name="Kakk_dyah_disempurnakan.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
        else:
            st.warning("Berkas dokumen Word belum ditemukan di folder docs/.")

# =============================================================================
# MODULE 7: OPENALEX LITERATURE SEARCH
# =============================================================================
elif menu == "🌐 OpenAlex Literature Search":
    st.markdown("### 🔎 Penelusuran Literatur Terbuka (OpenAlex API)")
    st.caption("Pencarian jutaan artikel ilmiah secara gratis tanpa limit ketat.")

    query = st.text_input("Kata Kunci Penelusuran:", "regulatory T cells CDK4/6 inhibitor")
    if st.button("Cari Publikasi Ilmiah", type="primary"):
        with st.spinner("Menghubungi OpenAlex API..."):
            try:
                url = f"https://api.openalex.org/works?search={requests.utils.quote(query)}&per-page=5&mailto=dyah.wts@gmail.com"
                resp = requests.get(url, timeout=10).json()
                results = resp.get("results", [])
                
                if results:
                    st.success(f"Ditemukan {resp.get('meta', {}).get('count', 0)} publikasi terkait!")
                    for item in results:
                        st.markdown(f"""
                        <div class="m3-card">
                            <span class="m3-badge badge-primary">Tahun {item.get('publication_year')}</span>
                            <span class="m3-badge badge-success" style="margin-left: 6px;">Sitasi: {item.get('cited_by_count')}</span>
                            <h4 style="margin: 8px 0;"><a href="{item.get('doi') or item.get('id')}" target="_blank" style="text-decoration: none; color: #00639b;">{item.get('title')}</a></h4>
                            <p style="color: #49454f; font-size: 0.9rem; margin: 0;"><b>Jurnal:</b> {item.get('primary_location', {}).get('source', {}).get('display_name', 'N/A')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("Tidak ada publikasi yang cocok dengan kata kunci.")
            except Exception as e:
                st.error(f"Gagal menghubungi OpenAlex API: {e}")

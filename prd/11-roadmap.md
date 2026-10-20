# 11. Milestones & Timeline

Roadmap 12 bulan dibagi menjadi 4 kuartal. Setiap milestone memiliki deliverable yang terukur dan kriteria sukses yang jelas.

### Q1 (Bulan 1–3): Fondasi & MVP

| Milestone | Deliverable | Kriteria Sukses | Dependensi |
|:---|:---|:---|:---|
| **M1.1: Setup Infrastruktur** | Docker Compose (FastAPI + Postgres + Qdrant + Redis + MinIO) berjalan lokal | `docker compose up` sukses; semua service healthy; health check endpoint aktif | Vendor repo sudah di-clone |
| **M1.2: Upload & Validasi Data (F-001)** | Endpoint `POST /upload` + parser CSV/Excel | File ≤50MB berhasil diunggah; kolom terdeteksi otomatis; error handling jelas | M1.1 |
| **M1.3: Dashboard KPI (F-002)** | Halaman dashboard dengan 4 KPI | Load ≤2 detik (p95); data dari Postgres; responsive di desktop & tablet | M1.1 |
| **M1.4: Sales Forecasting (F-003)** | Model Prophet/LSTM + endpoint prediksi | MAPE ≤10% pada data uji Enterprise Digital Twin; confidence interval ditampilkan | M1.2, dataset Kaggle |
| **M1.5: Anomaly Detection (F-004)** | Model Isolation Forest + notifikasi | Precision ≥0.8 pada data uji; alert muncul di dashboard | M1.2, dataset Kaggle |
| **M1.6: 10 Beta User** | Onboarding 10 pengguna beta | Feedback form terisi; NPS awal ≥30; minimal 3 bug kritis diperbaiki | M1.4, M1.5 |

**Risiko Q1**: Data pengguna belum tersedia → gunakan **Enterprise Digital Twin** (Kaggle) sebagai data uji.

### Q2 (Bulan 4–6): Growth & Monetisasi

| Milestone | Deliverable | Kriteria Sukses | Dependensi |
|:---|:---|:---|:---|
| **M2.1: Customer Segmentation (F-005)** | Model K-Means/RFM + UI segmentasi | Silhouette Score ≥0.5; 3–7 cluster dengan label | M1.2 |
| **M2.2: Laporan Mingguan (F-006)** | Generator PDF/slide + email scheduler | Laporan berisi KPI, trend, anomaly; terkirim otomatis Senin 08:00 | M1.3 |
| **M2.3: Chat with Data (F-007)** | RAG pipeline (Qdrant + LLM) | Akurasi ≥85% pada pertanyaan uji; respons ≤5 detik | M1.1, ODE dataset untuk intent |
| **M2.4: Integrasi Intent Routing** | Classifier intent (ODE dataset) | Akurasi ≥85% pada test set; routing ke modul yang tepat | ODE dataset |
| **M2.5: 100 Paying User** | Monetisasi (subscription) | MRR ≥$10K; churn ≤5%/bulan; conversion rate ≥5% dari beta | M2.1–M2.4 |

**Risiko Q2**: Biaya LLM membengkak → terapkan caching, small model untuk intent, self-host Llama untuk report.

### Q3 (Bulan 7–9): Scale & Enterprise

| Milestone | Deliverable | Kriteria Sukses | Dependensi |
|:---|:---|:---|:---|
| **M3.1: Multi-tenant & RBAC** | Isolasi data per tenant + role (Owner/Admin/Analyst/Viewer) | Tidak ada kebocoran data antar tenant; audit log aktif | M2.5 |
| **M3.2: Integrasi API Eksternal** | Konektor ke OpenAlex (via `oalex`) dan Semantic Scholar (MCP) | Fetch data berhasil; rate limit terkelola | API key tersedia |
| **M3.3: Mobile App (read-only)** | React Native app untuk dashboard | Load ≤3 detik; KPI utama tampil; notifikasi push | M2.1–M2.3 |
| **M3.4: 500 User** | Growth & retention | DAU/MAU ≥40%; NPS ≥50 | M3.1–M3.3 |

**Risiko Q3**: Kompleksitas multi-tenant → gunakan Row-Level Security di Postgres; uji dengan data sintetis multi-company.

### Q4 (Bulan 10–12): Expansion & AI Copilot

| Milestone | Deliverable | Kriteria Sukses | Dependensi |
|:---|:---|:---|:---|
| **M4.1: Agentic AI Copilot** | Multi-agent (CEO, Finance, Ops) dengan tool calling | Agent dapat memanggil tool (check_balance, request_payment) dengan approval queue | `agent-company-ai` sebagai referensi |
| **M4.2: What-if Simulator** | Simulasi skenario (harga, stok, diskon) | User dapat melihat dampak perubahan parameter terhadap KPI | M2.1–M2.3 |
| **M4.3: Enterprise Tier** | SLA 99.9%, SSO, dedicated support | Kontrak enterprise pertama | M3.1 |
| **M4.4: 2000 User, MRR $50K** | Skala & monetisasi | MRR ≥$50K; churn ≤3%/bulan | M4.1–M4.3 |

**Risiko Q4**: Agentic AI salah ambil keputusan → human-in-the-loop wajib untuk aksi finansial.

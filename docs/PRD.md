# Product Requirements Document (PRD)
## AI Business Management Platform

**Versi**: 0.1 (Draft)  
**Tanggal**: 2026-10-20  
**Pemilik**: Dyah Wahyu Tanjung Sari  
**Kategori Solusi**: AI Agent / Business Intelligence  

---

## 1. Executive Summary

Platform Manajemen Bisnis Berbasis AI ini dirancang untuk membantu pemilik usaha dan analis mengambil keputusan berbasis data tanpa memerlukan keahlian teknis mendalam. Produk ini mengintegrasikan data operasional (penjualan, CRM, keuangan) ke dalam satu dasbor yang dilengkapi dengan **agen AI** untuk melakukan peramalan permintaan, segmentasi pelanggan otomatis, dan pembuatan laporan mingguan.

**Nilai Bisnis Utama**:
- **Efisiensi**: Mengurangi waktu analisis manual dari 12 jam/minggu menjadi di bawah 3 jam/minggu melalui otomatisasi laporan dan insight.
- **Akurasi**: Meningkatkan akurasi peramalan penjualan (target MAPE ≤ 10%) dengan memanfaatkan data historis yang tersedia.
- **Skalabilitas**: Memungkinkan pemilik usaha untuk "mempekerjakan" agen AI dengan peran spesifik (CEO, CTO, Finance) yang dapat membantu pengambilan keputusan strategis tanpa biaya rekrutmen.

**Tujuan Produk (OKR Ringkas)**:
- **O1**: Mencapai 100 pengguna aktif berbayar dalam 6 bulan pertama.
- **O2**: Mencapai tingkat penerimaan rekomendasi AI (acceptance rate) ≥ 70%.
- **O3**: Menjaga waktu muat dasbor di bawah 2 detik (p95).


---

## 4. User Personas

Persona berikut diambil langsung dari label `persona` pada dataset **ODE Enterprise Use Cases** (15.000 use case berlabel), sehingga mencerminkan peran nyata dalam operasi bisnis, bukan asumsi.

### Persona 1: Buyer (Primary — Pengadaan)
- **Sumber Data**: ODE dataset, persona `Buyer`
- **Tugas Utama**: Membuat requisition, membandingkan vendor, memproses purchase order.
- **Pain Point**: Proses pengadaan manual memakan waktu; tidak ada visibilitas stok vs kebutuhan.
- **Fitur AI yang Dibutuhkan**: Prediksi kebutuhan stok (Sales Forecasting), rekomendasi vendor, deteksi anomali harga.
- **Metrik Sukses**: Touchless Rate (persentase requisition tanpa intervensi manual).

### Persona 2: Finance Manager (Primary — Keuangan)
- **Sumber Data**: ODE dataset, persona `Finance Manager`
- **Tugas Utama**: Menutup buku bulanan, analisis arus kas, approval pembayaran.
- **Pain Point**: Rekonsiliasi manual antar sistem; laporan keuangan terlambat.
- **Fitur AI yang Dibutuhkan**: Deteksi anomali transaksi, laporan keuangan otomatis, peramalan arus kas.
- **Metrik Sukses**: Waktu close bulanan; akurasi deteksi anomali.

### Persona 3: Operations (Secondary — Operasional)
- **Sumber Data**: ODE dataset, persona `Operations`
- **Tugas Utama**: Manajemen inventori, penjadwalan, pemantauan SLA.
- **Pain Point**: Tidak ada peringatan dini saat stok menipis atau SLA berisiko.
- **Fitur AI yang Dibutuhkan**: Anomaly detection (stok, SLA), segmentasi pelanggan untuk prioritas.
- **Metrik Sukses**: SLA breach rate; stockout frequency.

### Persona 4: Executive (Secondary — Pengambil Keputusan)
- **Sumber Data**: ODE dataset, persona `Executive`
- **Tugas Utama**: Meninjau KPI, mengambil keputusan strategis (ekspansi, investasi).
- **Pain Point**: Laporan dari tim datang terlambat dan tidak konsisten.
- **Fitur AI yang Dibutuhkan**: Dashboard KPI real-time, ringkasan laporan mingguan otomatis, "chat with data" untuk pertanyaan ad-hoc.
- **Metrik Sukses**: Waktu dari data ke insight (time-to-insight); frekuensi penggunaan dashboard.

> **Catatan untuk Persona**: Dataset ODE menyediakan 12 persona (Buyer, Approver, Auditor, Engineer, Executive, Finance Manager, IT Admin, Operations, Support Agent, Vendor, System, AP Clerk). PRD ini memilih 4 persona paling relevan untuk MVP. Persona lain dapat ditambahkan di Fase 2.


---

## 6. Functional Requirements

Requirement dikelompokkan berdasarkan prioritas (P0 = Must-have, P1 = Should-have). Setiap requirement memiliki ID, user story, dan acceptance criteria yang dapat diuji.

### 6.1. P0 — Must-Have (MVP, Bulan 1–3)

| ID | Fitur | User Story | Acceptance Criteria | Persona Terkait |
|:---|:---|:---|:---|:---|
| **F-001** | Upload & Validasi Data | Sebagai Buyer, saya ingin mengunggah CSV/Excel data transaksi agar sistem dapat menganalisisnya. | File CSV/Excel ≤50MB berhasil diunggah; sistem mendeteksi kolom otomatis; error ditampilkan jika format tidak sesuai. | Buyer, Finance Manager |
| **F-002** | Dashboard KPI Real-time | Sebagai Executive, saya ingin melihat KPI (penjualan, stok, arus kas) dalam satu layar agar cepat menilai kondisi bisnis. | Dashboard memuat ≤2 detik (p95); menampilkan minimal 4 KPI; data diperbarui harian. | Executive, Operations |
| **F-003** | Sales Forecasting per SKU | Sebagai Buyer, saya ingin melihat prediksi penjualan 30 hari ke depan per SKU agar dapat merestock tepat waktu. | MAPE ≤10% untuk SKU dengan ≥6 bulan data; confidence interval ditampilkan; alert jika forecast turun >20%. | Buyer, Operations |
| **F-004** | Anomaly Detection (Transaksi) | Sebagai Finance Manager, saya ingin mendapat peringatan otomatis jika ada transaksi tidak wajar agar dapat mencegah fraud/error. | Precision ≥0.8 pada data uji; notifikasi muncul di dashboard; dapat di-dismiss dengan alasan. | Finance Manager |

### 6.2. P1 — Should-Have (Fase 2, Bulan 4–6)

| ID | Fitur | User Story | Acceptance Criteria | Persona Terkait |
|:---|:---|:---|:---|:---|
| **F-005** | Customer Segmentation (RFM) | Sebagai Operations, saya ingin segmentasi pelanggan otomatis agar dapat memprioritaskan layanan. | Menghasilkan 3–7 cluster; setiap cluster memiliki label dan rekomendasi action; Silhouette Score ≥0.5. | Operations, Executive |
| **F-006** | Laporan Mingguan Otomatis | Sebagai Executive, saya ingin laporan PDF/slide yang di-generate otomatis setiap Senin agar tidak perlu membuat manual. | Laporan berisi KPI summary, trend, anomaly, rekomendasi; dikirim via email; dapat diedit templatenya. | Executive |
| **F-007** | Chat with Data (RAG) | Sebagai Executive, saya ingin bertanya dalam bahasa natural tentang data ("berapa penjualan bulan lalu?") dan mendapat jawaban akurat. | Jawaban ≤5 detik; akurasi ≥85% pada pertanyaan uji; sumber data ditampilkan. | Executive, Finance Manager |

### 6.3. Integrasi dengan Dataset Referensi

| Requirement | Dataset yang Digunakan | Cara Penggunaan |
|:---|:---|:---|
| **F-003 (Forecasting)** | Enterprise Digital Twin (Kaggle) | Gunakan tabel `sales_orders` + `finance` untuk menguji model Prophet/LSTM; ground-truth label untuk validasi. |
| **F-004 (Anomaly)** | Enterprise Digital Twin (Kaggle) | Gunakan label `procurement/finance anomalies` sebagai ground-truth untuk mengukur precision/recall. |
| **Intent Classification (F-007 pendukung)** | ODE Enterprise Use Cases (Hugging Face) | Latih/evaluasi classifier untuk memetakan pertanyaan user ke `module`/`submodule` yang tepat. |
| **Persona & User Story** | ODE Enterprise Use Cases (Hugging Face) | Label `persona` dan `kpi_metric` menjadi dasar persona dan metrik sukses di Section 4 & 6. |

### 6.4. Catatan Implementasi

- **Data Sintetis untuk Pengembangan**: Karena data pengguna riil belum tersedia di awal, gunakan **Enterprise Digital Twin** (16 tabel relasional, label ground-truth) sebagai data uji untuk F-003 dan F-004.
- **Intent Routing**: Untuk F-007 (Chat with Data), gunakan dataset ODE untuk melatih model klasifikasi intent agar pertanyaan user diarahkan ke modul yang tepat (Finance, Procurement, Inventory) sebelum query ke database.
- **Human-in-the-Loop**: Untuk aksi yang berdampak finansial (F-004 alert → tindakan), terapkan approval queue seperti pada `agent-company-ai`.


---

## 8. AI Requirements

Bagian ini mendefinisikan kebutuhan fungsional dan non-fungsional untuk komponen kecerdasan buatan (AI) dalam platform.

### 8.1. Model AI & Kemampuan Utama

| Fitur | Tipe Model / Teknologi | Metrik Target | Sumber Data / Referensi |
|:---|:---|:---|:---|
| **Peramalan Penjualan (Sales Forecasting)** | Time-series (Prophet / LSTM) | MAPE ≤ 10% (untuk SKU dengan ≥6 bulan data) | Data transaksi internal pengguna; dataset sintetis **Enterprise Digital Twin** untuk validasi |
| **Segmentasi Pelanggan (RFM)** | Clustering (K-Means / DBSCAN) | Silhouette Score ≥ 0.5 | Data CRM pengguna; dataset sintetis untuk pengujian awal |
| **Klasifikasi Intent & Routing Agen** | Text Classification (LLM / Embedding) | Akurasi ≥ 85% | Dataset **ODE Enterprise Use Cases** (15.000 contoh berlabel) untuk fine-tuning atau evaluasi |
| **Pembuatan Laporan Otomatis** | LLM (GPT-4o / Claude / Llama 3.1) + Template | Human Evaluation ≥ 4/5 | Data KPI dari dasbor; template laporan standar |
| **Deteksi Anomali** | Isolation Forest / Autoencoder | Precision ≥ 0.8 | Data penjualan, stok, dan keuangan; label ground-truth dari **Enterprise Digital Twin** |

### 8.2. Stack LLM & Integrasi

- **Provider LLM**: Platform harus mendukung setidaknya **Anthropic (Claude)**, **OpenAI (GPT)**, dan **Ollama (model lokal)** untuk fleksibilitas biaya dan privasi. Referensi implementasi multi-provider dapat dilihat pada `agent-company-ai`.
- **Orkestrasi**: Setiap agen AI (CEO, Finance, Ops) harus dapat memanggil *tools* spesifik (misalnya, `check_balance`, `list_payments`, `request_payment`) yang memerlukan persetujuan manusia (*human-in-the-loop*) untuk aksi finansial.
- **Vector Database (RAG)**: Gunakan **Qdrant** untuk menyimpan embedding dokumen internal (SOP, kontrak) dan mendukung fitur *chat with your data*.

### 8.3. Kebutuhan Data & Evaluasi

- **Data Sintetis untuk Pengembangan**: Karena data pengguna asli mungkin belum tersedia, gunakan **Enterprise Digital Twin** (Kaggle) yang mencakup 16 tabel relasional dan label ground-truth untuk menguji model peramalan, deteksi anomali, dan RAG.
- **Data Benchmark Intent**: Gunakan dataset **ODE Enterprise Use Cases** (Hugging Face) untuk mengukur performa klasifikasi intent dan routing agen sebelum data pengguna riil terkumpul.
- **Evaluasi**: Setiap model harus melalui evaluasi *offline* menggunakan data sintetis sebelum diuji pada data pengguna. Metrik evaluasi harus dicatat dalam log dan dapat diakses melalui dasbor admin.

### 8.4. Etika & Tata Kelola AI

- **Transparansi**: Setiap rekomendasi AI (terutama peramalan dan segmentasi) harus menyertakan penjelasan singkat (fitur utama yang mempengaruhi hasil) menggunakan SHAP atau feature importance.
- **Human-in-the-Loop**: Aksi yang berdampak finansial (pembayaran, perubahan harga, restock besar) harus memerlukan persetujuan pengguna sebelum dieksekusi. Referensi pola ini dapat dilihat pada sistem *approval queue* di `agent-company-ai`.
- **Privasi Data**: Data pengguna tidak boleh digunakan untuk melatih model global tanpa izin eksplisit. Model lokal (Ollama) harus menjadi opsi untuk pengguna yang sensitif terhadap privasi.


---

## 9. Integrasi Eksternal (Referensi Tambahan)

Untuk fitur riset pasar atau literature review (opsional, untuk segmen akademik), platform dapat mengintegrasikan:
- **OpenAlex API** melalui klien `oalex` (async, rate-limited, disk-cached). Catatan: OpenAlex memberlakukan budget kredit harian (1.000 kredit tanpa key; 10.000 dengan key gratis).
- **Semantic Scholar API** melalui **MCP Server** (`semanticscholar-mcp-server`) untuk rekomendasi paper dan citation graph.


---

## 10. Solution Architecture (Ringkas — untuk konteks)

| Komponen | Teknologi | Justifikasi |
|:---|:---|:---|
| Frontend | Next.js 14 + Tailwind | Cepat, SSR untuk dashboard |
| Backend | FastAPI + PostgreSQL | Async, cocok untuk AI service |
| AI Service | Python microservice | Terpisah untuk scaling |
| Vector DB | Qdrant (sudah di `vendor/`) | RAG untuk Chat with Data |
| Queue | Redis + Celery | Async job untuk forecasting/report |
| Storage | MinIO (sudah di `vendor/`) | Simpan file upload & laporan |
| LLM | Anthropic/OpenAI/Ollama | Fleksibel biaya & privasi |


---

## 11. Milestones & Timeline

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


---

## 12. Risks & Mitigation

Risiko diidentifikasi berdasarkan probabilitas (P) dan dampak (I), dengan mitigasi konkret.

| ID | Risiko | P | I | Mitigasi | Owner |
|:---|:---|:---|:---|:---|:---|
| **R-01** | Data pengguna jelek (missing >20%, duplikat, outlier) | High | High | Validasi ketat saat upload; auto-clean dengan pandas; tutorial data format; fallback ke data sintetis untuk demo | Backend + Data |
| **R-02** | Biaya LLM membengkak (API call tak terkendali) | High | Medium | Caching respons; small model untuk intent; self-host Llama 3.1 untuk report; budget alert per tenant | AI Eng |
| **R-03** | User tidak percaya rekomendasi AI | Medium | High | Explainability (SHAP/feature importance); human-in-the-loop untuk aksi finansial; tampilkan confidence level | AI Eng + UX |
| **R-04** | Kompetitor besar (Tableau, Power BI) masuk segmen UMKM | High | Medium | Fokus niche: Bahasa Indonesia, harga terjangkau, integrasi e-commerce lokal (Shopee, Tokopedia) | Product |
| **R-05** | Regulasi data (PDPA/GDPR) | Medium | High | Compliance by design: enkripsi at-rest & in-transit; data retention policy; DPA dengan vendor LLM; audit log | Legal + Backend |
| **R-06** | Model drift (akurasi forecasting turun seiring waktu) | Medium | Medium | Monitoring MAPE bulanan; retrain otomatis jika MAPE >15%; alert ke tim AI | AI Eng |
| **R-07** | Rate limit API eksternal (OpenAlex, Semantic Scholar) | Medium | Low | Cache hasil; fallback ke data lokal; gunakan API key gratis untuk kuota lebih tinggi | Backend |
| **R-08** | Kebocoran data antar tenant (multi-tenant) | Low | High | Row-Level Security di Postgres; uji penetrasi; audit log akses | Backend + Security |
| **R-09** | Ketergantungan pada satu provider LLM | Medium | Medium | Abstraksi LLM provider (Anthropic/OpenAI/Ollama); uji failover | AI Eng |
| **R-10** | Keterlambatan rekrutmen AI engineer | Medium | High | Mulai dengan 1 AI engineer + kontrak freelancer; dokumentasi ketat agar mudah onboarding | HR + Product |

### 12.1. Risk Register (Ringkas untuk Stakeholder)

| Kategori | Jumlah Risiko | Risiko Tertinggi |
|:---|:---|:---|
| Data | 1 (R-01) | Kualitas data pengguna |
| Biaya | 1 (R-02) | LLM cost |
| Adopsi | 1 (R-03) | Kepercayaan user |
| Kompetisi | 1 (R-04) | Tableau/Power BI |
| Regulasi | 1 (R-05) | PDPA/GDPR |
| Teknis | 3 (R-06, R-08, R-09) | Multi-tenant isolation |
| Operasional | 2 (R-07, R-10) | Rekrutmen |

### 12.2. Monitoring & Review

- **Risk review** dilakukan setiap akhir kuartal (Q1–Q4) bersama stakeholder.
- **Risk owner** bertanggung jawab update status risiko (Open/Mitigated/Closed) di `docs/risk-register.md`.
- **Escalation**: Jika risiko High/High (R-01) terjadi, eskalasi ke Product Owner dalam 24 jam.


---

## 13. Appendix: Referensi Data & Tools

| Referensi | Tipe | Penggunaan di PRD |
|:---|:---|:---|
| **ODE Enterprise Use Cases** (Hugging Face) | Dataset | Persona, intent classification, user story |
| **Enterprise Digital Twin** (Kaggle) | Dataset sintetis | Uji forecasting (F-003), anomaly detection (F-004) |
| **agent-company-ai** (GitHub) | Referensi arsitektur | Multi-agent, approval queue, LLM provider |
| **OpenAlex (`oalex`)** | API | Integrasi riset (opsional, Fase 3) |
| **Semantic Scholar MCP** | API | Rekomendasi paper (opsional) |
| **SAP Joule Studio PRD Template** | Template | Struktur PRD |


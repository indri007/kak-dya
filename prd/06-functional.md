# 6. Functional Requirements

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

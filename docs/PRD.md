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

- **Provider LLM**: Platform harus mendukung setidaknya **Anthropic (Claude)**, **OpenAI (GPT)**, dan **Ollama (model lokal)** untuk fleksibilitas biaya dan privasi. Referensi implementasi multi-provider dapat dilihat pada .
- **Orkestrasi**: Setiap agen AI (CEO, Finance, Ops) harus dapat memanggil *tools* spesifik (misalnya, , , ) yang memerlukan persetujuan manusia (*human-in-the-loop*) untuk aksi finansial.
- **Vector Database (RAG)**: Gunakan **Qdrant** untuk menyimpan embedding dokumen internal (SOP, kontrak) dan mendukung fitur *chat with your data*.

### 8.3. Kebutuhan Data & Evaluasi

- **Data Sintetis untuk Pengembangan**: Karena data pengguna asli mungkin belum tersedia, gunakan **Enterprise Digital Twin** (Kaggle) yang mencakup 16 tabel relasional dan label ground-truth untuk menguji model peramalan, deteksi anomali, dan RAG.
- **Data Benchmark Intent**: Gunakan dataset **ODE Enterprise Use Cases** (Hugging Face) untuk mengukur performa klasifikasi intent dan routing agen sebelum data pengguna riil terkumpul.
- **Evaluasi**: Setiap model harus melalui evaluasi *offline* menggunakan data sintetis sebelum diuji pada data pengguna. Metrik evaluasi harus dicatat dalam log dan dapat diakses melalui dasbor admin.

### 8.4. Etika & Tata Kelola AI

- **Transparansi**: Setiap rekomendasi AI (terutama peramalan dan segmentasi) harus menyertakan penjelasan singkat (fitur utama yang mempengaruhi hasil) menggunakan SHAP atau feature importance.
- **Human-in-the-Loop**: Aksi yang berdampak finansial (pembayaran, perubahan harga, restock besar) harus memerlukan persetujuan pengguna sebelum dieksekusi. Referensi pola ini dapat dilihat pada sistem *approval queue* di .
- **Privasi Data**: Data pengguna tidak boleh digunakan untuk melatih model global tanpa izin eksplisit. Model lokal (Ollama) harus menjadi opsi untuk pengguna yang sensitif terhadap privasi.

---

## 9. Integrasi Eksternal (Referensi Tambahan)

Untuk fitur riset pasar atau literature review (opsional, untuk segmen akademik), platform dapat mengintegrasikan:
- **OpenAlex API** melalui klien  (async, rate-limited, disk-cached). Catatan: OpenAlex memberlakukan budget kredit harian (1.000 kredit tanpa key; 10.000 dengan key gratis).
- **Semantic Scholar API** melalui **MCP Server** () untuk rekomendasi paper dan citation graph.

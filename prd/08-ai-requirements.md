# 8. AI Requirements

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

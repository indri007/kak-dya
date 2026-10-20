# Business Rules & System Guardrails
## AI Business Management Platform

Dokumen ini mendefinisikan aturan bisnis (*business rules*), batas toleransi model AI (*AI guardrails*), dan mekanisme validasi operasional yang wajib dipatuhi oleh seluruh layanan (Backend, AI Services, dan Agen AI).

---

## 1. Aturan Keuangan & Human-in-the-Loop (Approval Guardrails)

Aksi agen AI yang berdampak finansial **tidak boleh dieksekusi secara otomatis**. Aksi tersebut wajib dialihkan ke antrean persetujuan (`approval_queue`) dengan kriteria berikut:

| Kategori Aksi | Batas Pemicu (*Trigger Threshold*) | Tindakan Sistem | Otoritas Persetujuan |
|:---|:---|:---|:---|
| **Eksekusi Pembayaran Vendor** | Nominal > Rp 10.000.000 (atau > $1,000) | Tahan & buat tiket approval | `Owner` atau `Finance Manager` |
| **Penyesuaian Harga Jual (SKU)** | Perubahan harga > 10% dari harga saat ini | Tahan & buat tiket approval | `Owner` atau `Admin` |
| **Pemesanan Restock Otomatis** | Nilai PO > Rp 25.000.000 (atau > $2,500) | Tahan & buat tiket approval | `Buyer` atau `Operations` |
| **Penghapusan Data / Diskon Massal** | Diskon > 20% untuk > 50 SKU | Tahan & buat tiket approval | `Owner` |

* **Audit Trail**: Setiap persetujuan atau penolakan wajib mencatat `approver_id`, `approved_at`, dan catatan pertimbangan (`decision_notes`).

---

## 2. Aturan Peramalan Permintaan (Sales Forecasting Rules)

1. **Kelayakan Data Minimum**:
   * SKU yang memenuhi syarat untuk peramalan deret waktu (Prophet/LSTM) wajib memiliki histori transaksi $\ge 180\text{ hari}$ (6 bulan) dan minimal 30 transaksi aktif.
   * SKU baru (< 6 bulan) menggunakan metode estimasi moving average atau peramalan analogi kategori.
2. **Toleransi Akurasi (SLA)**:
   * Target **MAPE $\le 10\%$**.
   * Jika evaluasi bulanan menghasilkan MAPE $> 15\%$, sistem wajib memicu *retraining* otomatis dengan dataset terbaru.
3. **Peringatan Penurunan Drastis (*Forecast Drop Alert*)**:
   * Jika prediksi permintaan 30 hari ke depan turun $> 20\%$ dibandingkan rata-rata 3 bulan terakhir, sistem wajib memunculkan peringatan prioritas tinggi di dashboard.

---

## 3. Aturan Deteksi Anomali (Anomaly Detection Rules)

1. **Tingkat Keparahan (*Severity*)**:
   * **CRITICAL**: Anomali transaksi nominal $> 3\sigma$ (3 standar deviasi) dari rata-rata harian ATAU pengeluaran tidak terdaftar dalam anggaran.
   * **HIGH**: Selisih stok fisik vs tercatat $> 15\%$.
   * **MEDIUM**: Pola waktu transaksi di luar jam operasional wajar (pukul 23:00 - 04:00).
   * **LOW**: Fluktuasi margin keuntungan kecil ($\pm 5\%$).
2. **Kewajiban Penjelasan (*Explainability*)**:
   * Setiap anomali wajib disertai skor kontribusi fitur (SHAP / Feature Importance) yang menjelaskan faktor utama pemicu peringatan.

---

## 4. Aturan Segmentasi Pelanggan (RFM Clustering Rules)

1. **Periode Penghitungan**:
   * Metrik Recency (R), Frequency (F), dan Monetary (M) dihitung ulang secara otomatis setiap **Minggu pukul 00:00 UTC**.
2. **Klaster Baku**:
   * Sistem menghasilkan 4–6 klaster utama:
     * *Champions / High-Value*: Transaksi baru, frekuensi tinggi, nilai belanja besar.
     * *Loyal Customers*: Frekuensi stabil, nilai menengah ke atas.
     * *At-Risk*: Pernah belanja besar namun tidak aktif $> 90\text{ hari}$.
     * *Hibernating*: Tidak aktif $> 180\text{ hari}$ dengan nilai transaksi rendah.
3. **Threshold Kualitas**:
   * Klasterisasi hanya diterapkan jika *Silhouette Score* $\ge 0.5$. Jika di bawah nilai tersebut, sistem kembali ke aturan segmentasi kuartil heuristik.

---

## 5. Keamanan & Isolasi Multi-Tenant

1. **Prinsip Zero-Leakage**:
   * Setiap query basis data wajib menyertakan parameter sesi `app.current_tenant_id`.
   * Kebijakan *Row-Level Security (RLS)* di PostgreSQL aktif secara permanen.
2. **Anonimisasi PII**:
   * Nama, nomor telepon, dan email pelanggan wajib disamarkan (*masked*) saat diekspor untuk logging atau pengujian model LLM eksternal.
3. **Privasi Data LLM**:
   * Prompt yang dikirim ke LLM publik (Claude/GPT) tidak boleh menyertakan rahasia dagang mentah tanpa enkripsi/anonimisasi.
   * Opsi *self-hosted* (Ollama/Llama 3.1) wajib tersedia untuk pengguna tier Enterprise dengan regulasi kepatuhan ketat.

# 4. User Personas

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

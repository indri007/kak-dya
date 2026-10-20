# 12. Risks & Mitigation

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

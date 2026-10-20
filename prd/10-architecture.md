# 10. Solution Architecture (Ringkas — untuk konteks)

| Komponen | Teknologi | Justifikasi |
|:---|:---|:---|
| Frontend | Next.js 14 + Tailwind | Cepat, SSR untuk dashboard |
| Backend | FastAPI + PostgreSQL | Async, cocok untuk AI service |
| AI Service | Python microservice | Terpisah untuk scaling |
| Vector DB | Qdrant (sudah di `vendor/`) | RAG untuk Chat with Data |
| Queue | Redis + Celery | Async job untuk forecasting/report |
| Storage | MinIO (sudah di `vendor/`) | Simpan file upload & laporan |
| LLM | Anthropic/OpenAI/Ollama | Fleksibel biaya & privasi |

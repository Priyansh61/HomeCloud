# 🏠 HomeCloud

A self-hosted, privacy-focused alternative to Google Drive and Google Photos. Built for personal use, open source from day one.

---

## 🚀 Tech Stack

- **Frontend:** React.js + Tailwind CSS
- **Backend:** FastAPI (Python)
- **Storage:** MinIO (S3-compatible object storage)
- **Auth:** JWT + bcrypt
- **Deployment:** Docker + Docker Compose
- **CI/CD:** GitHub Actions

---

## 📦 MVP Features

- 🔐 Secure user authentication
- ⬆️ File and photo uploads
- 🖼️ Photo view (grid, by date)
- 📁 File explorer view
- ⬇️ Secure downloads with pre-signed links

---

## 🛠️ Development Setup

1. Clone this repo
2. Set up `.env` file from `.env.example`
3. Run:

```bash
docker-compose up --build

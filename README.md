\# 🛡️ SubsiGuard: Subsidy Leakage & Fraud Detection

SubsiGuard is an AI-powered dashboard designed to detect leakage and fraud patterns in Indian government subsidy programs (PDS, PM-KISAN, LPG, MGNREGA, etc.). It combines rule-based validation with Machine Learning to identify anomalies and ensure that subsidies reach the intended beneficiaries.

![SubsiGuard Banner](https://raw.githubusercontent.com/Mridul-SOl/SubsiGuard/main/frontend/public/vercel.svg) *(Replace with actual screenshot if available)*

## 🚀 Key Features

- 📁 **Smart CSV Upload**: Drag-and-drop interface with instant data validation and preview.
- 🧠 **AI-Powered Detection**: Hybrid approach using rule-based filters and **Isolation Forest** (Unsupervised ML) for anomaly detection.
- 🇮🇳 **Indian Context**: Optimized for Indian data formats (Aadhaar, INR, State-level schemes).
- 📊 **Interactive Analytics**: Rich dashboard with KPI cards, fraud distribution charts, and a state-wise heatmap.
- 📄 **Professional Export**: Generate PDF analysis reports or export flagged cases to CSV.
- 🎲 **Synthetic Data Generator**: Built-in tool to generate realistic Indian subsidy data for testing and demos.

## 🛠️ Tech Stack

### Backend (Python)
- **FastAPI**: High-performance web framework.
- **SQLModel & SQLite**: Efficient data modeling and local persistence.
- **Pandas**: Deep data manipulation and analysis.
- **Scikit-learn**: Machine learning implementation (Anomaly Detection).
- **Faker**: Localized Indian test data generation.

### Frontend (TypeScript)
- **Next.js 15 (App Router)**: Modern React framework.
- **TanStack Query v5**: Robust data fetching and state management.
- **Tailwind CSS & shadcn/ui**: Premium, dark-themed UI components.
- **Recharts**: Dynamic data visualizations.
- **React-Leaflet**: State-level India heatmap.

## ⚙️ Quick Start

### 1. Prerequisites
- Python 3.8+
- Node.js 18+
- npm

### 2. Automatic Setup
First, set up your local environment variables in the frontend:
```bash
cp frontend/.env.example frontend/.env.local
```
Then, use the included initializer script to set up both backend and frontend environments:
```bash
./init_project.sh
```

### 3. Launch the Application
Start both services concurrently:
```bash
./start.sh
```
- **Frontend**: [http://localhost:3000](http://localhost:3000)
- **Backend API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

### 4. Stop the Services
```bash
./stop.sh
```

## 📂 Project Structure

```
SubsiGuard/
├── backend/            # FastAPI Project
│   ├── api/            # API Routes (Upload, Analyze, Results)
│   ├── models/         # Database & Pydantic Schemas
│   ├── services/       # ML & Fraud Detection Logic
│   └── main.py         # Entry point
├── frontend/           # Next.js Project
│   ├── app/            # Pages & Routes
│   ├── components/     # UI Design System
│   ├── hooks/          # Custom React Hooks
│   └── lib/            # API Fetchers
├── docs/               # Technical Documentation
└── scripts/            # Automation (init, start, stop)
```

## 📜 License
MIT License - Developed for Hackathon demonstration.

---
Built with ❤️ for social impact.

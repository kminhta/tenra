# Tenra

Measure and optimize the environmental impact of LLM workloads.

## Quick Start

```bash
# Install dependencies
cd frontend && npm install && cd ..
cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && cd ..

# Start database
docker-compose up -d

# Run development servers
npm run dev
```

Access:
- Frontend: http://localhost:3000
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Tech Stack

- **Frontend**: Next.js 14, TypeScript, Tailwind, shadcn/ui
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Database**: TimescaleDB (PostgreSQL extension)

## Development

```bash
npm run dev        # Start both servers
npm run dev:web    # Frontend only
npm run dev:api    # Backend only
npm run db:up      # Start database
npm run db:down    # Stop database
```

## Environment Setup

Copy `.env.example` to `.env` and update values:

```bash
cp .env.example .env
```

Generate secure keys:

```bash
openssl rand -hex 32     # API_SECRET_KEY
openssl rand -base64 32  # NEXTAUTH_SECRET
```

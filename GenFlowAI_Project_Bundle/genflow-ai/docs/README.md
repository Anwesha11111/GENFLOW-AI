# GenFlowAI - Starlink Style Agentic Orchestration

## Quick Start
1. `cd infrastructure`
2. `cp .env.example .env` (Add your API keys)
3. `docker-compose up -d`
4. Import the JSON workflows from `/workflows` into your n8n instance at http://localhost:5678

## Architecture
- Hub: n8n
- Brain: LangChain (OpenAI/Groq)
- Memory: Redis
- Logs: Postgres

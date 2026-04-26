# GENFLOW-AI
## 🌌 GenFlowAI: Enterprise-Grade Agentic Orchestration
### *The "Starlink" of Autonomous Workflow Engines*

**GenFlowAI** is a high-throughput, LLM-powered automation engine designed for the rapid build and reuse of complex data pipelines. Built on the bedrock of **n8n**, **LangChain**, and **Docker**, it mirrors the modularity and reliability of Starlink satellite systems. Whether you are managing concurrent telemetry streams or automating cross-departmental enterprise logic, GenFlowAI provides the cognitive "brain" and deterministic "muscle" to execute with precision.

---

## 🛠 Core Architecture

GenFlowAI operates on a **Hub-and-Spoke** model. The central n8n orchestrator acts as the "Ground Station," while LangChain-driven agents serve as the "On-Board Computers" for individual data missions.



* **Orchestration:** n8n (Production-hardened v1.x+)
* **Intelligence:** LangChain ReAct Agents (OpenAI / Groq / Ollama)
* **Memory:** Redis (Persistent conversation buffers for cross-node context)
* **State & Audit:** PostgreSQL (Structured execution logs for "Black Box" mission replay)
* **Guardrails:** Deterministic FastAPI/Python nodes for heavy math and physics.

---

## ✨ Key Features

* **🛰 Concurrent Stream Processing:** Built-in logic for handling 10+ parallel data streams using advanced `SplitInBatches` and async sub-workflow patterns.
* **🧠 Memory-Aware Tooling:** Agents don't just "act"; they remember. Using Redis, agents maintain mission context across different execution stages.
* **🛑 HITL (Human-in-the-Loop) Gates:** High-risk actions (like orbital maneuvers or financial transfers) are paused for manual approval via Slack or Email.
* **♻️ Starlink-Style Rapid Reuse:** Modular workflow architecture allows you to "hot-swap" toolsets and worker nodes without touching the core agentic logic.
* **🛡 Sentinel Guardrails:** A secondary monitoring layer that audits agent reasoning in real-time to prevent logic drift or hallucinations.

---

## 📂 Project Structure

```text
genflow-ai/
├── 🏗 infrastructure/      # The Launchpad (Docker, Redis, Postgres)
├── 🧠 workflows/           # The Payloads (Master JSON, Sub-worker templates)
├── 🔧 tools/               # The Hardware (FastAPI Physics engine, JS pre-processors)
├── 📝 docs/                # The Manual (Flight rules, system prompts)
└── 🧪 tests/               # Stress tests for telemetry concurrency
```

---

## 🚀 Quick Start: 10 Minutes to Orbit

### 1. Fuel the Engine
Navigate to the `infrastructure` directory and set up your environment:
```bash
cp .env.example .env
# Open .env and add your OPENAI_API_KEY and N8N_ENCRYPTION_KEY
```

### 2. Ignition
Launch the entire stack using Docker Compose:
```bash
docker-compose up -d
```

### 3. Mission Upload
* Access n8n at `http://localhost:5678`.
* Go to **Workflows > Import from File**.
* Select `workflows/master_orchestrator.json`.

### 4. First Ping
Send a test telemetry packet via cURL:
```bash
curl -X POST http://localhost:5678/webhook/telemetry-ingest \
-H "Content-Type: application/json" \
-d '{
  "query": "Check status for STAR-102 and initiate cooling if temp > 85C",
  "sat_id": "STAR-102",
  "telemetry": { "temp": 89, "altitude": 550 }
}'
```

---

## 📊 Monitoring & Observability

Every "Thought" is logged. Connect your preferred BI tool to the **PostgreSQL** database to visualize:
* **Agent Decision Accuracy** (Sentinel Audit scores)
* **Token Consumption vs. Mission Priority**
* **Average HITL Approval Latency**

---

## 📜 Mission Statement
> *"To provide a deterministic, scalable, and modular framework for autonomous decision-making in high-stakes enterprise environments."*

**Build. Deploy. Scale. Welcome to the future of automation.**

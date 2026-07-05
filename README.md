# CIO Copilot Agent

[![CI](https://github.com/kogunlowo123/cio-copilot-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/cio-copilot-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Executive | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

CIO copilot agent that monitors IT portfolio health, tracks digital transformation progress, manages vendor relationships, assesses technology risks, and provides IT investment recommendations.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `assess_it_portfolio` | Assess health of IT application and infrastructure portfolio |
| `track_transformation` | Track digital transformation initiative progress |
| `evaluate_vendor` | Evaluate IT vendor performance and contract value |
| `assess_tech_risk` | Assess technology risks (tech debt, end-of-life, security) |
| `recommend_investment` | Generate IT investment recommendation with ROI analysis |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/cio-copilot/synthesize` | Synthesize data |
| `POST` | `/api/v1/cio-copilot/analyze` | Analyze |
| `GET` | `/api/v1/cio-copilot/track` | Track metrics |
| `POST` | `/api/v1/cio-copilot/recommend` | Get recommendation |
| `POST` | `/api/v1/cio-copilot/report` | Generate report |

## Features

- Cio
- Copilot
- Strategic Insights
- Decision Support

## Integrations

- Snowflake
- Tableau
- Salesforce
- Workday
- Jira

## Architecture

```
cio-copilot-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── cio_copilot_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Enterprise Data Platform + LLM + BI**

---

Built as part of the Enterprise AI Agent Platform.

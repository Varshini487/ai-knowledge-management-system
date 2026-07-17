# 🧠 AI Knowledge Management System

An **enterprise knowledge platform** that turns scattered internal documents into a searchable, intelligent knowledge base. Think: Confluence meets ChatGPT.

## How It Works (3-layer)

### Layer 1: Ingestion & Tagging
- Upload PDFs, Markdown, Confluence exports
- Auto-extract keywords using NLP (spaCy) + extract topics using LDA
- Tag documents with auto-generated tags (e.g., "onboarding", "api-design", "incident-response")
- Store in PostgreSQL with full-text search index

### Layer 2: Semantic Search
- Embed all documents using Sentence-Transformers
- Index in FAISS for fast vector similarity
- User query: "how do we handle payment refunds?" → finds related docs even if wording differs
- Hybrid search: keyword (fast) + semantic (relevant)

### Layer 3: Conversational Q&A
- RAG pipeline: user question → retrieve top-3 docs → LLM generates answer citing sources
- Fallback: "I don't know" if confidence < threshold (better than hallucination)
- User feedback loop: "Was this helpful?" → reweight docs for next similar query

## Tech Stack
- **Backend**: FastAPI, PostgreSQL, Redis
- **Search**: FAISS, BM25 (Elasticsearch)
- **Embeddings**: Sentence-Transformers (all-MiniLM-L6-v2)
- **LLM**: OpenAI GPT-4 / Claude
- **Frontend**: Streamlit

## 🚀 Getting Started
```bash
git clone https://github.com/Varshini487/ai-knowledge-management-system
pip install -r requirements.txt
streamlit run app.py
```

## 💡 Use Cases
- Internal wiki + FAQ automation
- Onboarding assistant for new employees
- Support agent training data
- Engineering runbooks searchable by natural language

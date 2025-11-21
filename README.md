<h1 align="center">🤖 OmniChat AI</h1>

<p align="center">
A multi-LLM conversational platform with document uploads, RAG search, and model switching — built using Next.js & FastAPI.
</p>

---

## 🚀 Overview

🧠 **OmniChat AI** is a full-stack multi-LLM chat application that allows users to interact with different AI models such as **OpenAI GPT, Anthropic Claude, Google Gemini, Meta Llama, and local models via vLLM/Ollama**.

Users can:

- Chat with AI in real-time
- Upload PDFs, text files, and website links
- Run **Retrieval-Augmented Generation (RAG)**
- Switch LLM providers dynamically
- Store and revisit conversations

Inspired by **ChatGPT**, **Perplexity**, and **ChatOllama** — designed for learning and production-grade architecture.

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js, React, TailwindCSS, shadcn UI |
| Backend | FastAPI, Python 3.11+ |
| Model Integration | OpenAI, Anthropic, Gemini, Ollama/vLLM |
| RAG | LangChain / LlamaIndex |
| Vector DB | Pinecone / Weaviate / PostgreSQL (pgvector) |
| Storage | Local or S3-compatible |
| Deployment Ready | Docker, Kubernetes |

---

## ✨ Features

- 🔄 **Model Switching** — choose your LLM on demand  
- 🧩 **Pluggable Model Architecture** for extending providers  
- 📁 **Document Upload Support** (PDF, TXT, DOCX)
- 🌐 **URL + Web Content ingestion**
- 🔍 **RAG Querying with embeddings**
- 💬 **Persistent chat history**
- 🛠 Modular service & clean architecture

---

## 📦 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/omnichat-ai
cd omnichat-ai

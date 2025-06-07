# 🤖 Multi-Agent Example Assignment

This repository demonstrates the use of multiple AI agent tools and LLM access methods including **Swarm**, **UVicorn**, **OpenRouter**, **LiteLLM**, and **Chainlit**. The structure follows modular examples in separate folders, each with its own purpose and use-case.

---

## 📁 Project Structure

Multi_agent_Example/
├── 00_swarm/
│ └── main.py # Basic multi-agent simulation
├── 01_uv/
│ └── main.py # REST API using FastAPI + Uvicorn
├── 02_openrouter/
│ └── main.py # Calling OpenRouter LLM via LiteLLM
├── 03_litellm_openai_agent/
│ ├── main.py # OpenAI LLM call via LiteLLM + Chainlit UI
│ └── .chainlit/ # (Optional) Chainlit configuration
├── .env # Environment variables
├── requirements.txt # Python dependencies
└── README.md # Project guide and documentation

---


## 🔑 Requires
OPENAI_API_KEY or GEMINI_API_KEY in `.env

## 🗝️ .env Configuration
Create a .env file in the root with your API keys:

```bash 
env

OPENROUTER_API_KEY=sk-or-...
GEMINI_API_KEY=your-gemini-key
```
## 📦 Install Requirements
Install all Python dependencies:

```bash

pip install -r requirements.txt
litellm
fastapi
uvicorn
python-dotenv
chainlit
```

## 💡 Tips
- OpenRouter is a good alternative if your OpenAI quota is exceeded.

- Use Chainlit for building chat-based LLM agents.

- Each folder is independent and demonstrates a different integration approach.

## 👨‍🎓 Author
**Student:** [Faryal Junaid](https://www.linkedin.com/in/faryal-junaid-06780b2b4/ "LinkedIn - Faryal Junaid")  
**Instructor:** Sir Asharib Ali
**Course:** Multi-Agent Systems – Quarter 4


## 📚 References

- [LiteLLM Documentation](https://docs.litellm.ai/ "LiteLLM - Lightweight LLM Interface")
- [Chainlit Documentation](https://docs.chainlit.io/ "Chainlit - Build LLM-powered apps in minutes")
- [OpenRouter](https://openrouter.ai/docs "OpenRouter - Multi-model API platform")
- [OpenAI API](https://platform.openai.com/docs "OpenAI - API Documentation")
- [FastAPI](https://fastapi.tiangolo.com/ "FastAPI - Modern Web Framework for Python")

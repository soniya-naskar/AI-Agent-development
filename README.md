AI RAG Agent – FastAPI Backend (Azure-Deployable)
Project Overview
This project implements an AI-powered Retrieval-Augmented Generation (RAG) system that
answers user questions based on internal documents such as company policies, FAQs, or technical
documentation.
Architecture Overview
The system consists of a FastAPI backend, a FAISS vector store for document retrieval, and a
Large Language Model (LLM) for generating answers using retrieved context.
Tech Stack Used
Python 3.10, FastAPI, Uvicorn, LangChain, FAISS, OpenAI or Azure OpenAI, Azure App Service.
Setup Instructions
Local setup includes creating a virtual environment, installing dependencies, setting environment
variables, and running the FastAPI server using Uvicorn. Azure deployment uses Azure App
Service with environment variables configured in the Azure portal.
Design Decisions
Retrieval-Augmented Generation was chosen over fine-tuning to reduce cost, improve
transparency, and allow easy updates to documents. FAISS was selected for its speed and
lightweight nature. FastAPI was used for performance and built-in API documentation.
Limitations
The system depends on an external LLM API, uses in-memory session storage, and is not
optimized for very large document collections.
Future Improvements
Future enhancements include persistent memory using a database, support for PDF ingestion,
advanced agent decision-making, authentication, rate limiting, and monitoring with Azure tools.
Status
The project is fully functional, RAG-enabled, locally runnable, and deployable on Azure

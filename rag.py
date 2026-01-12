import os

from openai import AzureOpenAI
from vectorstore import retriever

SESSION_MEMORY = {}

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

def get_answer(query, session_id):
    history = SESSION_MEMORY.get(session_id, [])

    needs_docs = any(word in query.lower() for word in ["policy", "leave", "faq", "security"])

    if needs_docs:
        docs = retriever.get_relevant_documents(query)
        context = "\n".join([d.page_content for d in docs])
        sources = list({d.metadata.get("source") for d in docs})
        prompt = f"Answer using the context below:\n{context}\nQuestion: {query}"
    else:
        prompt = query
        sources = []

    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content
    SESSION_MEMORY[session_id] = history + [query]

    return answer, sources

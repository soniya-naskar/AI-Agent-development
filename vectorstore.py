
# import os
# from langchain.embeddings import AzureOpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.document_loaders import TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# embedding = AzureOpenAIEmbeddings(
#     azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
#     openai_api_version="2024-02-15-preview"
# )

# if not os.path.exists("faiss_index"):
#     loaders = [
#         TextLoader("docs/leave_policy.txt"),
#         TextLoader("docs/work_from_home_policy.txt"),
#         TextLoader("docs/security_policy.txt"),
#         TextLoader("docs/product_faq.txt"),
#     ]
#     docs = []
#     for loader in loaders:
#         docs.extend(loader.load())

#     splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     split_docs = splitter.split_documents(docs)

#     vectorstore = FAISS.from_documents(split_docs, embedding)
#     vectorstore.save_local("faiss_index")

# vectorstore = FAISS.load_local("faiss_index", embedding)
# retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
import os
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

embedding = AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
    openai_api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)

if not os.path.exists("faiss_index"):
    loaders = [
        TextLoader("docs/leave_policy.txt"),
        TextLoader("docs/work_from_home_policy.txt"),
        TextLoader("docs/security_policy.txt"),
        TextLoader("docs/product_faq.txt"),
    ]

    documents = []
    for loader in loaders:
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    split_docs = splitter.split_documents(documents)

    vectorstore = FAISS.from_documents(split_docs, embedding)
    vectorstore.save_local("faiss_index")

vectorstore = FAISS.load_local("faiss_index", embedding)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

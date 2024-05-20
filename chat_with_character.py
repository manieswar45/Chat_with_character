from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_vectorstore(text_chunks):
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    hf = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=hf)
    return vectorstore

def handle_user_query(query, vector_store, memory, initial_context):
    llm = ChatOpenAI()
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory,
        get_chat_history=lambda h: h  # Retrieve the chat history stored in memory
    )

    # Construct the prompt with initial context and user query

    prompt = f"{initial_context}\n\nYou: {query}\nCharacter:"
    
    response = conversation_chain({'question': prompt})

    return response['answer']

def main():
    character_description = input("Describe the character: ")
    scene_description = input("Describe the scene: ")
    
    # Combine character and scene descriptions into initial context
    # Combine character and scene descriptions into initial context
    initial_context = f"Character Description: {character_description}\nScene: {scene_description}\nYou are the character described above. Answer questions and engage in conversation as this character."
    
    # Initialize vector store with the initial context
    vector_store = get_vectorstore([initial_context])
    
    # Initialize memory
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True, output_key='answer')
    
    print("Chatbot is ready! (Type 'exit' to stop)")
    
    while True:
        user_query = input("You: ")
        if user_query.lower() == 'exit':
            break
        answer = handle_user_query(user_query, vector_store, memory, initial_context)
        print(f"Character: {answer}")

if __name__ == "__main__":
    main()

import ollama

def generate_response(query, context):
    prompt = f"""
    You are an AI Code Assistant
     
    Use the provided context to answer the question.
     
    Context:
    {context}
     
    Question:
    {query}
    """
    
    response = ollama.chat(
        model="llama3.2",                        # ← was llama3
        messages=[
            {"role": "system", "content": prompt},
        ]
    )
    
    return response.message.content
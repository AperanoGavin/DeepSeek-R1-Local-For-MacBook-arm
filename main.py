from transformers import pipeline

model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
nlp = pipeline("question-answering", model=model_name)

while True:
    question = input("Posez votre question: ")
    if question.lower() in ["exit", "quit"]:
        break
    context = "Votre contexte ici"  # Remplacez par le contexte approprié
    result = nlp(question=question, context=context)
    print(f"Réponse: {result['answer']}")
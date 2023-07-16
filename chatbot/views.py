from django.shortcuts import render
from django.http import HttpResponse
from transformers import pipeline
def index(request):
    # Initialize the pipeline with the model
    qa_pipeline = pipeline("question-answering",
                           model="bert-large-uncased-whole-word-masking-finetuned-squad",
                           tokenizer="bert-large-uncased-whole-word-masking-finetuned-squad")

    # Provide a context and a question
    context = "fani working for nile university"
    question = request.GET.get("message")

    # Get the answer
    answer = qa_pipeline({"context": context, "question": question})


    return(HttpResponse(answer["answer"]))


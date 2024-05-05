import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def get_answer(url, question):
    response = requests.get(url)
    if response.status_code != 200:
        return 'Failed to fetch webpage content'

    soup = BeautifulSoup(response.text, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])

    qa_pipeline = pipeline("question-answering")
    answer = qa_pipeline({'context': text, 'question': question})

    if answer['score'] > 0.5:
        return answer['answer']
    else:
        return "I don't know the answer"

if __name__ == '__main__':
    url = input("Enter the URL of the webpage: ")
    question = input("Enter your question: ")
    print("Searching for the answer...")
    answer = get_answer(url, question)
    print("Answer:", answer)



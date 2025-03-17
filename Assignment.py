from flask import Flask, render_template, jsonify
import requests
import pandas as pd
from bs4 import BeautifulSoup

app =Flask(__name__)
@app.route('/', methods=['GET'])
def scrape_news():
    try:
        url ="https://en.wikipedia.org/wiki/Elon_Musk"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        text = [p.text for p in soup.find_all('p')]
        if not text:
            return jsonify({"Error":"We have an error"})
        create_csv(text)
        return jsonify({"para": text})

    except Exception as e:
        print(e)
    
def create_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("NewData.csv")
    print("File is saved as a CSV File")
    answer = df.head(5)
    return answer

if __name__ == "__main__":
    app.run(debug=True)
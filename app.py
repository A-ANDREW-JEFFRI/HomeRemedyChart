from flask import Flask, request, render_template
import requests
import openai

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method== 'POST':
        openai.api_key = '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'
        disease_name = request.form['disease_name']
        messages = [
        {"role": "system", "content": "You are a kind helpful assistant."},
    ]
        message = f"Give some home remedy for {disease_name}"
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
        return render_template('home.html', remedy=reply)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

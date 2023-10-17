from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods = ['POST'])
def process():
    solution_lst = []
    score = 0
    for i in range(6):
      correct_number = random.randint(0,222)
      solution_lst.append(correct_number)
    print(solution_lst)
  
    
    guess = [request.form[f'guessField{number}'] for number in range(6)]
  
    print(guess)
    for i in range(6):
      if guess[i] == solution_lst[i]:
        score = score + 1

    score_results = f'Your score is {score} out of 6.'
    
    return render_template('result.html',processed_data = score_results)
  
  

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=5000)
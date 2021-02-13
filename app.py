from flask import Flask, request, render_template
from Script import recommendations

app=Flask(__name__)

@app.route('/')
def home():  
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():  
    if request.method == 'POST':
        str = request.form
        movielist = recommendations(str['movie_name'])
        return render_template('index.html', movies = movielist )

    return render_template('index.html')
    
if __name__ == '__main__':
    app.run()
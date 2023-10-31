family = [
    {
        'name': 'Alex',
        'age': 10,
        'picture': 'alex.jpg'
    },
    {
        'name': 'John',
        'age': 35,
        'picture': 'john.jpg'
    },
    # Add more family members here
]

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def family_tree():
    return render_template('family.html', family=family)

if __name__ == '__main__':
    app.run(debug=True)


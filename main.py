from flask import Flask, render_template, jsonify
import sqlite3
import random


app = Flask(__name__)


CATS = {
    1: {"name": "白貓", "meaning": "來福招福"},
    2: {"name": "赤貓", "meaning": "病除招福"},
    3: {"name": "黑貓", "meaning": "厄除招福"},
    4: {"name": "櫻花貓", "meaning": "恋愛招福"},
    5: {"name": "青貓", "meaning": "安全招福"}
}

def init_db():

    conn = sqlite3.connect('lottery.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cat_name TEXT,
            meaning TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
  
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
   
   
    cat_id = random.randint(1, 5)
    cat = CATS[cat_id]
    
   
    conn = sqlite3.connect('lottery.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO results (cat_name, meaning) VALUES (?, ?)',
        (cat['name'], cat['meaning'])
    )
    conn.commit()
    conn.close()
    
    return jsonify({
        'name': cat['name'],
        'meaning': cat['meaning']
    })



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
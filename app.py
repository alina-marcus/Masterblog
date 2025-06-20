from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open('data.json', 'r') as f:
        blog_posts = json.load(f)
        print(blog_posts)
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
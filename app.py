from urllib import request

from flask import Flask, request, render_template, redirect, url_for
import json
import os
app = Flask(__name__)

@app.route('/')
def index():
    with open('data.json', 'r') as f:
        blog_posts = json.load(f)
        print(blog_posts)
    return render_template('index.html', posts=blog_posts, add_link='<a href="/add">Create new Post</a>')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']

        # checks if file exists, opens it and writes data into
        # variable blog_posts
        if os.path.exists('data.json'):
            with open('data.json', 'r') as f:
                blog_posts = json.load(f)
        else:
            blog_posts = []

        # gives each post a unique id and increments ids automatically
        if blog_posts:
            max_id = max(post.get('id', 0) for post in blog_posts)
        else:
            max_id = 0
        new_id = max_id + 1

        # puts data for new post together and appends it to the list
        # of blog_posts
        new_post = {
            'id': new_id,
            'author': author,
            'title': title,
            'content': content
        }
        blog_posts.append(new_post)

        # writes updated list of blog_posts into the json file
        with open('data.json', 'w') as f:
            json.dump(blog_posts, f, indent=4)

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    # opens json, removes blog post with the desired id and writes
    # the remaining blog posts back into the json file
    with open('data.json', 'r') as f:
        blog_posts = json.load(f)

        for post in blog_posts:
            if post['id'] == post_id:
                blog_posts.remove(post)

    with open('data.json', 'w') as f:
        json.dump(blog_posts, f, indent=4)

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
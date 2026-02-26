from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET', 'POST'])
def handle_posts():
    if request.method == 'POST':
        # Add the code that handles adding a new blog
        new_post = request.get_json()
        if 'title' not in new_post:
            return jsonify("Title is missing"), 400
        elif 'content' not in new_post:
            return jsonify("Content is missing"), 400
        # Set a new id
        if POSTS:
            new_id = max(post['id'] for post in POSTS) + 1
            new_post['id'] = new_id
        else:
            new_post['id'] = 1

        # Add new post to POSTS
        POSTS.append(new_post)

        # Return the new post to the client
        return jsonify(new_post), 201

    return jsonify(POSTS)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)

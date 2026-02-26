from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


def find_post_by_id(post_id):
    return next((post for post in POSTS if post['id'] == post_id), None)


@app.route('/api/posts', methods=['GET', 'POST'])
def handle_posts():
    if request.method == 'POST':
        # Add the code that handles adding a new blog
        new_post = request.get_json()
        if 'title' not in new_post:
            return jsonify({"message": "Title is missing"}), 400
        elif 'content' not in new_post:
            return jsonify({"message": "Content is missing"}), 400
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


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete(post_id):
    global POSTS

    post = find_post_by_id(post_id)
    if post is None:
        return '', 404
    POSTS.remove(post)

    successfully_deleted = {"message": f"Post with id {post_id} has been deleted successfully."}
    return jsonify(successfully_deleted), 200


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update(post_id):
    global POSTS
    post = find_post_by_id(post_id)
    if post is None:
        return '', 404

    new_post = request.get_json()

    if 'title' in new_post:
        post['title'] = new_post['title']
    if 'content' in new_post:
        post['content'] = new_post['content']

    return jsonify(post), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)

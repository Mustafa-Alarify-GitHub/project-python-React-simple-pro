from app import app, db
from models import Friend
from flask import jsonify, request

#  Get All Friends


@app.route('/api/friends', methods=['GET'])
def get_friends():
    friends = Friend.query.all()
    return jsonify([friend.to_json() for friend in friends])

# Create a New Friend


@app.route('/api/friends', methods=['POST'])
def create_friend():
    try:
        data = request.json
        new_friend = Friend(
            name=data.get('name'),
            role=data.get('role'),
            description=data.get('description'),
            gender=data.get('gender'),
            img_url=data.get('imgUrl')
        )
        db.session.add(new_friend)
        db.session.commit()
        return jsonify({
            "status": 200,
            "message": "Friend created successfully",
            "data": new_friend.to_json()
        })
    except Exception as e:
        return jsonify({
            "message": "Error creating friend",
            "error": str(e)
        }), 500

# Delete a Friend


@app.route('/api/friends/<int:friend_id>', methods=['DELETE'])
def delete_friend(friend_id):
    try:
        friend = Friend.query.get_or_404(friend_id)
        db.session.delete(friend)
        db.session.commit()
        return jsonify({
            "status": 200,
            "message": "Friend deleted successfully"
        })
    except Exception as e:
        return jsonify({
            "message": "Error deleting friend",
            "error": str(e)
        }), 500

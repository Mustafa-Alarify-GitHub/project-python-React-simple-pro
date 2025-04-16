from app import app, db
from models import Friend
from flask import jsonify, request


def handle_error(message, error, code=500):
    return jsonify({
        "status": code,
        "message": message,
        "error": str(error)
    }), code


@app.route('/api/friends', methods=['GET'])
def get_friends():
    """Get all friends"""
    friends = Friend.query.all()
    return jsonify([friend.to_json() for friend in friends]), 200


@app.route('/api/friends', methods=['POST'])
def create_friend():
    """Create a new friend"""
    try:
        # validate required fields
        required_fields = ['name', 'role', 'description', 'gender']
        for field in required_fields:
            if field not in request.json:
                return jsonify({
                    "status": 400,
                    "message": f"Missing required field: {field}"
                }), 400
                
        # create new friend Obj
        data = request.get_json()
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
            "status": 201,
            "message": "Friend created successfully",
            "data": new_friend.to_json()
        }), 201
    except Exception as e:
        return handle_error("Error creating friend", e)


@app.route('/api/friends/<int:friend_id>', methods=['DELETE'])
def delete_friend(friend_id):
    """Delete a friend by ID"""
    try:
        friend = Friend.query.get_or_404(friend_id)
        db.session.delete(friend)
        db.session.commit()
        return jsonify({
            "status": 200,
            "message": "Friend deleted successfully"
        }), 200
    except Exception as e:
        return handle_error("Error deleting friend", e)


@app.route('/api/friends/<int:friend_id>', methods=['PUT'])
def update_friend(friend_id):
    """Update a friend by ID"""
    try:
        friend = Friend.query.get_or_404(friend_id)
        data = request.get_json()
        friend.name = data.get('name')
        friend.role = data.get('role')
        friend.description = data.get('description')
        friend.gender = data.get('gender')
        friend.img_url = data.get('imgUrl')
        db.session.commit()
        return jsonify({
            "status": 200,
            "message": "Friend updated successfully",
            "data": friend.to_json()
        }), 200
    except Exception as e:
        return handle_error("Error updating friend", e)

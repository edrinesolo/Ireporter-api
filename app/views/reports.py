import datetime
from flask import Flask, json, jsonify, Blueprint, request


incident = Blueprint('report', __name__)
reports = []


@incident.route('/', methods=['GET'])
def index():
    """
      API index
    """
    return jsonify({'message': "welcome to Ireporter API"}), 200


@incident.route('/api/v1/redflags', methods=['GET'])
def getred_flags():
    """
      return all redflags
    """
    return jsonify({'redfags': reports}), 200

# getting a specific red flag


@incident.route('/api/v1/redflags/<int:redflag_id>', methods=['GET'])
def get_specific_red_flag(redflag_id):
    """
      return all redflags given the id
    """
    if not item_exists(redflag_id, reports):
        return jsonify({'msg': 'RedFlag not Found'}), 404

    for report in reports:
        if report['id'] == redflag_id:
            return jsonify({'data': report}), 200


@incident.route('/api/v1/redflags', methods=['POST'])
def postred_flags():
    """
      post a redflag
    """

    if not request.content_type == 'application/json':
        return jsonify(
            {"failed": "content-type must be application/json"}), 401
    request_data = request.get_json()

    report = {
        "id": len(reports) + 1,
        "created_on": datetime.datetime.utcnow(),
        "created_by": 1,
        "type": request_data['type'],
        "location": request_data['location'],
        "status": request_data['status'],
        "image": request_data['image'],
        "video": request_data['image'],
        "comment": request_data['comment']
    }
    reports.append(report)
    return jsonify({"success": "RedFlag created",
                    "crime": report.get('id')}), 201


@incident.route('/api/v1/redflags/<int:redflag_id>', methods=['PUT'])
def update_specific_red_flag(redflag_id):
    """
      edit a specific redflag
    """
    if not item_exists(redflag_id, reports):
        return jsonify({'msg': 'item not found'}), 404
    # CREATE A NEW LIST OBJECT
    data = request.get_json()
    report = {
        "id": redflag_id,
        "last_updated_on": datetime.datetime.utcnow(),
        "created_by": 1,
        "type": data['type'],
        "location": data['location'],
        "status": data['status'],
        "images": data['image'],
        "video": data['image'],
        "comment": data['comment']
    }
    for i in reports:
        if i['id'] == redflag_id:
            i.update(report)
    return jsonify({"msg": "updated"}), 200


@incident.route('/api/v1/redflags/<int:redflag_id>', methods=['DELETE'])
def delete_red_flags(redflag_id):
    """
      delete a redflag
    """
    if not item_exists(redflag_id, reports):
        return jsonify({'msg': 'item not found'}), 404

    for report in reports:
        if report['id'] == redflag_id:
            reports.remove(report)
    return jsonify({'Message': "RedFlag deleted"}), 200


@incident.route('/api/v1/redflags/<int:redflag_id>', methods=['PATCH'])
def edit_comment_of_a_redfag(redflag_id):
    data = request.get_json()
    if not item_exists(redflag_id, reports):
        return jsonify({'msg': 'redflag not found'}), 404
    for i in reports:
        if i['id'] == redflag_id:
            i['comment'] = data['comment']

            return jsonify({'msg': 'comment updated'}), 200


def item_exists(item_id, itemlist):
    """
      redflag exists
    """
    for item in itemlist:
        if item['id'] == item_id:
            return True
    return False

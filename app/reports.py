from flask import Flask, jsonify, request, Response, json, Blueprint,sessions

import datetime

ap = Blueprint('endpoint', __name__)
reports = []

 
# GET redflags
@ap.route('/api/v1/redflags')
def get_redflags():
    '''
    returns a list of all requests
    '''
    if len(reports) == 0:
        return jsonify({'msg': 'No redflags yet'}), 200
    return jsonify({'redflags': reports, 'count': len(reports)}), 200


# GET redflags/id
@ap.route('/api/v1/redflags/<int:id>')
def get_a_redflag(id):
    '''
    return  details for a specific redflag
    '''
    theredflag = []
    for report in reports:
        if report['id'] == id:
            theredflag.append(report)
    if len(theredflag) == 0:
        return jsonify({"msg": "redflag not found"}), 404
    return jsonify(theredflag[0]), 200


# POST /redflags
@ap.route('/api/v1/redflags', methods=['POST'])
def add_redflag():
    '''
    creates a new redflag
    '''

    if not request.content_type == 'application/json':
        return jsonify({"failed": 'Content-type must be application/json'}), 401
    request_data = request.get_json()
    if is_valid_request(request_data):
        report = {
            'id': len(reports) + 1,
            'incident_type': request_data['incident_type'],
            'comment_description': request_data['comment_description'],
            'status': request_data['status'],
            'current_location': request_data['current_location'],
            'video/image': request_data['video/image'],
            'created': datetime.datetime.now(),
            'user_id': request_data['user_id']
            
        }
        reports.append(report)
        response = Response(response=json.dumps({
            'msg': "redflag successfully created", 'request_id': report.get('id')}),
            status=201, mimetype="application/json")
        response.headers['Location'] = "redflags/" + str(report['id'])
        return response
    else:
        response = Response(json.dumps({"error": "Invalid redflag" }), 
        status=400, mimetype="application/json")
        return response



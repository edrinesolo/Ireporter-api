from flask import Flask,json,jsonify,Blueprint,request
import datetime

incident=Blueprint('report',__name__)
reports=[]
@incident.route('/',methods=['GET'])
def index():
    return jsonify({'message':"welcome"}),200

@incident.route('/api/v1/redflags',methods=['GET'])
def getred_flags():
        return jsonify({'data':reports}),200

  #getting a specific red flag
@incident.route('/api/v1/redflags<int:id>',methods=['GET'])
def get_specific_red_flag(id):
      #find the item by id
      for report in reports:
            if report['id'] == id:
                  return jsonify({'data' :report}),200
            return jsonify({'message': 'no item found'}),404
      


@incident.route('/api/v1/redflags',methods=['POST'])
def postred_flags():
    data=request.get_json()
    if not request.content_type is 'application/json':
        return jsonify({"failed": "content-type must be application/json"}), 401
    
           
    report={
          "id":len(reports)+1,
          "created_on":datetime.datetime.utcnow(),
          "created_by":1,
          "type":data['type'],
          "location":data['location'],
          "status":data['status'],
          "images":data['image'],
          "video":data['image'],
          "comment":data['comment']


    }
    reports.append(crime)
    return jsonify({"success":True,"crime":crime.get('id')}),201

#####Editing aspecific flag
@incident.route('/api/v1/redflags/<int:id>',methods=['PUT'])
def update_specific_red_flag(id):
      if not item_exists(id,reports):
            return jsonify({'msg':'item not found'}),404
      #CREATE A NEW LIST OBJECT
      data=request.get_json()
            #TODO VALIDATE
      crime={
            "id":id,
            "last_updated_on":datetime.datetime.utcnow(),
            "created_by":1,
            "crime_nature":data['crime_nature'],
            "location":data['location'],
            "status":data['status'],
            "images":data['image'],
            "video":data['image'],
            "comment":data['comment']


      }
      for i in reports:
          if i['id']==id:
                pass
      return jsonify({"msg":"updated"}),200

@incident.route('/api/v1/redflags/<int:id>',methods=['DELETE'])
def delete_red_flags(id):
    #find the item by id
    if not item_exists(id,reports):
       return jsonify({'msg':'item not found'}),404

    for crime in reports:
        if crime['id']==id:
           reports.remove(report)
    return jsonify({'Message': "item deleted"}),200
    

def item_exists(item_id,itemlist):
      for item in itemlist:
            if item['id']==item_id:
                  return True
      return False
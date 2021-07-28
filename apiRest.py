from flask import Flask,jsonify,request,make_response
from flask_restful import Resource, Api,reqparse
from scrapCoin import top10Kpi

# class tfSchema(Schema):
#     tf = fields.Int(required=False)
app = Flask("__main__")
api = Api(app)

todos = {}
# schema = tfSchema()

class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        print("here")
        tf = request.args.get('tf',type=int)
        print('tf:',tf)
        if( not tf ):
            print("heerreee eratum")
            return make_response(jsonify(
                status = 'error',
                message  ="missing  (tf) parameter"
                
            ),400)
        else:
            if(tf ==1):
                result = top10Kpi("24h")
                return make_response(jsonify(
                status = 'ok',
                data=result
            ),400)
            elif(tf ==7):
                result = top10Kpi("7d")
                return make_response(jsonify(
                status = 'ok',
                data=result
            ),400)
            else:
                return make_response(jsonify(
                status = 'error',
                message = "parameter (tf) is not valid"
            ),418)
            
        

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

api.add_resource(Todo1, '/',endpoint='')
if __name__ == '__main__':
    app.run(debug=True)
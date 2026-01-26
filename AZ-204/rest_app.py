from flask import Flask
from flask_restful import Api,Resource,request


app_  = Flask("REST")
api  =  Api(app_)


class SampleResource(Resource):
    def get(self,userId):
        return {"userId":userId}
    
    def post(self,userId):
        data = {}
        for k in request.form.items():
           data[k[0]] = k[1]
        return data



api.add_resource(SampleResource,"/sampleResource/<userId>")
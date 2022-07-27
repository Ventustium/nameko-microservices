import json
import bcrypt

from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from requests import session
from yaml import load

from werkzeug import Response

class UserGatewayService:
      name = 'user_gateway'
      #session_provider = SessionProvider()

      user_rpc = RpcProxy('user_service')

      @http('GET', '/api/user/email/')
      def checking_user_account_avaibility(self, request):
            # PLEASE CODE WITH SPECIFICATION BELOW

            ### RESPONSES

            # Checking User Account Availability
            # BODY:
            # {
            #     "status": "success",
            #     "data": {
            #           "name": "Kevin",
            #           "email_address": "kevin@kevin.com"
            #     }
            # }
            # STATUS CODE :
            # OK | 200

            # Checking User Account Availability
            # BODY:
            # {
            #     "status" : "error",
            #     "message" : "User not found"
            # }
            # STATUS CODE:
            # Not Found | 404
            email_address = request.get_json()["email_address"]
            json_response = self.user_rpc.checking_user_account_availability(email_address)
            # if json_response.get_json()["status"] == "success":
            #       print (json_response.get_json()["data"]["name"])
            # print(json_response["data"]["name"])
            response = Response(json.dumps(json_response), mimetype='application/json')
            response.status_code=200
            return response
      
      @http('POST', '/api/user/')
      def user_account_registration(self, request):
            email_address = request.get_json()["email_address"]
            check_email = self.user_rpc.checking_user_account_availability(email_address)
            if check_email["status"]=="success":
                  response = Response(json.dumps({
                        "status":"error",
                        "message":"Email already taken"
                  }), mimetype='application/json')
                  response.status_code=400
                  return response

            name = request.get_json()["name"]
            password = request.get_json()["password"]
            password = password.encode('utf-8')
            hashed_password= bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
            self.user_rpc.user_account_registration(name, email_address, hashed_password)
            response = Response(json.dumps({
                  "status" : "success",
                  "message" : "Account created successfully",
                  "data" : {
                        "name" : name,
                        "email_address" : email_address,
                        "password" : password.decode('utf-8')
                  }
            }), mimetype='application/json')
            response.status_code=201
            return response

      @http('POST','/api/user/login/')
      def login_user_account(self, request):
            email_address = request.get_json()["email_address"]
            password = request.get_json()["password"]

            if(self.user_rpc.login_user_account(email_address, password)):
                  response = Response(json.dumps({
                        "status":"success",
                        "message":"Logged in successfully"
                  }), mimetype='application/json')
                  response.status_code=200
                  return response

            response = Response(json.dumps({
                        "status":"error",
                        "message":"Unauthorized: invalid credentials (wrong email/password)"
            }), mimetype='application/json')
            response.status_code=401
            return response

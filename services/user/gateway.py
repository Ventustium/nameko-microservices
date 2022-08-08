import json
import bcrypt
import uuid

from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from dependencies.redis import SessionProvider

from werkzeug import Response

class UserGatewayService:
      name = 'user_gateway'
      session_provider = SessionProvider()

      user_rpc = RpcProxy('user_service')

      @http('GET', '/api/user/email')
      def checking_user_account_avaibility(self, request):
            # PLEASE CODE WITH SPECIFICATION BELOW

            ### RESPONSES

            # Checking User Account Availability
            # BODY:
            # {
            #     "status": "success",
            #     "data": {
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
      

      @http('POST', '/api/user')
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
            id_uuid = str(uuid.uuid4())
            hashed_password= bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
            self.user_rpc.user_account_registration(id_uuid, name, email_address, hashed_password)
            response = Response(json.dumps({
                  "status" : "success",
                  "message" : "Account created successfully",
                  "data" : {
                        "uuid" : id_uuid,
                        "name" : name,
                        "email_address" : email_address,
                        "password" : password.decode('utf-8')
                  }
            }), mimetype='application/json')
            response.status_code=201
            return response


      @http('POST','/api/user/login')
      def login_user_account(self, request):
            email_address = request.get_json()["email_address"]
            password = request.get_json()["password"]
            session_id=request.cookies.get('SESSID')
            if session_id:
                  session = self.session_provider.get_session_data(session_id)
                  if session:
                        json_response={"status":"error","message":"You are already logged in"}
                        response=Response(json.dumps(json_response), mimetype='application/json')
                        response.status_code=400
                        return response

            if(self.user_rpc.login_user_account(email_address, password)):
                  response = Response(json.dumps({
                        "status":"success",
                        "message":"Logged in successfully"
                  }), mimetype = 'application/json')
                  session_id = self.session_provider.generate_session_id()
                  user_data=self.user_rpc.checking_user_account_get_detail(email_address)
                  self.session_provider.set_session_data(session_id,json.dumps(user_data["data"]))
                  print(user_data)
                  response.set_cookie('SESSID', session_id)
                  response.status_code=200
                  return response

            response = Response(json.dumps({
                        "status":"error",
                        "message":"Unauthorized: invalid credentials (wrong email/password)"
            }), mimetype='application/json')
            response.status_code=401
            return response


      @http('POST', '/api/user/logout')
      def logout_user_account(self, request):
            session_id = request.cookies.get('SESSID')
            if session_id:
                  self.session_provider.destroy_session_data(session_id)
                  response=Response(json.dumps({"status":"success","message":"Logged out successfully"}),mimetype="application/json")
                  response.delete_cookie('SESSID')
                  response.status_code=200
                  return response
            response=Response(json.dumps({"status":"error","message":"You are not logged in"}),mimetype="application/json")
            response.status_code=400
            return response

      @http('GET', '/api/user/test/auth1')
      def user_test_auth(self, request):
            bearToken = request.headers.get("Authorization")
            password = request.get_json()["password"]
            if password == "hello":
                  response=Response(json.dumps({"status":"Success","message": "Hello There!"}),mimetype="application/json")
                  response.headers.set('Authorization', "Bearer HelloAgain")
                  response.status_code=200
                  return response
            if bearToken == "Bearer HelloAgain":
                  response=Response(json.dumps({"status":"Success","message": "Hello There Again!"}),mimetype="application/json")
                  response.headers.set('Authorization', "Bearer HelloAgain")
                  response.status_code=200
                  return response
            
            response=Response(json.dumps({"status":"Success","message": "Failed"}),mimetype="application/json")
            response.status_code=200
            return response
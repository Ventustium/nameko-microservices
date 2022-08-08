from ast import Return
import json
import bcrypt
import uuid

from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from dependencies.redis import SessionProvider

from werkzeug import Response

class UserLibraryGatewayService:
      name = 'user_library_gateway'
      session_provider = SessionProvider()

      user_library_rpc = RpcProxy('user_library_service')

      @http('GET', '/api/userlibrary')
      def checking_user_library_list(self, request):
            # PLEASE CODE WITH SPECIFICATION BELOW

            ### RESPONSES

            # Checking User Account Availability
            # BODY:
            # {
            #     "status": "success",
            #     "data": {
            #           "uuid" : "...."
            #           "title": "Book Title",
            #     }
            # }
            # STATUS CODE :
            # OK | 200

            # Checking User Account Availability
            # BODY:
            # {
            #     "status" : "error",
            #     "message" : "No favorite book"
            # }
            # STATUS CODE:
            # Not Found | 404

            cookies = request.cookies
            if cookies:
                  if self.session_provider.check_session_id(cookies['SESSID']):
                        json_response = self.session_provider.get_session_data(cookies['SESSID'])
                        if json_response:
                              json_response = json.loads(json_response)
                              data = self.user_library_rpc.checking_user_library_list(json_response['uuid'])
                              response=Response(json.dumps(data),mimetype="application/json")
                              response.status_code=200
                              return response
                  else:
                        response=Response(json.dumps({"status":"error","message":"Invalid session please re-login"}),mimetype="application/json")
                        return response

            else:
                  response=Response(json.dumps({"status":"error","message":"You are not logged in"}),mimetype="application/json")
                  return response
            
            # if json_response.get_json()["status"] == "success":
            #       print (json_response.get_json()["data"]["name"])
            # print(json_response["data"]["name"])

      @http('POST', '/api/userlibrary')
      def user_library_favorite_registration(self, request):
            cookies = request.cookies
            if cookies:
                  if self.session_provider.check_session_id(cookies['SESSID']):
                        sessid = self.session_provider.get_session_data(cookies['SESSID'])
                        
                        sessid = json.loads(sessid)
                        book_uuid = request.get_json()['uuid_book']
                        user_uuid = sessid['uuid']
                        
                        favorite = self.user_library_rpc.user_library_favorite_registration(user_uuid, book_uuid)
                        response=Response(json.dumps(favorite),mimetype="application/json")
                        return response
                        
                  else:
                        response=Response(json.dumps({"status":"error","message":"Invalid session please re-login"}),mimetype="application/json")
                        return response
            else:
                  response=Response(json.dumps({"status":"error","message":"You are not logged in"}),mimetype="application/json")
                  return response
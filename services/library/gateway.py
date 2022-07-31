from http import cookies
import json
import bcrypt

from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from requests import session
from yaml import load

from werkzeug import Response

class LibraryGateway:
      name = 'library_gateway'
      
      library_rpc = RpcProxy('library_service')

      @http('GET', '/api/library/lightnovel')
      def lightnovel_list(self, request):
            print("API CALLED")
            json_response = self.library_rpc.lightnovel_list()
            if json_response['status'] == "success":
                  response = Response(json.dumps(json_response), mimetype='application/json')
                  response.status_code=200
                  return response
            else:
                  response = Response(json.dumps(json_response), mimetype='application/json')
                  response.status_code=200
                  return response
      
      @http('GET', '/api/library/lightnovel/search/title/<string:title>')
      def lightnovel_search_title(self, request, title):
            json_response = self.library_rpc.checking_lightnovel_availability(title)
            response = Response(json.dumps(json_response), mimetype='application/json')
            response.status_code=200
            return response
      

      @http('GET', '/api/library/lightnovel/detail/<int:id>')
      def lightnovel_detail(self, request, id):
            json_response = self.library_rpc.lightnovel_detail(id)
            response = Response(json.dumps(json_response), mimetype='application/json')
            response.status_code=200
            return response
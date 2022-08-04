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

      @http('GET', '/api/library/book')
      def book_list(self, request):
            print("API CALLED")
            json_response = self.library_rpc.book_list()
            if json_response['status'] == "success":
                  response = Response(json.dumps(json_response), mimetype='application/json')
                  response.status_code=200
                  return response
            else:
                  response = Response(json.dumps(json_response), mimetype='application/json')
                  response.status_code=200
                  return response
      
      ### Add new Light Novel
      @http('POST', '/api/library/book')
      def book_add(self, request):
            request = request.form['data']
            json.dumps(request)
            jsondata =json.load(request)
            response = Response("Hello", mimetype='application/json')
            response.status_code=200
            return jsondata

      @http('GET', '/api/library/book/search/title/<string:title>')
      def book_search_title(self, request, title):
            json_response = self.library_rpc.checking_book_availability(title)
            response = Response(json.dumps(json_response), mimetype='application/json')
            response.status_code=200
            return response
      

      @http('GET', '/api/library/book/detail/<string:id_uuid>')
      def book_detail(self, request, id_uuid):
            json_response = self.library_rpc.book_detail(id_uuid)
            response = Response(json.dumps(json_response), mimetype='application/json')
            response.status_code=200
            return response
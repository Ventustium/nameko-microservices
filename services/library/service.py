from nameko.rpc import rpc
from dependencies.database import DatabaseProvider

class LibraryService:
      name = 'library_service'

      database = DatabaseProvider()

      @rpc
      def book_list(self):
            print("service book List Called")
            result = self.database.book_list()
            if result:
                  response = {
                        "status" : "success",
                        "data" : result
                  }
                  return response
            else:
                  return{
                        "status" : "error",
                        "message" : "No data"
                  }

      @rpc
      def checking_book_availability(self, title):
            result = self.database.checking_book_availability(title)
            if result:
                  print("succes")
                  response = {
                        "status" : "success",
                        "data" : result
                  }
                  return response
            else:
                  return{
                        "status" : "error",
                        "message" : "No data"
                  }
      @rpc
      def book_detail(self, id_uuid):
            result = self.database.book_detail(id_uuid)
            if result:
                  print("succes")
                  response = {
                        "status" : "success",
                        "data" : result
                  }
                  return response
            else:
                  return{
                        "status" : "error",
                        "message" : "No data"
                  }
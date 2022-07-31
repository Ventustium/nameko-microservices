from nameko.rpc import rpc
from dependencies.database import DatabaseProvider

class LibraryService:
      name = 'library_service'

      database = DatabaseProvider()

      @rpc
      def lightnovel_list(self):
            print("serviceLightNovelList Called")
            result = self.database.lightnovel_list()
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
      def checking_lightnovel_availability(self, title):
            result = self.database.checking_lightnovel_availability(title)
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
      def lightnovel_detail(self, id):
            result = self.database.lightnovel_detail(id)
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
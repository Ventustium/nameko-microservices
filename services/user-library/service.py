import re
from nameko.rpc import rpc
import bcrypt
from dependencies.database import DatabaseProvider

class UserService:
      name = 'user_library_service'

      database = DatabaseProvider()

      @rpc
      def checking_user_library_list(self, uuid):
            data = self.database.checking_user_library_list(uuid)
            if data:
                  return {
                        "status": "success",
                        "data": data
                        }
            else:
                  return{
                        "status": "error",
                        "message": "No favorite book"
                  }

      @rpc
      def checking_user_library_favorite(self, user_uuid, book_uuid):
            favorite = self.database.checking_user_library_favorite(user_uuid, book_uuid)
            if favorite:
                  return {
                        "status": "success",
                        "message" : "Already Favorite"
                  }
            else:
                  return{
                        "status": "error",
                        "message": "Books not found"
                  }

      @rpc
      def user_library_favorite_registration(self, user_uuid, book_uuid):
            if self.checking_user_library_favorite(user_uuid, book_uuid):
                  return {
                        "status": "success",
                        "message" : "Already Favorite"
                  }
            else:
                  if self.database.user_library_favorite_registration(user_uuid, book_uuid):
                        return {
                              "status": "success",
                              "message" : "Added to favorite"
                        }

                  else:
                        return {
                              "status": "success",
                              "message" : "Added to favorite"
                        }
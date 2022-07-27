from nameko.rpc import rpc
import bcrypt
from dependencies.database import DatabaseProvider

class UserService:
      name = 'user_service'

      database = DatabaseProvider()

      @rpc
      def checking_user_account_availability(self, email_address):
            user = self.database.checking_user_account_availability(email_address)
            if user:
                  return {
                        "status": "success",
                        "data": {
                              "id": user["id"],
                              "name": user["name"],
                              "email_address": user["email_address"]
                        }
                  }
            else:
                  return{
                        "status": "error",
                        "message": "User not found"
                  }

      @rpc
      def user_account_registration(self, name, email_address, password):
            return self.database.user_account_registration(name, email_address, password)
      
      @rpc
      def login_user_account(self, email_address, password):
            user = self.database.checking_user_account_availability(email_address)
            if user:
                  if bcrypt.checkpw(password.encode('UTF-8'), user["password"].encode('UTF-8')):
                        return True
                  return False

            
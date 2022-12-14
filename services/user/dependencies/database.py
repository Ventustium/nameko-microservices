import json
from nameko.extensions import DependencyProvider
import mysql.connector
from mysql.connector import Error
import mysql.connector.pooling
import os

class DatabaseWrapper:
      connection = None

      def __init__(self, connection):
            self.connection = connection
      
      def __del__(self):
            self.connection.close()

      def checking_user_account_availability(self, email_address):
            cursor = self.connection.cursor(dictionary=True)
            sql = """
                  SELECT * FROM user__users WHERE email_address = '{}'
            """.format(email_address)
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()

            return result
      
      def user_account_registration(self, id_uuid, name, email_address, password):
            cursor = self.connection.cursor(dictionary=True)
            sql = """
                  INSERT INTO user__users (uuid, name, email_address, password)
                  VALUES ('{}', '{}', '{}', '{}')
            """.format(id_uuid, name, email_address, password)
            cursor.execute(sql)
            self.connection.commit()
            cursor.close()


class DatabaseProvider(DependencyProvider):

      connection_pool = None

      def setup(self):
            try:

                  self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                        pool_size=8,
                        pool_reset_session=True,
                        host=os.environ.get('DB_HOST', '127.0.0.1'),
                        port=os.environ.get('DB_PORT', 3306),
                        database=os.environ.get('DB_NAME', 'nameko'),
                        user=os.environ.get('DB_USER', 'root'),
                        password=os.environ.get('DB_PASS', 'change_me')
                  )
            except Error as e:
                  print("Error while connecting to MySQL using Connection pool ", e)

      def get_dependency(self, worker_ctx):
            return DatabaseWrapper(self.connection_pool.get_connection())
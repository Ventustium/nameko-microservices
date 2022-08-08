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

      def checking_user_library_list(self, user_uuid):
            cursor = self.connection.cursor(dictionary=True)
            sql = """
                  SELECT user__books_favorite.book_uuid, user__books_favorite.status, library__books.title 
                  FROM user__books_favorite 
                  INNER JOIN library__books ON user__books_favorite.book_uuid = library__books.uuid
                  WHERE user_uuid = '{}'
            """.format(user_uuid)
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
      
      def user_library_favorite_registration(self, user_uuid, book_uuid):
            cursor = self.connection.cursor(dictionary=True)
            sql = """
                  INSERT INTO user__books_favorite (user_uuid, book_uuid, status)
                  VALUES ('{}', '{}', '1')
            """.format(user_uuid, book_uuid)
            cursor.execute(sql)
            self.connection.commit()
            cursor.close()

      def checking_user_library_favorite(self, user_uuid, book_uuid):
            cursor = self.connection.cursor(dictionary=True)
            sql = """
                  SELECT * FROM user__books_favorite WHERE user_uuid = '{}' AND book_uuid = '{}'
            """.format(user_uuid, book_uuid)
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()

            return result

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
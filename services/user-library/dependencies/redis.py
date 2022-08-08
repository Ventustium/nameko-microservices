import pickle
import uuid
import redis
from nameko.extensions import DependencyProvider
import os


class SessionWrapper:
    def __init__(self, connection) -> None:
        self.redis = connection
        self.default_expiration = 60 * 60

    ### SESSION TEMPLATE ###
    ### Feel free to remove or make changes ###

    def check_session_id(self, session_id):
        print (self.redis.exists(session_id))
        return self.redis.exists(session_id)

    def generate_session_id(self):
        key = str(uuid.uuid4())
        while self.check_session_id(key):
            key = str(uuid.uuid4())
        self.redis.set(key, pickle.dumps({}))
        return key

    def get_session_data(self, session_id):
            print(pickle.loads(self.redis.get(session_id)))
            return pickle.loads(self.redis.get(session_id))

    def set_session_data(self, session_id, data):
        self.redis.set(session_id, pickle.dumps(data))

    def reset_session_data(self, session_id):
        self.redis.set(session_id, pickle.dumps({}))

    def destroy_session_data(self, session_id):
        self.redis.delete(session_id)

    ### START YOUR CODE HERE ###

    # ...

    ### END YOUR CODE HERE ###


class SessionProvider(DependencyProvider):
    def __init__(self):
                # ACCEPT FROM INCOMING!!

        self.client = redis.Redis(host=os.environ.get('REDIS_HOST', '127.0.0.1'), port=os.environ.get('REDIS_PORT', 6379), db=0)

    def get_dependency(self, worker_ctx):
        return SessionWrapper(self.client)

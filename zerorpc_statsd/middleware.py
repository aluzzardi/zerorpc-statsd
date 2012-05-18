import time

class StatsdMiddleware(object):
    def __init__(self, statsd):
        self._statsd = statsd

    def call_procedure(self, procedure, *args, **kwargs):
        self._statsd.incr('zerorpc.requests')
        self._statsd.incr('zerorpc.requests.{0}'.format(procedure.__name__))
        start = time.time()
        try:
            return procedure(*args, **kwargs)
        except:
            self._statsd.incr('zerorpc.errors')
            self._statsd.incr('zerorpc.errors.{0}'.format(procedure.__name__))
            raise
        finally:
            dt = int((time.time() - start) * 1000)
            self._statsd.timing('zerorpc.response_time', dt)
            self._statsd.timing('zerorpc.response_time.{0}'.format(
                procedure.__name__), dt)

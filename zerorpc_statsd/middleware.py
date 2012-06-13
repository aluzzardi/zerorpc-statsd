import gevent.local
import time

class StatsdMiddleware(object):

    def __init__(self, statsd):
        self._statsd = statsd
        self._locals = gevent.local.local()

    @property
    def _exec_start(self):
        return self._locals.__dict__.get('_exec_start')

    @_exec_start.setter
    def _exec_start(self, ts):
        self._locals._exec_start = ts

    def _submit_response_time(self, procedure_name):
        dt = int((time.time() - self._exec_start) * 1000)
        self._statsd.timing('zerorpc.response_time', dt)
        self._statsd.timing(
            'zerorpc.response_time.{0}'.format(procedure_name),
            dt
        )

    def procedure_call_request(self, request_event):
        self._statsd.incr('zerorpc.requests')
        self._statsd.incr('zerorpc.requests.{0}'.format(request_event.name))
        self._exec_start = time.time()

    def procedure_call_reply(self, request_event, reply_event):
        self._submit_response_time(request_event.name)

    def inspect_error(self, task_context, request_event, reply_event, exc_info):
        # In the case of a NameError exception _exec_start will not have been
        # set but inspect_error will be called nonetheless. In that case we
        # can't submit the response_time.
        if self._exec_start:
            self._submit_response_time(request_event.name)
        self._statsd.incr('zerorpc.errors')
        self._statsd.incr('zerorpc.errors.{0}'.format(request_event.name))

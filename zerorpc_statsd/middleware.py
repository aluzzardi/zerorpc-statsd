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

    def server_before_exec(self, req_event):
        self._statsd.incr('zerorpc.requests')
        self._statsd.incr('zerorpc.requests.{0}'.format(req_event.name))
        self._exec_start = time.time()

    def server_after_exec(self, req_event, rep_event):
        self._submit_response_time(req_event.name)

    def server_inspect_exception(self, req_event, rep_event, task_context, exc_info):
        # In the case of a NameError exception _exec_start will not have been
        # set but inspect_error will be called nonetheless. In that case we
        # can't submit the response_time.
        if self._exec_start:
            self._submit_response_time(req_event.name)
        self._statsd.incr('zerorpc.errors')
        self._statsd.incr('zerorpc.errors.{0}'.format(req_event.name))

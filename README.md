# StatsD Middleware for ZeroRPC

A StatsD middleware to track requests and response times of ZeroRPC Services


```python

import zerorpc
import statsd
from zerorpc_statsd import StatsdMiddleware

# Create a statsd client
client = statsd.StatsClient()

# Register the middleware
zerorpc.Context.get_instance().register_middleware(StatsdMiddleware(client))

# Create a server as usual, it will be automatically tracked by the middleware

class Service(object):
    def do_something(self):
        pass

server = zerorpc.Server(Service())
server.bind('tcp://*:1234')
server.run()

```

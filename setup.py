try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='zerorpc_statsd',
    version='0.0.1',
    description='StatsD Middleware for ZeroRPC.',
    author='Andrea Luzzardi',
    author_email='andrea@luzzardi.com',
    url='https://github.com/aluzzardi/zerorpc-statsd',
    packages=['zerorpc_statsd'],
    install_requires=[
            'statsd>=0.5.1'
    ],
    license='MIT'
)

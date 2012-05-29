try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='zerorpc-statsd',
    version='0.1.0',
    description='StatsD Middleware for ZeroRPC.',
    author='Andrea Luzzardi',
    author_email='andrea@luzzardi.com',
    url='https://github.com/aluzzardi/zerorpc-statsd',
    packages=['zerorpc_statsd'],
    install_requires=[
            'statsd>=0.5.1'
    ],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)

from decouple import config as env_config

# ------- Debugging -------

DEBUG = env_config("DEBUG", False, cast=bool)
reload = True if DEBUG else False

# ------- Logging -------

accesslog = "-"
errorlog = "-"
loglevel = "debug" if DEBUG else "info"

# ------- Security -------

limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# ------- Server Mechanics -------

preload_app = False
forwarded_allow_ips = "*"
proxy_allow_ips = "*"

# ------- Server Socket -------

LOCAL = env_config("PHASE", "local") == "local"
host = "127.0.0.1" if LOCAL else "0.0.0.0"
port = "8080"
bind = "{host}:{port}".format(host=host, port=port)
backlog = 2048

# ------- Worker Processes -------

workers = 5
worker_class = "gevent"
threads = 1
worker_connections = 1500
max_requests = 0
max_requests_jitter = 0
timeout = 120

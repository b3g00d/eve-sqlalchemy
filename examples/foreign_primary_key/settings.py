from eve_sqlalchemy.config import DomainConfig, ResourceConfig

from foreign_primary_key.domain import Lock, Node

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite://'
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESOURCE_METHODS = ['GET', 'POST']

# The following two lines will output the SQL statements executed by
# SQLAlchemy. This is useful while debugging and in development, but is turned
# off by default.
# --------
# SQLALCHEMY_ECHO = True
# SQLALCHEMY_RECORD_QUERIES = True

# The default schema is generated using DomainConfig:
DOMAIN = DomainConfig({
    'nodes': ResourceConfig(Node),
    'locks': ResourceConfig(Lock)
}).render()

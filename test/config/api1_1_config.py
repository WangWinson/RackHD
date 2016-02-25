from settings import * 
from on_http import Configuration, ApiClient

config = Configuration() 
config.host = 'http://{0}:{1}'.format(HOST_IP,HOST_PORT)
config.host_authed = 'https://{0}:{1}'.format(HOST_IP,HOST_PORT_AUTH)
config.verify_ssl = False
config.api_client = ApiClient(host=config.host)
config.api_client_authed = ApiClient(host=config.host_authed)
config.auth_enabled = False
config.debug = False
config.logger_format = LOGFORMAT
for key,elem in config.logger.iteritems():
    elem.setLevel(LOGLEVELS[LOGGER_LVL])

from config.api1_1_config import *
from modules.logger import Log
from modules.auth import Auth
from on_http import NodesApi as Nodes
from on_http import rest
from proboscis.asserts import assert_equal
# from proboscis.asserts import assert_false
from proboscis.asserts import assert_raises
from proboscis.asserts import assert_not_equal
# from proboscis.asserts import assert_true
from proboscis import before_class
from proboscis import after_class
# from proboscis import SkipTest
from proboscis import test
from json import loads

LOG = Log(__name__)

@test(groups=['auth.tests'])
class AuthTests(object):

    def __init__(self):
        self.__client = config.api_client
        self.__auth = Auth()
        self.__nodeApi = Nodes()

    @before_class()
    def setup(self):
        """setup test environment"""
        self.__auth.enable()

    @after_class(always_run=True)
    def teardown(self):
        """ restore test environment """
        self.__auth.disable()

    # @test(groups=['enable-auth'])
    # def enable_auth(self):
    #     """ Testing enable auth """
    #     self.__auth.enable()

    @test(groups=['test-nodes-withauth'])
    def test_nodes(self):
        """ Testing GET:/nodes """
        self.__nodeApi.api1_1_nodes_get()
        nodes = loads(self.__client.last_response.data)
        LOG.debug(nodes, json=True)
        assert_not_equal(0, len(nodes), message='Node list was empty!')

    # @test(groups=['disable-auth'])
    # def disable_auth(self):
    #     """ Testing disable auth """
    #     self.__auth.disable()

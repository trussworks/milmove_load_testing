"""
    my.move.mil

    The internal/website API for my.move.mil  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import internal_client
from internal_client.api.service_members_api import ServiceMembersApi  # noqa: E501


class TestServiceMembersApi(unittest.TestCase):
    """ServiceMembersApi unit test stubs"""

    def setUp(self):
        self.api = ServiceMembersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_service_member(self):
        """Test case for create_service_member

        Creates service member for a logged-in user  # noqa: E501
        """
        pass

    def test_patch_service_member(self):
        """Test case for patch_service_member

        Patches the service member  # noqa: E501
        """
        pass

    def test_show_service_member(self):
        """Test case for show_service_member

        Returns the given service member  # noqa: E501
        """
        pass

    def test_show_service_member_orders(self):
        """Test case for show_service_member_orders

        Returns the latest orders for a given service member  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

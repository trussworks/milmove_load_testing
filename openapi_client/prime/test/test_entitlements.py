"""
    MilMove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import prime_client
from prime_client.model.entitlements import Entitlements


class TestEntitlements(unittest.TestCase):
    """Entitlements unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEntitlements(self):
        """Test Entitlements"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Entitlements()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ghc_client
from ghc_client.model.affiliation import Affiliation
from ghc_client.model.grade import Grade
globals()['Affiliation'] = Affiliation
globals()['Grade'] = Grade
from ghc_client.model.update_allowance_payload import UpdateAllowancePayload


class TestUpdateAllowancePayload(unittest.TestCase):
    """UpdateAllowancePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateAllowancePayload(self):
        """Test UpdateAllowancePayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UpdateAllowancePayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
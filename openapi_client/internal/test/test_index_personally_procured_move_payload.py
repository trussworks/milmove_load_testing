"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import internal_client
from internal_client.model.personally_procured_move_payload import PersonallyProcuredMovePayload
globals()['PersonallyProcuredMovePayload'] = PersonallyProcuredMovePayload
from internal_client.model.index_personally_procured_move_payload import IndexPersonallyProcuredMovePayload


class TestIndexPersonallyProcuredMovePayload(unittest.TestCase):
    """IndexPersonallyProcuredMovePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIndexPersonallyProcuredMovePayload(self):
        """Test IndexPersonallyProcuredMovePayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IndexPersonallyProcuredMovePayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

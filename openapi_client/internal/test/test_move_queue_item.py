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
from internal_client.model.service_member_rank import ServiceMemberRank
from internal_client.model.weight_allotment import WeightAllotment
globals()['ServiceMemberRank'] = ServiceMemberRank
globals()['WeightAllotment'] = WeightAllotment
from internal_client.model.move_queue_item import MoveQueueItem


class TestMoveQueueItem(unittest.TestCase):
    """MoveQueueItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMoveQueueItem(self):
        """Test MoveQueueItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MoveQueueItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

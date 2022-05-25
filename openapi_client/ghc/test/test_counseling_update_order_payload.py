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
from ghc_client.model.dept_indicator import DeptIndicator
from ghc_client.model.orders_type import OrdersType
from ghc_client.model.orders_type_detail import OrdersTypeDetail
globals()['DeptIndicator'] = DeptIndicator
globals()['OrdersType'] = OrdersType
globals()['OrdersTypeDetail'] = OrdersTypeDetail
from ghc_client.model.counseling_update_order_payload import CounselingUpdateOrderPayload


class TestCounselingUpdateOrderPayload(unittest.TestCase):
    """CounselingUpdateOrderPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCounselingUpdateOrderPayload(self):
        """Test CounselingUpdateOrderPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CounselingUpdateOrderPayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
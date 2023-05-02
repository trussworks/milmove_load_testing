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
from internal_client.model.dept_indicator import DeptIndicator
from internal_client.model.document import Document
from internal_client.model.duty_location_payload import DutyLocationPayload
from internal_client.model.entitlement import Entitlement
from internal_client.model.index_moves_payload import IndexMovesPayload
from internal_client.model.orders_status import OrdersStatus
from internal_client.model.orders_type import OrdersType
from internal_client.model.orders_type_detail import OrdersTypeDetail
globals()['DeptIndicator'] = DeptIndicator
globals()['Document'] = Document
globals()['DutyLocationPayload'] = DutyLocationPayload
globals()['Entitlement'] = Entitlement
globals()['IndexMovesPayload'] = IndexMovesPayload
globals()['OrdersStatus'] = OrdersStatus
globals()['OrdersType'] = OrdersType
globals()['OrdersTypeDetail'] = OrdersTypeDetail
from internal_client.model.orders import Orders


class TestOrders(unittest.TestCase):
    """Orders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrders(self):
        """Test Orders"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Orders()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

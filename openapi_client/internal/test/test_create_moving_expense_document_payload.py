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
from internal_client.model.move_document_type import MoveDocumentType
from internal_client.model.moving_expense_type import MovingExpenseType
globals()['MoveDocumentType'] = MoveDocumentType
globals()['MovingExpenseType'] = MovingExpenseType
from internal_client.model.create_moving_expense_document_payload import CreateMovingExpenseDocumentPayload


class TestCreateMovingExpenseDocumentPayload(unittest.TestCase):
    """CreateMovingExpenseDocumentPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateMovingExpenseDocumentPayload(self):
        """Test CreateMovingExpenseDocumentPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateMovingExpenseDocumentPayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

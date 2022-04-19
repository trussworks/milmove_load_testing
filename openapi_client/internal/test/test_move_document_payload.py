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
from internal_client.model.document_payload import DocumentPayload
from internal_client.model.move_document_status import MoveDocumentStatus
from internal_client.model.move_document_type import MoveDocumentType
from internal_client.model.moving_expense_type import MovingExpenseType
from internal_client.model.weight_ticket_set_type import WeightTicketSetType
globals()['DocumentPayload'] = DocumentPayload
globals()['MoveDocumentStatus'] = MoveDocumentStatus
globals()['MoveDocumentType'] = MoveDocumentType
globals()['MovingExpenseType'] = MovingExpenseType
globals()['WeightTicketSetType'] = WeightTicketSetType
from internal_client.model.move_document_payload import MoveDocumentPayload


class TestMoveDocumentPayload(unittest.TestCase):
    """MoveDocumentPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMoveDocumentPayload(self):
        """Test MoveDocumentPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MoveDocumentPayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

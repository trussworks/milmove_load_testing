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
from internal_client.model.method_of_receipt import MethodOfReceipt
globals()['MethodOfReceipt'] = MethodOfReceipt
from internal_client.model.create_reimbursement import CreateReimbursement


class TestCreateReimbursement(unittest.TestCase):
    """CreateReimbursement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateReimbursement(self):
        """Test CreateReimbursement"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateReimbursement()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

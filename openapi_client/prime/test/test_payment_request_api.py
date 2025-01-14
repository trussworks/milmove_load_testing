"""
    MilMove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import prime_client
from prime_client.api.payment_request_api import PaymentRequestApi  # noqa: E501


class TestPaymentRequestApi(unittest.TestCase):
    """PaymentRequestApi unit test stubs"""

    def setUp(self):
        self.api = PaymentRequestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_payment_request(self):
        """Test case for create_payment_request

        createPaymentRequest  # noqa: E501
        """
        pass

    def test_create_upload(self):
        """Test case for create_upload

        createUpload  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

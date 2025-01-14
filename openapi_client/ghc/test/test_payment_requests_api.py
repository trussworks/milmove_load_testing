"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import ghc_client
from ghc_client.api.payment_requests_api import PaymentRequestsApi  # noqa: E501


class TestPaymentRequestsApi(unittest.TestCase):
    """PaymentRequestsApi unit test stubs"""

    def setUp(self):
        self.api = PaymentRequestsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_payment_request(self):
        """Test case for get_payment_request

        Fetches a payment request by id  # noqa: E501
        """
        pass

    def test_get_payment_requests_for_move(self):
        """Test case for get_payment_requests_for_move

        Fetches payment requests using the move code (locator).  # noqa: E501
        """
        pass

    def test_get_shipments_payment_sit_balance(self):
        """Test case for get_shipments_payment_sit_balance

        Returns all shipment payment request SIT usage to support partial SIT invoicing  # noqa: E501
        """
        pass

    def test_update_payment_request_status(self):
        """Test case for update_payment_request_status

        Updates status of a payment request by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

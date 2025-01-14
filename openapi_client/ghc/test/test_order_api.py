"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import ghc_client
from ghc_client.api.order_api import OrderApi  # noqa: E501


class TestOrderApi(unittest.TestCase):
    """OrderApi unit test stubs"""

    def setUp(self):
        self.api = OrderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_acknowledge_excess_weight_risk(self):
        """Test case for acknowledge_excess_weight_risk

        Saves the date and time a TOO acknowledged the excess weight risk by dismissing the alert  # noqa: E501
        """
        pass

    def test_counseling_update_allowance(self):
        """Test case for counseling_update_allowance

        Updates an allowance (Orders with Entitlements)  # noqa: E501
        """
        pass

    def test_counseling_update_order(self):
        """Test case for counseling_update_order

        Updates an order (performed by a services counselor)  # noqa: E501
        """
        pass

    def test_get_order(self):
        """Test case for get_order

        Gets an order by ID  # noqa: E501
        """
        pass

    def test_tac_validation(self):
        """Test case for tac_validation

        Validation of a TAC value  # noqa: E501
        """
        pass

    def test_update_allowance(self):
        """Test case for update_allowance

        Updates an allowance (Orders with Entitlements)  # noqa: E501
        """
        pass

    def test_update_billable_weight(self):
        """Test case for update_billable_weight

        Updates the max billable weight  # noqa: E501
        """
        pass

    def test_update_max_billable_weight_as_tio(self):
        """Test case for update_max_billable_weight_as_tio

        Updates the max billable weight with TIO remarks  # noqa: E501
        """
        pass

    def test_update_order(self):
        """Test case for update_order

        Updates an order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

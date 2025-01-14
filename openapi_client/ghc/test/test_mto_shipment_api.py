"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import ghc_client
from ghc_client.api.mto_shipment_api import MtoShipmentApi  # noqa: E501


class TestMtoShipmentApi(unittest.TestCase):
    """MtoShipmentApi unit test stubs"""

    def setUp(self):
        self.api = MtoShipmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_mto_shipment(self):
        """Test case for create_mto_shipment

        createMTOShipment  # noqa: E501
        """
        pass

    def test_get_shipment(self):
        """Test case for get_shipment

        fetches a shipment by ID  # noqa: E501
        """
        pass

    def test_list_mto_shipments(self):
        """Test case for list_mto_shipments

        Gets all shipments for a move task order  # noqa: E501
        """
        pass

    def test_update_mto_shipment(self):
        """Test case for update_mto_shipment

        updateMTOShipment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

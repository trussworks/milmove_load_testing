"""
    MilMove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import prime_client
from prime_client.model.address import Address
from prime_client.model.destination_type import DestinationType
from prime_client.model.mto_shipment_type import MTOShipmentType
from prime_client.model.storage_facility import StorageFacility
globals()['Address'] = Address
globals()['DestinationType'] = DestinationType
globals()['MTOShipmentType'] = MTOShipmentType
globals()['StorageFacility'] = StorageFacility
from prime_client.model.update_mto_shipment import UpdateMTOShipment


class TestUpdateMTOShipment(unittest.TestCase):
    """UpdateMTOShipment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateMTOShipment(self):
        """Test UpdateMTOShipment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UpdateMTOShipment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
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
from prime_client.model.destination_type import DestinationType
from prime_client.model.mto_agents import MTOAgents
from prime_client.model.mto_service_item import MTOServiceItem
from prime_client.model.mto_shipment_destination_address import MTOShipmentDestinationAddress
from prime_client.model.mto_shipment_pickup_address import MTOShipmentPickupAddress
from prime_client.model.mto_shipment_secondary_delivery_address import MTOShipmentSecondaryDeliveryAddress
from prime_client.model.mto_shipment_secondary_pickup_address import MTOShipmentSecondaryPickupAddress
from prime_client.model.mto_shipment_storage_facility import MTOShipmentStorageFacility
from prime_client.model.mto_shipment_type import MTOShipmentType
from prime_client.model.ppm_shipment import PPMShipment
from prime_client.model.reweigh import Reweigh
from prime_client.model.sit_extensions import SITExtensions
globals()['DestinationType'] = DestinationType
globals()['MTOAgents'] = MTOAgents
globals()['MTOServiceItem'] = MTOServiceItem
globals()['MTOShipmentDestinationAddress'] = MTOShipmentDestinationAddress
globals()['MTOShipmentPickupAddress'] = MTOShipmentPickupAddress
globals()['MTOShipmentSecondaryDeliveryAddress'] = MTOShipmentSecondaryDeliveryAddress
globals()['MTOShipmentSecondaryPickupAddress'] = MTOShipmentSecondaryPickupAddress
globals()['MTOShipmentStorageFacility'] = MTOShipmentStorageFacility
globals()['MTOShipmentType'] = MTOShipmentType
globals()['PPMShipment'] = PPMShipment
globals()['Reweigh'] = Reweigh
globals()['SITExtensions'] = SITExtensions
from prime_client.model.mto_shipment import MTOShipment


class TestMTOShipment(unittest.TestCase):
    """MTOShipment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMTOShipment(self):
        """Test MTOShipment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MTOShipment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

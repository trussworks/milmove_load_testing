"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ghc_client
from ghc_client.model.omittable_ppm_document_status import OmittablePPMDocumentStatus
from ghc_client.model.weight_ticket_empty_document import WeightTicketEmptyDocument
from ghc_client.model.weight_ticket_full_document import WeightTicketFullDocument
from ghc_client.model.weight_ticket_proof_of_trailer_ownership_document import WeightTicketProofOfTrailerOwnershipDocument
globals()['OmittablePPMDocumentStatus'] = OmittablePPMDocumentStatus
globals()['WeightTicketEmptyDocument'] = WeightTicketEmptyDocument
globals()['WeightTicketFullDocument'] = WeightTicketFullDocument
globals()['WeightTicketProofOfTrailerOwnershipDocument'] = WeightTicketProofOfTrailerOwnershipDocument
from ghc_client.model.weight_ticket import WeightTicket


class TestWeightTicket(unittest.TestCase):
    """WeightTicket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWeightTicket(self):
        """Test WeightTicket"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WeightTicket()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
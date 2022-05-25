"""
    MilMove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import prime_client
from prime_client.api.move_task_order_api import MoveTaskOrderApi  # noqa: E501


class TestMoveTaskOrderApi(unittest.TestCase):
    """MoveTaskOrderApi unit test stubs"""

    def setUp(self):
        self.api = MoveTaskOrderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_excess_weight_record(self):
        """Test case for create_excess_weight_record

        createExcessWeightRecord  # noqa: E501
        """
        pass

    def test_get_move_task_order(self):
        """Test case for get_move_task_order

        getMoveTaskOrder  # noqa: E501
        """
        pass

    def test_list_moves(self):
        """Test case for list_moves

        listMoves  # noqa: E501
        """
        pass

    def test_update_mto_post_counseling_information(self):
        """Test case for update_mto_post_counseling_information

        updateMTOPostCounselingInformation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
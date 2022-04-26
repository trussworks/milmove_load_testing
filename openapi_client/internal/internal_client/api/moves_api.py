"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from internal_client.api_client import ApiClient, Endpoint as _Endpoint
from internal_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from internal_client.model.move_dates_summary import MoveDatesSummary
from internal_client.model.move_payload import MovePayload
from internal_client.model.patch_move_payload import PatchMovePayload
from internal_client.model.submit_move_for_approval_payload import SubmitMoveForApprovalPayload


class MovesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.patch_move_endpoint = _Endpoint(
            settings={
                'response_type': (MovePayload,),
                'auth': [],
                'endpoint_path': '/moves/{moveId}',
                'operation_id': 'patch_move',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_id',
                    'patch_move_payload',
                ],
                'required': [
                    'move_id',
                    'patch_move_payload',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'move_id':
                        (str,),
                    'patch_move_payload':
                        (PatchMovePayload,),
                },
                'attribute_map': {
                    'move_id': 'moveId',
                },
                'location_map': {
                    'move_id': 'path',
                    'patch_move_payload': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.show_move_endpoint = _Endpoint(
            settings={
                'response_type': (MovePayload,),
                'auth': [],
                'endpoint_path': '/moves/{moveId}',
                'operation_id': 'show_move',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_id',
                ],
                'required': [
                    'move_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'move_id':
                        (str,),
                },
                'attribute_map': {
                    'move_id': 'moveId',
                },
                'location_map': {
                    'move_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.show_move_dates_summary_endpoint = _Endpoint(
            settings={
                'response_type': (MoveDatesSummary,),
                'auth': [],
                'endpoint_path': '/moves/{moveId}/move_dates_summary',
                'operation_id': 'show_move_dates_summary',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_id',
                    'move_date',
                ],
                'required': [
                    'move_id',
                    'move_date',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'move_id':
                        (str,),
                    'move_date':
                        (date,),
                },
                'attribute_map': {
                    'move_id': 'moveId',
                    'move_date': 'moveDate',
                },
                'location_map': {
                    'move_id': 'path',
                    'move_date': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.show_shipment_summary_worksheet_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [],
                'endpoint_path': '/moves/{moveId}/shipment_summary_worksheet',
                'operation_id': 'show_shipment_summary_worksheet',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_id',
                    'preparation_date',
                ],
                'required': [
                    'move_id',
                    'preparation_date',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'move_id':
                        (str,),
                    'preparation_date':
                        (date,),
                },
                'attribute_map': {
                    'move_id': 'moveId',
                    'preparation_date': 'preparationDate',
                },
                'location_map': {
                    'move_id': 'path',
                    'preparation_date': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/pdf'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.submit_amended_orders_endpoint = _Endpoint(
            settings={
                'response_type': (MovePayload,),
                'auth': [],
                'endpoint_path': '/moves/{moveId}/submit_amended_orders',
                'operation_id': 'submit_amended_orders',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_id',
                ],
                'required': [
                    'move_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'move_id':
                        (str,),
                },
                'attribute_map': {
                    'move_id': 'moveId',
                },
                'location_map': {
                    'move_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.submit_move_for_approval_endpoint = _Endpoint(
            settings={
                'response_type': (MovePayload,),
                'auth': [],
                'endpoint_path': '/moves/{moveId}/submit',
                'operation_id': 'submit_move_for_approval',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_id',
                    'submit_move_for_approval_payload',
                ],
                'required': [
                    'move_id',
                    'submit_move_for_approval_payload',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'move_id':
                        (str,),
                    'submit_move_for_approval_payload':
                        (SubmitMoveForApprovalPayload,),
                },
                'attribute_map': {
                    'move_id': 'moveId',
                },
                'location_map': {
                    'move_id': 'path',
                    'submit_move_for_approval_payload': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def patch_move(
        self,
        move_id,
        patch_move_payload,
        **kwargs
    ):
        """Patches the move  # noqa: E501

        Any fields sent in this request will be set on the move referenced  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_move(move_id, patch_move_payload, async_req=True)
        >>> result = thread.get()

        Args:
            move_id (str): UUID of the move
            patch_move_payload (PatchMovePayload):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MovePayload
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['move_id'] = \
            move_id
        kwargs['patch_move_payload'] = \
            patch_move_payload
        return self.patch_move_endpoint.call_with_http_info(**kwargs)

    def show_move(
        self,
        move_id,
        **kwargs
    ):
        """Returns the given move  # noqa: E501

        Returns the given move  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.show_move(move_id, async_req=True)
        >>> result = thread.get()

        Args:
            move_id (str): UUID of the move

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MovePayload
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['move_id'] = \
            move_id
        return self.show_move_endpoint.call_with_http_info(**kwargs)

    def show_move_dates_summary(
        self,
        move_id,
        move_date,
        **kwargs
    ):
        """Returns projected move-related dates for a given move date  # noqa: E501

        Returns projected move-related dates for a given move date  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.show_move_dates_summary(move_id, move_date, async_req=True)
        >>> result = thread.get()

        Args:
            move_id (str): UUID of the move
            move_date (date): The chosen move date

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MoveDatesSummary
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['move_id'] = \
            move_id
        kwargs['move_date'] = \
            move_date
        return self.show_move_dates_summary_endpoint.call_with_http_info(**kwargs)

    def show_shipment_summary_worksheet(
        self,
        move_id,
        preparation_date,
        **kwargs
    ):
        """Returns Shipment Summary Worksheet  # noqa: E501

        Generates pre-filled PDF using data already collected  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.show_shipment_summary_worksheet(move_id, preparation_date, async_req=True)
        >>> result = thread.get()

        Args:
            move_id (str): UUID of the move
            preparation_date (date): The preparationDate of PDF

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['move_id'] = \
            move_id
        kwargs['preparation_date'] = \
            preparation_date
        return self.show_shipment_summary_worksheet_endpoint.call_with_http_info(**kwargs)

    def submit_amended_orders(
        self,
        move_id,
        **kwargs
    ):
        """Submits amended orders for review  # noqa: E501

        Submits amended orders for review by the office. The status of the move will be updated to an appropriate status depending on whether it needs services counseling or not.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.submit_amended_orders(move_id, async_req=True)
        >>> result = thread.get()

        Args:
            move_id (str): UUID of the move

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MovePayload
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['move_id'] = \
            move_id
        return self.submit_amended_orders_endpoint.call_with_http_info(**kwargs)

    def submit_move_for_approval(
        self,
        move_id,
        submit_move_for_approval_payload,
        **kwargs
    ):
        """Submits a move for approval  # noqa: E501

        Submits a move for approval by the office. The status of the move will be updated to SUBMITTED  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.submit_move_for_approval(move_id, submit_move_for_approval_payload, async_req=True)
        >>> result = thread.get()

        Args:
            move_id (str): UUID of the move
            submit_move_for_approval_payload (SubmitMoveForApprovalPayload):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MovePayload
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['move_id'] = \
            move_id
        kwargs['submit_move_for_approval_payload'] = \
            submit_move_for_approval_payload
        return self.submit_move_for_approval_endpoint.call_with_http_info(**kwargs)


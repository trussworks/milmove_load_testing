"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ghc_client.api_client import ApiClient, Endpoint as _Endpoint
from ghc_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ghc_client.model.error import Error
from ghc_client.model.payment_request import PaymentRequest
from ghc_client.model.payment_requests import PaymentRequests
from ghc_client.model.shipments_payment_sit_balance import ShipmentsPaymentSITBalance
from ghc_client.model.update_payment_request_status_payload import UpdatePaymentRequestStatusPayload
from ghc_client.model.validation_error import ValidationError


class PaymentRequestsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_payment_request_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentRequest,),
                'auth': [],
                'endpoint_path': '/payment-requests/{paymentRequestID}',
                'operation_id': 'get_payment_request',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_request_id',
                ],
                'required': [
                    'payment_request_id',
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
                    'payment_request_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_request_id': 'paymentRequestID',
                },
                'location_map': {
                    'payment_request_id': 'path',
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
        self.get_payment_requests_for_move_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentRequests,),
                'auth': [],
                'endpoint_path': '/moves/{locator}/payment-requests',
                'operation_id': 'get_payment_requests_for_move',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'locator',
                ],
                'required': [
                    'locator',
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
                    'locator':
                        (str,),
                },
                'attribute_map': {
                    'locator': 'locator',
                },
                'location_map': {
                    'locator': 'path',
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
        self.get_shipments_payment_sit_balance_endpoint = _Endpoint(
            settings={
                'response_type': (ShipmentsPaymentSITBalance,),
                'auth': [],
                'endpoint_path': '/payment-requests/{paymentRequestID}/shipments-payment-sit-balance',
                'operation_id': 'get_shipments_payment_sit_balance',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_request_id',
                ],
                'required': [
                    'payment_request_id',
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
                    'payment_request_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_request_id': 'paymentRequestID',
                },
                'location_map': {
                    'payment_request_id': 'path',
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
        self.update_payment_request_status_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentRequest,),
                'auth': [],
                'endpoint_path': '/payment-requests/{paymentRequestID}/status',
                'operation_id': 'update_payment_request_status',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_request_id',
                    'if_match',
                    'body',
                ],
                'required': [
                    'payment_request_id',
                    'if_match',
                    'body',
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
                    'payment_request_id':
                        (str,),
                    'if_match':
                        (str,),
                    'body':
                        (UpdatePaymentRequestStatusPayload,),
                },
                'attribute_map': {
                    'payment_request_id': 'paymentRequestID',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'payment_request_id': 'path',
                    'if_match': 'header',
                    'body': 'body',
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

    def get_payment_request(
        self,
        payment_request_id,
        **kwargs
    ):
        """Fetches a payment request by id  # noqa: E501

        Fetches an instance of a payment request by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payment_request(payment_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_request_id (str): UUID of payment request

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
            PaymentRequest
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
        kwargs['payment_request_id'] = \
            payment_request_id
        return self.get_payment_request_endpoint.call_with_http_info(**kwargs)

    def get_payment_requests_for_move(
        self,
        locator,
        **kwargs
    ):
        """Fetches payment requests using the move code (locator).  # noqa: E501

        Fetches payment requests for a move  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payment_requests_for_move(locator, async_req=True)
        >>> result = thread.get()

        Args:
            locator (str): move code to identify a move for payment requests

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
            PaymentRequests
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
        kwargs['locator'] = \
            locator
        return self.get_payment_requests_for_move_endpoint.call_with_http_info(**kwargs)

    def get_shipments_payment_sit_balance(
        self,
        payment_request_id,
        **kwargs
    ):
        """Returns all shipment payment request SIT usage to support partial SIT invoicing  # noqa: E501

        Returns all shipment payment request SIT usage to support partial SIT invoicing  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_shipments_payment_sit_balance(payment_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_request_id (str): payment request ID of the payment request with SIT service items being reviewed

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
            ShipmentsPaymentSITBalance
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
        kwargs['payment_request_id'] = \
            payment_request_id
        return self.get_shipments_payment_sit_balance_endpoint.call_with_http_info(**kwargs)

    def update_payment_request_status(
        self,
        payment_request_id,
        if_match,
        body,
        **kwargs
    ):
        """Updates status of a payment request by id  # noqa: E501

        Updates status of a payment request by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_payment_request_status(payment_request_id, if_match, body, async_req=True)
        >>> result = thread.get()

        Args:
            payment_request_id (str): UUID of payment request
            if_match (str):
            body (UpdatePaymentRequestStatusPayload):

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
            PaymentRequest
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
        kwargs['payment_request_id'] = \
            payment_request_id
        kwargs['if_match'] = \
            if_match
        kwargs['body'] = \
            body
        return self.update_payment_request_status_endpoint.call_with_http_info(**kwargs)


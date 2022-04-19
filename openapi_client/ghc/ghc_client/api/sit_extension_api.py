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
from ghc_client.model.approve_sit_extension import ApproveSITExtension
from ghc_client.model.create_sit_extension_as_too import CreateSITExtensionAsTOO
from ghc_client.model.deny_sit_extension import DenySITExtension
from ghc_client.model.error import Error
from ghc_client.model.mto_shipment import MTOShipment
from ghc_client.model.validation_error import ValidationError


class SitExtensionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.approve_sit_extension_endpoint = _Endpoint(
            settings={
                'response_type': (MTOShipment,),
                'auth': [],
                'endpoint_path': '/shipments/{shipmentID}/sit-extensions/{sitExtensionID}/approve',
                'operation_id': 'approve_sit_extension',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'shipment_id',
                    'sit_extension_id',
                    'if_match',
                    'body',
                ],
                'required': [
                    'shipment_id',
                    'sit_extension_id',
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
                    'shipment_id':
                        (str,),
                    'sit_extension_id':
                        (str,),
                    'if_match':
                        (str,),
                    'body':
                        (ApproveSITExtension,),
                },
                'attribute_map': {
                    'shipment_id': 'shipmentID',
                    'sit_extension_id': 'sitExtensionID',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'shipment_id': 'path',
                    'sit_extension_id': 'path',
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
        self.create_sit_extension_as_too_endpoint = _Endpoint(
            settings={
                'response_type': (MTOShipment,),
                'auth': [],
                'endpoint_path': '/shipments/{shipmentID}/sit-extensions/',
                'operation_id': 'create_sit_extension_as_too',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'shipment_id',
                    'if_match',
                    'body',
                ],
                'required': [
                    'shipment_id',
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
                    'shipment_id':
                        (str,),
                    'if_match':
                        (str,),
                    'body':
                        (CreateSITExtensionAsTOO,),
                },
                'attribute_map': {
                    'shipment_id': 'shipmentID',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'shipment_id': 'path',
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
        self.deny_sit_extension_endpoint = _Endpoint(
            settings={
                'response_type': (MTOShipment,),
                'auth': [],
                'endpoint_path': '/shipments/{shipmentID}/sit-extensions/{sitExtensionID}/deny',
                'operation_id': 'deny_sit_extension',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'shipment_id',
                    'sit_extension_id',
                    'if_match',
                    'body',
                ],
                'required': [
                    'shipment_id',
                    'sit_extension_id',
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
                    'shipment_id':
                        (str,),
                    'sit_extension_id':
                        (str,),
                    'if_match':
                        (str,),
                    'body':
                        (DenySITExtension,),
                },
                'attribute_map': {
                    'shipment_id': 'shipmentID',
                    'sit_extension_id': 'sitExtensionID',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'shipment_id': 'path',
                    'sit_extension_id': 'path',
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

    def approve_sit_extension(
        self,
        shipment_id,
        sit_extension_id,
        if_match,
        body,
        **kwargs
    ):
        """Approves a SIT extension  # noqa: E501

        Approves a SIT extension  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.approve_sit_extension(shipment_id, sit_extension_id, if_match, body, async_req=True)
        >>> result = thread.get()

        Args:
            shipment_id (str): ID of the shipment
            sit_extension_id (str): ID of the SIT extension
            if_match (str): We want the shipment's eTag rather than the SIT extension eTag as the SIT extension is always associated with a shipment
            body (ApproveSITExtension):

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
            MTOShipment
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
        kwargs['shipment_id'] = \
            shipment_id
        kwargs['sit_extension_id'] = \
            sit_extension_id
        kwargs['if_match'] = \
            if_match
        kwargs['body'] = \
            body
        return self.approve_sit_extension_endpoint.call_with_http_info(**kwargs)

    def create_sit_extension_as_too(
        self,
        shipment_id,
        if_match,
        body,
        **kwargs
    ):
        """Create an approved SIT extension  # noqa: E501

        TOO can creates an already-approved SIT extension on behalf of a customer  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_sit_extension_as_too(shipment_id, if_match, body, async_req=True)
        >>> result = thread.get()

        Args:
            shipment_id (str): ID of the shipment
            if_match (str): We want the shipment's eTag rather than the SIT extension eTag as the SIT extension is always associated with a shipment
            body (CreateSITExtensionAsTOO):

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
            MTOShipment
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
        kwargs['shipment_id'] = \
            shipment_id
        kwargs['if_match'] = \
            if_match
        kwargs['body'] = \
            body
        return self.create_sit_extension_as_too_endpoint.call_with_http_info(**kwargs)

    def deny_sit_extension(
        self,
        shipment_id,
        sit_extension_id,
        if_match,
        body,
        **kwargs
    ):
        """Denies a SIT extension  # noqa: E501

        Denies a SIT extension  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.deny_sit_extension(shipment_id, sit_extension_id, if_match, body, async_req=True)
        >>> result = thread.get()

        Args:
            shipment_id (str): ID of the shipment
            sit_extension_id (str): ID of the SIT extension
            if_match (str):
            body (DenySITExtension):

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
            MTOShipment
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
        kwargs['shipment_id'] = \
            shipment_id
        kwargs['sit_extension_id'] = \
            sit_extension_id
        kwargs['if_match'] = \
            if_match
        kwargs['body'] = \
            body
        return self.deny_sit_extension_endpoint.call_with_http_info(**kwargs)


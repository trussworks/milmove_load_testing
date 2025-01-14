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
from ghc_client.model.queue_moves_result import QueueMovesResult
from ghc_client.model.queue_payment_requests_result import QueuePaymentRequestsResult


class QueuesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_moves_queue_endpoint = _Endpoint(
            settings={
                'response_type': (QueueMovesResult,),
                'auth': [],
                'endpoint_path': '/queues/moves',
                'operation_id': 'get_moves_queue',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'sort',
                    'order',
                    'branch',
                    'locator',
                    'last_name',
                    'dod_id',
                    'origin_duty_location',
                    'destination_duty_location',
                    'appeared_in_too_at',
                    'requested_move_date',
                    'status',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'sort',
                    'order',
                    'status',
                ],
                'validation': [
                    'status',
                ]
            },
            root_map={
                'validations': {
                    ('status',): {

                    },
                },
                'allowed_values': {
                    ('sort',): {

                        "LASTNAME": "lastName",
                        "DODID": "dodID",
                        "BRANCH": "branch",
                        "LOCATOR": "locator",
                        "STATUS": "status",
                        "ORIGINDUTYLOCATION": "originDutyLocation",
                        "DESTINATIONDUTYLOCATION": "destinationDutyLocation",
                        "REQUESTEDMOVEDATE": "requestedMoveDate",
                        "APPEAREDINTOOAT": "appearedInTooAt"
                    },
                    ('order',): {

                        "ASC": "asc",
                        "DESC": "desc"
                    },
                    ('status',): {

                        "SUBMITTED": "SUBMITTED",
                        "APPROVALS_REQUESTED": "APPROVALS REQUESTED",
                        "APPROVED": "APPROVED"
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'sort':
                        (str,),
                    'order':
                        (str,),
                    'branch':
                        (str,),
                    'locator':
                        (str,),
                    'last_name':
                        (str,),
                    'dod_id':
                        (str,),
                    'origin_duty_location':
                        (str,),
                    'destination_duty_location':
                        (str,),
                    'appeared_in_too_at':
                        (datetime,),
                    'requested_move_date':
                        (str,),
                    'status':
                        ([str],),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'perPage',
                    'sort': 'sort',
                    'order': 'order',
                    'branch': 'branch',
                    'locator': 'locator',
                    'last_name': 'lastName',
                    'dod_id': 'dodID',
                    'origin_duty_location': 'originDutyLocation',
                    'destination_duty_location': 'destinationDutyLocation',
                    'appeared_in_too_at': 'appearedInTooAt',
                    'requested_move_date': 'requestedMoveDate',
                    'status': 'status',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'sort': 'query',
                    'order': 'query',
                    'branch': 'query',
                    'locator': 'query',
                    'last_name': 'query',
                    'dod_id': 'query',
                    'origin_duty_location': 'query',
                    'destination_duty_location': 'query',
                    'appeared_in_too_at': 'query',
                    'requested_move_date': 'query',
                    'status': 'query',
                },
                'collection_format_map': {
                    'status': 'csv',
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
        self.get_payment_requests_queue_endpoint = _Endpoint(
            settings={
                'response_type': (QueuePaymentRequestsResult,),
                'auth': [],
                'endpoint_path': '/queues/payment-requests',
                'operation_id': 'get_payment_requests_queue',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'sort',
                    'order',
                    'page',
                    'per_page',
                    'submitted_at',
                    'branch',
                    'locator',
                    'last_name',
                    'dod_id',
                    'destination_duty_location',
                    'origin_duty_location',
                    'status',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'sort',
                    'order',
                    'status',
                ],
                'validation': [
                    'status',
                ]
            },
            root_map={
                'validations': {
                    ('status',): {

                    },
                },
                'allowed_values': {
                    ('sort',): {

                        "LASTNAME": "lastName",
                        "LOCATOR": "locator",
                        "SUBMITTEDAT": "submittedAt",
                        "BRANCH": "branch",
                        "STATUS": "status",
                        "DODID": "dodID",
                        "AGE": "age",
                        "ORIGINDUTYLOCATION": "originDutyLocation"
                    },
                    ('order',): {

                        "ASC": "asc",
                        "DESC": "desc"
                    },
                    ('status',): {

                        "PAYMENT_REQUESTED": "Payment requested",
                        "REVIEWED": "Reviewed",
                        "REJECTED": "Rejected",
                        "PAID": "Paid"
                    },
                },
                'openapi_types': {
                    'sort':
                        (str,),
                    'order':
                        (str,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'submitted_at':
                        (datetime,),
                    'branch':
                        (str,),
                    'locator':
                        (str,),
                    'last_name':
                        (str,),
                    'dod_id':
                        (str,),
                    'destination_duty_location':
                        (str,),
                    'origin_duty_location':
                        (str,),
                    'status':
                        ([str],),
                },
                'attribute_map': {
                    'sort': 'sort',
                    'order': 'order',
                    'page': 'page',
                    'per_page': 'perPage',
                    'submitted_at': 'submittedAt',
                    'branch': 'branch',
                    'locator': 'locator',
                    'last_name': 'lastName',
                    'dod_id': 'dodID',
                    'destination_duty_location': 'destinationDutyLocation',
                    'origin_duty_location': 'originDutyLocation',
                    'status': 'status',
                },
                'location_map': {
                    'sort': 'query',
                    'order': 'query',
                    'page': 'query',
                    'per_page': 'query',
                    'submitted_at': 'query',
                    'branch': 'query',
                    'locator': 'query',
                    'last_name': 'query',
                    'dod_id': 'query',
                    'destination_duty_location': 'query',
                    'origin_duty_location': 'query',
                    'status': 'query',
                },
                'collection_format_map': {
                    'status': 'csv',
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
        self.get_services_counseling_queue_endpoint = _Endpoint(
            settings={
                'response_type': (QueueMovesResult,),
                'auth': [],
                'endpoint_path': '/queues/counseling',
                'operation_id': 'get_services_counseling_queue',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'sort',
                    'order',
                    'branch',
                    'locator',
                    'last_name',
                    'dod_id',
                    'requested_move_date',
                    'submitted_at',
                    'origin_gbloc',
                    'origin_duty_location',
                    'destination_duty_location',
                    'status',
                    'needs_ppm_closeout',
                    'ppm_type',
                    'closeout_initiated',
                    'closeout_location',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'sort',
                    'order',
                    'status',
                    'ppm_type',
                ],
                'validation': [
                    'status',
                ]
            },
            root_map={
                'validations': {
                    ('status',): {

                    },
                },
                'allowed_values': {
                    ('sort',): {

                        "LASTNAME": "lastName",
                        "DODID": "dodID",
                        "BRANCH": "branch",
                        "LOCATOR": "locator",
                        "STATUS": "status",
                        "REQUESTEDMOVEDATE": "requestedMoveDate",
                        "SUBMITTEDAT": "submittedAt",
                        "ORIGINGBLOC": "originGBLOC",
                        "ORIGINDUTYLOCATION": "originDutyLocation",
                        "DESTINATIONDUTYLOCATION": "destinationDutyLocation",
                        "PPMTYPE": "ppmType",
                        "CLOSEOUTINITIATED": "closeoutInitiated",
                        "CLOSEOUTLOCATION": "closeoutLocation"
                    },
                    ('order',): {

                        "ASC": "asc",
                        "DESC": "desc"
                    },
                    ('status',): {

                        "NEEDS_SERVICE_COUNSELING": "NEEDS SERVICE COUNSELING",
                        "SERVICE_COUNSELING_COMPLETED": "SERVICE COUNSELING COMPLETED"
                    },
                    ('ppm_type',): {

                        "FULL": "FULL",
                        "PARTIAL": "PARTIAL"
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'sort':
                        (str,),
                    'order':
                        (str,),
                    'branch':
                        (str,),
                    'locator':
                        (str,),
                    'last_name':
                        (str,),
                    'dod_id':
                        (str,),
                    'requested_move_date':
                        (str,),
                    'submitted_at':
                        (datetime,),
                    'origin_gbloc':
                        (str,),
                    'origin_duty_location':
                        (str,),
                    'destination_duty_location':
                        (str,),
                    'status':
                        ([str],),
                    'needs_ppm_closeout':
                        (bool,),
                    'ppm_type':
                        (str,),
                    'closeout_initiated':
                        (datetime,),
                    'closeout_location':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'perPage',
                    'sort': 'sort',
                    'order': 'order',
                    'branch': 'branch',
                    'locator': 'locator',
                    'last_name': 'lastName',
                    'dod_id': 'dodID',
                    'requested_move_date': 'requestedMoveDate',
                    'submitted_at': 'submittedAt',
                    'origin_gbloc': 'originGBLOC',
                    'origin_duty_location': 'originDutyLocation',
                    'destination_duty_location': 'destinationDutyLocation',
                    'status': 'status',
                    'needs_ppm_closeout': 'needsPPMCloseout',
                    'ppm_type': 'ppmType',
                    'closeout_initiated': 'closeoutInitiated',
                    'closeout_location': 'closeoutLocation',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'sort': 'query',
                    'order': 'query',
                    'branch': 'query',
                    'locator': 'query',
                    'last_name': 'query',
                    'dod_id': 'query',
                    'requested_move_date': 'query',
                    'submitted_at': 'query',
                    'origin_gbloc': 'query',
                    'origin_duty_location': 'query',
                    'destination_duty_location': 'query',
                    'status': 'query',
                    'needs_ppm_closeout': 'query',
                    'ppm_type': 'query',
                    'closeout_initiated': 'query',
                    'closeout_location': 'query',
                },
                'collection_format_map': {
                    'status': 'csv',
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

    def get_moves_queue(
        self,
        **kwargs
    ):
        """Gets queued list of all customer moves by GBLOC origin  # noqa: E501

        An office TOO user will be assigned a transportation office that will determine which moves are displayed in their queue based on the origin duty location.  GHC moves will show up here onced they have reached the submitted status sent by the customer and have move task orders, shipments, and service items to approve.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_moves_queue(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): requested page of results. [optional]
            per_page (int): results per page. [optional]
            sort (str): field that results should be sorted by. [optional]
            order (str): direction of sort order if applied. [optional]
            branch (str): [optional]
            locator (str): [optional]
            last_name (str): [optional]
            dod_id (str): [optional]
            origin_duty_location (str): [optional]
            destination_duty_location (str): [optional]
            appeared_in_too_at (datetime): [optional]
            requested_move_date (str): filters the requested pickup date of a shipment on the move. [optional]
            status ([str]): Filtering for the status.. [optional]
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
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            QueueMovesResult
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
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_moves_queue_endpoint.call_with_http_info(**kwargs)

    def get_payment_requests_queue(
        self,
        **kwargs
    ):
        """Gets queued list of all payment requests by GBLOC origin  # noqa: E501

        An office TIO user will be assigned a transportation office that will determine which payment requests are displayed in their queue based on the origin duty location.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payment_requests_queue(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            sort (str): field that results should be sorted by. [optional]
            order (str): direction of sort order if applied. [optional]
            page (int): requested page of results. [optional]
            per_page (int): number of records to include per page. [optional]
            submitted_at (datetime): Start of the submitted at date in the user's local time zone converted to UTC. [optional]
            branch (str): [optional]
            locator (str): [optional]
            last_name (str): [optional]
            dod_id (str): [optional]
            destination_duty_location (str): [optional]
            origin_duty_location (str): [optional]
            status ([str]): Filtering for the status.. [optional]
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
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            QueuePaymentRequestsResult
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
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_payment_requests_queue_endpoint.call_with_http_info(**kwargs)

    def get_services_counseling_queue(
        self,
        **kwargs
    ):
        """Gets queued list of all customer moves needing services counseling by GBLOC origin  # noqa: E501

        An office services counselor user will be assigned a transportation office that will determine which moves are displayed in their queue based on the origin duty location.  GHC moves will show up here onced they have reached the NEEDS SERVICE COUNSELING status after submission from a customer or created on a customer's behalf.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_services_counseling_queue(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): requested page number of paginated move results. [optional]
            per_page (int): maximum number of moves to show on each page of paginated results. [optional]
            sort (str): field that results should be sorted by. [optional]
            order (str): direction of sort order if applied. [optional]
            branch (str): filters by the branch of the move's service member. [optional]
            locator (str): filters to match the unique move code locator. [optional]
            last_name (str): filters using a prefix match on the service member's last name. [optional]
            dod_id (str): filters to match the unique service member's DoD ID. [optional]
            requested_move_date (str): filters the requested pickup date of a shipment on the move. [optional]
            submitted_at (datetime): Start of the submitted at date in the user's local time zone converted to UTC. [optional]
            origin_gbloc (str): filters the GBLOC of the service member's origin duty location. [optional]
            origin_duty_location (str): filters the name of the origin duty location on the orders. [optional]
            destination_duty_location (str): filters the name of the destination duty location on the orders. [optional]
            status ([str]): filters the status of the move. [optional]
            needs_ppm_closeout (bool): Only used for Services Counseling queue. If true, show PPM moves that are ready for closeout. Otherwise, show all other moves.. [optional]
            ppm_type (str): filters PPM type. [optional]
            closeout_initiated (datetime): Latest date that closeout was initiated on a PPM on the move. [optional]
            closeout_location (str): closeout location. [optional]
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
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            QueueMovesResult
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
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_services_counseling_queue_endpoint.call_with_http_info(**kwargs)


"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from internal_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from internal_client.exceptions import ApiAttributeError


def lazy_import():
    from internal_client.model.moving_expense_document import MovingExpenseDocument
    from internal_client.model.omittable_moving_expense_type import OmittableMovingExpenseType
    from internal_client.model.omittable_ppm_document_status import OmittablePPMDocumentStatus
    globals()['MovingExpenseDocument'] = MovingExpenseDocument
    globals()['OmittableMovingExpenseType'] = OmittableMovingExpenseType
    globals()['OmittablePPMDocumentStatus'] = OmittablePPMDocumentStatus


class MovingExpense(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'ppm_shipment_id': (str,),  # noqa: E501
            'document_id': (str,),  # noqa: E501
            'document': (MovingExpenseDocument,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'moving_expense_type': (OmittableMovingExpenseType,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'paid_with_gtcc': (bool, none_type,),  # noqa: E501
            'amount': (int, none_type,),  # noqa: E501
            'missing_receipt': (bool, none_type,),  # noqa: E501
            'status': (OmittablePPMDocumentStatus,),  # noqa: E501
            'reason': (str, none_type,),  # noqa: E501
            'sit_start_date': (date, none_type,),  # noqa: E501
            'sit_end_date': (date, none_type,),  # noqa: E501
            'e_tag': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'ppm_shipment_id': 'ppmShipmentId',  # noqa: E501
        'document_id': 'documentId',  # noqa: E501
        'document': 'document',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'moving_expense_type': 'movingExpenseType',  # noqa: E501
        'description': 'description',  # noqa: E501
        'paid_with_gtcc': 'paidWithGtcc',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'missing_receipt': 'missingReceipt',  # noqa: E501
        'status': 'status',  # noqa: E501
        'reason': 'reason',  # noqa: E501
        'sit_start_date': 'sitStartDate',  # noqa: E501
        'sit_end_date': 'sitEndDate',  # noqa: E501
        'e_tag': 'eTag',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'ppm_shipment_id',  # noqa: E501
        'document_id',  # noqa: E501
        'created_at',  # noqa: E501
        'updated_at',  # noqa: E501
        'e_tag',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, ppm_shipment_id, document_id, document, created_at, updated_at, *args, **kwargs):  # noqa: E501
        """MovingExpense - a model defined in OpenAPI

        Args:
            id (str): Unique primary identifier of the Moving Expense object
            ppm_shipment_id (str): The PPM Shipment id that this moving expense belongs to
            document_id (str): The id of the Document that contains all file uploads for this expense
            document (MovingExpenseDocument):
            created_at (datetime): Timestamp the moving expense object was initially created in the system (UTC)
            updated_at (datetime): Timestamp when a property of this moving expense object was last modified (UTC)

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            moving_expense_type (OmittableMovingExpenseType): [optional]  # noqa: E501
            description (str, none_type): A brief description of the expense. [optional]  # noqa: E501
            paid_with_gtcc (bool, none_type): Indicates if the service member used their government issued card to pay for the expense. [optional]  # noqa: E501
            amount (int, none_type): The total amount of the expense as indicated on the receipt. [optional]  # noqa: E501
            missing_receipt (bool, none_type): Indicates if the service member is missing the receipt with the proof of expense amount. [optional]  # noqa: E501
            status (OmittablePPMDocumentStatus): [optional]  # noqa: E501
            reason (str, none_type): The reason the services counselor has excluded or rejected the item.. [optional]  # noqa: E501
            sit_start_date (date, none_type): The date the shipment entered storage, applicable for the `STORAGE` movingExpenseType only. [optional]  # noqa: E501
            sit_end_date (date, none_type): The date the shipment exited storage, applicable for the `STORAGE` movingExpenseType only. [optional]  # noqa: E501
            e_tag (str): A hash that should be used as the \"If-Match\" header for any updates.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.ppm_shipment_id = ppm_shipment_id
        self.document_id = document_id
        self.document = document
        self.created_at = created_at
        self.updated_at = updated_at
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, document, *args, **kwargs):  # noqa: E501
        """MovingExpense - a model defined in OpenAPI

            document (MovingExpenseDocument):
        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            moving_expense_type (OmittableMovingExpenseType): [optional]  # noqa: E501
            description (str, none_type): A brief description of the expense. [optional]  # noqa: E501
            paid_with_gtcc (bool, none_type): Indicates if the service member used their government issued card to pay for the expense. [optional]  # noqa: E501
            amount (int, none_type): The total amount of the expense as indicated on the receipt. [optional]  # noqa: E501
            missing_receipt (bool, none_type): Indicates if the service member is missing the receipt with the proof of expense amount. [optional]  # noqa: E501
            status (OmittablePPMDocumentStatus): [optional]  # noqa: E501
            reason (str, none_type): The reason the services counselor has excluded or rejected the item.. [optional]  # noqa: E501
            sit_start_date (date, none_type): The date the shipment entered storage, applicable for the `STORAGE` movingExpenseType only. [optional]  # noqa: E501
            sit_end_date (date, none_type): The date the shipment exited storage, applicable for the `STORAGE` movingExpenseType only. [optional]  # noqa: E501
            e_tag (str): A hash that should be used as the \"If-Match\" header for any updates.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.document = document
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

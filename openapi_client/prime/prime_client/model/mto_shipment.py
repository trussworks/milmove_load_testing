"""
    MilMove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from prime_client.model_utils import (  # noqa: F401
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
from prime_client.exceptions import ApiAttributeError


def lazy_import():
    from prime_client.model.address import Address
    from prime_client.model.destination_type import DestinationType
    from prime_client.model.mto_agents import MTOAgents
    from prime_client.model.mto_service_item import MTOServiceItem
    from prime_client.model.mto_shipment_type import MTOShipmentType
    from prime_client.model.ppm_shipment import PPMShipment
    from prime_client.model.reweigh import Reweigh
    from prime_client.model.sit_extensions import SITExtensions
    from prime_client.model.storage_facility import StorageFacility
    globals()['Address'] = Address
    globals()['DestinationType'] = DestinationType
    globals()['MTOAgents'] = MTOAgents
    globals()['MTOServiceItem'] = MTOServiceItem
    globals()['MTOShipmentType'] = MTOShipmentType
    globals()['PPMShipment'] = PPMShipment
    globals()['Reweigh'] = Reweigh
    globals()['SITExtensions'] = SITExtensions
    globals()['StorageFacility'] = StorageFacility


class MTOShipment(ModelNormal):
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
        ('status',): {
            'SUBMITTED': "SUBMITTED",
            'APPROVED': "APPROVED",
            'REJECTED': "REJECTED",
            'CANCELLATION_REQUESTED': "CANCELLATION_REQUESTED",
            'CANCELED': "CANCELED",
            'DIVERSION_REQUESTED': "DIVERSION_REQUESTED",
        },
    }

    validations = {
        ('prime_estimated_weight',): {
            'inclusive_minimum': 1,
        },
        ('prime_actual_weight',): {
            'inclusive_minimum': 1,
        },
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
            'move_task_order_id': (str,),  # noqa: E501
            'approved_date': (date, none_type,),  # noqa: E501
            'requested_pickup_date': (date, none_type,),  # noqa: E501
            'requested_delivery_date': (date, none_type,),  # noqa: E501
            'scheduled_pickup_date': (date, none_type,),  # noqa: E501
            'actual_pickup_date': (date, none_type,),  # noqa: E501
            'first_available_delivery_date': (date, none_type,),  # noqa: E501
            'required_delivery_date': (date, none_type,),  # noqa: E501
            'scheduled_delivery_date': (date, none_type,),  # noqa: E501
            'actual_delivery_date': (date, none_type,),  # noqa: E501
            'prime_estimated_weight': (int, none_type,),  # noqa: E501
            'prime_estimated_weight_recorded_date': (date, none_type,),  # noqa: E501
            'prime_actual_weight': (int, none_type,),  # noqa: E501
            'nts_recorded_weight': (int, none_type,),  # noqa: E501
            'customer_remarks': (str, none_type,),  # noqa: E501
            'counselor_remarks': (str, none_type,),  # noqa: E501
            'agents': (MTOAgents,),  # noqa: E501
            'sit_extensions': (SITExtensions,),  # noqa: E501
            'reweigh': (Reweigh,),  # noqa: E501
            'mto_service_items': ([MTOServiceItem],),  # noqa: E501
            'pickup_address': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'destination_address': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'destination_type': (DestinationType,),  # noqa: E501
            'secondary_pickup_address': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'secondary_delivery_address': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'storage_facility': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'shipment_type': (MTOShipmentType,),  # noqa: E501
            'diversion': (bool,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'rejection_reason': (str, none_type,),  # noqa: E501
            'ppm_shipment': (PPMShipment,),  # noqa: E501
            'e_tag': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'point_of_contact': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'move_task_order_id': 'moveTaskOrderID',  # noqa: E501
        'approved_date': 'approvedDate',  # noqa: E501
        'requested_pickup_date': 'requestedPickupDate',  # noqa: E501
        'requested_delivery_date': 'requestedDeliveryDate',  # noqa: E501
        'scheduled_pickup_date': 'scheduledPickupDate',  # noqa: E501
        'actual_pickup_date': 'actualPickupDate',  # noqa: E501
        'first_available_delivery_date': 'firstAvailableDeliveryDate',  # noqa: E501
        'required_delivery_date': 'requiredDeliveryDate',  # noqa: E501
        'scheduled_delivery_date': 'scheduledDeliveryDate',  # noqa: E501
        'actual_delivery_date': 'actualDeliveryDate',  # noqa: E501
        'prime_estimated_weight': 'primeEstimatedWeight',  # noqa: E501
        'prime_estimated_weight_recorded_date': 'primeEstimatedWeightRecordedDate',  # noqa: E501
        'prime_actual_weight': 'primeActualWeight',  # noqa: E501
        'nts_recorded_weight': 'ntsRecordedWeight',  # noqa: E501
        'customer_remarks': 'customerRemarks',  # noqa: E501
        'counselor_remarks': 'counselorRemarks',  # noqa: E501
        'agents': 'agents',  # noqa: E501
        'sit_extensions': 'sitExtensions',  # noqa: E501
        'reweigh': 'reweigh',  # noqa: E501
        'mto_service_items': 'mtoServiceItems',  # noqa: E501
        'pickup_address': 'pickupAddress',  # noqa: E501
        'destination_address': 'destinationAddress',  # noqa: E501
        'destination_type': 'destinationType',  # noqa: E501
        'secondary_pickup_address': 'secondaryPickupAddress',  # noqa: E501
        'secondary_delivery_address': 'secondaryDeliveryAddress',  # noqa: E501
        'storage_facility': 'storageFacility',  # noqa: E501
        'shipment_type': 'shipmentType',  # noqa: E501
        'diversion': 'diversion',  # noqa: E501
        'status': 'status',  # noqa: E501
        'rejection_reason': 'rejectionReason',  # noqa: E501
        'ppm_shipment': 'ppmShipment',  # noqa: E501
        'e_tag': 'eTag',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'point_of_contact': 'pointOfContact',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'move_task_order_id',  # noqa: E501
        'approved_date',  # noqa: E501
        'requested_pickup_date',  # noqa: E501
        'requested_delivery_date',  # noqa: E501
        'required_delivery_date',  # noqa: E501
        'prime_estimated_weight_recorded_date',  # noqa: E501
        'customer_remarks',  # noqa: E501
        'counselor_remarks',  # noqa: E501
        'mto_service_items',  # noqa: E501
        'status',  # noqa: E501
        'rejection_reason',  # noqa: E501
        'e_tag',  # noqa: E501
        'created_at',  # noqa: E501
        'updated_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """MTOShipment - a model defined in OpenAPI

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
            id (str): The ID of the shipment.. [optional]  # noqa: E501
            move_task_order_id (str): The ID of the move for this shipment.. [optional]  # noqa: E501
            approved_date (date, none_type): The date when the Transportation Ordering Officer first approved this shipment for the move.. [optional]  # noqa: E501
            requested_pickup_date (date, none_type): The date the customer selects during onboarding as their preferred pickup date. Other dates, such as required delivery date and (outside MilMove) the pack date, are derived from this date. . [optional]  # noqa: E501
            requested_delivery_date (date, none_type): The customer's preferred delivery date.. [optional]  # noqa: E501
            scheduled_pickup_date (date, none_type): The date the Prime contractor scheduled to pick up this shipment after consultation with the customer.. [optional]  # noqa: E501
            actual_pickup_date (date, none_type): The date when the Prime contractor actually picked up the shipment. Updated after-the-fact.. [optional]  # noqa: E501
            first_available_delivery_date (date, none_type): The date the Prime provides to the customer as the first possible delivery date so that they can plan their travel accordingly. . [optional]  # noqa: E501
            required_delivery_date (date, none_type): The latest date by which the Prime can deliver a customer's shipment without violating the contract. This is calculated based on weight, distance, and the scheduled pickup date. It cannot be modified. . [optional]  # noqa: E501
            scheduled_delivery_date (date, none_type): The date the Prime contractor scheduled to deliver this shipment after consultation with the customer.. [optional]  # noqa: E501
            actual_delivery_date (date, none_type): The date when the Prime contractor actually delivered the shipment. Updated after-the-fact.. [optional]  # noqa: E501
            prime_estimated_weight (int, none_type): The estimated weight of this shipment, determined by the movers during the pre-move survey. This value **can only be updated once.** If there was an issue with estimating the weight and a mistake was made, the Prime contracter will need to contact the TOO to change it. . [optional]  # noqa: E501
            prime_estimated_weight_recorded_date (date, none_type): The date when the Prime contractor recorded the shipment's estimated weight.. [optional]  # noqa: E501
            prime_actual_weight (int, none_type): The actual weight of the shipment, provided after the Prime packs, picks up, and weighs a customer's shipment.. [optional]  # noqa: E501
            nts_recorded_weight (int, none_type): The previously recorded weight for the NTS Shipment. Used for NTS Release to know what the previous primeActualWeight or billable weight was.. [optional]  # noqa: E501
            customer_remarks (str, none_type): The customer can use the customer remarks field to inform the services counselor and the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address.  Customer enters this information during onboarding. Optional field. . [optional]  # noqa: E501
            counselor_remarks (str, none_type): The counselor can use the counselor remarks field to inform the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address.  Counselors enters this information when creating or editing an MTO Shipment. Optional field. . [optional]  # noqa: E501
            agents (MTOAgents): [optional]  # noqa: E501
            sit_extensions (SITExtensions): [optional]  # noqa: E501
            reweigh (Reweigh): [optional]  # noqa: E501
            mto_service_items ([MTOServiceItem]): A list of service items connected to this shipment.. [optional]  # noqa: E501
            pickup_address ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): The address where the movers should pick up this shipment, entered by the customer during onboarding when they enter shipment details. . [optional]  # noqa: E501
            destination_address ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Where the movers should deliver this shipment. Often provided by the customer when they enter shipment details during onboarding, if they know their new address already.  May be blank when entered by the customer, required when entered by the Prime. May not represent the true final destination due to the shipment being diverted or placed in SIT. . [optional]  # noqa: E501
            destination_type (DestinationType): [optional]  # noqa: E501
            secondary_pickup_address ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): A second pickup address for this shipment, if the customer entered one. An optional field.. [optional]  # noqa: E501
            secondary_delivery_address ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): A second delivery address for this shipment, if the customer entered one. An optional field.. [optional]  # noqa: E501
            storage_facility ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            shipment_type (MTOShipmentType): [optional]  # noqa: E501
            diversion (bool): This value indicates whether or not this shipment is part of a diversion. If yes, the shipment can be either the starting or ending segment of the diversion. . [optional]  # noqa: E501
            status (str): The status of a shipment, indicating where it is in the TOO's approval process. Can only be updated by the contractor in special circumstances. . [optional]  # noqa: E501
            rejection_reason (str, none_type): The reason why this shipment was rejected by the TOO.. [optional]  # noqa: E501
            ppm_shipment (PPMShipment): [optional]  # noqa: E501
            e_tag (str): A hash unique to this shipment that should be used as the \"If-Match\" header for any updates.. [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            point_of_contact (str): Email or ID of the person who will be contacted in the event of questions or concerns about this update. May be the person performing the update, or someone else working with the Prime contractor. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """MTOShipment - a model defined in OpenAPI

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
            id (str): The ID of the shipment.. [optional]  # noqa: E501
            move_task_order_id (str): The ID of the move for this shipment.. [optional]  # noqa: E501
            approved_date (date, none_type): The date when the Transportation Ordering Officer first approved this shipment for the move.. [optional]  # noqa: E501
            requested_pickup_date (date, none_type): The date the customer selects during onboarding as their preferred pickup date. Other dates, such as required delivery date and (outside MilMove) the pack date, are derived from this date. . [optional]  # noqa: E501
            requested_delivery_date (date, none_type): The customer's preferred delivery date.. [optional]  # noqa: E501
            scheduled_pickup_date (date, none_type): The date the Prime contractor scheduled to pick up this shipment after consultation with the customer.. [optional]  # noqa: E501
            actual_pickup_date (date, none_type): The date when the Prime contractor actually picked up the shipment. Updated after-the-fact.. [optional]  # noqa: E501
            first_available_delivery_date (date, none_type): The date the Prime provides to the customer as the first possible delivery date so that they can plan their travel accordingly. . [optional]  # noqa: E501
            required_delivery_date (date, none_type): The latest date by which the Prime can deliver a customer's shipment without violating the contract. This is calculated based on weight, distance, and the scheduled pickup date. It cannot be modified. . [optional]  # noqa: E501
            scheduled_delivery_date (date, none_type): The date the Prime contractor scheduled to deliver this shipment after consultation with the customer.. [optional]  # noqa: E501
            actual_delivery_date (date, none_type): The date when the Prime contractor actually delivered the shipment. Updated after-the-fact.. [optional]  # noqa: E501
            prime_estimated_weight (int, none_type): The estimated weight of this shipment, determined by the movers during the pre-move survey. This value **can only be updated once.** If there was an issue with estimating the weight and a mistake was made, the Prime contracter will need to contact the TOO to change it. . [optional]  # noqa: E501
            prime_estimated_weight_recorded_date (date, none_type): The date when the Prime contractor recorded the shipment's estimated weight.. [optional]  # noqa: E501
            prime_actual_weight (int, none_type): The actual weight of the shipment, provided after the Prime packs, picks up, and weighs a customer's shipment.. [optional]  # noqa: E501
            nts_recorded_weight (int, none_type): The previously recorded weight for the NTS Shipment. Used for NTS Release to know what the previous primeActualWeight or billable weight was.. [optional]  # noqa: E501
            customer_remarks (str, none_type): The customer can use the customer remarks field to inform the services counselor and the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address.  Customer enters this information during onboarding. Optional field. . [optional]  # noqa: E501
            counselor_remarks (str, none_type): The counselor can use the counselor remarks field to inform the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address.  Counselors enters this information when creating or editing an MTO Shipment. Optional field. . [optional]  # noqa: E501
            agents (MTOAgents): [optional]  # noqa: E501
            sit_extensions (SITExtensions): [optional]  # noqa: E501
            reweigh (Reweigh): [optional]  # noqa: E501
            mto_service_items ([MTOServiceItem]): A list of service items connected to this shipment.. [optional]  # noqa: E501
            pickup_address ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): The address where the movers should pick up this shipment, entered by the customer during onboarding when they enter shipment details. . [optional]  # noqa: E501
            destination_address ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Where the movers should deliver this shipment. Often provided by the customer when they enter shipment details during onboarding, if they know their new address already.  May be blank when entered by the customer, required when entered by the Prime. May not represent the true final destination due to the shipment being diverted or placed in SIT. . [optional]  # noqa: E501
            destination_type (DestinationType): [optional]  # noqa: E501
            secondary_pickup_address ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): A second pickup address for this shipment, if the customer entered one. An optional field.. [optional]  # noqa: E501
            secondary_delivery_address ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): A second delivery address for this shipment, if the customer entered one. An optional field.. [optional]  # noqa: E501
            storage_facility ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            shipment_type (MTOShipmentType): [optional]  # noqa: E501
            diversion (bool): This value indicates whether or not this shipment is part of a diversion. If yes, the shipment can be either the starting or ending segment of the diversion. . [optional]  # noqa: E501
            status (str): The status of a shipment, indicating where it is in the TOO's approval process. Can only be updated by the contractor in special circumstances. . [optional]  # noqa: E501
            rejection_reason (str, none_type): The reason why this shipment was rejected by the TOO.. [optional]  # noqa: E501
            ppm_shipment (PPMShipment): [optional]  # noqa: E501
            e_tag (str): A hash unique to this shipment that should be used as the \"If-Match\" header for any updates.. [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            point_of_contact (str): Email or ID of the person who will be contacted in the event of questions or concerns about this update. May be the person performing the update, or someone else working with the Prime contractor. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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

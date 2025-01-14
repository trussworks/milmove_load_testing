# prime_client.MtoServiceItemApi

All URIs are relative to */prime/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mto_service_item**](MtoServiceItemApi.md#create_mto_service_item) | **POST** /mto-service-items | createMTOServiceItem
[**update_mto_service_item**](MtoServiceItemApi.md#update_mto_service_item) | **PATCH** /mto-service-items/{mtoServiceItemID} | updateMTOServiceItem


# **create_mto_service_item**
> [MTOServiceItem] create_mto_service_item()

createMTOServiceItem

Creates one or more MTOServiceItems. Not all service items may be created, please see details below.  This endpoint supports different body definitions. In the modelType field below, select the modelType corresponding  to the service item you wish to create and the documentation will update with the new definition.  Upon creation these items are associated with a Move Task Order and an MTO Shipment. The request must include UUIDs for the MTO and MTO Shipment connected to this service item. Some service item types require additional service items to be autogenerated when added - all created service items, autogenerated included, will be returned in the response.  To update a service item, please use [updateMTOServiceItem](#operation/updateMTOServiceItem) endpoint.  ---  **`MTOServiceItemOriginSIT`**  MTOServiceItemOriginSIT is a subtype of MTOServiceItem.  This model type describes a domestic origin SIT service item. Items can be created using this model type with the following codes:  **DOFSIT**  **1st day origin SIT service item**. When a DOFSIT is requested, the API will auto-create the following group of service items:   * DOFSIT - Domestic origin 1st day SIT   * DOASIT - Domestic origin Additional day SIT   * DOPSIT - Domestic origin SIT pickup  **DOASIT**  **Addt'l days origin SIT service item**. This represents an additional day of storage for the same item. Additional DOASIT service items can be created and added to an existing shipment that **includes a DOFSIT service item**.  ---  **`MTOServiceItemDestSIT`**  MTOServiceItemDestSIT is a subtype of MTOServiceItem.  This model type describes a domestic destination SIT service item. Items can be created using this model type with the following codes:  **DDFSIT**  **1st day origin SIT service item**. The additional fields are required for creating a DDFSIT:   * `firstAvailableDeliveryDate1`     * string <date>     * First available date that Prime can deliver SIT service item.   * `firstAvailableDeliveryDate2`     * string <date>     * Second available date that Prime can deliver SIT service item.   * `timeMilitary1`     * string\\d{4}Z     * Time of delivery corresponding to `firstAvailableDeliveryDate1`, in military format.   * `timeMilitary2`     * string\\d{4}Z     * Time of delivery corresponding to `firstAvailableDeliveryDate2`, in military format.  When a DDFSIT is requested, the API will auto-create the following group of service items:   * DDFSIT - Domestic destination 1st day SIT   * DDASIT - Domestic destination Additional day SIT   * DDDSIT - Domestic destination SIT delivery  **DDASIT**  **Addt'l days destination SIT service item**. This represents an additional day of storage for the same item. Additional DDASIT service items can be created and added to an existing shipment that **includes a DDFSIT service item**. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_service_item_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.mto_service_item import MTOServiceItem
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    body = MTOServiceItem() # MTOServiceItem |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # createMTOServiceItem
        api_response = api_instance.create_mto_service_item(body=body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->create_mto_service_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MTOServiceItem**](MTOServiceItem.md)|  | [optional]

### Return type

[**[MTOServiceItem]**](MTOServiceItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created an MTO service item. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_service_item**
> MTOServiceItem update_mto_service_item(mto_service_item_id, if_match, body)

updateMTOServiceItem

Updates MTOServiceItems after creation. Not all service items or fields may be updated, please see details below.  This endpoint supports different body definitions. In the modelType field below, select the modelType corresponding  to the service item you wish to update and the documentation will update with the new definition.  To create a service item, please use [createMTOServiceItem](#operation/createMTOServiceItem)) endpoint. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_service_item_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.mto_service_item import MTOServiceItem
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from prime_client.model.update_mto_service_item import UpdateMTOServiceItem
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    mto_service_item_id = "mtoServiceItemID_example" # str | UUID of service item to update.
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = UpdateMTOServiceItem() # UpdateMTOServiceItem | 

    # example passing only required values which don't have defaults set
    try:
        # updateMTOServiceItem
        api_response = api_instance.update_mto_service_item(mto_service_item_id, if_match, body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->update_mto_service_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_service_item_id** | **str**| UUID of service item to update. |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **body** | [**UpdateMTOServiceItem**](UpdateMTOServiceItem.md)|  |

### Return type

[**MTOServiceItem**](MTOServiceItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the MTO service item. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


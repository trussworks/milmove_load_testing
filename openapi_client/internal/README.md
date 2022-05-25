# internal-client
The Internal API is a RESTful API that enables the Customer application for
MilMove.

All endpoints are located under `/internal`.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import internal_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import internal_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import internal_client
from pprint import pprint
from internal_client.api import addresses_api
from internal_client.model.address import Address
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)



# Enter a context with an instance of the API client
with internal_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    address_id = "addressId_example" # str | UUID of the address to return

    try:
        # Returns an address
        api_response = api_instance.show_address(address_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling AddressesApi->show_address: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */internal*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressesApi* | [**show_address**](docs/AddressesApi.md#show_address) | **GET** /addresses/{addressId} | Returns an address
*BackupContactsApi* | [**create_service_member_backup_contact**](docs/BackupContactsApi.md#create_service_member_backup_contact) | **POST** /service_members/{serviceMemberId}/backup_contacts | Submits backup contact for a logged-in user
*BackupContactsApi* | [**index_service_member_backup_contacts**](docs/BackupContactsApi.md#index_service_member_backup_contacts) | **GET** /service_members/{serviceMemberId}/backup_contacts | List all service member backup contacts
*BackupContactsApi* | [**show_service_member_backup_contact**](docs/BackupContactsApi.md#show_service_member_backup_contact) | **GET** /backup_contacts/{backupContactId} | Returns the given service member backup contact
*BackupContactsApi* | [**update_service_member_backup_contact**](docs/BackupContactsApi.md#update_service_member_backup_contact) | **PUT** /backup_contacts/{backupContactId} | Updates a service member backup contact
*CalendarApi* | [**show_available_move_dates**](docs/CalendarApi.md#show_available_move_dates) | **GET** /calendar/available_move_dates | Returns available dates for the move calendar
*CertificationApi* | [**create_signed_certification**](docs/CertificationApi.md#create_signed_certification) | **POST** /moves/{moveId}/signed_certifications | Submits signed certification for the given move ID
*CertificationApi* | [**index_signed_certification**](docs/CertificationApi.md#index_signed_certification) | **GET** /moves/{moveId}/signed_certifications | gets the signed certifications for the given move ID
*DocumentsApi* | [**create_document**](docs/DocumentsApi.md#create_document) | **POST** /documents | Create a new document
*DocumentsApi* | [**show_document**](docs/DocumentsApi.md#show_document) | **GET** /documents/{documentId} | Returns a document
*DpsAuthApi* | [**get_cookie_url**](docs/DpsAuthApi.md#get_cookie_url) | **POST** /dps_auth/cookie_url | Returns the URL to redirect to that begins DPS auth
*DutyLocationsApi* | [**search_duty_locations**](docs/DutyLocationsApi.md#search_duty_locations) | **GET** /duty_locations | Returns the duty locations matching the search query
*EntitlementsApi* | [**index_entitlements**](docs/EntitlementsApi.md#index_entitlements) | **GET** /entitlements | List weight weights allotted by entitlement
*MoveDocsApi* | [**create_generic_move_document**](docs/MoveDocsApi.md#create_generic_move_document) | **POST** /moves/{moveId}/move_documents | Creates a move document
*MoveDocsApi* | [**create_moving_expense_document**](docs/MoveDocsApi.md#create_moving_expense_document) | **POST** /moves/{moveId}/moving_expense_documents | Creates a moving expense document
*MoveDocsApi* | [**create_weight_ticket_document**](docs/MoveDocsApi.md#create_weight_ticket_document) | **POST** /moves/{moveId}/weight_ticket | Creates a weight ticket document
*MoveDocsApi* | [**delete_move_document**](docs/MoveDocsApi.md#delete_move_document) | **DELETE** /move_documents/{moveDocumentId} | Deletes a move document
*MoveDocsApi* | [**index_move_documents**](docs/MoveDocsApi.md#index_move_documents) | **GET** /moves/{moveId}/move_documents | Returns a list of all Move Documents associated with this move
*MoveDocsApi* | [**update_move_document**](docs/MoveDocsApi.md#update_move_document) | **PUT** /move_documents/{moveDocumentId} | Updates a move document
*MovesApi* | [**patch_move**](docs/MovesApi.md#patch_move) | **PATCH** /moves/{moveId} | Patches the move
*MovesApi* | [**show_move**](docs/MovesApi.md#show_move) | **GET** /moves/{moveId} | Returns the given move
*MovesApi* | [**show_move_dates_summary**](docs/MovesApi.md#show_move_dates_summary) | **GET** /moves/{moveId}/move_dates_summary | Returns projected move-related dates for a given move date
*MovesApi* | [**show_shipment_summary_worksheet**](docs/MovesApi.md#show_shipment_summary_worksheet) | **GET** /moves/{moveId}/shipment_summary_worksheet | Returns Shipment Summary Worksheet
*MovesApi* | [**submit_amended_orders**](docs/MovesApi.md#submit_amended_orders) | **POST** /moves/{moveId}/submit_amended_orders | Submits amended orders for review
*MovesApi* | [**submit_move_for_approval**](docs/MovesApi.md#submit_move_for_approval) | **POST** /moves/{moveId}/submit | Submits a move for approval
*MtoShipmentApi* | [**create_mto_shipment**](docs/MtoShipmentApi.md#create_mto_shipment) | **POST** /mto_shipments | createMTOShipment
*MtoShipmentApi* | [**delete_shipment**](docs/MtoShipmentApi.md#delete_shipment) | **DELETE** /mto-shipments/{mtoShipmentId} | Soft deletes a shipment by ID
*MtoShipmentApi* | [**list_mto_shipments**](docs/MtoShipmentApi.md#list_mto_shipments) | **GET** /moves/{moveTaskOrderID}/mto_shipments | Gets all shipments for a move task order
*MtoShipmentApi* | [**update_mto_shipment**](docs/MtoShipmentApi.md#update_mto_shipment) | **PATCH** /mto-shipments/{mtoShipmentId} | updateMTOShipment
*OfficeApi* | [**approve_move**](docs/OfficeApi.md#approve_move) | **POST** /moves/{moveId}/approve | Approves a move to proceed
*OfficeApi* | [**approve_ppm**](docs/OfficeApi.md#approve_ppm) | **POST** /personally_procured_moves/{personallyProcuredMoveId}/approve | Approves the PPM
*OfficeApi* | [**approve_reimbursement**](docs/OfficeApi.md#approve_reimbursement) | **POST** /reimbursement/{reimbursementId}/approve | Approves the reimbursement
*OfficeApi* | [**cancel_move**](docs/OfficeApi.md#cancel_move) | **POST** /moves/{moveId}/cancel | Cancels a move
*OfficeApi* | [**show_office_orders**](docs/OfficeApi.md#show_office_orders) | **GET** /moves/{moveId}/orders | Returns orders information for a move for office use
*OrdersApi* | [**create_orders**](docs/OrdersApi.md#create_orders) | **POST** /orders | Creates an orders model for a logged-in user
*OrdersApi* | [**show_orders**](docs/OrdersApi.md#show_orders) | **GET** /orders/{ordersId} | Returns the given order
*OrdersApi* | [**update_orders**](docs/OrdersApi.md#update_orders) | **PUT** /orders/{ordersId} | Updates orders
*OrdersApi* | [**upload_amended_orders**](docs/OrdersApi.md#upload_amended_orders) | **PATCH** /orders/{ordersId}/upload_amended_orders | Patch the amended orders for a given order
*PostalCodesApi* | [**validate_postal_code_with_rate_data**](docs/PostalCodesApi.md#validate_postal_code_with_rate_data) | **GET** /rate_engine_postal_codes/{postal_code} | Validate if a zipcode is valid for origin or destination location for a move.
*PpmApi* | [**create_personally_procured_move**](docs/PpmApi.md#create_personally_procured_move) | **POST** /moves/{moveId}/personally_procured_move | Creates a new PPM for the given move
*PpmApi* | [**create_ppm_attachments**](docs/PpmApi.md#create_ppm_attachments) | **POST** /personally_procured_moves/{personallyProcuredMoveId}/create_ppm_attachments | Creates PPM attachments PDF
*PpmApi* | [**index_personally_procured_moves**](docs/PpmApi.md#index_personally_procured_moves) | **GET** /moves/{moveId}/personally_procured_move | Returns a list of all PPMs associated with this move
*PpmApi* | [**patch_personally_procured_move**](docs/PpmApi.md#patch_personally_procured_move) | **PATCH** /moves/{moveId}/personally_procured_move/{personallyProcuredMoveId} | Patches the PPM
*PpmApi* | [**request_ppm_expense_summary**](docs/PpmApi.md#request_ppm_expense_summary) | **GET** /personally_procured_move/{personallyProcuredMoveId}/expense_summary | Returns an expense summary organized by expense type
*PpmApi* | [**request_ppm_payment**](docs/PpmApi.md#request_ppm_payment) | **POST** /personally_procured_move/{personallyProcuredMoveId}/request_payment | Moves the PPM and the move into the PAYMENT_REQUESTED state
*PpmApi* | [**show_personally_procured_move**](docs/PpmApi.md#show_personally_procured_move) | **GET** /moves/{moveId}/personally_procured_move/{personallyProcuredMoveId} | Returns the given PPM
*PpmApi* | [**show_ppm_estimate**](docs/PpmApi.md#show_ppm_estimate) | **GET** /estimates/ppm | Return a PPM cost estimate
*PpmApi* | [**show_ppm_incentive**](docs/PpmApi.md#show_ppm_incentive) | **GET** /personally_procured_moves/incentive | Return a PPM incentive value
*PpmApi* | [**show_ppm_sit_estimate**](docs/PpmApi.md#show_ppm_sit_estimate) | **GET** /estimates/ppm_sit | Return a PPM move&#39;s SIT cost estimate
*PpmApi* | [**submit_personally_procured_move**](docs/PpmApi.md#submit_personally_procured_move) | **POST** /personally_procured_move/{personallyProcuredMoveId}/submit | Submits a PPM for approval
*PpmApi* | [**update_personally_procured_move**](docs/PpmApi.md#update_personally_procured_move) | **PUT** /moves/{moveId}/personally_procured_move/{personallyProcuredMoveId} | Updates the PPM
*PpmApi* | [**update_personally_procured_move_estimate**](docs/PpmApi.md#update_personally_procured_move_estimate) | **PATCH** /moves/{moveId}/personally_procured_move/{personallyProcuredMoveId}/estimate | Calculates the estimated incentive of a PPM
*QueuesApi* | [**show_queue**](docs/QueuesApi.md#show_queue) | **GET** /queues/{queueType} | Show all moves in a queue
*ServiceMembersApi* | [**create_service_member**](docs/ServiceMembersApi.md#create_service_member) | **POST** /service_members | Creates service member for a logged-in user
*ServiceMembersApi* | [**patch_service_member**](docs/ServiceMembersApi.md#patch_service_member) | **PATCH** /service_members/{serviceMemberId} | Patches the service member
*ServiceMembersApi* | [**show_service_member**](docs/ServiceMembersApi.md#show_service_member) | **GET** /service_members/{serviceMemberId} | Returns the given service member
*ServiceMembersApi* | [**show_service_member_orders**](docs/ServiceMembersApi.md#show_service_member_orders) | **GET** /service_members/{serviceMemberId}/current_orders | Returns the latest orders for a given service member
*TransportationOfficesApi* | [**show_duty_location_transportation_office**](docs/TransportationOfficesApi.md#show_duty_location_transportation_office) | **GET** /duty_locations/{dutyLocationId}/transportation_office | Returns the transportation office for a given duty location
*UploadsApi* | [**create_upload**](docs/UploadsApi.md#create_upload) | **POST** /uploads | Create a new upload
*UploadsApi* | [**delete_upload**](docs/UploadsApi.md#delete_upload) | **DELETE** /uploads/{uploadId} | Deletes an upload
*UploadsApi* | [**delete_uploads**](docs/UploadsApi.md#delete_uploads) | **DELETE** /uploads | Deletes a collection of uploads
*UsersApi* | [**is_logged_in_user**](docs/UsersApi.md#is_logged_in_user) | **GET** /users/is_logged_in | Returns boolean as to whether the user is logged in
*UsersApi* | [**show_logged_in_user**](docs/UsersApi.md#show_logged_in_user) | **GET** /users/logged_in | Returns the user info for the currently logged in user


## Documentation For Models

 - [Address](docs/Address.md)
 - [Affiliation](docs/Affiliation.md)
 - [ApprovePersonallyProcuredMovePayload](docs/ApprovePersonallyProcuredMovePayload.md)
 - [AvailableMoveDates](docs/AvailableMoveDates.md)
 - [BackupContactPermission](docs/BackupContactPermission.md)
 - [CancelMove](docs/CancelMove.md)
 - [CategoryExpenseSummary](docs/CategoryExpenseSummary.md)
 - [ClientError](docs/ClientError.md)
 - [CreateGenericMoveDocumentPayload](docs/CreateGenericMoveDocumentPayload.md)
 - [CreateMovingExpenseDocumentPayload](docs/CreateMovingExpenseDocumentPayload.md)
 - [CreatePPMShipment](docs/CreatePPMShipment.md)
 - [CreatePersonallyProcuredMovePayload](docs/CreatePersonallyProcuredMovePayload.md)
 - [CreateReimbursement](docs/CreateReimbursement.md)
 - [CreateServiceMemberBackupContactPayload](docs/CreateServiceMemberBackupContactPayload.md)
 - [CreateServiceMemberPayload](docs/CreateServiceMemberPayload.md)
 - [CreateShipment](docs/CreateShipment.md)
 - [CreateSignedCertificationPayload](docs/CreateSignedCertificationPayload.md)
 - [CreateUpdateOrders](docs/CreateUpdateOrders.md)
 - [CreateWeightTicketDocumentsPayload](docs/CreateWeightTicketDocumentsPayload.md)
 - [DPSAuthCookieURLPayload](docs/DPSAuthCookieURLPayload.md)
 - [DeptIndicator](docs/DeptIndicator.md)
 - [DocumentPayload](docs/DocumentPayload.md)
 - [DutyLocationPayload](docs/DutyLocationPayload.md)
 - [DutyLocationsPayload](docs/DutyLocationsPayload.md)
 - [Error](docs/Error.md)
 - [ExpenseSummaryPayload](docs/ExpenseSummaryPayload.md)
 - [ExpenseSummaryPayloadGrandTotal](docs/ExpenseSummaryPayloadGrandTotal.md)
 - [IndexEntitlements](docs/IndexEntitlements.md)
 - [IndexMovesPayload](docs/IndexMovesPayload.md)
 - [IndexPersonallyProcuredMovePayload](docs/IndexPersonallyProcuredMovePayload.md)
 - [IndexServiceMemberBackupContactsPayload](docs/IndexServiceMemberBackupContactsPayload.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InvalidRequestResponsePayload](docs/InvalidRequestResponsePayload.md)
 - [LoggedInUserPayload](docs/LoggedInUserPayload.md)
 - [MTOAgent](docs/MTOAgent.md)
 - [MTOAgentType](docs/MTOAgentType.md)
 - [MTOAgents](docs/MTOAgents.md)
 - [MTOShipment](docs/MTOShipment.md)
 - [MTOShipmentStatus](docs/MTOShipmentStatus.md)
 - [MTOShipmentType](docs/MTOShipmentType.md)
 - [MTOShipments](docs/MTOShipments.md)
 - [MethodOfReceipt](docs/MethodOfReceipt.md)
 - [MoveDatesSummary](docs/MoveDatesSummary.md)
 - [MoveDocumentPayload](docs/MoveDocumentPayload.md)
 - [MoveDocumentStatus](docs/MoveDocumentStatus.md)
 - [MoveDocumentType](docs/MoveDocumentType.md)
 - [MoveDocuments](docs/MoveDocuments.md)
 - [MovePayload](docs/MovePayload.md)
 - [MoveQueueItem](docs/MoveQueueItem.md)
 - [MoveStatus](docs/MoveStatus.md)
 - [MovingExpenseType](docs/MovingExpenseType.md)
 - [OfficeUser](docs/OfficeUser.md)
 - [Orders](docs/Orders.md)
 - [OrdersStatus](docs/OrdersStatus.md)
 - [OrdersType](docs/OrdersType.md)
 - [OrdersTypeDetail](docs/OrdersTypeDetail.md)
 - [PPMEstimateRange](docs/PPMEstimateRange.md)
 - [PPMIncentive](docs/PPMIncentive.md)
 - [PPMShipment](docs/PPMShipment.md)
 - [PPMShipmentStatus](docs/PPMShipmentStatus.md)
 - [PPMSitEstimate](docs/PPMSitEstimate.md)
 - [PPMStatus](docs/PPMStatus.md)
 - [PatchMovePayload](docs/PatchMovePayload.md)
 - [PatchPersonallyProcuredMovePayload](docs/PatchPersonallyProcuredMovePayload.md)
 - [PatchServiceMemberPayload](docs/PatchServiceMemberPayload.md)
 - [PaymentMethodsTotals](docs/PaymentMethodsTotals.md)
 - [PersonallyProcuredMovePayload](docs/PersonallyProcuredMovePayload.md)
 - [PostDocumentPayload](docs/PostDocumentPayload.md)
 - [RateEnginePostalCodePayload](docs/RateEnginePostalCodePayload.md)
 - [Reimbursement](docs/Reimbursement.md)
 - [ReimbursementStatus](docs/ReimbursementStatus.md)
 - [Role](docs/Role.md)
 - [SelectedMoveType](docs/SelectedMoveType.md)
 - [ServiceMemberBackupContactPayload](docs/ServiceMemberBackupContactPayload.md)
 - [ServiceMemberPayload](docs/ServiceMemberPayload.md)
 - [ServiceMemberRank](docs/ServiceMemberRank.md)
 - [SignedCertificationPayload](docs/SignedCertificationPayload.md)
 - [SignedCertificationType](docs/SignedCertificationType.md)
 - [SignedCertificationTypeCreate](docs/SignedCertificationTypeCreate.md)
 - [SignedCertifications](docs/SignedCertifications.md)
 - [SubmitMoveForApprovalPayload](docs/SubmitMoveForApprovalPayload.md)
 - [SubmitPersonallyProcuredMovePayload](docs/SubmitPersonallyProcuredMovePayload.md)
 - [TShirtSize](docs/TShirtSize.md)
 - [TransportationOffice](docs/TransportationOffice.md)
 - [UpdatePPMShipment](docs/UpdatePPMShipment.md)
 - [UpdatePersonallyProcuredMovePayload](docs/UpdatePersonallyProcuredMovePayload.md)
 - [UpdateServiceMemberBackupContactPayload](docs/UpdateServiceMemberBackupContactPayload.md)
 - [UpdateShipment](docs/UpdateShipment.md)
 - [UploadPayload](docs/UploadPayload.md)
 - [ValidationError](docs/ValidationError.md)
 - [WeightAllotment](docs/WeightAllotment.md)
 - [WeightTicketSetType](docs/WeightTicketSetType.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

ppp@truss.works


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in internal_client.apis and internal_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from internal_client.api.default_api import DefaultApi`
- `from internal_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import internal_client
from internal_client.apis import *
from internal_client.models import *
```

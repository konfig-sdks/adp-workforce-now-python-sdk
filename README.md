<div align="center">

[![Visit Adp](./header.png)](https://adp.com)

# Adp<a id="adp"></a>

ADP API endpoints.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`adpworkforcenow.hr.check_async_request_status`](#adpworkforcenowhrcheck_async_request_status)
  * [`adpworkforcenow.hr.get_worker_by_aoid`](#adpworkforcenowhrget_worker_by_aoid)
  * [`adpworkforcenow.hr.get_worker_demographics_by_aoid`](#adpworkforcenowhrget_worker_demographics_by_aoid)
  * [`adpworkforcenow.hr.list_top5_prevent_cache`](#adpworkforcenowhrlist_top5_prevent_cache)
  * [`adpworkforcenow.hr.list_top5_prevent_cache_0`](#adpworkforcenowhrlist_top5_prevent_cache_0)
  * [`adpworkforcenow.payroll.list_payroll_outputs`](#adpworkforcenowpayrolllist_payroll_outputs)
  * [`adpworkforcenow.token_request.create_with_authorization_header`](#adpworkforcenowtoken_requestcreate_with_authorization_header)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=ADP&serviceName=WorkforceNow&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from adp_workforce_now_python_sdk import AdpWorkforceNow, ApiException

adpworkforcenow = AdpWorkforceNow()

try:
    # Worker V2 (Check Async Request Status)
    adpworkforcenow.hr.check_async_request_status(
        body=None,
        key="key_example",
        select="processingStatus",
    )
except ApiException as e:
    print("Exception when calling HRApi.check_async_request_status: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from adp_workforce_now_python_sdk import AdpWorkforceNow, ApiException

adpworkforcenow = AdpWorkforceNow()


async def main():
    try:
        # Worker V2 (Check Async Request Status)
        await adpworkforcenow.hr.acheck_async_request_status(
            body=None,
            key="key_example",
            select="processingStatus",
        )
    except ApiException as e:
        print("Exception when calling HRApi.check_async_request_status: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from adp_workforce_now_python_sdk import AdpWorkforceNow, ApiException

adpworkforcenow = AdpWorkforceNow()

try:
    # Worker V2 (Check Async Request Status)
    check_async_request_status_response = (
        adpworkforcenow.hr.raw.check_async_request_status(
            body=None,
            key="key_example",
            select="processingStatus",
        )
    )
    pprint(check_async_request_status_response.headers)
    pprint(check_async_request_status_response.status)
    pprint(check_async_request_status_response.round_trip_time)
except ApiException as e:
    print("Exception when calling HRApi.check_async_request_status: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `adpworkforcenow.hr.check_async_request_status`<a id="adpworkforcenowhrcheck_async_request_status"></a>

Check the status of an async request to the Worker API given the key returned as part of the original asyn response's "link" header.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
adpworkforcenow.hr.check_async_request_status(
    body=None,
    key="key_example",
    select="processingStatus",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

##### select: `str`<a id="select-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/core/v1/operations/workerInformationManagement/hr.v2.workers/{key}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `adpworkforcenow.hr.get_worker_by_aoid`<a id="adpworkforcenowhrget_worker_by_aoid"></a>

Request a single worker given their AOID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
adpworkforcenow.hr.get_worker_by_aoid(
    body=None,
    anthony_albright_aoid="anthony-albright-aoid_example",
    prevent_cache="TIMESTAMP",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### anthony_albright_aoid: `str`<a id="anthony_albright_aoid-str"></a>

##### prevent_cache: `str`<a id="prevent_cache-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hr/v2/workers/{anthony-albright-aoid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `adpworkforcenow.hr.get_worker_demographics_by_aoid`<a id="adpworkforcenowhrget_worker_demographics_by_aoid"></a>

Request demographic data for a single worker given their AOID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
adpworkforcenow.hr.get_worker_demographics_by_aoid(
    body=None,
    anthony_albright_aoid="anthony-albright-aoid_example",
    prevent_cache="TIMESTAMP",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### anthony_albright_aoid: `str`<a id="anthony_albright_aoid-str"></a>

##### prevent_cache: `str`<a id="prevent_cache-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hr/v2/worker-demographics/{anthony-albright-aoid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `adpworkforcenow.hr.list_top5_prevent_cache`<a id="adpworkforcenowhrlist_top5_prevent_cache"></a>

Request a collection of the top 5 workers using a URI cache-buster.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
adpworkforcenow.hr.list_top5_prevent_cache(
    body=None,
    top="5",
    prevent_cache="TIMESTAMP",
    filter="workers/workAssignments/homeOrganizationalUnits/typeCode/codeValue eq 'Department' and workers/workAssignments/homeOrganizationalUnits/nameCode/codeValue eq '001000'",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `str`<a id="top-str"></a>

##### prevent_cache: `str`<a id="prevent_cache-str"></a>

##### filter: `str`<a id="filter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hr/v2/workers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `adpworkforcenow.hr.list_top5_prevent_cache_0`<a id="adpworkforcenowhrlist_top5_prevent_cache_0"></a>

Request demographic data for a collection of the top 5 workers using a URI cache-buster.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
adpworkforcenow.hr.list_top5_prevent_cache_0(
    body=None,
    top="5",
    prevent_cache="TIMESTAMP",
    filter="workers/workAssignments/homeOrganizationalUnits/typeCode/codeValue eq 'Department' and workers/workAssignments/homeOrganizationalUnits/nameCode/codeValue eq '001000'",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `str`<a id="top-str"></a>

##### prevent_cache: `str`<a id="prevent_cache-str"></a>

##### filter: `str`<a id="filter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hr/v2/worker-demographics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `adpworkforcenow.payroll.list_payroll_outputs`<a id="adpworkforcenowpayrolllist_payroll_outputs"></a>

Fetches a list of payroll outputs given a Region Code, Company Code, Year and Week.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
adpworkforcenow.payroll.list_payroll_outputs(
    body=None,
    filter="payrollScheduleReference/payrollYear eq 2018 and payrollScheduleReference/payrollWeekNumber eq 10 and payrollGroupCode/codeValue eq %26Y%26 and payrollRegionCode/codeValue eq BALT",
    count="true",
    use_cache="false",
    level="details",
    select="earnings,reportableEarningsAndBenefits,reimbursements,statutoryDeductions,nonStatutoryDeductions,memos,configurationTags",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filter: `str`<a id="filter-str"></a>

##### count: `str`<a id="count-str"></a>

##### use_cache: `str`<a id="use_cache-str"></a>

##### level: `str`<a id="level-str"></a>

##### select: `str`<a id="select-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/payroll-output` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `adpworkforcenow.token_request.create_with_authorization_header`<a id="adpworkforcenowtoken_requestcreate_with_authorization_header"></a>

A request to get an OAuth bearer token for our demo ADP Workforce Now by adding an Authorization header containing the base-64 encoded credentials.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
adpworkforcenow.token_request.create_with_authorization_header(
    body=None,
    grant_type="client_credentials",
    client_id="{{client-id}}",
    client_secret="{{client-secret}}",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### client_secret: `str`<a id="client_secret-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/oauth/v2/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)

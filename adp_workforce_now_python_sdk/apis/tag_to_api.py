import typing_extensions

from adp_workforce_now_python_sdk.apis.tags import TagValues
from adp_workforce_now_python_sdk.apis.tags.hr_api import HRApi
from adp_workforce_now_python_sdk.apis.tags.payroll_api import PayrollApi
from adp_workforce_now_python_sdk.apis.tags.token_request_api import TokenRequestApi
from adp_workforce_now_python_sdk.apis.tags.core_api import CoreApi
from adp_workforce_now_python_sdk.apis.tags.staffing_api import StaffingApi
from adp_workforce_now_python_sdk.apis.tags.talent_api import TalentApi
from adp_workforce_now_python_sdk.apis.tags.time_api import TimeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.HR: HRApi,
        TagValues.PAYROLL: PayrollApi,
        TagValues.TOKEN_REQUEST: TokenRequestApi,
        TagValues.CORE: CoreApi,
        TagValues.STAFFING: StaffingApi,
        TagValues.TALENT: TalentApi,
        TagValues.TIME: TimeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.HR: HRApi,
        TagValues.PAYROLL: PayrollApi,
        TagValues.TOKEN_REQUEST: TokenRequestApi,
        TagValues.CORE: CoreApi,
        TagValues.STAFFING: StaffingApi,
        TagValues.TALENT: TalentApi,
        TagValues.TIME: TimeApi,
    }
)

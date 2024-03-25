# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from adp_workforce_now_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    HR_V2_WORKERS = "/hr/v2/workers"
    HR_V2_WORKERS_ANTHONYALBRIGHTAOID = "/hr/v2/workers/{anthony-albright-aoid}"
    CORE_V1_OPERATIONS_WORKER_INFORMATION_MANAGEMENT_HR_V2_WORKERS_KEY = "/core/v1/operations/workerInformationManagement/hr.v2.workers/{key}"
    HR_V2_WORKERDEMOGRAPHICS = "/hr/v2/worker-demographics"
    HR_V2_WORKERDEMOGRAPHICS_ANTHONYALBRIGHTAOID = "/hr/v2/worker-demographics/{anthony-albright-aoid}"
    PAYROLL_V1_PAYROLLOUTPUT = "/payroll/v1/payroll-output"
    AUTH_OAUTH_V2_TOKEN = "/auth/oauth/v2/token"

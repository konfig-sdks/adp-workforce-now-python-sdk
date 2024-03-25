import typing_extensions

from adp_workforce_now_python_sdk.paths import PathValues
from adp_workforce_now_python_sdk.apis.paths.hr_v2_workers import HrV2Workers
from adp_workforce_now_python_sdk.apis.paths.hr_v2_workers_anthony_albright_aoid import HrV2WorkersAnthonyAlbrightAoid
from adp_workforce_now_python_sdk.apis.paths.core_v1_operations_worker_information_management_hr_v2_workers_key import CoreV1OperationsWorkerInformationManagementHrV2WorkersKey
from adp_workforce_now_python_sdk.apis.paths.hr_v2_worker_demographics import HrV2WorkerDemographics
from adp_workforce_now_python_sdk.apis.paths.hr_v2_worker_demographics_anthony_albright_aoid import HrV2WorkerDemographicsAnthonyAlbrightAoid
from adp_workforce_now_python_sdk.apis.paths.payroll_v1_payroll_output import PayrollV1PayrollOutput
from adp_workforce_now_python_sdk.apis.paths.auth_oauth_v2_token import AuthOauthV2Token

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HR_V2_WORKERS: HrV2Workers,
        PathValues.HR_V2_WORKERS_ANTHONYALBRIGHTAOID: HrV2WorkersAnthonyAlbrightAoid,
        PathValues.CORE_V1_OPERATIONS_WORKER_INFORMATION_MANAGEMENT_HR_V2_WORKERS_KEY: CoreV1OperationsWorkerInformationManagementHrV2WorkersKey,
        PathValues.HR_V2_WORKERDEMOGRAPHICS: HrV2WorkerDemographics,
        PathValues.HR_V2_WORKERDEMOGRAPHICS_ANTHONYALBRIGHTAOID: HrV2WorkerDemographicsAnthonyAlbrightAoid,
        PathValues.PAYROLL_V1_PAYROLLOUTPUT: PayrollV1PayrollOutput,
        PathValues.AUTH_OAUTH_V2_TOKEN: AuthOauthV2Token,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HR_V2_WORKERS: HrV2Workers,
        PathValues.HR_V2_WORKERS_ANTHONYALBRIGHTAOID: HrV2WorkersAnthonyAlbrightAoid,
        PathValues.CORE_V1_OPERATIONS_WORKER_INFORMATION_MANAGEMENT_HR_V2_WORKERS_KEY: CoreV1OperationsWorkerInformationManagementHrV2WorkersKey,
        PathValues.HR_V2_WORKERDEMOGRAPHICS: HrV2WorkerDemographics,
        PathValues.HR_V2_WORKERDEMOGRAPHICS_ANTHONYALBRIGHTAOID: HrV2WorkerDemographicsAnthonyAlbrightAoid,
        PathValues.PAYROLL_V1_PAYROLLOUTPUT: PayrollV1PayrollOutput,
        PathValues.AUTH_OAUTH_V2_TOKEN: AuthOauthV2Token,
    }
)

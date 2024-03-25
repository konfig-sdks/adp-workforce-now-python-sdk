operation_parameter_map = {
    '/core/v1/operations/workerInformationManagement/hr.v2.workers/{key}-GET': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': '$select'
            },
        ]
    },
    '/hr/v2/workers/{anthony-albright-aoid}-GET': {
        'parameters': [
            {
                'name': 'anthony-albright-aoid'
            },
            {
                'name': 'preventCache'
            },
        ]
    },
    '/hr/v2/worker-demographics/{anthony-albright-aoid}-GET': {
        'parameters': [
            {
                'name': 'anthony-albright-aoid'
            },
            {
                'name': 'preventCache'
            },
        ]
    },
    '/hr/v2/workers-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': 'preventCache'
            },
            {
                'name': '$filter'
            },
        ]
    },
    '/hr/v2/worker-demographics-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': 'preventCache'
            },
            {
                'name': '$filter'
            },
        ]
    },
    '/payroll/v1/payroll-output-GET': {
        'parameters': [
            {
                'name': '$filter'
            },
            {
                'name': '$count'
            },
            {
                'name': 'use-cache'
            },
            {
                'name': 'level'
            },
            {
                'name': '$select'
            },
        ]
    },
    '/auth/oauth/v2/token-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
        ]
    },
};
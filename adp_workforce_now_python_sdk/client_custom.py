# coding: utf-8
"""
    ADP APIs

    ADP API endpoints.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import typing

from adp_workforce_now_python_sdk.configuration import Configuration
from adp_workforce_now_python_sdk.api_client import ApiClient



class ClientCustom:

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        # customize here

    # add custom methods here
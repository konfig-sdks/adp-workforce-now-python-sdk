# coding: utf-8

"""
    ADP APIs

    ADP API endpoints.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from adp_workforce_now_python_sdk.paths.auth_oauth_v2_token.post import CreateWithAuthorizationHeader
from adp_workforce_now_python_sdk.apis.tags.token_request_api_raw import TokenRequestApiRaw


class TokenRequestApi(
    CreateWithAuthorizationHeader,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TokenRequestApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TokenRequestApiRaw(api_client)

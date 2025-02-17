# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

VERSION = "unknown"

class AzureFileStorageConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for AzureFileStorage.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param url: The URL of the service account, share, directory or file that is the target of the
     desired operation.
    :type url: str
    :keyword version: Specifies the version of the operation to use for this request. Default value
     is "2021-04-10". Note that overriding this default value may result in unsupported behavior.
    :paramtype version: str
    :keyword file_range_write_from_url: Only update is supported: - Update: Writes the bytes
     downloaded from the source url into the specified range. Default value is "update". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype file_range_write_from_url: str
    """

    def __init__(
        self,
        url: str,
        **kwargs: Any
    ) -> None:
        super(AzureFileStorageConfiguration, self).__init__(**kwargs)
        version = kwargs.pop('version', "2021-04-10")  # type: str
        file_range_write_from_url = kwargs.pop('file_range_write_from_url', "update")  # type: str

        if url is None:
            raise ValueError("Parameter 'url' must not be None.")

        self.url = url
        self.version = version
        self.file_range_write_from_url = file_range_write_from_url
        kwargs.setdefault('sdk_moniker', 'azurefilestorage/{}'.format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self,
        **kwargs: Any
    ) -> None:
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get('http_logging_policy') or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')

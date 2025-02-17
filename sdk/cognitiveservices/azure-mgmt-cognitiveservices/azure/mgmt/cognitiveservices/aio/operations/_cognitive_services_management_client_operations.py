# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._cognitive_services_management_client_operations import build_check_domain_availability_request, build_check_sku_availability_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class CognitiveServicesManagementClientOperationsMixin:

    @distributed_trace_async
    async def check_sku_availability(
        self,
        location: str,
        skus: List[str],
        kind: str,
        type: str,
        **kwargs: Any
    ) -> "_models.SkuAvailabilityListResult":
        """Check available SKUs.

        :param location: Resource location.
        :type location: str
        :param skus: The SKU of the resource.
        :type skus: list[str]
        :param kind: The Kind of the resource.
        :type kind: str
        :param type: The Type of the resource.
        :type type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SkuAvailabilityListResult, or the result of cls(response)
        :rtype: ~azure.mgmt.cognitiveservices.models.SkuAvailabilityListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SkuAvailabilityListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _parameters = _models.CheckSkuAvailabilityParameter(skus=skus, kind=kind, type=type)
        _json = self._serialize.body(_parameters, 'CheckSkuAvailabilityParameter')

        request = build_check_sku_availability_request(
            subscription_id=self._config.subscription_id,
            location=location,
            content_type=content_type,
            json=_json,
            template_url=self.check_sku_availability.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SkuAvailabilityListResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_sku_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.CognitiveServices/locations/{location}/checkSkuAvailability'}  # type: ignore


    @distributed_trace_async
    async def check_domain_availability(
        self,
        subdomain_name: str,
        type: str,
        kind: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.DomainAvailability":
        """Check whether a domain is available.

        :param subdomain_name: The subdomain name to use.
        :type subdomain_name: str
        :param type: The Type of the resource.
        :type type: str
        :param kind: The Kind of the resource.
        :type kind: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DomainAvailability, or the result of cls(response)
        :rtype: ~azure.mgmt.cognitiveservices.models.DomainAvailability
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DomainAvailability"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _parameters = _models.CheckDomainAvailabilityParameter(subdomain_name=subdomain_name, type=type, kind=kind)
        _json = self._serialize.body(_parameters, 'CheckDomainAvailabilityParameter')

        request = build_check_domain_availability_request(
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.check_domain_availability.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DomainAvailability', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_domain_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.CognitiveServices/checkDomainAvailability'}  # type: ignore


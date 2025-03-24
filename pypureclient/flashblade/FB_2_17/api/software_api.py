# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.17, developed by Pure Storage, Inc. (http://www.purestorage.com/). 

    OpenAPI spec version: 2.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class SoftwareApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api217_software_check_get_with_http_info(
        self,
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        names=None,  # type: List[str]
        offset=None,  # type: int
        software_names=None,  # type: List[str]
        software_versions=None,  # type: List[str]
        sort=None,  # type: List[str]
        total_item_count=None,  # type: bool
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.SoftwareChecksGetResponse
        """List software check tasks

        Displays a list of software check tasks.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api217_software_check_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str filter: Narrows down the results to only the response objects that satisfy the filter criteria. 
        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned.  This cannot be provided together with the `name` or `names` query parameters. 
        :param int limit: Limits the size of the response to the specified number of objects on each page. To return the total number of resources, set `limit=0`. The total number of resources is returned as a `total_item_count` value. If the page size requested is larger than the system maximum limit, the server returns the maximum limit, disregarding the requested page size. 
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of `names`, then an error is returned. 
        :param int offset: The offset of the first resource to return from a collection. 
        :param list[str] software_names: A comma-separated list of software names. 
        :param list[str] software_versions: A comma-separated list of target software versions. 
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). NOTE: If you provide a sort you will not get a `continuation_token` in the response. 
        :param bool total_item_count: If set to `true`, the `total_item_count` matching the specified query parameters is calculated and returned in the response. If set to `false`, the `total_item_count`  is `null` in the response. This may speed up queries where the `total_item_count` is large. If not specified, defaults to `false`. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: SoftwareChecksGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        if names is not None:
            if not isinstance(names, list):
                names = [names]
        if software_names is not None:
            if not isinstance(software_names, list):
                software_names = [software_names]
        if software_versions is not None:
            if not isinstance(software_versions, list):
                software_versions = [software_versions]
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        if 'limit' in params and params['limit'] < 0:
            raise ValueError("Invalid value for parameter `limit` when calling `api217_software_check_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api217_software_check_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'software_names' in params:
            query_params.append(('software_names', params['software_names']))
            collection_formats['software_names'] = 'csv'
        if 'software_versions' in params:
            query_params.append(('software_versions', params['software_versions']))
            collection_formats['software_versions'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'total_item_count' in params:
            query_params.append(('total_item_count', params['total_item_count']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.17/software-check', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SoftwareChecksGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api217_software_check_post_with_http_info(
        self,
        x_request_id=None,  # type: str
        software_names=None,  # type: List[str]
        software_versions=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.SoftwareChecksResponse
        """Create a software check task

        Creates a software check task. To create a task, use a software name and version. If a task is already running, an error is returned. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api217_software_check_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] software_names: A comma-separated list of software names. 
        :param list[str] software_versions: A comma-separated list of target software versions. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: SoftwareChecksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if software_names is not None:
            if not isinstance(software_names, list):
                software_names = [software_names]
        if software_versions is not None:
            if not isinstance(software_versions, list):
                software_versions = [software_versions]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'software_names' in params:
            query_params.append(('software_names', params['software_names']))
            collection_formats['software_names'] = 'csv'
        if 'software_versions' in params:
            query_params.append(('software_versions', params['software_versions']))
            collection_formats['software_versions'] = 'csv'

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.17/software-check', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SoftwareChecksResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

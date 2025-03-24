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

class TargetsApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api217_targets_delete_with_http_info(
        self,
        x_request_id=None,  # type: str
        ids=None,  # type: List[str]
        names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """DELETE targets

        Delete the connection to the target for replication.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api217_targets_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned.  This cannot be provided together with the `name` or `names` query parameters. 
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of `names`, then an error is returned. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        if names is not None:
            if not isinstance(names, list):
                names = [names]
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
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.17/targets', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api217_targets_get_with_http_info(
        self,
        x_request_id=None,  # type: str
        allow_errors=None,  # type: bool
        context_names=None,  # type: List[str]
        continuation_token=None,  # type: str
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        names=None,  # type: List[str]
        offset=None,  # type: int
        sort=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.TargetGetResponse
        """GET targets

        List targets used for replication.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api217_targets_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str x_request_id: Supplied by client during request or generated by server. 
        :param bool allow_errors: If set to `true`, the API will allow the operation to continue even if there are errors. Any errors will be returned in the `errors` field of the response. If set to `false`, the operation will fail if there are any errors. 
        :param list[str] context_names: Performs the operation on the unique contexts specified. If specified, each context name must be the name of an array in the same fleet. If not specified, the context will default to the array that received this request.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`.  Enter multiple names in comma-separated format. For example, `name01,name02`. 
        :param str continuation_token: A token used to retrieve the next page of data with some consistency guaranteed. The token is a Base64 encoded value. Set `continuation_token` to the system-generated token taken from the `x-next-token` header field of the response. A query has reached its last page when the response does not include a token. Pagination requires the `limit` and `continuation_token` query parameters. 
        :param str filter: Narrows down the results to only the response objects that satisfy the filter criteria. 
        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned.  This cannot be provided together with the `name` or `names` query parameters. 
        :param int limit: Limits the size of the response to the specified number of objects on each page. To return the total number of resources, set `limit=0`. The total number of resources is returned as a `total_item_count` value. If the page size requested is larger than the system maximum limit, the server returns the maximum limit, disregarding the requested page size. 
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of `names`, then an error is returned. 
        :param int offset: The offset of the first resource to return from a collection. 
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). NOTE: If you provide a sort you will not get a `continuation_token` in the response. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: TargetGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if context_names is not None:
            if not isinstance(context_names, list):
                context_names = [context_names]
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        if names is not None:
            if not isinstance(names, list):
                names = [names]
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
            raise ValueError("Invalid value for parameter `limit` when calling `api217_targets_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api217_targets_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'allow_errors' in params:
            query_params.append(('allow_errors', params['allow_errors']))
        if 'context_names' in params:
            query_params.append(('context_names', params['context_names']))
            collection_formats['context_names'] = 'csv'
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
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
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

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
            '/api/2.17/targets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TargetGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api217_targets_patch_with_http_info(
        self,
        target=None,  # type: models.Target
        x_request_id=None,  # type: str
        ids=None,  # type: List[str]
        names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.TargetResponse
        """PATCH targets

        Modify the target attributes for replication.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api217_targets_patch_with_http_info(target, async_req=True)
        >>> result = thread.get()

        :param Target target: (required)
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned.  This cannot be provided together with the `name` or `names` query parameters. 
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of `names`, then an error is returned. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: TargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        if names is not None:
            if not isinstance(names, list):
                names = [names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())
        # verify the required parameter 'target' is set
        if target is None:
            raise TypeError("Missing the required parameter `target` when calling `api217_targets_patch`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'target' in params:
            body_params = params['target']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.17/targets', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TargetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api217_targets_performance_replication_get_with_http_info(
        self,
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        end_time=None,  # type: int
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        names=None,  # type: List[str]
        offset=None,  # type: int
        resolution=None,  # type: int
        sort=None,  # type: List[str]
        start_time=None,  # type: int
        total_only=None,  # type: bool
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.ResourcePerformanceReplicationGetResponse
        """GET targets/performance/replication

        List replication performance metrics for targets.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api217_targets_performance_replication_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str x_request_id: Supplied by client during request or generated by server. 
        :param str continuation_token: A token used to retrieve the next page of data with some consistency guaranteed. The token is a Base64 encoded value. Set `continuation_token` to the system-generated token taken from the `x-next-token` header field of the response. A query has reached its last page when the response does not include a token. Pagination requires the `limit` and `continuation_token` query parameters. 
        :param int end_time: When the time window ends (in milliseconds since epoch). 
        :param str filter: Narrows down the results to only the response objects that satisfy the filter criteria. 
        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned.  This cannot be provided together with the `name` or `names` query parameters. 
        :param int limit: Limits the size of the response to the specified number of objects on each page. To return the total number of resources, set `limit=0`. The total number of resources is returned as a `total_item_count` value. If the page size requested is larger than the system maximum limit, the server returns the maximum limit, disregarding the requested page size. 
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of `names`, then an error is returned. 
        :param int offset: The offset of the first resource to return from a collection. 
        :param int resolution: The desired ms between samples. Available resolutions may depend on data type, `start_time` and `end_time`. In general `1000`, `30000`, `300000`, `1800000`, `7200000`, and `86400000` are possible values. 
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). NOTE: If you provide a sort you will not get a `continuation_token` in the response. 
        :param int start_time: When the time window starts (in milliseconds since epoch). 
        :param bool total_only: If set to `true`, returns the aggregate value of all items after filtering. Where it makes more sense, the average value is displayed instead. The values are displayed for each name where meaningful. If `total_only=true`, the `items` list will be empty. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: ResourcePerformanceReplicationGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        if names is not None:
            if not isinstance(names, list):
                names = [names]
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

        if 'end_time' in params and params['end_time'] < 0:
            raise ValueError("Invalid value for parameter `end_time` when calling `api217_targets_performance_replication_get`, must be a value greater than or equal to `0`")
        if 'limit' in params and params['limit'] < 0:
            raise ValueError("Invalid value for parameter `limit` when calling `api217_targets_performance_replication_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api217_targets_performance_replication_get`, must be a value greater than or equal to `0`")
        if 'resolution' in params and params['resolution'] < 0:
            raise ValueError("Invalid value for parameter `resolution` when calling `api217_targets_performance_replication_get`, must be a value greater than or equal to `0`")
        if 'start_time' in params and params['start_time'] < 0:
            raise ValueError("Invalid value for parameter `start_time` when calling `api217_targets_performance_replication_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))
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
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))
        if 'total_only' in params:
            query_params.append(('total_only', params['total_only']))

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
            '/api/2.17/targets/performance/replication', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcePerformanceReplicationGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api217_targets_post_with_http_info(
        self,
        target=None,  # type: models.TargetPost
        names=None,  # type: List[str]
        x_request_id=None,  # type: str
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.TargetResponse
        """POST targets

        Add a target for replication.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api217_targets_post_with_http_info(target, names, async_req=True)
        >>> result = thread.get()

        :param TargetPost target: (required)
        :param list[str] names: A comma-separated list of resource names.  (required)
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: TargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if names is not None:
            if not isinstance(names, list):
                names = [names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())
        # verify the required parameter 'target' is set
        if target is None:
            raise TypeError("Missing the required parameter `target` when calling `api217_targets_post`")
        # verify the required parameter 'names' is set
        if names is None:
            raise TypeError("Missing the required parameter `names` when calling `api217_targets_post`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'target' in params:
            body_params = params['target']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.17/targets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TargetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

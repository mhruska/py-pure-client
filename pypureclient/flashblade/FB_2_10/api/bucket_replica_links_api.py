# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.10, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
from typing import List, Optional

from .. import models

class BucketReplicaLinksApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api210_bucket_replica_links_delete_with_http_info(
        self,
        ids=None,  # type: List[str]
        local_bucket_ids=None,  # type: List[str]
        local_bucket_names=None,  # type: List[str]
        remote_bucket_names=None,  # type: List[str]
        remote_ids=None,  # type: List[str]
        remote_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """DELETE bucket-replica-links

        Delete a bucket replica link.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api210_bucket_replica_links_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned. This cannot be provided together with the `name` or `names` query parameters.
        :param list[str] local_bucket_ids: A comma-separated list of local bucket IDs. If after filtering, there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `local_bucket_names` query parameter.
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names. If there is not at least one resource that matches each of the elements, then an error is returned.
        :param list[str] remote_ids: A comma-separated list of remote array IDs. If after filtering, there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `remote_names` query parameter.
        :param list[str] remote_names: A comma-separated list of remote array names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with `remote_ids` query parameter.
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
        if local_bucket_ids is not None:
            if not isinstance(local_bucket_ids, list):
                local_bucket_ids = [local_bucket_ids]
        if local_bucket_names is not None:
            if not isinstance(local_bucket_names, list):
                local_bucket_names = [local_bucket_names]
        if remote_bucket_names is not None:
            if not isinstance(remote_bucket_names, list):
                remote_bucket_names = [remote_bucket_names]
        if remote_ids is not None:
            if not isinstance(remote_ids, list):
                remote_ids = [remote_ids]
        if remote_names is not None:
            if not isinstance(remote_names, list):
                remote_names = [remote_names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'local_bucket_ids' in params:
            query_params.append(('local_bucket_ids', params['local_bucket_ids']))
            collection_formats['local_bucket_ids'] = 'csv'
        if 'local_bucket_names' in params:
            query_params.append(('local_bucket_names', params['local_bucket_names']))
            collection_formats['local_bucket_names'] = 'csv'
        if 'remote_bucket_names' in params:
            query_params.append(('remote_bucket_names', params['remote_bucket_names']))
            collection_formats['remote_bucket_names'] = 'csv'
        if 'remote_ids' in params:
            query_params.append(('remote_ids', params['remote_ids']))
            collection_formats['remote_ids'] = 'csv'
        if 'remote_names' in params:
            query_params.append(('remote_names', params['remote_names']))
            collection_formats['remote_names'] = 'csv'

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
            '/api/2.10/bucket-replica-links', 'DELETE',
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

    def api210_bucket_replica_links_get_with_http_info(
        self,
        continuation_token=None,  # type: str
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        local_bucket_ids=None,  # type: List[str]
        local_bucket_names=None,  # type: List[str]
        offset=None,  # type: int
        remote_bucket_names=None,  # type: List[str]
        remote_ids=None,  # type: List[str]
        remote_names=None,  # type: List[str]
        sort=None,  # type: List[str]
        total_only=None,  # type: bool
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.BucketReplicaLinkGetResponse
        """GET bucket-replica-links

        List bucket replica links for object replication.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api210_bucket_replica_links_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :param str filter: Exclude resources that don't match the specified criteria.
        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned. This cannot be provided together with the `name` or `names` query parameters.
        :param int limit: Limit the size of the response to the specified number of resources. A `limit` of `0` can be used to get the number of resources without getting all of the resources. It will be returned in the `total_item_count` field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request.
        :param list[str] local_bucket_ids: A comma-separated list of local bucket IDs. If after filtering, there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `local_bucket_names` query parameter.
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with `local_bucket_ids` query parameter.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names. If there is not at least one resource that matches each of the elements, then an error is returned.
        :param list[str] remote_ids: A comma-separated list of remote array IDs. If after filtering, there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `remote_names` query parameter.
        :param list[str] remote_names: A comma-separated list of remote array names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with `remote_ids` query parameter.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). NOTE: If you provide a sort you will not get a `continuation_token` in the response.
        :param bool total_only: Only return the total record for the specified items. The total record will be the total of all items after filtering. The `items` list will be empty.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: BucketReplicaLinkGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        if local_bucket_ids is not None:
            if not isinstance(local_bucket_ids, list):
                local_bucket_ids = [local_bucket_ids]
        if local_bucket_names is not None:
            if not isinstance(local_bucket_names, list):
                local_bucket_names = [local_bucket_names]
        if remote_bucket_names is not None:
            if not isinstance(remote_bucket_names, list):
                remote_bucket_names = [remote_bucket_names]
        if remote_ids is not None:
            if not isinstance(remote_ids, list):
                remote_ids = [remote_ids]
        if remote_names is not None:
            if not isinstance(remote_names, list):
                remote_names = [remote_names]
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]

        if 'limit' in params and params['limit'] < 1:
            raise ValueError("Invalid value for parameter `limit` when calling `api210_bucket_replica_links_get`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api210_bucket_replica_links_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'local_bucket_ids' in params:
            query_params.append(('local_bucket_ids', params['local_bucket_ids']))
            collection_formats['local_bucket_ids'] = 'csv'
        if 'local_bucket_names' in params:
            query_params.append(('local_bucket_names', params['local_bucket_names']))
            collection_formats['local_bucket_names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'remote_bucket_names' in params:
            query_params.append(('remote_bucket_names', params['remote_bucket_names']))
            collection_formats['remote_bucket_names'] = 'csv'
        if 'remote_ids' in params:
            query_params.append(('remote_ids', params['remote_ids']))
            collection_formats['remote_ids'] = 'csv'
        if 'remote_names' in params:
            query_params.append(('remote_names', params['remote_names']))
            collection_formats['remote_names'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'total_only' in params:
            query_params.append(('total_only', params['total_only']))

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
            '/api/2.10/bucket-replica-links', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BucketReplicaLinkGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api210_bucket_replica_links_patch_with_http_info(
        self,
        bucket_replica_link=None,  # type: models.BucketReplicaLink
        ids=None,  # type: List[str]
        local_bucket_ids=None,  # type: List[str]
        local_bucket_names=None,  # type: List[str]
        remote_bucket_names=None,  # type: List[str]
        remote_ids=None,  # type: List[str]
        remote_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.BucketReplicaLinkResponse
        """PATCH bucket-replica-links

        Modify the configuration of a bucket replica link including whether the link is paused and the object store remote credentials used.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api210_bucket_replica_links_patch_with_http_info(bucket_replica_link, async_req=True)
        >>> result = thread.get()

        :param BucketReplicaLink bucket_replica_link: (required)
        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned. This cannot be provided together with the `name` or `names` query parameters.
        :param list[str] local_bucket_ids: A comma-separated list of local bucket IDs. If after filtering, there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `local_bucket_names` query parameter.
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names. If there is not at least one resource that matches each of the elements, then an error is returned.
        :param list[str] remote_ids: A comma-separated list of remote array IDs. If after filtering, there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `remote_names` query parameter.
        :param list[str] remote_names: A comma-separated list of remote array names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with `remote_ids` query parameter.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: BucketReplicaLinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        if local_bucket_ids is not None:
            if not isinstance(local_bucket_ids, list):
                local_bucket_ids = [local_bucket_ids]
        if local_bucket_names is not None:
            if not isinstance(local_bucket_names, list):
                local_bucket_names = [local_bucket_names]
        if remote_bucket_names is not None:
            if not isinstance(remote_bucket_names, list):
                remote_bucket_names = [remote_bucket_names]
        if remote_ids is not None:
            if not isinstance(remote_ids, list):
                remote_ids = [remote_ids]
        if remote_names is not None:
            if not isinstance(remote_names, list):
                remote_names = [remote_names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # verify the required parameter 'bucket_replica_link' is set
        if bucket_replica_link is None:
            raise TypeError("Missing the required parameter `bucket_replica_link` when calling `api210_bucket_replica_links_patch`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'local_bucket_ids' in params:
            query_params.append(('local_bucket_ids', params['local_bucket_ids']))
            collection_formats['local_bucket_ids'] = 'csv'
        if 'local_bucket_names' in params:
            query_params.append(('local_bucket_names', params['local_bucket_names']))
            collection_formats['local_bucket_names'] = 'csv'
        if 'remote_bucket_names' in params:
            query_params.append(('remote_bucket_names', params['remote_bucket_names']))
            collection_formats['remote_bucket_names'] = 'csv'
        if 'remote_ids' in params:
            query_params.append(('remote_ids', params['remote_ids']))
            collection_formats['remote_ids'] = 'csv'
        if 'remote_names' in params:
            query_params.append(('remote_names', params['remote_names']))
            collection_formats['remote_names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bucket_replica_link' in params:
            body_params = params['bucket_replica_link']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.10/bucket-replica-links', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BucketReplicaLinkResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api210_bucket_replica_links_post_with_http_info(
        self,
        bucket_replica_link=None,  # type: models.BucketReplicaLinkPost
        local_bucket_names=None,  # type: List[str]
        local_bucket_ids=None,  # type: List[str]
        remote_bucket_names=None,  # type: List[str]
        remote_credentials_names=None,  # type: List[str]
        remote_credentials_ids=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.BucketReplicaLinkResponse
        """POST bucket-replica-links

        Create a bucket replica link for object replication.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api210_bucket_replica_links_post_with_http_info(bucket_replica_link, async_req=True)
        >>> result = thread.get()

        :param BucketReplicaLinkPost bucket_replica_link: (required)
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] local_bucket_ids: A comma-separated list of local bucket IDs. If after filtering, there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `local_bucket_names` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names. If there is not at least one resource that matches each of the elements, then an error is returned.
        :param list[str] remote_credentials_names: A comma-separated list of remote credentials names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `remote_credentials_ids` query parameter.
        :param list[str] remote_credentials_ids: A comma-separated list of remote credentials IDs. If after filtering, there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `remote_credentials_names` query parameter.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: BucketReplicaLinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if local_bucket_names is not None:
            if not isinstance(local_bucket_names, list):
                local_bucket_names = [local_bucket_names]
        if local_bucket_ids is not None:
            if not isinstance(local_bucket_ids, list):
                local_bucket_ids = [local_bucket_ids]
        if remote_bucket_names is not None:
            if not isinstance(remote_bucket_names, list):
                remote_bucket_names = [remote_bucket_names]
        if remote_credentials_names is not None:
            if not isinstance(remote_credentials_names, list):
                remote_credentials_names = [remote_credentials_names]
        if remote_credentials_ids is not None:
            if not isinstance(remote_credentials_ids, list):
                remote_credentials_ids = [remote_credentials_ids]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # verify the required parameter 'bucket_replica_link' is set
        if bucket_replica_link is None:
            raise TypeError("Missing the required parameter `bucket_replica_link` when calling `api210_bucket_replica_links_post`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'local_bucket_names' in params:
            query_params.append(('local_bucket_names', params['local_bucket_names']))
            collection_formats['local_bucket_names'] = 'csv'
        if 'local_bucket_ids' in params:
            query_params.append(('local_bucket_ids', params['local_bucket_ids']))
            collection_formats['local_bucket_ids'] = 'csv'
        if 'remote_bucket_names' in params:
            query_params.append(('remote_bucket_names', params['remote_bucket_names']))
            collection_formats['remote_bucket_names'] = 'csv'
        if 'remote_credentials_names' in params:
            query_params.append(('remote_credentials_names', params['remote_credentials_names']))
            collection_formats['remote_credentials_names'] = 'csv'
        if 'remote_credentials_ids' in params:
            query_params.append(('remote_credentials_ids', params['remote_credentials_ids']))
            collection_formats['remote_credentials_ids'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bucket_replica_link' in params:
            body_params = params['bucket_replica_link']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.10/bucket-replica-links', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BucketReplicaLinkResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

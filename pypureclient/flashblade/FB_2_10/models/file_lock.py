# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.10, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_10 import models

class FileLock(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'access_type': 'str',
        'client': 'FixedReferenceNoId',
        'created_at': 'int',
        'inode': 'int',
        'path': 'str',
        'protocol': 'str',
        'range': 'FileLockRange',
        'source': 'FixedReference'
    }

    attribute_map = {
        'name': 'name',
        'access_type': 'access_type',
        'client': 'client',
        'created_at': 'created_at',
        'inode': 'inode',
        'path': 'path',
        'protocol': 'protocol',
        'range': 'range',
        'source': 'source'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        access_type=None,  # type: str
        client=None,  # type: models.FixedReferenceNoId
        created_at=None,  # type: int
        inode=None,  # type: int
        path=None,  # type: str
        protocol=None,  # type: str
        range=None,  # type: models.FileLockRange
        source=None,  # type: models.FixedReference
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            access_type (str): Type of access the lock provides. Valid values are `shared`, `exclusive` and `no-access`.
            client (FixedReferenceNoId): Reference to the file system client that holds the lock.
            created_at (int): Creation timestamp of the lock. Measured in milliseconds since the UNIX epoch.
            inode (int): The inode of the file where the lock is found relative to the specified `source`.
            path (str): Path to the file where the lock is found relative to `source`. If it is longer than 1023 characters, it will be truncated and only the last 1023 characters will be returned. If multiple hard links exist to the file on which the lock is held, only one is returned. This field will be `null` if the path cannot be resolved.
            protocol (str): The protocol utilized for obtaining and managing the lock. Valid values include `NLM`, `NFSv4.1` and `SMB`.
            range (FileLockRange)
            source (FixedReference): Reference to location where the path/inode can be found.
        """
        if name is not None:
            self.name = name
        if access_type is not None:
            self.access_type = access_type
        if client is not None:
            self.client = client
        if created_at is not None:
            self.created_at = created_at
        if inode is not None:
            self.inode = inode
        if path is not None:
            self.path = path
        if protocol is not None:
            self.protocol = protocol
        if range is not None:
            self.range = range
        if source is not None:
            self.source = source

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FileLock`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(FileLock, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.11, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_11 import models

class ObjectStoreAccount(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'created': 'int',
        'object_count': 'int',
        'space': 'Space',
        'bucket_defaults': 'BucketDefaultsReadonly',
        'hard_limit_enabled': 'bool',
        'quota_limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'created': 'created',
        'object_count': 'object_count',
        'space': 'space',
        'bucket_defaults': 'bucket_defaults',
        'hard_limit_enabled': 'hard_limit_enabled',
        'quota_limit': 'quota_limit'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        created=None,  # type: int
        object_count=None,  # type: int
        space=None,  # type: models.Space
        bucket_defaults=None,  # type: models.BucketDefaultsReadonly
        hard_limit_enabled=None,  # type: bool
        quota_limit=None,  # type: int
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            created (int): Creation timestamp of the object.
            object_count (int): The count of objects within the account.
            space (Space): The space specification of the object store account.
            bucket_defaults (BucketDefaultsReadonly): Default settings to be applied to newly created buckets associated with this account. Values here will be used in bucket creation requests which do not specify their own values for corresponding fields.
            hard_limit_enabled (bool): If set to `true`, the account's size, as defined by `quota_limit`, is used as a hard limit quota. If set to `false`, a hard limit quota will not be applied to the account, but soft quota alerts will still be sent if the account has a value set for `quota_limit`.
            quota_limit (int): The effective quota limit applied against the size of the account, displayed in bytes. If unset, the account is unlimited in size.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if object_count is not None:
            self.object_count = object_count
        if space is not None:
            self.space = space
        if bucket_defaults is not None:
            self.bucket_defaults = bucket_defaults
        if hard_limit_enabled is not None:
            self.hard_limit_enabled = hard_limit_enabled
        if quota_limit is not None:
            self.quota_limit = quota_limit

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ObjectStoreAccount`".format(key))
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
        if issubclass(ObjectStoreAccount, dict):
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
        if not isinstance(other, ObjectStoreAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

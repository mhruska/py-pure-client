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

class Bucket(object):
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
        'account': 'FixedReference',
        'created': 'int',
        'destroyed': 'bool',
        'object_count': 'int',
        'space': 'Space',
        'time_remaining': 'int',
        'versioning': 'str',
        'bucket_type': 'str',
        'eradication_config': 'BucketEradicationConfig',
        'hard_limit_enabled': 'bool',
        'object_lock_config': 'ObjectLockConfigResponse',
        'quota_limit': 'int',
        'retention_lock': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'account': 'account',
        'created': 'created',
        'destroyed': 'destroyed',
        'object_count': 'object_count',
        'space': 'space',
        'time_remaining': 'time_remaining',
        'versioning': 'versioning',
        'bucket_type': 'bucket_type',
        'eradication_config': 'eradication_config',
        'hard_limit_enabled': 'hard_limit_enabled',
        'object_lock_config': 'object_lock_config',
        'quota_limit': 'quota_limit',
        'retention_lock': 'retention_lock'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        account=None,  # type: models.FixedReference
        created=None,  # type: int
        destroyed=None,  # type: bool
        object_count=None,  # type: int
        space=None,  # type: models.Space
        time_remaining=None,  # type: int
        versioning=None,  # type: str
        bucket_type=None,  # type: str
        eradication_config=None,  # type: models.BucketEradicationConfig
        hard_limit_enabled=None,  # type: bool
        object_lock_config=None,  # type: models.ObjectLockConfigResponse
        quota_limit=None,  # type: int
        retention_lock=None,  # type: str
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            account (FixedReference)
            created (int): Creation timestamp of the object.
            destroyed (bool): Is the bucket destroyed?
            object_count (int): The count of objects within the bucket.
            space (Space): The space specification of the bucket.
            time_remaining (int): Time in milliseconds before the bucket is eradicated. `null` if not destroyed.
            versioning (str): The versioning state for objects within the bucket. Valid values are `none`, `enabled`, and `suspended`.
            bucket_type (str): The bucket type for the bucket.
            eradication_config (BucketEradicationConfig)
            hard_limit_enabled (bool): If set to `true`, the bucket's size, as defined by `quota_limit`, is used as a hard limit quota. If set to `false`, a hard limit quota will not be applied to the bucket, but soft quota alerts will still be sent if the bucket has a value set for `quota_limit`.
            object_lock_config (ObjectLockConfigResponse)
            quota_limit (int): The effective quota limit applied against the size of the bucket, displayed in bytes. If unset, the bucket is unlimited in size.
            retention_lock (str): If set to `ratcheted`, then `object_lock_config.default_retention_mode` cannot be changed if set to `compliance`. In this case, the value of `object_lock_config.default_retention` can only be increased and `object_lock_config.default_retention_mode` cannot be changed once set to `compliance`. Valid values are `unlocked` and `ratcheted`. Contact Pure Technical Services to change `ratcheted` to `unlocked`.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if account is not None:
            self.account = account
        if created is not None:
            self.created = created
        if destroyed is not None:
            self.destroyed = destroyed
        if object_count is not None:
            self.object_count = object_count
        if space is not None:
            self.space = space
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if versioning is not None:
            self.versioning = versioning
        if bucket_type is not None:
            self.bucket_type = bucket_type
        if eradication_config is not None:
            self.eradication_config = eradication_config
        if hard_limit_enabled is not None:
            self.hard_limit_enabled = hard_limit_enabled
        if object_lock_config is not None:
            self.object_lock_config = object_lock_config
        if quota_limit is not None:
            self.quota_limit = quota_limit
        if retention_lock is not None:
            self.retention_lock = retention_lock

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Bucket`".format(key))
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
        if issubclass(Bucket, dict):
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
        if not isinstance(other, Bucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

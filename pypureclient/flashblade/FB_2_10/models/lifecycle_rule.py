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

class LifecycleRule(object):
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
        'bucket': 'FixedReference',
        'enabled': 'bool',
        'keep_previous_version_for': 'int',
        'prefix': 'str',
        'rule_id': 'str',
        'abort_incomplete_multipart_uploads_after': 'int',
        'keep_current_version_for': 'int',
        'keep_current_version_until': 'int',
        'cleanup_expired_object_delete_marker': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'bucket': 'bucket',
        'enabled': 'enabled',
        'keep_previous_version_for': 'keep_previous_version_for',
        'prefix': 'prefix',
        'rule_id': 'rule_id',
        'abort_incomplete_multipart_uploads_after': 'abort_incomplete_multipart_uploads_after',
        'keep_current_version_for': 'keep_current_version_for',
        'keep_current_version_until': 'keep_current_version_until',
        'cleanup_expired_object_delete_marker': 'cleanup_expired_object_delete_marker'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        bucket=None,  # type: models.FixedReference
        enabled=None,  # type: bool
        keep_previous_version_for=None,  # type: int
        prefix=None,  # type: str
        rule_id=None,  # type: str
        abort_incomplete_multipart_uploads_after=None,  # type: int
        keep_current_version_for=None,  # type: int
        keep_current_version_until=None,  # type: int
        cleanup_expired_object_delete_marker=None,  # type: bool
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            bucket (FixedReference): The bucket which this lifecycle rule is targeting.
            enabled (bool): If set to `true`, this rule will be enabled.
            keep_previous_version_for (int): Time after which previous versions will be marked expired. Measured in milliseconds. Must be a multiple of 86400000 to represent a whole number of days.
            prefix (str): Object key prefix identifying one or more objects in the bucket. Can have a maximum length of 1024 characters.
            rule_id (str): Unique identifier for the rule. Can have a maximum length of 255 characters.
            abort_incomplete_multipart_uploads_after (int): Duration of time after which incomplete multipart uploads will be aborted. Measured in milliseconds. Must be a multiple of 86400000 to represent a whole number of days.
            keep_current_version_for (int): Time after which current versions will be marked expired. Measured in milliseconds. Must be a multiple of 86400000 to represent a whole number of days.
            keep_current_version_until (int): Time after which current versions will be marked expired. Measured in milliseconds, time since epoch. Must be a valid date, accurate to day.
            cleanup_expired_object_delete_marker (bool): Returns a value of `true` if the expired object delete markers will be removed.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if bucket is not None:
            self.bucket = bucket
        if enabled is not None:
            self.enabled = enabled
        if keep_previous_version_for is not None:
            self.keep_previous_version_for = keep_previous_version_for
        if prefix is not None:
            self.prefix = prefix
        if rule_id is not None:
            self.rule_id = rule_id
        if abort_incomplete_multipart_uploads_after is not None:
            self.abort_incomplete_multipart_uploads_after = abort_incomplete_multipart_uploads_after
        if keep_current_version_for is not None:
            self.keep_current_version_for = keep_current_version_for
        if keep_current_version_until is not None:
            self.keep_current_version_until = keep_current_version_until
        if cleanup_expired_object_delete_marker is not None:
            self.cleanup_expired_object_delete_marker = cleanup_expired_object_delete_marker

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LifecycleRule`".format(key))
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
        if issubclass(LifecycleRule, dict):
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
        if not isinstance(other, LifecycleRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

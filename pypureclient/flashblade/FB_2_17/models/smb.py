# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.17, developed by Pure Storage, Inc. (http://www.purestorage.com/). 

    OpenAPI spec version: 2.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_17 import models

class Smb(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'continuous_availability_enabled': 'bool',
        'share_policy': 'ReferenceWritable',
        'client_policy': 'ReferenceWritable',
        'enabled': 'bool'
    }

    attribute_map = {
        'continuous_availability_enabled': 'continuous_availability_enabled',
        'share_policy': 'share_policy',
        'client_policy': 'client_policy',
        'enabled': 'enabled'
    }

    required_args = {
    }

    def __init__(
        self,
        continuous_availability_enabled=None,  # type: bool
        share_policy=None,  # type: models.ReferenceWritable
        client_policy=None,  # type: models.ReferenceWritable
        enabled=None,  # type: bool
    ):
        """
        Keyword args:
            continuous_availability_enabled (bool): If set to `true`, the file system will be continuously available during disruptive scenarios such as network disruption, blades failover, etc. If not specified, defaults to `true`. 
            share_policy (ReferenceWritable): Deprecated. See File System Exports for newer functionality. The value returned will be the `policy` of the File System Export for the default server, and SMB, with the `export_name` matching the file system name, if there is one and null otherwise. Modifying this field will still work. If the current value is null, then setting this field will attempt to create a File System Export with the policy and other default values. The `export_name` will be the same as the file system's `name`. If the current value is not null, then setting this field will change the `policy` in the matching File System Export. The SMB Share policy for the file system. Setting a policy here grants access permissions (e.g. allow or deny Full Control, Change, and/or Read) to the file system via SMB on a per-user / per-group basis. If no policy is set here, no user or group will have access. Use \"\" to clear. 
            client_policy (ReferenceWritable): Deprecated. See File System Exports for newer functionality. The value returned will be the `client_policy` of the File System Export for the default server, and SMB, with the `export_name` matching the file system name, if there is one and null otherwise. Modifying this field will still work. If the current value is null, then setting this field will attempt to create a File System Export with the `client_policy` and other default values. The `export_name` will be the same as the file system's `name`. If the current value is not null, then setting this field will change the `client_policy` in the matching File System Export. The SMB Client policy for the file system. Setting a policy here grants access permissions (e.g. read-only or read-write) to the file system via SMB on a per-client basis. If no policy is set here, no client will have access. Use \"\" to clear. 
            enabled (bool): If set to `true`, enables access to the file system over the SMB protocol. If not specified, defaults to `false`. 
        """
        if continuous_availability_enabled is not None:
            self.continuous_availability_enabled = continuous_availability_enabled
        if share_policy is not None:
            self.share_policy = share_policy
        if client_policy is not None:
            self.client_policy = client_policy
        if enabled is not None:
            self.enabled = enabled

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Smb`".format(key))
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
        if issubclass(Smb, dict):
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
        if not isinstance(other, Smb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

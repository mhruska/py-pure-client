# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.6, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_6 import models

class Nfs(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'v3_enabled': 'bool',
        'v4_1_enabled': 'bool',
        'rules': 'str',
        'export_policy': 'ReferenceWritable'
    }

    attribute_map = {
        'v3_enabled': 'v3_enabled',
        'v4_1_enabled': 'v4_1_enabled',
        'rules': 'rules',
        'export_policy': 'export_policy'
    }

    required_args = {
    }

    def __init__(
        self,
        v3_enabled=None,  # type: bool
        v4_1_enabled=None,  # type: bool
        rules=None,  # type: str
        export_policy=None,  # type: models.ReferenceWritable
    ):
        """
        Keyword args:
            v3_enabled (bool): If set to `true`, the NFSv3 protocol will be enabled.
            v4_1_enabled (bool): If set to `true`, the NFSv4.1 protocol will be enabled.
            rules (str): The NFS export rules for the system. Either the `export_policy` or `rules` will control the NFS export functionality for the file system. If this is set, then the `policy` field will be cleared. Both `export_policy` and `rules` can not be set in the same request. Rules can be applied to an individual client or a range of clients specified by IP address (`ip_address(options)`), netmask (`ip_address/length(options)`), or netgroup (`@groupname(options)`). Possible export options include `rw`, `ro`, `fileid_32bit`,  `no_fileid_32bit`, `anonuid`, `anongid`, `root_squash`, `no_root_squash`, `all_squash`, `no_all_squash`,  `secure`, `insecure`, `atime`, `noatime`, and `sec`. If not specified, defaults to `*(rw,no_root_squash)`.
            export_policy (ReferenceWritable): The NFS export policy for the system. Either the `export_policy` or `rules` will control the NFS export functionality for the file system. If this is set, then the `rules` field will be cleared. Both `export_policy` and `rules` can not be set in the same request.
        """
        if v3_enabled is not None:
            self.v3_enabled = v3_enabled
        if v4_1_enabled is not None:
            self.v4_1_enabled = v4_1_enabled
        if rules is not None:
            self.rules = rules
        if export_policy is not None:
            self.export_policy = export_policy

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Nfs`".format(key))
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
        if issubclass(Nfs, dict):
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
        if not isinstance(other, Nfs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

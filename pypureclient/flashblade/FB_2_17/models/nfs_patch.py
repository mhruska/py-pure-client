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

class NfsPatch(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'export_policy': 'ReferenceWritable',
        'v3_enabled': 'bool',
        'rules': 'str',
        'v4_1_enabled': 'bool',
        'add_rules': 'str',
        'after': 'str',
        'remove_rules': 'str'
    }

    attribute_map = {
        'export_policy': 'export_policy',
        'v3_enabled': 'v3_enabled',
        'rules': 'rules',
        'v4_1_enabled': 'v4_1_enabled',
        'add_rules': 'add_rules',
        'after': 'after',
        'remove_rules': 'remove_rules'
    }

    required_args = {
    }

    def __init__(
        self,
        export_policy=None,  # type: models.ReferenceWritable
        v3_enabled=None,  # type: bool
        rules=None,  # type: str
        v4_1_enabled=None,  # type: bool
        add_rules=None,  # type: str
        after=None,  # type: str
        remove_rules=None,  # type: str
    ):
        """
        Keyword args:
            export_policy (ReferenceWritable): Deprecated. See File System Exports for newer functionality. The value returned will be the `policy` of the File System Export for the default server, and NFS, with the `export_name` matching the file system name, if there is one and null otherwise. Modifying this field will still work. If the current value is null, then setting this field will attempt to create a File System Export with the policy and other default values. The `export_name` will be the same as the file system's `name`. If the current value is not null, then setting this field will change the policy in the matching File System Export. Either the `export_policy` or `rules` will control the NFS export functionality for the file system. If this is set, then the `rules` field will be cleared. Both `export_policy` and `rules` can not be set in the same request. 
            v3_enabled (bool): If set to `true`, the NFSv3 protocol will be enabled. 
            rules (str): Deprecated. See File System Exports and NFS Export Policies for newer functionality. Modifying this field will still work, causing the matching File System Export to be deleted, if there is one. See `export_policy`. Both `export_policy` and `rules` can not be set in the same request. Rules can be applied to an individual client or a range of clients specified by IP address (`ip_address(options)`), netmask (`ip_address/length(options)`), netgroup (`@groupname(options)`), hostname (`hostname(options)`) (see RFC-1123 part 2.1), fully qualified domain name (`host.exampledomain.com(options)`) (see RFC-1123 part 2.1, RFC 2181 part 11), or wildcards with fully qualified domain name or hostname (`*.exampledomain?.com(options)`). Possible export options include `rw`, `ro`, `fileid_32bit`,  `no_fileid_32bit`, `anonuid`, `anongid`, `root_squash`, `no_root_squash`, `all_squash`, `no_all_squash`,  `secure`, `insecure`, `atime`, `noatime`, and `sec`. If not specified, defaults to `*(rw,no_root_squash)`. 
            v4_1_enabled (bool): If set to `true`, the NFSv4.1 protocol will be enabled. 
            add_rules (str): The rules which will be added to the existing NFS export rules for the file system. If `export_policy` is in use and and this field is set, the operation will fail. 
            after (str): The `after` field can be used with `add_rules` or `remove_rules` or both. If used with `add_rules`, then the `add_rules` string will be inserted after the first occurrence of the `after` string. If used with `remove_rules`, then remove the first occurrence of `remove_rules` after the first occurrence of the `after` string. The `remove_rules` will be processed before the `add_rules`. 
            remove_rules (str): The rules which will be removed from the existing NFS export rules for the file system. Only the first occurrence of the `remove_rules` will be removed. If `export_policy` is in use and and this field is set, the operation will fail. 
        """
        if export_policy is not None:
            self.export_policy = export_policy
        if v3_enabled is not None:
            self.v3_enabled = v3_enabled
        if rules is not None:
            self.rules = rules
        if v4_1_enabled is not None:
            self.v4_1_enabled = v4_1_enabled
        if add_rules is not None:
            self.add_rules = add_rules
        if after is not None:
            self.after = after
        if remove_rules is not None:
            self.remove_rules = remove_rules

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NfsPatch`".format(key))
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
        if issubclass(NfsPatch, dict):
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
        if not isinstance(other, NfsPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

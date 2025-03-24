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

class ActiveDirectoryPatch(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'global_catalog_servers': 'list[str]',
        'directory_servers': 'list[str]',
        'kerberos_servers': 'list[str]',
        'join_ou': 'str',
        'service_principal_names': 'list[str]',
        'encryption_types': 'list[str]',
        'fqdns': 'list[str]'
    }

    attribute_map = {
        'global_catalog_servers': 'global_catalog_servers',
        'directory_servers': 'directory_servers',
        'kerberos_servers': 'kerberos_servers',
        'join_ou': 'join_ou',
        'service_principal_names': 'service_principal_names',
        'encryption_types': 'encryption_types',
        'fqdns': 'fqdns'
    }

    required_args = {
    }

    def __init__(
        self,
        global_catalog_servers=None,  # type: List[str]
        directory_servers=None,  # type: List[str]
        kerberos_servers=None,  # type: List[str]
        join_ou=None,  # type: str
        service_principal_names=None,  # type: List[str]
        encryption_types=None,  # type: List[str]
        fqdns=None,  # type: List[str]
    ):
        """
        Keyword args:
            global_catalog_servers (list[str]): A list of global catalog servers that will be used for lookups related to user authorization. Accepted server formats are IP address and DNS name with optional @domain suffix. If the suffix is ommited, the joined domain is assumed. All specified servers must be registered to the domain appropriately in the array's configured DNS and will only be communicated with over the secure LDAP (LDAPS) protocol. The specified list can have a maximum length of 50. 
            directory_servers (list[str]): A list of directory servers that will be used for lookups related to user authorization. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array's configured DNS and will only be communicated with over the secure LDAP (LDAPS) protocol. If not specified, servers are resolved for the domain in DNS. The specified list can have a maximum length of 5. 
            kerberos_servers (list[str]): A list of key distribution servers to use for Kerberos protocol. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array's configured DNS. If not specified, servers are resolved for the domain in DNS. The specified list can have a maximum length of 5. 
            join_ou (str): The relative distinguished name of the organizational unit in which the computer account should be created when joining the domain. 
            service_principal_names (list[str]): A list of service principal names to register for the machine account, which can be used for the creation of keys for Kerberos authentication. If neither `service_principal_names` nor `fqdns` is specified, the default `service_principal_names` are constructed using the `computer_name` and `domain` fields. Cannot be provided in combination with `fqdns`. 
            encryption_types (list[str]): The encryption types that will be supported for use by clients for Kerberos authentication. Valid values include `aes256-cts-hmac-sha1-96`, `aes128-cts-hmac-sha1-96`, and `arcfour-hmac`. 
            fqdns (list[str]): A list of fully qualified domain names to use to register service principal names for the machine account. If specified, every service principal that is supported by the array will be registered for each fully qualified domain name specified. If neither `fqdns` nor `service_principal_names` is specified, the default `service_principal_names` are constructed using the `computer_name` and `domain` fields. Cannot be provided in combination with `service_principal_names`. 
        """
        if global_catalog_servers is not None:
            self.global_catalog_servers = global_catalog_servers
        if directory_servers is not None:
            self.directory_servers = directory_servers
        if kerberos_servers is not None:
            self.kerberos_servers = kerberos_servers
        if join_ou is not None:
            self.join_ou = join_ou
        if service_principal_names is not None:
            self.service_principal_names = service_principal_names
        if encryption_types is not None:
            self.encryption_types = encryption_types
        if fqdns is not None:
            self.fqdns = fqdns

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ActiveDirectoryPatch`".format(key))
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
        if issubclass(ActiveDirectoryPatch, dict):
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
        if not isinstance(other, ActiveDirectoryPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    Pure1 Public REST API

    Pure1 Public REST API, developed by [Pure Storage, Inc.](https://www.purestorage.com)   The Pure1 REST API 2.0 offers one single form of authentication: OAuth 2.0 via the [Token Exchange protocol](https://datatracker.ietf.org/doc/draft-ietf-oauth-token-exchange).  OAuth 2.0 is an open protocol to allow secure authorization in a simple and standard method from web, mobile, desktop and background applications.  Note that the [Authentication](#section/Authentication) section below mentions 'API Key' as the security scheme type. This is solely for the purpose of allowing testing this API with [Swagger UI](https://static.pure1.purestorage.com/api-swagger/index.html).  [Knowledge base reference documentation](https://support.purestorage.com/Pure1/Pure1_Manage/Pure1_Manage_-_REST_API/Pure1_Manage_-_REST_API__Reference)

    OpenAPI spec version: 1.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_4 import models

class Target(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'as_of': 'int',
        'name': 'str',
        'id': 'str',
        'arrays': 'list[FixedReferenceFqdn]',
        'address': 'str',
        'status_details': 'str',
        'status': 'str'
    }

    attribute_map = {
        'as_of': '_as_of',
        'name': 'name',
        'id': 'id',
        'arrays': 'arrays',
        'address': 'address',
        'status_details': 'status_details',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        name=None,  # type: str
        id=None,  # type: str
        arrays=None,  # type: List[models.FixedReferenceFqdn]
        address=None,  # type: str
        status_details=None,  # type: str
        status=None,  # type: str
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            name (str): A non-modifiable, locally unique name chosen by the system.
            id (str): A non-modifiable, globally unique ID chosen by the system.
            arrays (list[FixedReferenceFqdn]): The list of arrays where this resource exists. Many resources are on a single array, but some resources, such as pods, can be shared across multiple arrays. 
            address (str): IP address or FQDN of the target system.
            status_details (str): Additional information describing any issues encountered when connecting, or `null` if the `status` is `connected`. 
            status (str): Status of the connection. Values include `connected` and `connecting`. 
        """
        if as_of is not None:
            self.as_of = as_of
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if arrays is not None:
            self.arrays = arrays
        if address is not None:
            self.address = address
        if status_details is not None:
            self.status_details = status_details
        if status is not None:
            self.status = status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Target`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Target`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Target`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Target`".format(key))
        object.__delattr__(self, key)

    def keys(self):
        return self.attribute_map.keys()

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
        if issubclass(Target, dict):
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
        if not isinstance(other, Target):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

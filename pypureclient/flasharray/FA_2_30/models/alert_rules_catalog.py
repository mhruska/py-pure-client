# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.30
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_30 import models

class AlertRulesCatalog(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'subject': 'str',
        'parameter': 'str',
        'allowed_values': 'str',
        'default_value': 'str'
    }

    attribute_map = {
        'code': 'code',
        'subject': 'subject',
        'parameter': 'parameter',
        'allowed_values': 'allowed_values',
        'default_value': 'default_value'
    }

    required_args = {
    }

    def __init__(
        self,
        code=None,  # type: int
        subject=None,  # type: str
        parameter=None,  # type: str
        allowed_values=None,  # type: str
        default_value=None,  # type: str
    ):
        """
        Keyword args:
            code (int): The alert code that the rule applies to.
            subject (str): The alert code description.
            parameter (str): The parameter of the custom alert rule.
            allowed_values (str): The range of values allowed to set the custom alert rule to.
            default_value (str): The system default values for the alert code and parameter.
        """
        if code is not None:
            self.code = code
        if subject is not None:
            self.subject = subject
        if parameter is not None:
            self.parameter = parameter
        if allowed_values is not None:
            self.allowed_values = allowed_values
        if default_value is not None:
            self.default_value = default_value

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AlertRulesCatalog`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AlertRulesCatalog`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AlertRulesCatalog`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AlertRulesCatalog`".format(key))
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
        if issubclass(AlertRulesCatalog, dict):
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
        if not isinstance(other, AlertRulesCatalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

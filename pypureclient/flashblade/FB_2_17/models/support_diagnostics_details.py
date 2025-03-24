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

class SupportDiagnosticsDetails(object):
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
        'severity': 'str',
        'index': 'float',
        'task_id': 'str',
        'test_name': 'str',
        'result_details': 'str',
        'test_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'severity': 'severity',
        'index': 'index',
        'task_id': 'task_id',
        'test_name': 'test_name',
        'result_details': 'result_details',
        'test_type': 'test_type'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        severity=None,  # type: str
        index=None,  # type: float
        task_id=None,  # type: str
        test_name=None,  # type: str
        result_details=None,  # type: str
        test_type=None,  # type: str
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system. 
            severity (str): Severity level of the test. Valid values include `info`, `warning`, `critical`. 
            index (float): The unique index of the test. It will be of the format A.B where A is the task index and B is the test index. 
            task_id (str): The task ID of the diagnostics for which this refers to. 
            test_name (str): Name of the test that was performed. 
            result_details (str): More details related to the test. This field can provide remediation information as well. 
            test_type (str): Category to which the test belongs to. 
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if severity is not None:
            self.severity = severity
        if index is not None:
            self.index = index
        if task_id is not None:
            self.task_id = task_id
        if test_name is not None:
            self.test_name = test_name
        if result_details is not None:
            self.result_details = result_details
        if test_type is not None:
            self.test_type = test_type

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SupportDiagnosticsDetails`".format(key))
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
        if issubclass(SupportDiagnosticsDetails, dict):
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
        if not isinstance(other, SupportDiagnosticsDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

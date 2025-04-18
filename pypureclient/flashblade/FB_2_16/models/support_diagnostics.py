# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.16, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.16
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_16 import models

class SupportDiagnostics(object):
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
        'task_id': 'str',
        'index': 'int',
        'start_time': 'int',
        'analysis_period': 'StartEndTime',
        'version': 'str',
        'status': 'str',
        'severity_count': 'list[SupportDiagnosticsSeverityCount]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'task_id': 'task_id',
        'index': 'index',
        'start_time': 'start_time',
        'analysis_period': 'analysis_period',
        'version': 'version',
        'status': 'status',
        'severity_count': 'severity_count'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        task_id=None,  # type: str
        index=None,  # type: int
        start_time=None,  # type: int
        analysis_period=None,  # type: models.StartEndTime
        version=None,  # type: str
        status=None,  # type: str
        severity_count=None,  # type: List[models.SupportDiagnosticsSeverityCount]
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            task_id (str): A globally unique, system-generated ID. The ID cannot be modified.
            index (int): The unique index of the task.
            start_time (int): Start time in milliseconds since the UNIX epoch.
            analysis_period (StartEndTime)
            version (str): Version of diagnostics tool.
            status (str): Status of the diagnostics. A status of `running` indicates that the diagnostics is still running. A status of `completed` indicates that the diagnostics has completed. A status of `failed` indicates that the diagnostics has failed.
            severity_count (list[SupportDiagnosticsSeverityCount]): List of severity counts.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if task_id is not None:
            self.task_id = task_id
        if index is not None:
            self.index = index
        if start_time is not None:
            self.start_time = start_time
        if analysis_period is not None:
            self.analysis_period = analysis_period
        if version is not None:
            self.version = version
        if status is not None:
            self.status = status
        if severity_count is not None:
            self.severity_count = severity_count

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SupportDiagnostics`".format(key))
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
        if issubclass(SupportDiagnostics, dict):
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
        if not isinstance(other, SupportDiagnostics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

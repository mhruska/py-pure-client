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

class Alert(object):
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
        'severity': 'str',
        'summary': 'str',
        'actual': 'str',
        'code': 'int',
        'knowledge_base_url': 'str',
        'created': 'int',
        'notified': 'int',
        'component_name': 'str',
        'expected': 'str',
        'origin': 'str',
        'description': 'str',
        'component_type': 'str',
        'closed': 'int',
        'state': 'str',
        'category': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'as_of': '_as_of',
        'name': 'name',
        'id': 'id',
        'arrays': 'arrays',
        'severity': 'severity',
        'summary': 'summary',
        'actual': 'actual',
        'code': 'code',
        'knowledge_base_url': 'knowledge_base_url',
        'created': 'created',
        'notified': 'notified',
        'component_name': 'component_name',
        'expected': 'expected',
        'origin': 'origin',
        'description': 'description',
        'component_type': 'component_type',
        'closed': 'closed',
        'state': 'state',
        'category': 'category',
        'updated': 'updated'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        name=None,  # type: str
        id=None,  # type: str
        arrays=None,  # type: List[models.FixedReferenceFqdn]
        severity=None,  # type: str
        summary=None,  # type: str
        actual=None,  # type: str
        code=None,  # type: int
        knowledge_base_url=None,  # type: str
        created=None,  # type: int
        notified=None,  # type: int
        component_name=None,  # type: str
        expected=None,  # type: str
        origin=None,  # type: str
        description=None,  # type: str
        component_type=None,  # type: str
        closed=None,  # type: int
        state=None,  # type: str
        category=None,  # type: str
        updated=None,  # type: int
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            name (str): A modifiable, locally unique name chosen by the user.
            id (str): A non-modifiable, globally unique ID chosen by the system.
            arrays (list[FixedReferenceFqdn]): The list of arrays where this resource exists. Many resources are on a single array, but some resources, such as pods, can be shared across multiple arrays. 
            severity (str): Current severity level. Valid values are `info`, `warning`, `critical`, and `hidden`. 
            summary (str): Summary of the alert.
            actual (str): Actual condition at the time of the alert.
            code (int): Code associated with the alert.
            knowledge_base_url (str): URL of the relevant Knowledge Base page.
            created (int): Time when the alert was created, in milliseconds since UNIX epoch. 
            notified (int): Time when the user was notified of the alert, in milliseconds since UNIX epoch. 
            component_name (str): Name of the component alerted about.
            expected (str): Expected state/threshold under normal conditions.
            origin (str): Origin of the alert. Valid values are `array` and `Pure1`.
            description (str): Short description of the alert.
            component_type (str): Type of the component alerted about.
            closed (int): Time when the alert was closed, in milliseconds since UNIX epoch. 
            state (str): Current state of the alert. Valid values are `open`, `closing`, and `closed`. 
            category (str): Category of the alert. Valid values are `array`, `hardware`, and `software`. 
            updated (int): Time when the alert was last updated, in milliseconds since UNIX epoch. 
        """
        if as_of is not None:
            self.as_of = as_of
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if arrays is not None:
            self.arrays = arrays
        if severity is not None:
            self.severity = severity
        if summary is not None:
            self.summary = summary
        if actual is not None:
            self.actual = actual
        if code is not None:
            self.code = code
        if knowledge_base_url is not None:
            self.knowledge_base_url = knowledge_base_url
        if created is not None:
            self.created = created
        if notified is not None:
            self.notified = notified
        if component_name is not None:
            self.component_name = component_name
        if expected is not None:
            self.expected = expected
        if origin is not None:
            self.origin = origin
        if description is not None:
            self.description = description
        if component_type is not None:
            self.component_type = component_type
        if closed is not None:
            self.closed = closed
        if state is not None:
            self.state = state
        if category is not None:
            self.category = category
        if updated is not None:
            self.updated = updated

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
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
        if issubclass(Alert, dict):
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
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

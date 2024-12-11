# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.38
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_38 import models

class PolicyRuleSmbClient(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'anonymous_access_allowed': 'bool',
        'client': 'str',
        'name': 'str',
        'policy': 'FixedReferenceWithType',
        'smb_encryption_required': 'bool',
        'destroyed': 'bool',
        'time_remaining': 'int',
        'context': 'Reference'
    }

    attribute_map = {
        'anonymous_access_allowed': 'anonymous_access_allowed',
        'client': 'client',
        'name': 'name',
        'policy': 'policy',
        'smb_encryption_required': 'smb_encryption_required',
        'destroyed': 'destroyed',
        'time_remaining': 'time_remaining',
        'context': 'context'
    }

    required_args = {
    }

    def __init__(
        self,
        anonymous_access_allowed=None,  # type: bool
        client=None,  # type: str
        name=None,  # type: str
        policy=None,  # type: models.FixedReferenceWithType
        smb_encryption_required=None,  # type: bool
        destroyed=None,  # type: bool
        time_remaining=None,  # type: int
        context=None,  # type: models.Reference
    ):
        """
        Keyword args:
            anonymous_access_allowed (bool): Specifies whether access to information is allowed for anonymous users. Returns a value of `false` if not specified.
            client (str): Specifies which clients are given access to the export. Accepted notation includes IP, IP mask, or hostname. The default is `*` if not specified.
            name (str): Name of this rule. The name is automatically generated by the system.
            policy (FixedReferenceWithType): The policy to which this rule belongs.
            smb_encryption_required (bool): Specifies whether the remote client is required to use SMB encryption. If not specified, defaults to `false`.
            destroyed (bool): Returns a value of `true` if the pod containing the SMB policy rule has been destroyed and is pending eradication. The `time_remaining` value displays the amount of time left until the destroyed policy is permanently eradicated. Once the `time_remaining` period has elapsed, the SMB policy rule is permanently eradicated and can no longer be recovered.
            time_remaining (int): The amount of time left, in milliseconds, until the destroyed SMB policy rule is permanently eradicated.
            context (Reference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request. Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`.
        """
        if anonymous_access_allowed is not None:
            self.anonymous_access_allowed = anonymous_access_allowed
        if client is not None:
            self.client = client
        if name is not None:
            self.name = name
        if policy is not None:
            self.policy = policy
        if smb_encryption_required is not None:
            self.smb_encryption_required = smb_encryption_required
        if destroyed is not None:
            self.destroyed = destroyed
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if context is not None:
            self.context = context

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleSmbClient`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleSmbClient`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleSmbClient`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleSmbClient`".format(key))
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
        if issubclass(PolicyRuleSmbClient, dict):
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
        if not isinstance(other, PolicyRuleSmbClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

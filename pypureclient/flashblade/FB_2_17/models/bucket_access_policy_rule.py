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

class BucketAccessPolicyRule(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'effect': 'str',
        'resources': 'list[str]',
        'principals': 'BucketAccessPolicyRulePrincipal',
        'actions': 'list[str]',
        'policy': 'FixedReference'
    }

    attribute_map = {
        'name': 'name',
        'effect': 'effect',
        'resources': 'resources',
        'principals': 'principals',
        'actions': 'actions',
        'policy': 'policy'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        effect=None,  # type: str
        resources=None,  # type: List[str]
        principals=None,  # type: models.BucketAccessPolicyRulePrincipal
        actions=None,  # type: List[str]
        policy=None,  # type: models.FixedReference
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            effect (str): Effect of this rule. When `allow`, the rule allows the given actions to be performed on the given resources, subject to the given conditions. The only currently supported effect is `allow`. 
            resources (list[str]): The list of resources which this rule applies to. The only currently supported resource is all objects in a bucket to which the parent policy belongs. 
            principals (BucketAccessPolicyRulePrincipal): The principals to which this rule applies. Currently, only all principals are supported. 
            actions (list[str]): The list of actions granted by this rule. Each included action may restrict other properties of the rule. The only currently supported action is `s3:GetObject`. 
            policy (FixedReference): The policy to which this rule belongs.
        """
        if name is not None:
            self.name = name
        if effect is not None:
            self.effect = effect
        if resources is not None:
            self.resources = resources
        if principals is not None:
            self.principals = principals
        if actions is not None:
            self.actions = actions
        if policy is not None:
            self.policy = policy

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `BucketAccessPolicyRule`".format(key))
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
        if issubclass(BucketAccessPolicyRule, dict):
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
        if not isinstance(other, BucketAccessPolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

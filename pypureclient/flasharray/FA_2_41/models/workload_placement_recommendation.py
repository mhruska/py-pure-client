# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_41 import models

class WorkloadPlacementRecommendation(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'context': 'FixedReference',
        'id': 'str',
        'name': 'str',
        'created': 'int',
        'expires': 'int',
        'status': 'str',
        'progress': 'float',
        'preset': 'FixedReference',
        'placement_names': 'list[str]',
        'projection_months': 'int',
        'parameters': 'list[WorkloadParameter]',
        'additional_constraints': 'WorkloadPlacementRecommendationAdditionalConstraints',
        'results_limit': 'int',
        'more_results_available': 'bool',
        'results': 'list[WorkloadPlacementRecommendationResult]'
    }

    attribute_map = {
        'context': 'context',
        'id': 'id',
        'name': 'name',
        'created': 'created',
        'expires': 'expires',
        'status': 'status',
        'progress': 'progress',
        'preset': 'preset',
        'placement_names': 'placement_names',
        'projection_months': 'projection_months',
        'parameters': 'parameters',
        'additional_constraints': 'additional_constraints',
        'results_limit': 'results_limit',
        'more_results_available': 'more_results_available',
        'results': 'results'
    }

    required_args = {
    }

    def __init__(
        self,
        context=None,  # type: models.FixedReference
        id=None,  # type: str
        name=None,  # type: str
        created=None,  # type: int
        expires=None,  # type: int
        status=None,  # type: str
        progress=None,  # type: float
        preset=None,  # type: models.FixedReference
        placement_names=None,  # type: List[str]
        projection_months=None,  # type: int
        parameters=None,  # type: List[models.WorkloadParameter]
        additional_constraints=None,  # type: models.WorkloadPlacementRecommendationAdditionalConstraints
        results_limit=None,  # type: int
        more_results_available=None,  # type: bool
        results=None,  # type: List[models.WorkloadPlacementRecommendationResult]
    ):
        """
        Keyword args:
            context (FixedReference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request. Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`.
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A globally unique, system-generated name. The name cannot be modified and cannot refer to another resource.
            created (int): The time the recommendation was made, measured in milliseconds since the UNIX epoch.
            expires (int): The time when recommendation expires, measured in milliseconds since the UNIX epoch.
            status (str): The status of the recommendation. Possible values are `processing`, `completed`, and `failed`.
            progress (float): The percentage progress of the recommendation computation. The percentage is displayed as a decimal value, starting at 0.00 and ending at 1.00.
            preset (FixedReference)
            placement_names (list[str])
            projection_months (int): The number of months to compute the projections. If not specified, defaults to 1 month.
            parameters (list[WorkloadParameter]): The parameter values to pass to the preset. Value must be supplied for all parameters that do not have a default defined in the preset.
            additional_constraints (WorkloadPlacementRecommendationAdditionalConstraints)
            results_limit (int): The maximum number of results to return. If not specified, defaults to 10 results.
            more_results_available (bool)
            results (list[WorkloadPlacementRecommendationResult]): The results of the recommendation.
        """
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if expires is not None:
            self.expires = expires
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if preset is not None:
            self.preset = preset
        if placement_names is not None:
            self.placement_names = placement_names
        if projection_months is not None:
            self.projection_months = projection_months
        if parameters is not None:
            self.parameters = parameters
        if additional_constraints is not None:
            self.additional_constraints = additional_constraints
        if results_limit is not None:
            self.results_limit = results_limit
        if more_results_available is not None:
            self.more_results_available = more_results_available
        if results is not None:
            self.results = results

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `WorkloadPlacementRecommendation`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `WorkloadPlacementRecommendation`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `WorkloadPlacementRecommendation`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `WorkloadPlacementRecommendation`".format(key))
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
        if issubclass(WorkloadPlacementRecommendation, dict):
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
        if not isinstance(other, WorkloadPlacementRecommendation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

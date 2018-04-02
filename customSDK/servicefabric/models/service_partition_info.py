# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServicePartitionInfo(Model):
    """Information about a partition of a Service Fabric service.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: StatefulServicePartitionInfo,
    StatelessServicePartitionInfo

    :param health_state: The health state of a Service Fabric entity such as
     Cluster, Node, Application, Service, Partition, Replica etc. Possible
     values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type health_state: str or ~azure.servicefabric.models.HealthState
    :param partition_status: The status of the service fabric service
     partition. Possible values include: 'Invalid', 'Ready', 'NotReady',
     'InQuorumLoss', 'Reconfiguring', 'Deleting'
    :type partition_status: str or
     ~azure.servicefabric.models.ServicePartitionStatus
    :param partition_information: Information about the partition identity,
     partitioning scheme and keys supported by it.
    :type partition_information:
     ~azure.servicefabric.models.PartitionInformation
    :param service_kind: Constant filled by server.
    :type service_kind: str
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'partition_status': {'key': 'PartitionStatus', 'type': 'str'},
        'partition_information': {'key': 'PartitionInformation', 'type': 'PartitionInformation'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
    }

    _subtype_map = {
        'service_kind': {'Stateful': 'StatefulServicePartitionInfo', 'Stateless': 'StatelessServicePartitionInfo'}
    }

    def __init__(self, health_state=None, partition_status=None, partition_information=None):
        self.health_state = health_state
        self.partition_status = partition_status
        self.partition_information = partition_information
        self.service_kind = None

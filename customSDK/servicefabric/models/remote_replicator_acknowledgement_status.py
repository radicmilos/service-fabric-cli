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


class RemoteReplicatorAcknowledgementStatus(Model):
    """Provides details about the remote replicators from the primary replicator's
    point of view.

    :param replication_stream_acknowledgement_detail: Details about the
     acknowledgements for operations that are part of the replication stream
     data.
    :type replication_stream_acknowledgement_detail:
     ~azure.servicefabric.models.RemoteReplicatorAcknowledgementDetail
    :param copy_stream_acknowledgement_detail: Details about the
     acknowledgements for operations that are part of the copy stream data.
    :type copy_stream_acknowledgement_detail:
     ~azure.servicefabric.models.RemoteReplicatorAcknowledgementDetail
    """

    _attribute_map = {
        'replication_stream_acknowledgement_detail': {'key': 'ReplicationStreamAcknowledgementDetail', 'type': 'RemoteReplicatorAcknowledgementDetail'},
        'copy_stream_acknowledgement_detail': {'key': 'CopyStreamAcknowledgementDetail', 'type': 'RemoteReplicatorAcknowledgementDetail'},
    }

    def __init__(self, replication_stream_acknowledgement_detail=None, copy_stream_acknowledgement_detail=None):
        self.replication_stream_acknowledgement_detail = replication_stream_acknowledgement_detail
        self.copy_stream_acknowledgement_detail = copy_stream_acknowledgement_detail

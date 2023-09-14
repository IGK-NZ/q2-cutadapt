# ----------------------------------------------------------------------------
# Copyright (c) 2017-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
from q2_types.feature_table import FeatureTable
from qiime2.plugin import SemanticType

CutadaptReadStatistics = SemanticType(
    "CutadaptReadStatistics", variant_of=FeatureTable.field["content"]
)

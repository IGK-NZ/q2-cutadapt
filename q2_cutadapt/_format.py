# ----------------------------------------------------------------------------
# Copyright (c) 2017-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import qiime2.plugin.model as model


class CutadapatReadStatsFileFormat(model.TextFileFormat):
    """CutadaptReadStatsFileFormat."""

    # TODO: Add validation
    def _validate_(self, *args):
        pass


CutadaptReadStatsDirFormat = model.SingleFileDirectoryFormat(
    "CutadaptReadStatsFileFormat",
    "cutadapt_read_stats.tsv",
    CutadapatReadStatsFileFormat,
)

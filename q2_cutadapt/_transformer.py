# ----------------------------------------------------------------------------
# Copyright (c) 2017-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import numpy as np
import pandas as pd

from q2_cutadapt._format import CutadapatReadStatsFileFormat
from q2_cutadapt.plugin_setup import plugin


# taken from
# https://github.com/qiime2/q2-sample-classifier/blob/
# e05f05c36a1e8b97344e5d1f1a317294420eef12/q2_sample_classifier/
# _transformer.py#L27C1-L33C14
def _read_dataframe(fh):
    # Using `dtype=object` and `set_index` to avoid type casting/inference
    # of any columns or the index.
    df = pd.read_csv(fh, sep="\t", header=0, dtype="str")
    df.set_index(df.columns[0], drop=True, append=False, inplace=True)
    df.index.name = "id"
    return df


@plugin.register_transformer
def _1(data: pd.DataFrame) -> CutadapatReadStatsFileFormat:
    ff = CutadapatReadStatsFileFormat()
    with ff.open() as fh:
        data.to_csv(fh, sep="\t", header=True, na_rep=np.nan)
    return ff


@plugin.register_transformer
def _2(ff: CutadapatReadStatsFileFormat) -> pd.DataFrame:
    with ff.open() as fh:
        return _read_dataframe(fh).apply(
            lambda x: pd.to_numeric(x, errors="raise")
        )

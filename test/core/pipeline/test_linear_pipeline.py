# SPDX-FileCopyrightText: 2022-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
import logging

from deepstack.core.pipeline import Pipeline
from deepstack.testing.sample_components import AddFixedValue, Double

logging.basicConfig(level=logging.DEBUG)


def test_pipeline():
    pipeline = Pipeline()
    pipeline.add_component("first_addition", AddFixedValue(add=2))
    pipeline.add_component("second_addition", AddFixedValue())
    pipeline.add_component("double", Double())
    pipeline.connect("first_addition", "double")
    pipeline.connect("double", "second_addition")

    results = pipeline.run({"first_addition": {"value": 1}})
    assert results == {"second_addition": {"result": 7}}

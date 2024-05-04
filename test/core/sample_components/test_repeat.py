# SPDX-FileCopyrightText: 2022-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
from deepstack.testing.sample_components import Repeat
from deepstack.core.serialization import component_to_dict, component_from_dict


def test_repeat_default():
    component = Repeat(outputs=["one", "two"])
    results = component.run(value=10)
    assert results == {"one": 10, "two": 10}

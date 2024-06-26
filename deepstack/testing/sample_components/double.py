# SPDX-FileCopyrightText: 2022-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
from deepstack.core.component import component


@component
class Double:
    """
    Doubles the input value.
    """

    @component.output_types(value=int)
    def run(self, value: int):
        """
        Doubles the input value.
        """
        return {"value": value * 2}

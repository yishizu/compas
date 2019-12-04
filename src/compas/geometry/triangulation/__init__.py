from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import compas

from .triangulation import *  # noqa: F401 F403

if not compas.IPY:
    from .triangulation_numpy import *  # noqa: F401 F403


__all__ = [name for name in dir() if not name.startswith('_')]

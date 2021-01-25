# -----------------------------------------------------------
# 123.py
# v.2.1
# Updated: 20210124
# Houdini version: 18.0.499
# -----------------------------------------------------------

"""
Start-up file runs on Houdini load of a new session.
"""

# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# IMPORTANT: Reset 'USERNAME' with path to user-defined path
# of scripts location.
library_path = r'C:\Users\USERNAME\Documents\houdini18.0\scripts'

# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# IMPORT LIBRARIES )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

import sys
sys.path.append(library_path)
from common_py_lib import utils, uiUtils

# -----------------------------------------------------------
# IMPORT LIBRARIES )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# MAIN )))))))))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

def main():
    r"""
        Initialize Houdini session with custom presets

        Args:
            None

        Returns:
            None
        """

    # Configure playbar options
    uiUtils.lib_config_playbar()

    # Set default colors for sticky notes & network boxes
    utils.lib_set_stickyNotesNetBoxDefaults()


if __name__ == '__main__':
    main()

# -----------------------------------------------------------
# MAIN )))))))))))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
# -----------------------------------------------------------
# houToolSceneRnD.py
# v.1.0
# Updated: 20210123
# -----------------------------------------------------------

"""
Shelf tool to auto populate networks with relevant nodes and
configurations for quick research & development. Setup includes
base geometry, camera and light setups, basic material palette,
and typical Redshift render ROP.
"""

from common_py_lib import utils, uiUtils

def main():
    # -----------------------------------------------------------
    # CONTENT CREATION )))))))))))))))))))))))))))))))))))) START
    # -----------------------------------------------------------
    utils.lib_create_refNodeNet()
    utils.lib_create_geoNodeNet()
    utils.lib_create_dopNodeNet()
    utils.lib_create_rndrNodeNet()
    utils.lib_create_cameraNodeNet()
    utils.lib_create_redshiftNodeNet()
    utils.lib_create_lightNodeNet()
    utils.lib_create_matNodeNet()
    # accessory content creation
    utils.lib_create_geoBkgdGrid()
    # -----------------------------------------------------------
    # CONTENT CREATION )))))))))))))))))))))))))))))))))))}}) END
    # -----------------------------------------------------------

main()
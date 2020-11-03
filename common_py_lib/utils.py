# -----------------------------------------------------------
# utils.py
# v.1.0
# Updated: 20201102
# -----------------------------------------------------------

"""
Custom Houdini utilities for use with startup and quick node creation
"""


# -----------------------------------------------------------
# NETWORKS & NODES )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
def lib_create_lopNodeNet(network):
    r"""
    Create LOP node and network

    Args:
        network:
            Houdini network; typically 'obj'.

    Returns:
        None
    """
    # Houdini library passed through as function parameter since
    # it is accessible directly through the 123.py file. Access
    # to it otherwise will need to be made explicit, as noted in
    # SideFX doc: https://www.sidefx.com/docs/houdini/hom/commandline.html
    lop_new_node = network.createNode("lopnet", node_name="LOPNet")

#************************************************************

def lib_create_matNode(network, name, color, pos):
    r"""
    Create mat node, color, and position

    Args:
        network:
            Houdini network; typicall 'mat'.
        name:
            Node name.
        color:
            Node color.
        position:
            X, Y position as tuple.

    Returns:
        None
    """

    name = network.createNode("redshift_vopnet", node_name=name)
    # Set color using hou color system (RGB)
    name.setColor(color)
    # Position nodes using (x, y) values
    name.setPosition(pos)

# -----------------------------------------------------------
# NETWORKS & NODES )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# CUSTOM PARAMETERS ))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
def lib_set_rizomExe(object):
    r"""
    Set path to Rizom.exe

    Args:
        object:
            Houdini object; typically 'node'.

    Returns:
        None
    """
    object.parm("rizomloc").set("C:/Program Files/Rizom Lab/RizomUV 2020/rizomuv.exe")

#************************************************************

def lib_set_opname(object, node_name):
    r"""
    Set param name to operator name

    Args:
        object:
            Houdini object; typically 'node'.
        node_name:
            Formal node name.

    Returns:
        None
    """
    object.parm(node_name).set("`opname('.')`")

# -----------------------------------------------------------
# CUSTOM PARAMETERS ))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
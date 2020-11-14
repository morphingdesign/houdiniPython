# -----------------------------------------------------------
# utils.py
# v.1.0
# Updated: 20201102
# -----------------------------------------------------------

"""
Custom Houdini utilities for use with startup and quick node creation
"""
import hou
import toolutils

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

#************************************************************

def lib_set_camViewComment(object):
    r"""

    """
    ##################
    # Add custom parameters for texture input into RS SubP mat node
    # Add folder used to collect all newly create parameters, namely texture inputs
    viewport_folder = hou.FolderParmTemplate("folder", "Viewport")
    # Define folder type; default is Tabs. Set to Simple
    viewport_folder.setFolderType(hou.folderType.Tabs)
    # Define parameter group used to collect folder/s
    group = object.parmTemplateGroup()

    # Add string, file reference parameters
    # Diffuse texture
    viewport_folder.addParmTemplate(hou.StringParmTemplate("vcomment", "Viewport Comment", 1))

    # Add folder to group and group to RS SubP mat node
    group.append(viewport_folder)
    object.setParmTemplateGroup(group)

    #object.parm("vcomment").set('CAMERA: %10s' % ('$OS') + '\nRES: %27s' % ('`chs("resx")` x `chs("resy")`') + '\n{:.<42}'.format('') + '\nSHOT: %16s' % ('$SHOT') + '\nTAKE: %18s' % ('$ACTIVETAKE') + '\n{:.<42}'.format('') + '\nFRAME: %14s' % ('$F4'))
    #object.parm("vcomment").set('CAMERA: %10s' % ('$OS') + '\nRES: %50s' % ('`chs("resx")` x `chs("resy")`') + '\n{:.<42}'.format('') + '\nSHOT: %17s' % ('$SHOT') + '\nTAKE: %22s' % ('$ACTIVETAKE') + '\n{:.<42}'.format('') + '\nFRAME: %14s' % ('$F4'))
    object.parm("vcomment").set('CAMERA: %10s' % ('$OS')
                                + '\nRES: %45s' % ('`chs("resx")` x `chs("resy")`')
                                + '\n{:.<42}'.format('')
                                + '\nSHOT: %18s' % ('$SHOT')
                                + '\nTAKE: %25s' % ('$ACTIVETAKE')
                                + '\n{:.<42}'.format('')
                                + '\nFRAME: %14s' % ('$F4'))


# -----------------------------------------------------------
# CUSTOM PARAMETERS ))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
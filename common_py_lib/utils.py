#########################################################
"""Custom Houdini Library for use with startup and quick node creation"""

# Function to create lop network
def lib_create_lopNodeNet(obj):
    """Create LOP node and network"""
    # Houdini library passed through as function parameter since
    # it is accessible directly through the 123.py file. Access
    # to it otherwise will need to be made explicit, as noted in
    # SideFX doc: https://www.sidefx.com/docs/houdini/hom/commandline.html
    lop_new_node = obj.createNode("lopnet", node_name="LOPNet")

# Function to create mat node
def lib_create_matNode(mat, name, color, pos):
    """Create mat node, color, and position"""
    name = mat.createNode("redshift_vopnet", node_name=name)
    # Set color using hou color system (RGB)
    name.setColor(color)
    # Position nodes using (x, y) values
    name.setPosition(pos)

# Function to set path to Rizom.exe on disk
def lib_set_rizomExe(sop_name):
    """Set path to Rizom.exe"""
    sop_name.parm("rizomloc").set("C:/Program Files/Rizom Lab/RizomUV 2020/rizomuv.exe")

# Function to set parameter name to operator name
def lib_set_opname(sop_name, parm_name):
    """Set param name to op name"""
    sop_name.parm(parm_name).set("`opname('.')`")
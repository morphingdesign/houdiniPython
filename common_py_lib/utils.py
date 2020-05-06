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
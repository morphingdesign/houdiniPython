# 456.py
# File is run when Houdini opens an existing hou file

#########################################################
# Function to create blank geo node
def create_geoNode():

    # Access obj network
    obj = hou.node("/obj")

    # Create geo node
    geo = obj.createNode("geo", node_name="newGeo")


#########################################################
# Function to create camera node
def create_cameraNode():

    # Access obj network
    obj = hou.node("/obj")

    # Create cam node in obj network
    cam = obj.createNode("cam", "cam_1080")

    # Define resolution using dictionary format
    res = {'resx': 1920, 'resy': 1080}
    # Apply resolution to camera
    cam.setParms(res)

    # Turn off camera node display flag
    cam.setDisplayFlag(False)


#########################################################
# Function to create Redshift render ROP & IPR nodes
def create_redshiftNode():

    # Access out network
    out = hou.node("/out")

    # Create Redshift ROP in out network
    redRop = out.createNode("Redshift_ROP")

    # Set ROP gamma to No Gamma
    redRop.setParms({"RS_gammaFileMode": "noGamma"})

    #########################################
    # Create Redshift IPR in out network
    redIPR = out.createNode("Redshift_IPR")

#########################################################
# Collect functions to generate all new nodes at startup
# in new main() function
def main():

    # Collect all nodes in obj network and returns them
    # in the form of a tuple (list)
    nodes = hou.node('/obj').glob('*')
    # Declare/initialize cam_exists as false
    cam_exists = False

    # Check each node in the obj network to see if the
    # type matches that of a camera
    for node in nodes:
        if node.type().name() == 'cam':
            # If there is a match, switch cam_exists and
            # exit loop
            cam_exists = True
            break

    if not cam_exists:
        create_cameraNode()

    #########################################
    # Collect all nodes in out network and returns them
    # in the form of a tuple (list)
    rops = hou.node('/out').glob('*')
    # Declare/initialize rop_exists as false
    rop_exists = False

    # Check each node in the out network to see if the
    # type matches that of a Redshift ROP
    for node in rops:
        if node.type().name() == 'Redshift_ROP':
            # If there is a match, switch rop_exists and
            # exit loop
            rop_exists = True
            break

    if not rop_exists:
        create_redshiftNode()

#########################################################
# Call main function
main()
# 123.py
# File is run when Houdini starts up a new hou file

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
    # Also, move it so that it doesn't overlap other nodes
    cam = obj.createNode("cam", "cam_1080").moveToGoodPosition()

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
    # Also, move it so that it doesn't overlap other nodes
    redIPR = out.createNode("Redshift_IPR").moveToGoodPosition()

#########################################################
# Collect functions to generate all new nodes at startup
# in new main() function
def main():
    create_geoNode()
    create_cameraNode()
    create_redshiftNode()

#########################################################
# Call main function
main()
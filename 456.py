# 456.py
# File is run when Houdini opens an existing hou file

#########################################################
# Function to create blank geo node
def create_geoNode():

    # Access obj network
    obj = hou.node("/obj")

    # Create geo node
    geo = obj.createNode("geo", node_name="newGeo")

    # Turn off geo node select flag
    geo.setSelectableInViewport(False)

    # Set color for node to dark green
    geo.setColor(hou.Color(0.302, 0.525, 0.114))


#########################################################
# Function to create Redshift light dome & single light nodes
def create_lightNodes():

    # Access obj network
    obj = hou.node("/obj")

    #########################################
    # Create Redshift light dome node
    rslightdome = obj.createNode("rslightdome", node_name="rsLightDome")

    #########################################
    # Create Redshift light node
    rslight = obj.createNode("rslight", node_name="rsLight")

    # Move them so that they don't overlap other nodes
    rslightdome.moveToGoodPosition()
    rslight.moveToGoodPosition()

    # Turn off light nodes display & select flags
    rslightdome.setDisplayFlag(False)
    rslight.setDisplayFlag(False)
    rslightdome.setSelectableInViewport(False)
    rslight.setSelectableInViewport(False)

    # Set color for nodes to dark yellow
    rslightdome.setColor(hou.Color(1.0, 0.725, 0.0))
    rslight.setColor(hou.Color(1.0, 0.725, 0.0))


#########################################################
# Function to create camera node
def create_cameraNode():

    # Access obj network
    obj = hou.node("/obj")

    # Create cam node in obj network
    cam = obj.createNode("cam", "cam_1080")

    # Also, move it so that it doesn't overlap other nodes
    cam.moveToGoodPosition()

    # Define resolution using dictionary format
    res = {'resx': 1920, 'resy': 1080}
    # Apply resolution to camera
    cam.setParms(res)

    # Turn off camera node display & select flags
    cam.setDisplayFlag(False)
    cam.setSelectableInViewport(False)

    # Set color for node to dark blue
    cam.setColor(hou.Color(0.094, 0.369, 0.69))


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

    # Also, move it so that it doesn't overlap other nodes
    redIPR.moveToGoodPosition()


#########################################################
# Function to create blank geo node
def create_matNode():

    # Access obj network
    shop = hou.node("/shop")

    # Create geo node
    rsmat = shop.createNode("RS_Material", node_name="rsMat")

    # Set color for node to dark red
    rsmat.setColor(hou.Color(0.8, 0.016, 0.016))

    # Set mat node to the preset of Plastic, which has a
    # token of 2, hence the option identified
    rsmat.setParms({"preset": "2"})


#########################################################
# Collect functions to generate all new nodes at startup
# in new main() function
def main():
    #########################################
    # Collect all nodes in obj network and returns them
    # in the form of a tuple (list)
    geos = hou.node('/obj').glob('*')
    # Declare/initialize geo_exists as false
    geo_exists = False

    # Check each node in the obj network to see if the
    # type matches that of a geo node
    for node in geos:
        if node.type().name() == 'geo':
            # If there is a match, switch geo_exists and
            # exit loop
            geo_exists = True
            break

    if not geo_exists:
        create_geoNode()


    #########################################
    # Collect all nodes in obj network and returns them
    # in the form of a tuple (list)
    lights = hou.node('/obj').glob('*')
    # Declare/initialize light_exists as false
    light_exists = False

    # Check each node in the obj network to see if the
    # type matches that of a light node
    for node in lights:
        if node.type().name() == 'rslightdome':
            # If there is a match, switch light_exists and
            # exit loop
            light_exists = True
            break

    if not light_exists:
        create_lightNodes()


    #########################################
    # Collect all nodes in obj network and returns them
    # in the form of a tuple (list)
    cams = hou.node('/obj').glob('*')
    # Declare/initialize cam_exists as false
    cam_exists = False

    # Check each node in the obj network to see if the
    # type matches that of a camera node
    for node in cams:
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
    # type matches that of a Redshift ROP node
    for node in rops:
        if node.type().name() == 'Redshift_ROP':
            # If there is a match, switch rop_exists and
            # exit loop
            rop_exists = True
            break

    # Error checking using (try/except) and message display
    try:
        if not rop_exists:
            create_redshiftNode()
    # If Redshift could not be created, deliver this message to UI
    except:
        hou.ui.displayMessage("An error occurred and Redshift ROP could not be created.")


    #########################################
    # Collect all nodes in shop network and returns them
    # in the form of a tuple (list)
    mats = hou.node('/shop').glob('*')
    # Declare/initialize mat_exists as false
    mat_exists = False

    # Check each node in the obj network to see if the
    # type matches that of an RS material node
    for node in mats:
        if node.type().name() == 'RS_Material':
            # If there is a match, switch mat_exists and
            # exit loop
            mat_exists = True
            break

    if not mat_exists:
        create_matNode()


#########################################################
# Call main function
main()
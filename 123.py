#########################################################
# Access obj network
obj = hou.node("/obj")

# Create geo node
geo = obj.createNode("geo", node_name="newGeo")


#########################################################
# Create cam node in obj network
cam = obj.createNode("cam", "cam_1080")

# Define resolution using dictionary format
res = {'resx': 1920, 'resy': 1080}
# Apply resolution to camera
cam.setParms(res)

# Turn off camera node display flag
cam.setDisplayFlag(False)


#########################################################
# Access out network
out = hou.node("/out")

# Create Redshift ROP in out network
redRop = out.createNode("Redshift_ROP")

# Set ROP gamma to No Gamma
redRop.setParms({"RS_gammaFileMode": "noGamma"})


#########################################################
# Create Redshift IPR in out network
redIPR = out.createNode("Redshift_IPR")
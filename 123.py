# 123.py
# File is run when Houdini starts up a new hou file

#########################################################
# Function to create blank ref geo node
def create_refNodeNet():

    # Access obj network
    obj = hou.node("/obj")

    # Create ref node
    ref_new_node = obj.createNode("geo", node_name="ref_geo")

    # Turn off ref node select flag
    ref_new_node.setSelectableInViewport(False)

    # Set color for node to dark brown
    ref_new_node.setColor(hou.Color(0.573, 0.353, 0.0))

    #########################################
    # Set parameters


    #########################################

    # Create network box in obj network
    refnet = obj.createNetworkBox()

    # Set network box size & position
    refnet.setSize([4,3])
    refnet.setPosition([0,4])

    # Set network box label & color
    refnet.setComment("REFNET")
    refnet.setColor(hou.Color(0.573, 0.353, 0.0))

    ref_new_node.setPosition([0.5, 6])
    # Add ref node to network box
    refnet.addItem(ref_new_node)


#########################################################
# Function to create blank geo node
def create_geoNodeNet():

    # Access obj network
    obj = hou.node("/obj")

    # Create geo node
    geo_new_node = obj.createNode("geo", node_name="geo_newGeo")

    # Turn off geo node select flag
    geo_new_node.setSelectableInViewport(False)

    # Set color for node to dark green
    geo_new_node.setColor(hou.Color(0.302, 0.525, 0.114))

    #########################################
    # Set parameters
    # Set material to reflect material
    #geo_new_node.setParms({"shop_materialpath": "/shop/rsMat_Reflect"})

    #########################################

    # Create network box in obj network
    geonet = obj.createNetworkBox()

    # Set network box size & position
    geonet.setSize([4,3])
    geonet.setPosition([5,4])

    # Set network box label & color
    geonet.setComment("GEONET")
    geonet.setColor(hou.Color(0.302, 0.525, 0.114))

    geo_new_node.setPosition([5.5, 6])
    # Add geo node to network box
    geonet.addItem(geo_new_node)


#########################################################
# Function to create blank dopnet node
def create_dopNodeNet():
    # Access obj network
    obj = hou.node("/obj")

    # Create dop node
    dop_node = obj.createNode("dopnet", node_name="dop")

    # Turn off dop node select flag
    dop_node.setSelectableInViewport(False)

    # Turn off dop node display flag
    dop_node.setDisplayFlag(False)

    # Set color for node to dark purple
    dop_node.setColor(hou.Color(0.384, 0.184, 0.329))

    #########################################
    # Set parameters

    #########################################

    # Create network box in obj network
    dopnet = obj.createNetworkBox()

    # Set network box size & position
    dopnet.setSize([4, 3])
    dopnet.setPosition([10, 4])

    # Set network box label & color
    dopnet.setComment("DOPNET")
    dopnet.setColor(hou.Color(0.384, 0.184, 0.329))

    dop_node.setPosition([10.5, 6])
    # Add dop node to network box
    dopnet.addItem(dop_node)


#########################################################
# Function to create blank render geo node
def create_rndrNodeNet():

    # Access obj network
    obj = hou.node("/obj")

    # Create render geo node
    rndrgeo_new_node = obj.createNode("geo", node_name="rndr_newGeo")

    # Turn off geo node select flag
    rndrgeo_new_node.setSelectableInViewport(False)

    # Set color for node to red
    rndrgeo_new_node.setColor(hou.Color(0.8, 0.016, 0.016))

    #########################################
    # Set parameters
    # Set material to reflect material
    rndrgeo_new_node.setParms({"shop_materialpath": "/mat/rsMat_Cd_Reflect"})

    #########################################

    # Create network box in obj network
    rndrgeonet = obj.createNetworkBox()

    # Set network box size & position
    rndrgeonet.setSize([4,3])
    rndrgeonet.setPosition([15,4])

    # Set network box label & color
    rndrgeonet.setComment("RNDRNET")
    rndrgeonet.setColor(hou.Color(0.8, 0.016, 0.016))

    # Set node position
    rndrgeo_new_node.setPosition([15.5, 6])
    # Add geo node to network box
    rndrgeonet.addItem(rndrgeo_new_node)


#########################################################
# Function to create Redshift light dome & single light nodes
def create_lightNodeNet():

    # Access obj network
    obj = hou.node("/obj")

    #########################################
    # Create Redshift light dome node
    rslightdome_node = obj.createNode("rslightdome", node_name="rsLightDome")

    #########################################
    # Create Redshift area light node
    rslight_node = obj.createNode("rslight", node_name="rsLight")

    #########################################
    # Set parameters
    # Disable area light
    rslight_node.setParms({"light_enabled": "0"})
    # Add path to default Houdini HDRI in light dome
    rslightdome_node.setParms({"env_map": "$HFS/houdini/pic/hdri/HDRIHaven_kiara_5_noon_2k.rat"})
    # Disable HDRI background in light dome
    rslightdome_node.setParms({"background_enable": "0"})

    #########################################

    # Turn off light nodes display & select flags
    rslightdome_node.setDisplayFlag(False)
    rslight_node.setDisplayFlag(False)
    rslightdome_node.setSelectableInViewport(False)
    rslight_node.setSelectableInViewport(False)

    # Set color for nodes to dark yellow
    rslightdome_node.setColor(hou.Color(1.0, 0.725, 0.0))
    rslight_node.setColor(hou.Color(1.0, 0.725, 0.0))

    # Move them so that they don't overlap other nodes
    rslightdome_node.setPosition([20.5, 6])
    rslight_node.setPosition([20.5, 5])

    #########################################

    # Create network box in obj network
    lightnet = obj.createNetworkBox()

    # Set network box size & position
    lightnet.setSize([4,3])
    lightnet.setPosition([20,4])

    # Set network box label & color
    lightnet.setComment("LIGHTNET")
    lightnet.setColor(hou.Color(1.0, 0.725, 0.0))

    # Add geo node to network box
    lightnet.addItem(rslightdome_node)
    lightnet.addItem(rslight_node)


#########################################################
# Function to create camera node
def create_cameraNodeNet():

    # Access obj network
    obj = hou.node("/obj")

    # Create cam node in obj network
    cam_node = obj.createNode("cam", "cam_1080")

    # Also, move it so that it doesn't overlap other nodes
    #cam.moveToGoodPosition()
    cam_node.setPosition([25.5, 6])

    # Define resolution using dictionary format
    res = {'resx': 1920, 'resy': 1080}
    # Apply resolution to camera
    cam_node.setParms(res)

    # Turn off camera node display & select flags
    cam_node.setDisplayFlag(False)
    cam_node.setSelectableInViewport(False)

    # Set color for node to dark blue
    cam_node.setColor(hou.Color(0.094, 0.369, 0.69))

    #########################################

    # Create network box in obj network
    camnet = obj.createNetworkBox()

    # Set network box size & position
    camnet.setSize([4,3])
    camnet.setPosition([25,4])

    # Set network box label & color
    camnet.setComment("CAMNET")
    camnet.setColor(hou.Color(0.094, 0.369, 0.69))

    # Add geo node to network box
    camnet.addItem(cam_node)


#########################################################
# Function to create Redshift render ROP & IPR nodes
def create_redshiftNodeNet():

    # Access out network
    out = hou.node("/out")

    # Create Redshift ROP in out network
    redRop = out.createNode("Redshift_ROP")

    #########################################
    # Set parameters
    # Set render camera to main camera
    redRop.setParms({"RS_renderCamera": "/obj/cam_1080"})
    # Set to No Gamma
    redRop.setParms({"RS_gammaFileMode": "noGamma"})
    # Set render camera to main camera
    redRop.setParms({"PrimaryGIEngine": "RS_GIENGINE_BRUTE_FORCE"})

    #########################################
    # Create Redshift IPR in out network
    redIPR = out.createNode("Redshift_IPR")

    # Set color for node to dark red
    redRop.setColor(hou.Color(0.8, 0.016, 0.016))
    redIPR.setColor(hou.Color(0.8, 0.016, 0.016))

    # Also, move it so that it doesn't overlap other nodes
    #redIPR.moveToGoodPosition()

    # Position nodes
    redIPR.setPosition([0, 2])
    redRop.setPosition([0, 4])


#########################################################
# Function to create shop nodes
def create_shopNodeNet():

    # Access shop network
    shop = hou.node("/shop")

    # Create Redshift material node
    rsMatReflect = shop.createNode("RS_Material", node_name="rsMat_Reflect")
    rsMatMatte = shop.createNode("RS_Material", node_name="rsMat_Matte")
    rsMatCd = shop.createNode("redshift_vopnet", node_name="rsMat_Cd")

    # Set color for node to dark red
    rsMatReflect.setColor(hou.Color(0.8, 0.016, 0.016))
    rsMatMatte.setColor(hou.Color(0.8, 0.016, 0.016))
    rsMatCd.setColor(hou.Color(0.8, 0.016, 0.016))

    # Set reflect mat node to the preset of Plastic, which has a
    # token of 2, hence the option identified
    # Matte mat node set to 12, paper
    rsMatReflect.setParms({"preset": "2"})
    rsMatMatte.setParms({"preset": "12"})

    # Position nodes
    rsMatReflect.setPosition([0, 2])
    rsMatMatte.setPosition([0, 4])
    rsMatCd.setPosition([0, 6])

    #########################################
    # Access inside rsMat_Cd
    rsMatCdVex = hou.node("shop/rsMat_Cd")

    rsMatCd_mat = rsMatCdVex.createNode("redshift::Material", node_name="Material_Comp")
    rsMatCd_cd = rsMatCdVex.createNode("redshift::ParticleAttributeLookup", node_name="Pt_Attribute")

    #########################################
    # Position nodes
    rsMatCd_mat.setPosition([-3, 0])
    rsMatCd_cd.setPosition([-6, 0])

    #########################################
    # Set parameters and network connections
    # Set @Cd attribute for Pt_Attribute
    rsMatCd_cd.setParms({"attribute": "Cd"})
    # Connect Pt_Attribute to Diffuse input in Material_Comp
    rsMatCd_mat.setInput(0, rsMatCd_cd, 0)

    # Assign existing redshift material out node to variable rsMatOut
    rsMatOut = rsMatCdVex.node('redshift_material1')
    # Connect Material_Comp to Surface in redshift_material
    rsMatOut.setInput(0, rsMatCd_mat, 0)


#########################################################
# Function to create mat nodes
def create_matNodeNet():

    # Access shop network
    mat = hou.node("/mat")

    # Create Redshift material nodes
    rsMat_Cd_Matte = mat.createNode("redshift_vopnet", node_name="rsMat_Cd_Matte")
    rsMat_Cd_Reflect = mat.createNode("redshift_vopnet", node_name="rsMat_Cd_Reflect")
    rsMat_Glass = mat.createNode("redshift_vopnet", node_name="rsMat_Glass")

    # Set color for node to dark red
    rsMat_Cd_Matte.setColor(hou.Color(0.8, 0.016, 0.016))
    rsMat_Cd_Reflect.setColor(hou.Color(0.8, 0.016, 0.016))
    rsMat_Glass.setColor(hou.Color(0.8, 0.016, 0.016))

    # Set reflect mat node to the preset of Plastic, which has a
    # token of 2, hence the option identified
    # Matte mat node set to 12, paper
    #rsMatReflect.setParms({"preset": "2"})
    #rsMatMatte.setParms({"preset": "12"})

    # Position nodes
    rsMat_Cd_Matte.setPosition([0, 2])
    rsMat_Cd_Reflect.setPosition([0, 4])
    rsMat_Glass.setPosition([0, 6])

    #########################################
    # Access inside rsMat_Cd
    #rsMatCdVex = hou.node("shop/rsMat_Cd")

    #rsMatCd_mat = rsMatCdVex.createNode("redshift::Material", node_name="Material_Comp")
    #rsMatCd_cd = rsMatCdVex.createNode("redshift::ParticleAttributeLookup", node_name="Pt_Attribute")

    #########################################
    # Position nodes
    #rsMatCd_mat.setPosition([-3, 0])
    #rsMatCd_cd.setPosition([-6, 0])

    #########################################
    # Set parameters and network connections
    # Set @Cd attribute for Pt_Attribute
    #rsMatCd_cd.setParms({"attribute": "Cd"})
    # Connect Pt_Attribute to Diffuse input in Material_Comp
    #rsMatCd_mat.setInput(0, rsMatCd_cd, 0)

    # Assign existing redshift material out node to variable rsMatOut
    #rsMatOut = rsMatCdVex.node('redshift_material1')
    # Connect Material_Comp to Surface in redshift_material
    #rsMatOut.setInput(0, rsMatCd_mat, 0)


#########################################################
# Collect functions to generate all new nodes at startup
# in new main() function
def main():
    # content creation
    create_refNodeNet()
    create_geoNodeNet()
    create_dopNodeNet()
    create_rndrNodeNet()
    create_cameraNodeNet()
    create_redshiftNodeNet()
    create_lightNodeNet()
    create_shopNodeNet()
    create_matNodeNet()


#########################################################
# Call main function
main()
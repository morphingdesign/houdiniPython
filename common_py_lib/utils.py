# -----------------------------------------------------------
# utils.py
# v.1.7
# Updated: 20211117
# Houdini version: 18.5.563, Python 3
# Redshift version: 3.0.46
# -----------------------------------------------------------

"""
Custom Houdini utilities for use with startup and quick node creation
"""
import hou
import toolutils

# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Access relevant networks
obj = hou.node("/obj")
mat = hou.node("/mat")
out = hou.node("/out")

# Node/Net Color Variables  - Settings
ref_color = hou.Color(0.573, 0.353, 0.0)
geo_color = hou.Color(0.302, 0.525, 0.114)
dop_color = hou.Color(0.384, 0.184, 0.329)
rndr_color = hou.Color(0.8, 0.016, 0.016)
light_color = hou.Color(1.0, 0.725, 0.0)
cam_color = hou.Color(0.094, 0.369, 0.69)
eof_color = hou.Color(0.8, 0.016, 0.016)
group_color = hou.Color(1.0, 0.725, 0.0)
delete_color = hou.Color(0.8, 0.016, 0.016)
# Generic Color Palette
color_black = hou.Color(0.0, 0.0, 0.0)
color_white = hou.Color(1.0, 1.0, 1.0)

# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# PRESET NETWORKS & NODES ))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
def lib_create_lopNodeNet():
    r"""
    Create LOP node and network

    Args:
        None

    Returns:
        None
    """
    # Houdini library passed through as function parameter since
    # it is accessible directly through the 123.py file. Access
    # to it otherwise will need to be made explicit, as noted in
    # SideFX doc: https://www.sidefx.com/docs/houdini/hom/commandline.html
    lop_new_node = obj.createNode("lopnet", node_name="LOPNet")

#************************************************************

def lib_create_refNodeNet():
    r"""
    Create reference geo node, color, and position

    Args:
        None

    Returns:
        None
    """

    # Create ref node
    ref_new_node = obj.createNode("geo", node_name="ref_geo")

    # Turn off ref node select flag
    ref_new_node.setSelectableInViewport(False)

    # Set color for node to dark brown
    ref_new_node.setColor(ref_color)

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
    refnet.setColor(ref_color)

    ref_new_node.setPosition([0.5, 6])
    # Add ref node to network box
    refnet.addItem(ref_new_node)

#************************************************************

def lib_create_geoNodeNet():
    r"""
    Create base geo node, color, and position

    Args:
        None

    Returns:
        None
    """

    # Create geo node
    geo_new_node = obj.createNode("geo", node_name="geo_newGeo")

    # Turn off geo node select flag
    geo_new_node.setSelectableInViewport(False)

    # Set color for node to dark green
    geo_new_node.setColor(geo_color)

    #########################################
    # Set parameters
    # Set material to reflect material
    # geo_new_node.setParms({"shop_materialpath": "/shop/rsMat_Reflect"})

    #########################################

    # Create network box in obj network
    geonet = obj.createNetworkBox()

    # Set network box size & position
    geonet.setSize([4,3])
    geonet.setPosition([5,4])

    # Set network box label & color
    geonet.setComment("GEONET")
    geonet.setColor(geo_color)

    geo_new_node.setPosition([5.5, 5])
    # Add geo node to network box
    geonet.addItem(geo_new_node)

    #########################################

    # Create null EOF node within, color & enable display
    geonet_EOF = geo_new_node.createNode("null", node_name="OUT")
    geonet_EOF.setColor(eof_color)
    geonet_EOF.setDisplayFlag(True)

#************************************************************

def lib_create_geoBkgdGrid():
    r"""
    Create background grid geo node, color, and position

    Args:
        None

    Returns:
        None
    """

    # Create geo node for grid background
    grid_new_node = obj.createNode("geo", node_name="geo_gridBkgd")
    # Turn off geo node select flag
    grid_new_node.setSelectableInViewport(False)
    # Set color for node to dark green
    grid_new_node.setColor(geo_color)
    # Position in obj
    grid_new_node.setPosition([5.5, 6])
    # Turn off geo node select flag
    grid_new_node.setDisplayFlag(False)
    # Transform grid geo node away from scene center
    grid_new_node.setParms({"tz": "-5"})

    # Acquire existing Geonet Netbox and append new geo to it
    geonet = hou.item('/obj/__netbox2')
    geonet.addItem(grid_new_node)

    #########################################

    # Create null EOF node within, color & enable display
    geonet_EOF = grid_new_node.createNode("null", node_name="OUT")
    geonet_EOF.setColor(eof_color)
    geonet_EOF.setDisplayFlag(True)

    # Create color node within, set to blue
    grid_color_sop = grid_new_node.createNode("color", node_name="Set_cd")
    # Set point color to blue; note that parameter is not accessible via tuple,
    # but rather individual float fields as follows:
    grid_color_sop.setParms({"colorr": "0.0"})
    grid_color_sop.setParms({"colorg": "0.25"})
    grid_color_sop.setParms({"colorb": "0.5"})

    # Create grid node within, position and orient
    grid_sop = grid_new_node.createNode("grid", node_name="grid")
    # Orient grid to vertical plane, perpendicular to camera position
    grid_sop.setParms({"orient": "xy"})
    # Rotate along y-axis to face camera
    grid_sop.setParms({"ry": "180"})

    # Link Grid to Color to EOF, & organize nodes in geo
    grid_color_sop.setInput(0, grid_sop, 0)
    geonet_EOF.setInput(0, grid_color_sop, 0)
    grid_new_node.layoutChildren()

    #########################################

    # Create render geo node
    rndrgeo_grid_node = obj.createNode("geo", node_name="rndr_gridBkgd")
    # Turn off geo node select flag
    rndrgeo_grid_node.setSelectableInViewport(False)
    # Set color for node to red
    rndrgeo_grid_node.setColor(rndr_color)
    # Position node in obj
    rndrgeo_grid_node.setPosition([15.5, 6])
    # Turn off node visibility flag
    rndrgeo_grid_node.setDisplayFlag(False)
    # Set material to matte material
    rndrgeo_grid_node.setParms({"shop_materialpath": "/mat/rsMat_Cd_Matte"})

    # Add geo node to existing render network box
    rndrgeonet = hou.item('/obj/__netbox4')
    rndrgeonet.addItem(rndrgeo_grid_node)

    #########################################

    # Create null EOF node within, color & enable display
    rndrgrid_eof = rndrgeo_grid_node.createNode("null", node_name="OUT")
    rndrgrid_eof.setColor(rndr_color)
    rndrgrid_eof.setDisplayFlag(True)

    # Create object merge node within & color
    rndrgrid_om = rndrgeo_grid_node.createNode("object_merge", node_name="get_grid_geo")
    rndrgrid_om.setColor(geo_color)
    # Link OM obj with EOF in render grid geo obj
    rndrgrid_om.setParms({"objpath1": "/obj/geo_gridBkgd/OUT"})

    # Set OM transform to 'Into This Object' token
    rndrgrid_om.setParms({"xformtype": "local"})

    # Link OM to EOF, & organize nodes in geo
    rndrgrid_eof.setInput(0, rndrgrid_om, 0)
    rndrgeo_grid_node.layoutChildren()

#************************************************************

def lib_create_dopNodeNet():
    r"""
    Create empty dopnet node, color, and position

    Args:
        None

    Returns:
        None
    """

    # Create dop node
    dop_node = obj.createNode("dopnet", node_name="dop")

    # Turn off dop node select flag
    dop_node.setSelectableInViewport(False)

    # Turn off dop node display flag
    dop_node.setDisplayFlag(False)

    # Set color for node to dark purple
    dop_node.setColor(dop_color)

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
    dopnet.setColor(dop_color)

    dop_node.setPosition([10.5, 6])
    # Add dop node to network box
    dopnet.addItem(dop_node)

#************************************************************

def lib_create_rndrNodeNet():
    r"""
    Create render geo nodes, color, and position

    Args:
        None

    Returns:
        None
    """

    # Create render geo node
    rndrgeo_new_node = obj.createNode("geo", node_name="rndr_newGeo")

    # Turn off geo node select flag
    rndrgeo_new_node.setSelectableInViewport(False)

    # Turn off node visibility flag
    rndrgeo_new_node.setDisplayFlag(False)

    # Set color for node to red
    rndrgeo_new_node.setColor(rndr_color)

    #########################################
    # Set parameters
    # Set material to reflect material
    # DISABLE RS
    # #rndrgeo_new_node.setParms({"shop_materialpath": "/mat/rsMat_Cd_Reflect"})

    #########################################

    # Create network box in obj network
    rndrgeonet = obj.createNetworkBox()

    # Set network box size & position
    rndrgeonet.setSize([4,3])
    rndrgeonet.setPosition([15,4])

    # Set network box label & color
    rndrgeonet.setComment("RNDRNET")
    rndrgeonet.setColor(rndr_color)

    # Set node position
    rndrgeo_new_node.setPosition([15.5, 5])
    # Add geo node to network box
    rndrgeonet.addItem(rndrgeo_new_node)

    #########################################

    # Create null EOF node within, color & enable display
    rndrnet_eof = rndrgeo_new_node.createNode("null", node_name="OUT")
    rndrnet_eof.setColor(rndr_color)
    rndrnet_eof.setDisplayFlag(True)

    # Create object merge node within & color
    rndrnet_om = rndrgeo_new_node.createNode("object_merge", node_name="get_geo")
    rndrnet_om.setColor(geo_color)

    # Link OM obj with EOF in GEONET geo obj
    rndrnet_om.setParms({"objpath1": "/obj/geo_newGeo/OUT"})

    # Set OM transform to 'Into This Object' token
    rndrnet_om.setParms({"xformtype": "local"})

    # Link OM to EOF, & organize nodes in RNDRNET
    rndrnet_eof.setInput(0, rndrnet_om, 0)
    rndrgeo_new_node.layoutChildren()

#************************************************************

def lib_create_lightNodeNet():
    r"""
    Create Redshift scene lights, including light dome &
    2 single lights; color, and position

    Args:
        None

    Returns:
        None
    """

    #########################################
    # Create Redshift light dome node to serve as Fill Light
    rslightdome_node = obj.createNode("rslightdome", node_name="rsLightDome")

    #########################################
    # Create Redshift point light node to serve as Back Light
    rslightback_node = obj.createNode("rslight", node_name="rsLightBack")

    #########################################
    # Create Redshift area light node to serve as Key Light
    rslightkey_node = obj.createNode("rslight", node_name="rsLightKey")

    #########################################
    # Set dome light parameters
    # Add path to default Houdini HDRI in light dome
    rslightdome_node.setParms({"env_map": "D:/DataSync/01_Resources/HDRI/HdrStudioCharacterRembrandt001/HdrStudioCharacterRembrandt001/8K/HdrStudioCharacterRembrandt001_HDR_8K.exr"})
    # Orient hdri for frontal view in cam
    rslightdome_node.setParms({"ry":"270"})
    # Disable HDRI background in light dome
    rslightdome_node.setParms({"background_enable": "0"})

    #########################################
    # Set point light parameters
    # Position light with cam position
    rslightback_node.setParms({"tz": "-2.5"})
    # Change from default of area to point type
    rslightback_node.setParms({"light_type": "point"})
    # Decrease intensity multiplier from default of 100
    rslightback_node.setParms({"RSL_intensityMultiplier": "10"})

    #########################################
    # Set area light parameters
    # Disable area light
    # rslight_node.setParms({"light_enabled": "0"})
    # Position area light with cam position
    rslightkey_node.setParms({"tz":"5.0"})
    # Decrease intensity multiplier from default of 100
    rslightkey_node.setParms({"RSL_intensityMultiplier": "1"})
    # Disable Affect Specular on area light
    #rslightkey_node.setParms({"RSL_affectSpecular":"0"})
    # Change area light shape to Disc, token 1
    rslightkey_node.setParms({"RSL_areaShape": "1"})
    # Disable area light visibility in render view
    rslightkey_node.setParms({"RSL_visible": "0"})
    # Normalize area light intensity
    rslightkey_node.setParms({"RSL_normalize": "1"})

    #########################################

    # Turn off light nodes display & select flags
    rslightdome_node.setDisplayFlag(False)
    rslightkey_node.setDisplayFlag(False)
    rslightback_node.setDisplayFlag(False)
    rslightdome_node.setSelectableInViewport(False)
    rslightkey_node.setSelectableInViewport(False)
    rslightback_node.setSelectableInViewport(False)

    # Set color for nodes to dark yellow
    rslightdome_node.setColor(light_color)
    rslightkey_node.setColor(light_color)
    rslightback_node.setColor(light_color)

    # Move them so that they don't overlap other nodes
    rslightdome_node.setPosition([20.5, 6])
    rslightkey_node.setPosition([20.5, 5])
    rslightback_node.setPosition([20.5, 4])

    #########################################

    # Create network box in obj network
    lightnet = obj.createNetworkBox()

    # Set network box size & position
    lightnet.setSize([4,3])
    lightnet.setPosition([20,4])

    # Set network box label & color
    lightnet.setComment("LIGHTNET")
    lightnet.setColor(light_color)

    # Add geo node to network box
    lightnet.addItem(rslightdome_node)
    lightnet.addItem(rslightkey_node)
    lightnet.addItem(rslightback_node)

#************************************************************

def lib_create_cameraNodeNet():
    r"""
    Create camera node linked to pivot point, color, and position

    Args:
        None

    Returns:
        None
    """

    # Create cam node in obj network
    cam_node = obj.createNode("cam", "cam_1080")
    # Create geo node to serve as linked origin to cam
    cam_origin = obj.createNode("geo", node_name="cam_origin")

    #########################################
    # Set parameters
    # Define resolution using dictionary format
    res = {'resx': 1920, 'resy': 1080}
    # Apply resolution to camera
    cam_node.setParms(res)

    # Position camera for viewing scene
    cam_node.setParms({"ty": "0.0"})
    cam_node.setParms({"tz": "5.0"})

    # DISABLE RS
    # Enable DOF & link cam focus distance to RS cam
    cam_node.setParms({"RS_campro_dofEnable": "1"})
    # Disable Houdini cam DOF link
    cam_node.setParms({"RS_campro_dofUseHoudiniCamera": "0"})
    # Adjust DOF power to be lower
    cam_node.setParms({"RS_campro_dofPower": "0.01"})
    # Set Houdini cam focus distance to variable
    focus = hou.parm('/obj/cam_1080/focus')
    # Use focus distance variable as channel reference in RS cam
    cam_node.setParms({"RS_campro_dofDistance": focus})

    # Add viewport comment using function in CUSTOM PARAMETERS
    # section.
    lib_set_camViewComment(cam_node)

    #########################################

    # Turn off camera node display & select flags
    cam_origin.setDisplayFlag(False)
    cam_origin.setSelectableInViewport(False)
    cam_node.setDisplayFlag(False)
    cam_node.setSelectableInViewport(False)

    # Set color for nodes to dark blue
    cam_origin.setColor(cam_color)
    cam_node.setColor(cam_color)

    # Set positions
    cam_origin.setPosition([25.5, 6])
    cam_node.setPosition([25.5, 5])

    #########################################

    # Create network box in obj network
    camnet = obj.createNetworkBox()

    # Set network box size & position
    camnet.setSize([4,3])
    camnet.setPosition([25,4])

    # Set network box label & color
    camnet.setComment("CAMNET")
    camnet.setColor(cam_color)

    # Add geo node to network box
    camnet.addItem(cam_node)
    camnet.addItem(cam_origin)

    # Link cam to origin
    cam_node.setInput(0, cam_origin, 0)

#************************************************************

def lib_create_redshiftNodeNet():
    r"""
    Create Redshift render ROP & IPR nodes, color, and position

    Args:
        None

    Returns:
        None
    """

    # Create Redshift ROP in out network
    redRop = out.createNode("Redshift_ROP")

    #########################################
    # Set parameters
    # Set render camera to main camera
    redRop.setParms({"RS_renderCamera": "/obj/cam_1080"})
    # Set to No Gamma
    redRop.setParms({"RS_gammaPreview": "1"})
    # Set samples
    redRop.setParms({"UnifiedMinSamples": "16"})
    redRop.setParms({"UnifiedMaxSamples": "128"})
    # Set primary engine to Brute Force
    redRop.setParms({"PrimaryGIEngine": "RS_GIENGINE_BRUTE_FORCE"})
    redRop.setParms({"BruteForceGINumRays": "128"})
    # Set render objects
    redRop.setParms({"RS_objects_candidate": ""})
    redRop.setParms({"RS_objects_force": "rndr_*"})
    # Set IPR Renderer
    redRop.setParms({"RS_iprProgressive": "0"})
    redRop.setParms({"RS_iprUpdateMeshDeform": "1"})
    redRop.setParms({"RS_iprUpdateStylesheets": "1"})
    redRop.setParms({"RS_iprUpdateCOP2": "1"})

    #########################################
    # Create Redshift IPR in out network
    redIPR = out.createNode("Redshift_IPR")

    # Set color for node to dark red
    redRop.setColor(rndr_color)
    redIPR.setColor(rndr_color)

    # Also, move it so that it doesn't overlap other nodes
    #redIPR.moveToGoodPosition()

    # Position nodes
    redIPR.setPosition([0, 2])
    redRop.setPosition([0, 4])

#************************************************************

def lib_create_matNodeNet():
    r"""
    Create collection in base Redshift material nodes in material
    network; color, and position

    Args:
        None

    Returns:
        None
    """

    # Create dict of mat nodes to create
    node_names = {'1': 'rsMat_Cd_Matte', '2': 'rsMat_Cd_Reflect', '3': 'rsMat_Glass', '4': 'rsMat_Vol'}
    mat_color = rndr_color

    # Iterate through dict values and generate nodes
    i = 1
    for name in node_names.values():
        posx = i * 2
        # Access function from CREATE NODES section
        name = lib_create_matNode(mat, name, mat_color, [0, posx])
        i += 1

    # Collect new nodes for use in internal setups
    # Above for loop does not currently link the nodes to the variables, so they
    # are explicitly linked here:
    rsMat_Cd_Matte = hou.node('/mat/rsMat_Cd_Matte')
    rsMat_Cd_Reflect = hou.node('/mat/rsMat_Cd_Reflect')
    rsMat_Glass = hou.node('/mat/rsMat_Glass')
    rsMat_Vol = hou.node('/mat/rsMat_Vol')

    #########################################
    # Access inside rsMat_Cd_Matte to create nodes
    # RS mat nodes originally did not have a material node within, hence the following:
    # cdmatte_mat = rsMat_Cd_Matte.createNode("redshift::Material", node_name="Material_Comp")
    # ..., but latest versions have material node within, so the following attributes a variable:
    cdmatte_mat = hou.node('/mat/rsMat_Cd_Matte/Material1')
    cdmatte_cd = rsMat_Cd_Matte.createNode("redshift::ParticleAttributeLookup", node_name="Pt_Attribute")

    # Position nodes
    cdmatte_mat.setPosition([-3, 0])
    cdmatte_cd.setPosition([-6, 0])

    # Set parameters and network connections
    # Set @Cd attribute for Pt_Attribute
    cdmatte_cd.setParms({"attribute": "Cd"})
    # Connect Pt_Attribute to Diffuse input in Material_Comp
    cdmatte_mat.setInput(0, cdmatte_cd, 0)

    # Matte mat node set to 12, paper
    cdmatte_mat.setParms({"preset":"12"})
    # Matte mat node set Reflection: Roughness to 1.0
    # By default, this is set to 0.0 by Houdini
    cdmatte_mat.setParms({"refl_roughness": "1.0"})

    # Assign existing redshift material out node to variable
    cdmatte_out = rsMat_Cd_Matte.node('redshift_material1')
    # Connect Material to Surface in redshift_material
    cdmatte_out.setInput(0, cdmatte_mat, 0)

    #########################################
    # Access inside rsMat_Cd_Reflect to create nodes
    cdreflect_mat = hou.node('/mat/rsMat_Cd_Reflect/Material1')
    cdreflect_cd = rsMat_Cd_Reflect.createNode("redshift::ParticleAttributeLookup", node_name="Pt_Attribute")

    # Position nodes
    cdreflect_mat.setPosition([-3, 0])
    cdreflect_cd.setPosition([-6, 0])

    # Set parameters and network connections
    # Set @Cd attribute for Pt_Attribute
    cdreflect_cd.setParms({"attribute": "Cd"})
    # Connect Pt_Attribute to Diffuse input in Material_Comp
    cdreflect_mat.setInput(0, cdreflect_cd, 0)

    # Mat node set to 2, plastic
    cdreflect_mat.setParms({"preset":"2"})

    # Assign existing redshift material out node to variable
    cdreflect_out = rsMat_Cd_Reflect.node('redshift_material1')
    # Connect Material to Surface in redshift_material
    cdreflect_out.setInput(0, cdreflect_mat, 0)

    #########################################
    # Access inside rsMat_Cd_Glass to create node
    glass_mat = hou.node('/mat/rsMat_Glass/Material1')

    # Position node
    glass_mat.setPosition([-3, 0])

    # Set parameters and network connections
    # Mat node set to 0, glass
    glass_mat.setParms({"preset":"0"})
    glass_mat.setParms({"diffuse_weight": "0"})
    # Set to GGX (option 2)
    glass_mat.setParms({"refl_brdf": "1"})
    # Set to Metal (option 3)
    glass_mat.setParms({"refl_fresnel_mode": "2"})
    # Set metal color to dark gray; note that parameter is not accessible via tuple,
    # but rather individual float fields as follows:
    glass_mat.setParms({"refl_reflectivityr": "0.0125"})
    glass_mat.setParms({"refl_reflectivityg": "0.0125"})
    glass_mat.setParms({"refl_reflectivityb": "0.0125"})
    # Enable Refraction Weight to '1'.
    glass_mat.setParms({"refr_weight": "1"})
    # Toggle to On
    glass_mat.setParms({"refr_thin_walled": "1"})

    # Assign existing redshift material out node to variable
    glass_out = rsMat_Glass.node('redshift_material1')
    # Connect Material to Surface in redshift_material
    glass_out.setInput(0, glass_mat, 0)

    #########################################
    # Access inside rsMat_Vol to create node
    vol_mat = hou.node('/mat/rsMat_Vol/Material1')
    vol_vol = rsMat_Vol.createNode("redshift::Volume", node_name="Volume_In")

    # Position nodes
    vol_vol.setPosition([-3, 0])

    # Destroy existing mat node within mat builder; it was auto created at onset
    vol_mat.destroy(False)

    # Assign existing redshift material out node to variable
    vol_out = rsMat_Vol.node('redshift_material1')
    # Connect Volume (out port 0) to Volume (in port 5) in redshift_material
    vol_out.setInput(4, vol_vol, 0)

    #########################################
    # Create RS SubP mat node
    lib_create_RSMatForSubP(mat, [0,10])

#************************************************************

def lib_create_copMatNetForSbsar():
    r"""
        Create Substance Archive node in compositing
        network and accompanying RSmat for Substance textures
        in material network.

        Args:
            None

        Returns:
            None
        """

    #########################################

    # Create standalone networks

    ##################
    # Collect selected nodes, if applicable; returns tuple.
    selected = hou.selectedNodes()

    # If node selected within network, add networks within,
    # otherwise add networks to obj network.
    if (len(selected) > 0):
        # Specify first selected node
        geo = selected[0]
        copnet = geo.createNode("cop2net", node_name="copnet")
        matnet = geo.createNode("matnet", node_name="matnet")
    else:
        # Create standalone networks
        copnet = obj.createNode("cop2net", node_name="copnet")
        matnet = obj.createNode("matnet", node_name="matnet")

    #########################################

    # Setup compositing network

    # Create node to access Substance Archive file (sbsar) and null node
    opSubP = copnet.createNode("sbs_archive")
    opNull = copnet.createNode("null", node_name="OUT")

    # Link node output to input
    opNull.setInput(0, opSubP, 0)

    # Organize child nodes layout
    copnet.layoutChildren()

    #########################################

    # Setup material network

    lib_create_RSMatForSubP(matnet, [0,0])

    #########################################

    # Access RS material in newly created mat network. Select 1st item
    # from tuple returned by glob() matching pattern.

    rsMat_SubP = matnet.glob("rsMat_SubP", ignore_case=False)[0]

    ##################
    # Set material parameters

    # Specify operator input path to COPnet for use with Substance operator
    parms = ("tex_diffuse", "tex_roughness", "tex_metallic", "tex_normal")
    for parm in parms:
        # Align path to COPnet output Null node.
        # copnet.path() used to fill in path since it may vary depending
        # on whether the COPnet is in OBJnet or selected geo node.
        rsMat_SubP.setParms({parm: "op:`opfullpath('%s/OUT')`" % copnet.path()})

    ##################
    # Set texture parameters

    # Texture output from sbsar node in COPnet is in layers, which
    # need to be specified here per texture.

    # Collect nodes in RS material specified as texture, which should
    # return 4 texture nodes, in sequence.
    textures = rsMat_SubP.glob("Texture*")
    # Texture sequence aligns with the following list of typical
    # layers that are input individually into each texture node's
    # parameter specifying the layer it reads from the COPnet.
    layers = ("Base Color", "Roughness", "Metallic", "Normal")
    if (len(textures)==4):
        # Iterate through each texture node in glob() collection.
        for i in range(len(textures)):
            # Set parameter value with layer name.
            textures[i].setParms({"tex0_layername": layers[i]})

# -----------------------------------------------------------
# PRESET NETWORKS & NODES ))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

#************************************************************

def lib_set_groupNodeDefaults(object):
    r"""
        Set default node shape and color for group nodes.

        Args:
            object:
                Houdini object; typically 'node'.

        Returns:
            None
    """

    #########################################

    # Create standalone networks

    ##################
    # Set default shape to 'peanut'.
    object.setUserData('nodeshape', 'peanut')
    # Set default color to default global group color.
    object.setColor(group_color)

#************************************************************

def lib_set_deleteNodeDefaults(object):
    r"""
        Set default node shape and color for nodes that
        employ deleting processes.

        Args:
            object:
                Houdini object; typically 'node'.

        Returns:
            None
    """

    #########################################

    # Create standalone networks

    ##################
    # Set default shape to 'star'.
    object.setUserData('nodeshape', 'star')
    # Set default color to default global group color.
    object.setColor(delete_color)

#************************************************************

def lib_set_stickyNotesNetBoxDefaults():
    r"""
        Set default colors for sticky notes and network boxes.

        Args:
            None

        Returns:
            None
    """

    ##################
    # Set custom default colors for Houdini Sticky Notes and Network Boxes
    # Sticky Notes set to white
    hou.setDefaultColor(hou.colorItemType.StickyNote, color_white)
    # Sticky Notes Text default retained as black; uncomment to customize
    # hou.setDefaultColor(hou.colorItemType.StickyNoteText, hou.Color(0.0, 0.0, 0.0))

    ##################
    # Network Boxes set to black
    hou.setDefaultColor(hou.colorItemType.NetworkBox, color_black)

#************************************************************

# -----------------------------------------------------------
# CREATE NODES ))}}}})))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

def lib_create_RSMatForSubP(network, pos=None):
    r"""
    Create Redshift material with embedded structure for reading
    textures, in alignment with Substance Painter output or an
    sbsar file linked via a compositing network.

    Args:
        network:
            Houdini network; typically 'mat'.
        position:
            X, Y position as tuple.

    Returns:
        None
    """

    # Local variable for node color
    mat_color = rndr_color

    # test
    if pos is None:
        pos = [0, 0]

    # Generate node
    # Custom function returns node created so reference to variable persists
    # throughout this function.
    rsMat_SubP = lib_create_matNode(network, "rsMat_SubP", mat_color, pos)

    #########################################
    # Coordinate textures and material setup in RS SubP mat node

    ##################
    # Add custom parameters for texture input into RS SubP mat node
    # Add folder used to collect all newly create parameters, namely texture inputs
    subP_mat_folder = hou.FolderParmTemplate("folder", "Textures")
    # Define folder type; default is Tabs. Set to Simple
    subP_mat_folder.setFolderType(hou.folderType.Simple)
    # Define parameter group used to collect folder/s
    group = rsMat_SubP.parmTemplateGroup()

    # Add string, file reference parameters
    # Diffuse texture
    subP_mat_folder.addParmTemplate(hou.StringParmTemplate("tex_diffuse", "Diffuse", 1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Image))
    # Roughness texture
    subP_mat_folder.addParmTemplate(hou.StringParmTemplate("tex_roughness", "Roughness", 1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Image))
    # Metallic texture
    subP_mat_folder.addParmTemplate(hou.StringParmTemplate("tex_metallic", "Metallic", 1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Image))
    # Normal texture
    subP_mat_folder.addParmTemplate(hou.StringParmTemplate("tex_normal", "Normal", 1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Image))
    # Height texture
    subP_mat_folder.addParmTemplate(hou.StringParmTemplate("tex_height", "Height", 1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Image))
    # Emission texture
    subP_mat_folder.addParmTemplate(hou.StringParmTemplate("tex_emission", "Emission", 1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Image))

    # Add folder to group and group to RS SubP mat node
    group.append(subP_mat_folder)
    rsMat_SubP.setParmTemplateGroup(group)

    ##################
    # Access inside RS material nodes by collecting material node matching pattern exactly
    # The glob() function outputs a tuple, so selection will be the 1st and only node.
    subP_mat = rsMat_SubP.glob("Material1", ignore_case=False)[0]
    subP_matOut = rsMat_SubP.glob("redshift_material1", ignore_case=False)[0]

    ##################
    # Create texture nodes to link into material
    subP_mat_tex_diffuse = rsMat_SubP.createNode("redshift::TextureSampler", node_name="Texture_Diffuse")
    subP_mat_tex_rough = rsMat_SubP.createNode("redshift::TextureSampler", node_name="Texture_Roughness")
    subP_mat_tex_metal = rsMat_SubP.createNode("redshift::TextureSampler", node_name="Texture_Metallic")
    subP_mat_tex_normal = rsMat_SubP.createNode("redshift::TextureSampler", node_name="Texture_Normal")
    subP_mat_bumpMap = rsMat_SubP.createNode("redshift::BumpMap")
    subP_mat_tex_height = rsMat_SubP.createNode("redshift::TextureSampler", node_name="Texture_Height")
    subP_mat_displaceMap = rsMat_SubP.createNode("redshift::Displacement")
    subP_mat_tex_emission = rsMat_SubP.createNode("redshift::TextureSampler", node_name="Texture_Emission")

    # Link texture/image file inputs at Mat Builder level to corresponding texture samplers
    # Note the backslash to preserve the interior quotation marks for the path
    subP_mat_tex_diffuse.setParms({"tex0": "`chs(\"../tex_diffuse\")`"})    # Link to diffuse
    subP_mat_tex_rough.setParms({"tex0": "`chs(\"../tex_roughness\")`"})    # Link to roughness
    subP_mat_tex_metal.setParms({"tex0": "`chs(\"../tex_metallic\")`"})     # Link to metallic
    subP_mat_tex_normal.setParms({"tex0": "`chs(\"../tex_normal\")`"})      # Link to normal
    subP_mat_tex_height.setParms({"tex0": "`chs(\"../tex_height\")`"})      # Link to height
    subP_mat_tex_emission.setParms({"tex0": "`chs(\"../tex_emission\")`"})  # Link to emission

    # Link node outputs to inputs
    subP_mat.setInput(0, subP_mat_tex_diffuse, 0)               # To diffuse_color
    subP_mat.setInput(7, subP_mat_tex_rough, 0)                 # To refl_roughness
    subP_mat.setInput(14, subP_mat_tex_metal, 0)                # To refl_metalness
    subP_mat_bumpMap.setInput(0, subP_mat_tex_normal, 0)        # From normal to bumpMap
    subP_mat.setInput(52, subP_mat_bumpMap, 0)                  # To bump_input
    subP_mat_displaceMap.setInput(0, subP_mat_tex_height, 0)    # From height to displaceMap
    subP_matOut.setInput(1, subP_mat_displaceMap, 0)            # To displacement_input in mat out node
    subP_mat.setInput(51, subP_mat_tex_emission, 0)             # To emission_color

    ##################

    # Set material parameters

    # Align with Substance color management
    # Ref: https://docs.substance3d.com/integrations/redshift-substance-painter-196215709.html
    # Set BRDF to GGX
    # By default, this is set to Beckmann
    subP_mat.setParms({"refl_brdf": "1"})
    # Set Fresnel Type to Metalness
    # By default, this is set to IOR
    subP_mat.setParms({"refl_fresnel_mode": "2"})
    # Normal texture params are set correctly by default to tangent space normal and height scale of 1.

    # Set bump map node parameter to set Input Map Type to Tangent-Space Normal.
    # By default, this is set to Height Field
    subP_mat_bumpMap.setParms({"inputType": "1"})

    ##################

    # Organize child nodes layout
    rsMat_SubP.layoutChildren()

#************************************************************

def lib_create_matNode(network, name, color, pos):
    r"""
    Create mat node, color, and position

    Args:
        network:
            Houdini network; typically 'mat'.
        name:
            Node name.
        color:
            Node color.
        position:
            X, Y position as tuple.

    Returns:
        Created network node.
    """

    name = network.createNode("redshift_vopnet", node_name=name, force_valid_node_name=True)
    # Set color using hou color system (RGB)
    name.setColor(color)
    # Position nodes using (x, y) values
    name.setPosition(pos)
    # Return network name for reference, if applicable
    return name

# -----------------------------------------------------------
# CREATE NODES ))}}}})))))))))))))))))))))))))))))))))))) END
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
            Parameter name for formal node name.

    Returns:
        None
    """
    object.parm(node_name).set("`opname('.')`")

#************************************************************

def lib_set_camViewComment(object):
    r"""
    Set param name to operator name

    Args:
        object:
            Houdini object; typically 'node'.

    Returns:
        None
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


# SCENE FILE EVENT CALLBACK

def scene_was_loaded(event_type):
    if event_type == hou.hipFileEventType.AfterLoad:
        print("The user loaded", hou.hipFile.path())
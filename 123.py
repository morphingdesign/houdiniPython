# 123.py
"""Start-up file runs on Houdini load"""
# Requires Redshift

import sys

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# IMPORTANT: Reset path to user-defined path with 'username'
library_path = r'C:\Users\username\Documents\houdini18.0\scripts'
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

sys.path.append(library_path)
from common_py_lib import utils


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
    # geo_new_node.setParms({"shop_materialpath": "/shop/rsMat_Reflect"})

    #########################################

    # Create network box in obj network
    geonet = obj.createNetworkBox()

    # Set network box size & position
    geonet.setSize([4,3])
    geonet.setPosition([5,4])

    # Set network box label & color
    geonet.setComment("GEONET")
    geonet.setColor(hou.Color(0.302, 0.525, 0.114))

    geo_new_node.setPosition([5.5, 5])
    # Add geo node to network box
    geonet.addItem(geo_new_node)

    #########################################

    # Create null EOF node within, color & enable display
    geonet_EOF = geo_new_node.createNode("null", node_name="OUT")
    geonet_EOF.setColor(hou.Color(0.8, 0.016, 0.016))
    geonet_EOF.setDisplayFlag(True)

#########################################################
# Function to create background grid geo node
def create_geoBkgdGrid():

    # Access obj network
    obj = hou.node("/obj")

    # Create geo node for grid background
    grid_new_node = obj.createNode("geo", node_name="geo_gridBkgd")
    # Turn off geo node select flag
    grid_new_node.setSelectableInViewport(False)
    # Set color for node to dark green
    grid_new_node.setColor(hou.Color(0.302, 0.525, 0.114))
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
    geonet_EOF.setColor(hou.Color(0.8, 0.016, 0.016))
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
    rndrgeo_grid_node.setColor(hou.Color(0.8, 0.016, 0.016))
    # Position node in obj
    rndrgeo_grid_node.setPosition([15.5, 6])
    # Set material to matte material
    rndrgeo_grid_node.setParms({"shop_materialpath": "/mat/rsMat_Cd_Matte"})

    # Add geo node to existing render network box
    rndrgeonet = hou.item('/obj/__netbox4')
    rndrgeonet.addItem(rndrgeo_grid_node)

    #########################################

    # Create null EOF node within, color & enable display
    rndrgrid_eof = rndrgeo_grid_node.createNode("null", node_name="OUT")
    rndrgrid_eof.setColor(hou.Color(0.8, 0.016, 0.016))
    rndrgrid_eof.setDisplayFlag(True)

    # Create object merge node within & color
    rndrgrid_om = rndrgeo_grid_node.createNode("object_merge", node_name="get_grid_geo")
    rndrgrid_om.setColor(hou.Color(0.302, 0.525, 0.114))
    # Link OM obj with EOF in render grid geo obj
    rndrgrid_om.setParms({"objpath1": "/obj/geo_gridBkgd/OUT"})

    # Set OM transform to 'Into This Object' token
    rndrgrid_om.setParms({"xformtype": "local"})

    # Link OM to EOF, & organize nodes in geo
    rndrgrid_eof.setInput(0, rndrgrid_om, 0)
    rndrgeo_grid_node.layoutChildren()


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
    rndrgeonet.setColor(hou.Color(0.8, 0.016, 0.016))

    # Set node position
    rndrgeo_new_node.setPosition([15.5, 5])
    # Add geo node to network box
    rndrgeonet.addItem(rndrgeo_new_node)

    #########################################

    # Create null EOF node within, color & enable display
    rndrnet_eof = rndrgeo_new_node.createNode("null", node_name="OUT")
    rndrnet_eof.setColor(hou.Color(0.8, 0.016, 0.016))
    rndrnet_eof.setDisplayFlag(True)

    # Create object merge node within & color
    rndrnet_om = rndrgeo_new_node.createNode("object_merge", node_name="get_geo")
    rndrnet_om.setColor(hou.Color(0.302, 0.525, 0.114))

    # Link OM obj with EOF in GEONET geo obj
    rndrnet_om.setParms({"objpath1": "/obj/geo_newGeo/OUT"})

    # Set OM transform to 'Into This Object' token
    rndrnet_om.setParms({"xformtype": "local"})

    # Link OM to EOF, & organize nodes in RNDRNET
    rndrnet_eof.setInput(0, rndrnet_om, 0)
    rndrgeo_new_node.layoutChildren()


#########################################################
# Function to create Redshift light dome & single light nodes
def create_lightNodeNet():

    # Access obj network
    obj = hou.node("/obj")

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
    rslightdome_node.setParms({"env_map": "D:/OneDrive/01_Resources/HDRI/HdrStudioCharacterRembrandt001/HdrStudioCharacterRembrandt001/8K/HdrStudioCharacterRembrandt001_HDR_8K.exr"})
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
    rslightdome_node.setColor(hou.Color(1.0, 0.725, 0.0))
    rslightkey_node.setColor(hou.Color(1.0, 0.725, 0.0))
    rslightback_node.setColor(hou.Color(1.0, 0.725, 0.0))

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
    lightnet.setColor(hou.Color(1.0, 0.725, 0.0))

    # Add geo node to network box
    lightnet.addItem(rslightdome_node)
    lightnet.addItem(rslightkey_node)
    lightnet.addItem(rslightback_node)


#########################################################
# Function to create camera node
def create_cameraNodeNet():

    # Access obj network
    obj = hou.node("/obj")

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
    cam_node.setParms({"ty": "0.5"})
    cam_node.setParms({"tz": "5.0"})

    # DISABLE RS
    # Enable DOF & link cam focus distance to RS cam
    cam_node.setParms({"RS_campro_dofEnable": "1"})
    # Disable Houdini cam DOF link
    cam_node.setParms({"RS_campro_dofUseHoudiniCamera": "0"})
    # Adjust DOF power to be lower
    cam_node.setParms({"RS_campro_dofPower": "0.001"})
    # Set Houdini cam focus distance to variable
    focus = hou.parm('/obj/cam_1080/focus')
    # Use focus distance variable as channel reference in RS cam
    cam_node.setParms({"RS_campro_dofDistance": focus})


    #########################################

    # Turn off camera node display & select flags
    cam_origin.setDisplayFlag(False)
    cam_origin.setSelectableInViewport(False)
    cam_node.setDisplayFlag(False)
    cam_node.setSelectableInViewport(False)

    # Set color for nodes to dark blue
    cam_origin.setColor(hou.Color(0.094, 0.369, 0.69))
    cam_node.setColor(hou.Color(0.094, 0.369, 0.69))

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
    camnet.setColor(hou.Color(0.094, 0.369, 0.69))

    # Add geo node to network box
    camnet.addItem(cam_node)
    camnet.addItem(cam_origin)

    # Link cam to origin
    cam_node.setInput(0, cam_origin, 0)


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
    redRop.setColor(hou.Color(0.8, 0.016, 0.016))
    redIPR.setColor(hou.Color(0.8, 0.016, 0.016))

    # Also, move it so that it doesn't overlap other nodes
    #redIPR.moveToGoodPosition()

    # Position nodes
    redIPR.setPosition([0, 2])
    redRop.setPosition([0, 4])

#########################################################
# Function to create mat nodes
def create_matNodeNet():

    # Access shop network
    mat = hou.node("/mat")

    # Create dict of mat nodes to create
    node_names = {'1': 'rsMat_Cd_Matte', '2': 'rsMat_Cd_Reflect', '3': 'rsMat_Glass', '4': 'rsMat_Vol', '5': 'rsMat_SubP'}
    color = hou.Color(0.8, 0.016, 0.016)

    # Iterate through dict values and generate nodes
    i = 1
    for name in node_names.values():
        posx = i * 2
        # Access function from utils lib
        name = utils.lib_create_matNode(mat, name, color, [0, posx])
        i += 1

    # Collect new nodes for use in internal setups
    # Above for loop does not currently link the nodes to the variables, so they
    # are explicitly linked here:
    rsMat_Cd_Matte = hou.node('/mat/rsMat_Cd_Matte')
    rsMat_Cd_Reflect = hou.node('/mat/rsMat_Cd_Reflect')
    rsMat_Glass = hou.node('/mat/rsMat_Glass')
    rsMat_Vol = hou.node('/mat/rsMat_Vol')
    rsMat_SubP = hou.node('/mat/rsMat_SubP')

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
    subP_mat_folder.addParmTemplate( hou.StringParmTemplate("tex_normal", "Normal", 1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Image))

    # Add folder to group and group to RS SubP mat node
    group.append(subP_mat_folder)
    rsMat_SubP.setParmTemplateGroup(group)

    ##################

    # Access inside rsMat_SubP to create nodes
    subP_mat = hou.node('/mat/rsMat_SubP/Material1')
    subP_mat_tex_diffuse = rsMat_SubP.createNode("redshift::TextureSampler", node_name="Texture_Diffuse")
    subP_mat_tex_rough = rsMat_SubP.createNode("redshift::TextureSampler", node_name="Texture_Roughness")
    subP_mat_tex_metal = rsMat_SubP.createNode("redshift::TextureSampler", node_name="Texture_Metallic")
    subP_mat_tex_normal = rsMat_SubP.createNode("redshift::NormalMap", node_name="Texture_Normal")

    # Link texture/image file inputs at Mat Builder level to corresponding texture samplers
    # Note the backslash to preserve the interior quotation marks for the path
    subP_mat_tex_diffuse.setParms({"tex0": "`chs(\"../tex_diffuse\")`"})    # Link to diffuse
    subP_mat_tex_rough.setParms({"tex0": "`chs(\"../tex_roughness\")`"})    # Link to roughness
    subP_mat_tex_metal.setParms({"tex0": "`chs(\"../tex_metallic\")`"})     # Link to metallic
    subP_mat_tex_normal.setParms({"tex0": "`chs(\"../tex_normal\")`"})      # Link to normal

    # Assign existing redshift material out node to variable
    subP_mat.setInput(0, subP_mat_tex_diffuse, 0)   # To diffuse_color
    subP_mat.setInput(7, subP_mat_tex_rough, 0)     # To refl_roughness
    subP_mat.setInput(14, subP_mat_tex_metal, 0)    # To refl_metalness
    subP_mat.setInput(49, subP_mat_tex_normal, 0)   # To bump_input

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

    ##################

    # Organize child nodes layout
    rsMat_SubP.layoutChildren()

    #########################################

#########################################################
# Function to create lop network
def create_lopNodeNet():
    # Access obj network. Var used to pass Houdini library
    # into utils lib function
    obj = hou.node("/obj")

    # Access function from utils lib
    utils.lib_create_lopNodeNet(obj)

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
    create_matNodeNet()
    # accessory content creation
    create_geoBkgdGrid()
    # create lop net
    #create_lopNodeNet()

#########################################################
# Call main function
# Check if program running main function
if __name__ == '__main__':
    main()
# Intended to differentiate between program running main and
# all included functions or for calling individual functions
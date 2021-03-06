# Houdini Python
Houdini tools and operations
#
### Shelf Tools Setup
* New Shelf Location
    * Saved to _Documents\houdini18.0\toolbar_
* New Tool Checklist
    * Options
        * Complete <code>Name</code> and <code>Label</code>
        * Search for <code>Icon</code> from other existing tools
    * Script
        * Populate field with script and comments
        * These are located within this repo
    * Context
        * Select applicable network contexts, such as <code>OBJ</code> and/or <code>SOP</code>, or others as applicable.
#
### Starting Template File
File: [123.py](123.py)
* Coordinated to configure playbar.
#
### Scene RnD Shelf Tool
* Documented within the [houToolSceneRnD.py](shelf/houToolSceneRnD.py) file and intended to expedite the process of starting a working file with prebuilt nodes and networks.
* Currently set up with Redshift renderer (ROP & materials)
* Accompanied by supporting [utils.py](common_py_lib/utils.py) with functions
* The following are some screencaps of networks with the prebuilt nodes:

| *Object Network* |
| --- |
| ![Houdini Object Network](img/20200508_HouTemplate_ObjNet.PNG) |      

| *Material Network* | *Out Network* |
| --- | ---|
| ![Houdini Object Network](img/20200508_HouTemplate_MatNet.PNG) | ![Houdini Object Network](img/20200508_HouTemplate_OutNet.PNG) |
#
### SOP Nodes
* SideFX Labs Rizom nodes
    * Default parameter noting path to Rizom.exe configured for 2020
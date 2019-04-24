# Import relevant library modules
import hou
import random

######################################################

# Var for geo node
die = hou.node('obj/newGeo')

# Var for transform node within geo node
dieTransform = hou.node('obj/newGeo/transform')

# Var for obj network
obj = hou.node('obj')

######################################################

numOfDice = 5       # Geo quantity
numOfSides = 6      # Geo sides
count = 0           # Counter for loop

######################################################

while count < numOfDice:

    # Reset transform parms for first geo
    if count == 0:
        dieTransform.parm('tx').set(0)
        dieTransform.parm('ty').set(0)
        dieTransform.parm('tz').set(0)
        dieTransform.parm('rx').set(0)
        dieTransform.parm('ry').set(0)
        dieTransform.parm('rz').set(0)

        ##########################

        # Collect all children within obj network
        # Returns array
        allGeo = obj.children()

        # Counter for loop
        oCount = 0

        # Iterate through each geo in array of children
        for object in allGeo:
            # Check if geo exist within any and all children
            # within the obj network
            if oCount > 0:
                # Reset geo to 0 if any geo exists
                # This resets all of the geo
                object.destroy()
            # Iterate next counter
            oCount = oCount + 1

    else:
        # Copy geo node
        # Placed in an array since that is what this
        # function requires as parm
        hou.copyNodesToClipboard([die])
        # Paste geo from clipboard into obj network
        hou.pasteNodesFromClipboard(obj)

    # Offset next geo copy by 5 units
    dieTransform.parm('tx').set(count * 5)

    ##########################

    # Iterate counter
    count = count + 1

    ##########################

    # Get random number based on geo sides
    dieRoll = random.randint(1, numOfSides)

    ##########################

    # Rotation based on roll option
    if dieRoll == 1:
        dieTransform.parm('rx').set(180)
        dieTransform.parm('ry').set(0)
        dieTransform.parm('rz').set(0)
    elif dieRoll == 2:
        dieTransform.parm('rx').set(0)
        dieTransform.parm('ry').set(0)
        dieTransform.parm('rz').set(-90)
    elif dieRoll == 3:
        dieTransform.parm('rx').set(90)
        dieTransform.parm('ry').set(0)
        dieTransform.parm('rz').set(0)  
    elif dieRoll == 4:
        dieTransform.parm('rx').set(-90)
        dieTransform.parm('ry').set(0)
        dieTransform.parm('rz').set(0) 
    elif dieRoll == 5:
        dieTransform.parm('rx').set(0)
        dieTransform.parm('ry').set(0)
        dieTransform.parm('rz').set(90)  
    elif dieRoll == 6:
        dieTransform.parm('rx').set(0)
        dieTransform.parm('ry').set(0)
        dieTransform.parm('rz').set(0)

######################################################
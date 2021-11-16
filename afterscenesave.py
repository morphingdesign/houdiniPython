# -----------------------------------------------------------
# afterscenesave.py
# v.1.0
# Updated: 20211117
# Houdini version: 18.5.563, Python 3
# -----------------------------------------------------------

"""
Script recognized by Houdini to run before a save operation is
 performed on the working .hip file.
Ref: https://www.sidefx.com/docs/houdini/hom/locations.html#run-scripts-before-and-or-after-saving-the-scene-hip-file
"""

# -----------------------------------------------------------
# OPERATIONS )))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

print("**************************")
print("After Scene Save")
# Use global dict kwargs to access save success bool. The autosave
# bool is another item from the dict that toggles the autosave
# operation; returns true when autosave triggered.
if kwargs["success"] and not kwargs["autosave"]:
    # Dict also includes absolute file path for intended
    # save location.
    print("File successfully saved to %s." % kwargs["file"])
# Print operations log to the Houdini console.

# -----------------------------------------------------------
# OPERATIONS )))))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
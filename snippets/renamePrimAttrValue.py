# -----------------------------------------------------------
# renamePrimAttrValue.py
# v.1.0
# Updated: 20210831
# ----------------------------------------------------------

"""
Snippet used within a Python SOP to rename a primitive attribute
value with a string search.
"""

node = hou.pwd()
geo = node.geometry()

# Iterate through each prim in the current geo stream.
for prim in geo.prims():
    # Access primitive attribute value. In this case,
    # value is stored as string.
    searchString = prim.attribValue("shop_materialpath")

    # Identify string to be replaced and string used
    # to replace it.
    matchString = "Original"
    replaceString = "New"

    # Check if string being sought after is located within
    # primitive attribute value.
    if matchString in searchString:
        # If string is located, then replace it with the
        # string intended to replace it and store the new
        # revised string.
        replaceString = searchString.replace(matchString, replaceString)
        # Set the aforementioned primitive attribute value
        # with this newly created string with the replaced
        # string section.
        prim.setAttribValue("shop_materialpath", replaceString)
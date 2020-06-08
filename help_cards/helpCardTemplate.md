
<!-- ******************************************************
Wikimedia formatting for help cards in Houdini
More info. found in the following resources.
-Source: http://www.sidefx.com/docs/houdini/help/format.html

Info for accessing help cards in private server.
-Source: https://www.sidefx.com/docs/houdini/help/central.html

Add title of the node, context in which it is used, and the icon.
****************************************************** -->

= Hans =
#context: obj
#icon: opdef:.?hansPalacios_parasiteSketchUp_03.png

<!-- ******************************************************
Add quick description for node.
****************************************************** -->

""" Automatically does this and that."""

<!-- ******************************************************
Add section title and text.
****************************************************** -->

== Overview ==
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip 
ex ea commodo consequat.

Separate paragraphs by adding a full line between paragraphs.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<!-- ******************************************************
Add @-sign section top-level heading.
-Source: http://www.sidefx.com/docs/houdini/help/format.html#sign-sections
****************************************************** -->

@parameters

<!-- ******************************************************
Add properties for the parameters and their specific data.
****************************************************** -->

Float Parameter:
        #id: floatparameter
        This parameter controls this and that.

Uniform Scale:
        #id: uniformscale
        This controls this and that.

<!-- ******************************************************
Include the @name syntax followed by the intended title for the section
Source: http://www.sidefx.com/docs/houdini/help/format#sign-sections
****************************************************** -->

@name Section title

<!-- ******************************************************
Add a web link using the following formatting.
****************************************************** -->

[Hans Palacios|https://www.hanspalacios.com]

<!-- ******************************************************
This help file is stored by Houdini in a JSON format in the following folder:
...\Documents\houdini18.0\config\Help\cache\nodes\sop
****************************************************** -->
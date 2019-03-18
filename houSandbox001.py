
scene = "MyHoudiniFile.hip"
version = 14
vector = [0, 0, 0]
colors = ["red", "green", "blue"]
geo = {"ROP": "Mantra", "COP": "Color", "SOP": "Geometry"}

print("Hello World")
print(scene)
print(version)
print(type(vector))
print(type(colors))
print(colors[0])
print(type(geo))
print(geo["ROP"])
print(type(geo["ROP"]))


# hou.parmTuple('/obj/geo1/t').eval()
# (0.0, 0.0, 0.0)
# hou.parmTuple('/obj/geo1/t').eval()
# (5.0, 10.0, 2.0)
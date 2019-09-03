HEX_COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2":
               "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4}",
               "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}

colour_name = input("Name of colour: ")
while colour_name != "":
    if colour_name in HEX_COLOURS:
        print(colour_name, "code is", HEX_COLOURS[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Name of colour: ")

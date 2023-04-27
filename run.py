import ScriptEnv

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

import os
os.chdir(oProject.GetPath())

from parse import parse
rectangles = parse("design.pcb")
names = ""
i = 0
for rect in rectangles:
    names+="Rectangle{},".format(i)
    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "{}".format(rect.XStart),
            "YStart:=", "{}".format(rect.YStart),
            "ZStart:=", "{}".format(rect.ZStart),
            "Width:=", "{}".format(rect.Width),
            "Height:=", "{}".format(rect.Height),
            "WhichAxis:=", "Z"
        ], 
        [
            "NAME:Attributes",
            "Name:=", "Rectangle{}".format(i),
            "Flags:=", "",
            "Color:=", "(143 175 143)",
            "Transparency:=", 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:=", "",
            "MaterialValue:=", "\"vacuum\"",
            "SurfaceMaterialValue:=", "\"\"",
            "SolveInside:=", True,
            "ShellElement:=", False,
            "ShellElementThickness:=", "1mm",
            "IsMaterialEditable:=", True,
            "UseMaterialAppearance:=", False,
            "IsLightweight:=", False
        ])
    i+=1

oEditor.ThickenSheet(
	[
		"NAME:Selections",
		"Selections:="		, names,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:SheetThickenParameters",
		"Thickness:="		, "1mm",
		"BothSides:="		, False,
		[
			"NAME:ThickenAdditionalInfo",
			[
				"NAME:ShellThickenDirectionInfo",
				"SampleFaceID:="	, 3119,
				"ComponentSense:="	, True,
				[
					"NAME:PointOnSampleFace",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:DirectionAtPoint",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "1mm"
				]
			]
		]
	])

oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, names
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
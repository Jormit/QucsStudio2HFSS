import ScriptEnv

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

import os
os.chdir(oProject.GetPath())

from parse import parse
rectangles, substrate = parse("design.pcb")
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
            "SolveInside:="		, False,
            "MaterialValue:="	, "\"copper\"",
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
		"Thickness:="		, substrate.Thickness,
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

oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle0"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material Appearance",
					"Value:="		, False
				],
				[
					"NAME:Material Appearance",
					"Value:="		, True
				]
			]
		]
	])

oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "{}".format(substrate.Rectangle.XStart),
            "YStart:=", "{}".format(substrate.Rectangle.YStart),
            "ZStart:=", "{}".format(substrate.Rectangle.ZStart),
            "Width:=", "{}".format(substrate.Rectangle.Width),
            "Height:=", "{}".format(substrate.Rectangle.Height),
            "WhichAxis:=", "Z"
        ], 
        [
            "NAME:Attributes",
            "Name:=", "Substrate",
        ])

oEditor.ThickenSheet(
	[
		"NAME:Selections",
		"Selections:="		, "Substrate",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:SheetThickenParameters",
		"Thickness:="		, "-" + substrate.Height,
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
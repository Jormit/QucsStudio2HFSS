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

########################### DRAW COPPER RECTANGLES ############################
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
					"Value:="		, True
				]
			]
		]
	])

########################### DRAW SUBSTRATE ############################
oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "{}".format(substrate.Rectangle.XStart - substrate.Rectangle.Width / 5),
            "YStart:=", "{}".format(substrate.Rectangle.YStart - substrate.Rectangle.Height / 5),
            "ZStart:=", "{}".format(substrate.Rectangle.ZStart),
            "Width:=", "{}".format(substrate.Rectangle.Width * 1.4),
            "Height:=", "{}".format(substrate.Rectangle.Height * 1.4),
            "WhichAxis:=", "Z"
        ], 
        [
            "NAME:Attributes",
            "Name:=", "Substrate",
            "MaterialValue:="	, "\"FR4_epoxy\"",
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

oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Substrate"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material Appearance",
					"Value:="		, True
				]
			]
		]
	])

########################### DRAW GROUND ############################
oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "{}".format(substrate.Rectangle.XStart - substrate.Rectangle.Width / 5),
            "YStart:=", "{}".format(substrate.Rectangle.YStart - substrate.Rectangle.Height / 5),
            "ZStart:=", "{}".format("-" + substrate.Height),
            "Width:=", "{}".format(substrate.Rectangle.Width * 1.4),
            "Height:=", "{}".format(substrate.Rectangle.Height * 1.4),
            "WhichAxis:=", "Z"
        ], 
        [
            "NAME:Attributes",
            "Name:=", "Ground",
            "MaterialValue:="	, "\"Copper\"",
            "SolveInside:="		, False,
        ])

oEditor.ThickenSheet(
	[
		"NAME:Selections",
		"Selections:="		, "Ground",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:SheetThickenParameters",
		"Thickness:="		, -0.00001,
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

oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Ground"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material Appearance",
					"Value:="		, True
				]
			]
		]
	])
import CommandLine as CL


CLParser = CL.CommandLineParser()
CLaction = CLParser.parseit()
CLaction.Connect_DB()


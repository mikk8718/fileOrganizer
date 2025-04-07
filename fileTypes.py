import pandas as pd

file_types = [
".py",
".png",
".jpg",
".docx",
".xlsx",
".pptx",
".pdf",
".txt",
".csv",
".html",
".css",
".js",
".json",
".xml",
".zip",
".mp3",
".mp4",
".avi",
".mov",
".sh",
".bat",
".cpp",
".c",
".java",
".rb",
".php",
".svg",
".md",
".rtf"
]

files = pd.DataFrame({
    'fileType':file_types
    }).to_csv('fileTypes.csv', index=False)

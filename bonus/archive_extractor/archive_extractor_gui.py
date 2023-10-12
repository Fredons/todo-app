import PySimpleGUI as sg
from functions import extract_archive

sg.theme("LightBlue2")

layout = [
    [sg.Text("Select archive:"), sg.Input(),
     sg.FilesBrowse("Choose", key="archive")],
    [sg.Text("Select dest dir:"), sg.Input(),
     sg.FolderBrowse("Choose", key="folder")],
    [sg.Button("Extract", key="extract"),
     sg.Text(key="output", text_color="Red"),]
]

window = sg.Window("Archive Extractor", layout, font=("Poppins", 15))

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values['archive']
    dest_dir = values['folder']
    extract_archive(archivepath, dest_dir)
    window['output'].update(value="Extraction complete")

window.close()
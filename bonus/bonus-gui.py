import PySimpleGUI as sg


label1 = sg.Text("Select files to compress")
file_path = sg.Input()
choose_file_btn = sg.FilesBrowse("Choose")

label2 = sg.Text("Select files to compress")
folder_path = sg.Input()
folder_btn = sg.FolderBrowse("Choose")

compress_btn = sg.Button("Compress")

window = sg.Window("File Zipper", layout=[
    [label1, file_path, choose_file_btn],
    [label2, folder_path, folder_btn],
    [compress_btn]
], font=('Helvetica', 15))
window.read()
window.close()

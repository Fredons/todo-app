import PySimpleGUI as sg

label1 = sg.Text("Enter feet:")
input_text1 = sg.InputText(tooltip="Enter feet here")
label2 = sg.Text("Enter inches:")
input_text2 = sg.InputText(tooltip="Enter inches here")
convert_btn = sg.Button("Convert")

window = sg.Window("Convertor", layout=[
    [label1, input_text1],
    [label2, input_text2],
    [convert_btn]
])

window.read()
window.close()
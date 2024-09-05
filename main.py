import PySimpleGUI as gui
import kmp_algo as kmp
import re
 
sublayout_1 = [
  [gui.Text("KMP Algorithm visualization", background_color="#FFA658", text_color="#535353", size=(30, 1), font=('Helvetica', 14, 'bold'))],
  [gui.Text("Text to Search:", background_color="#FFA658", text_color="#535353", size=(15, 1), font=('Helvetica', 12, 'bold')), gui.InputText(key='text_to_search', text_color="#535353", size=(30, 1))],
  [gui.Text("Pattern:", background_color="#FFA658", text_color="#535353", size=(15, 1), font=('Helvetica', 12, 'bold')), gui.InputText(key='pattern', text_color="#535353", size=(30, 1))],
  [gui.Button('Search')],
]

sublayout_2 = [
  [gui.Text()]
]

layout = [
]

LSPTableInformation = []

def loadMainMenu():
  layout = [
      sublayout_1,
  ]

  window = gui.Window("KMP Algorithm visualization", layout=layout, margins=(250, 250), background_color="#FFA658")

  while True:
    event, values = window.read()

    if event == gui.WINDOW_CLOSED:
      break

    if event == 'Search':
      if not (re.search('[a-zA-Z]', values['text_to_search']) and re.search('[a-zA-Z]', values['pattern']) and len(values['pattern']) <= len(values['text_to_search'])):
        gui.popup_error("you can't have empty strings as arguments to KMP algorithm")
      else:
        text_to_search = values['text_to_search']
        pattern = values['pattern']
        search_result = kmp.KMPSearch(text_to_search, pattern)

        if search_result == []:
          gui.popup_ok("no matches found :(")
        else:
          loadSecondScreen(text_to_search, pattern);

        print(f"Pattern found at positions: {search_result}")

  window.close()

def loadSecondScreen(text_to_search: str, pattern: str):
  # here we compute the LSP table
  global LSPTableInformation
  LSPTableInformation = []

  lsp = []
  kmp.ComputeLSP(pattern, len(pattern), lsp)

  row1 = []
  row2 = []

  for index in range(0, len(pattern)):
    row1.append(index)

  for letter in pattern:
    row2.append(letter)

  row3 = [str(value) for value in lsp]

  data = [row1, row2, row3]

  LSPTableInformation = [
    [gui.Table(
    values=data,
    auto_size_columns=False,
    justification='right',
    num_rows=3,
    display_row_numbers=False,
    bind_return_key=True,
    key='-TABLE-',
    col_widths=[10, 10, 10])],
  ]

  allFindingsText = []
  findings = kmp.KMPSearch(text_to_search, pattern)
  for find in findings:
    thisFindingText = []
    for index in range(len(text_to_search)):
      if find[0] <= index <= find[1]:
        thisFindingText.append(gui.Text(text_to_search[index], background_color='white', text_color='green', font=('Helvetica', 16)))
      else:
        thisFindingText.append(gui.Text(text_to_search[index], background_color='white', text_color='red', font=('Helvetica', 16)))
    allFindingsText.append(thisFindingText)



  layout_second_screen = [
    LSPTableInformation,
    allFindingsText
  ]

  window = gui.Window("KMP Algorithm visualization", layout=layout_second_screen, margins=(250, 250), background_color="#FFA658")

  while True:
    event, values = window.read()

    if event == gui.WINDOW_CLOSED:
      break

  window.close()


if __name__ == '__main__':
    loadMainMenu()
  
 
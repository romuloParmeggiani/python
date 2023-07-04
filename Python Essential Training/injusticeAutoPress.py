import pyautogui
import pygetwindow

def main():
    print(pygetwindow.getAllTitles())
    code = pygetwindow.getActiveWindow()
    code.pygetWindow.minimize()

if __name__ == "__main__":
    main()
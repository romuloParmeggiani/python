import urllib.request

def main():
    weburl = urllib.request.urlopen("https://www.google.com")
    print("result code:", weburl.getcode())
    data = weburl.read()
    print(data)

if __name__ == "__main__":
    main()
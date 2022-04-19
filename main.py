# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url='https://www.baidu.com'
    tar=input("yg")
    param={
        's?wd':tar
    }
    response=requests.get(url,param)

    # response= requests.get(url)
    text=response.text
    with open('./baiduq.html','w+',encoding='utf-8') as fps:
        fps.write(text)
    print(text)
    print_hi('PyCharm')

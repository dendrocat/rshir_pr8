from django.shortcuts import render
import subprocess
from testsite.utils import *

# Create your views here.


def drawer(request, id):
    size = 300
    img = {'title': "Сервис Drawer", 'size': size}
    svg = ""
    c = size // 2
    match id % 3:
        case 0:
            svg = f"<circle cx='{c}' cy='{c}' r='{c}' fill='red'>"
        case 1:
            svg = "<rect width='100%' height='100%' fill='blue'>"
        case 2:
            svg = f"<polygon points='{c},0 0,{size} {size},{size}' fill='green'>"
    img['svg'] = svg
    return render(request, "services/drawer.html", context=img)



def sort(request, arr):
    arr = list(map(str.strip, arr.split(',')))
    arr = list(map(int, arr))
    context = {
        'title': "Сортировка массива",
        "until": ' '.join(map(str, arr)), 
        "after": ' '.join(map(str, sorted(arr)))}
    return render(request, "services/sort.html", context=context)


def run(com: str):
    #coms = ["cmd.exe", '/c', com]
    res = subprocess.run(com.split(' '), 
        capture_output=True, 
        text=True)
    if res.returncode == 0:
        return res.stdout
    return f"Error: {res.stderr}"

def shell(request):
    cms = ['ls -a', 'pwd', 'uname -m -s', 'date']
    
    context = {
        "title": 'Команды',
        "comands": [
        { 'com': com, 'res': run(com) }
        for com in cms
    ]}
    
    return render(request, "services/shell.html", context=context)

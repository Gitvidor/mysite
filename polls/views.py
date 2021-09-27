from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import paramiko


def index(request):
    html="<h1>what the </h1"
    return HttpResponse(html)

def test_html(request):
    if request.method == 'GET':
        return render(request, 'test_html.html',locals())
    elif request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']
        res = 0
        if op == 'add':
            res = x + y
        elif op == 'sub':
            res = x - y
        elif op == 'mul':
            res = x * y
        elif op == 'div':
            res = x / y
    return render(request, 'test_html.html',locals())

def base_view(request):
    return render(request, 'base.html')

def music_view(request):
    return render(request, 'music.html')

def sport_view(request):
    return render(request, 'sport.html')

def test_url_result(request):
    return HttpResponse('---test url res is ok')

def shell(request):
    if request.method == 'GET':
        return render(request, 'shell.html')
    elif request.method == 'POST':
        username = 'root'
        passwd = 'Cvax47hWYbWN'
        Hostip = request.POST['Hostip']
        cmd = request.POST['cmd']
        # Hostip = '104.168.204.109'
        # cmd = 'date && ls -lh'
        # cmd = 'sh /root/weather/check_config_version.sh'
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(Hostip, 22, username, passwd)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            # message = "%s 环境执行命令'%s' OK\n" % (Hostip, cmd)
            outlist = stdout.readlines()
            # for i in outlist:
            #     print(i, end = '')
            # return 0
            ssh.close()
            return render(request, 'shell.html', locals())
        except Exception as ex:
            print("\tError %s\n" % ex)

from django.http import HttpResponse
import getpass
import datetime
import subprocess

def htop(request):
    username = getpass.getuser()  # FIXED: Replaced os.getlogin() with getpass.getuser()
    ist_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.getoutput("top -b -n 1 | head -10")  # Get system info

    response = f"""
    <h1>Name: Vyasam S D V Naga Harsha Vardhan</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {ist_time}</h2>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)

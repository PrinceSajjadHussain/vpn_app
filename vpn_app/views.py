from django.shortcuts import render, redirect
from .models import VPNUser
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VPNConfigForm
import os

# views.py
import subprocess
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VPNConfigForm, SudoPasswordForm
from .models import VPNUser

@login_required
def user_dashboard(request):
    vpn_user, created = VPNUser.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        vpn_form = VPNConfigForm(request.POST, initial={'country': vpn_user.country, 'enable_vpn': vpn_user.is_enabled})
        sudo_form = SudoPasswordForm(request.POST)
        
        if vpn_form.is_valid() and sudo_form.is_valid():
            vpn_user.country = vpn_form.cleaned_data['country']
            vpn_user.is_enabled = vpn_form.cleaned_data['enable_vpn']
            vpn_user.save()

            sudo_password = sudo_form.cleaned_data['sudo_password']
            # Here, execute the necessary sudo command
            try:
                command = f'echo {sudo_password} | sudo -S openvpn --config /etc/openvpn/{vpn_user.country}.conf'
                result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(e.stderr)
                # Handle the error accordingly

            return redirect('vpn_dashboard')
    else:
        vpn_form = VPNConfigForm(initial={'country': vpn_user.country, 'enable_vpn': vpn_user.is_enabled})
        sudo_form = SudoPasswordForm()

    return render(request, 'vpn/dashboard.html', {'vpn_form': vpn_form, 'sudo_form': sudo_form, 'vpn_user': vpn_user})
def restart_vpn_service(config_file):
    # code to restart vpn service
    pass

def stop_vpn_service(config_file):
    # code to stop vpn service
    pass
def generate_vpn_config(country):
    # This function should return the OpenVPN configuration based on the country
    # You should have pre-configured templates for each country
    # For simplicity, let's assume we have a dictionary of templates
    templates = {
        'US': 'config for US',
        'UK': 'config for UK',
        'CA': 'config for CA',
    }
    return templates.get(country, 'default config')


def restart_vpn_service(config_data):
    config_file_path = '/etc/openvpn/server.conf'
    try:
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_data)
        # Command to restart the OpenVPN service (modify as needed)
        os.system('sudo systemctl restart openvpn')
    except PermissionError:
        # Handle permission error
        print("Permission denied: Unable to write to the VPN config file.")
def home(request):
    return render(request, 'vpn_app/home.html')

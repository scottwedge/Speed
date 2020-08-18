import click
import os
import subprocess
from subprocess import Popen, PIPE
from sys import platform
from getpass import getpass
from progress.spinner import Spinner
from progress.bar import IncrementalBar
import time

@click.group()
def cli():
    pass

@cli.command()
def version():
    '''
    Information About The Current Speed You Are Running
    '''
    print('Version: 1.0 \nDistribution: Stable x64')


@cli.command()
@click.argument('package_name', required=True)
def install(package_name):
    '''
    Install A Specified Package
    '''
    os_bar = IncrementalBar('Getting Operating System...', max = 1)
    if platform == 'linux':
        os_bar.next()
        click.echo('\n')
        finding_bar = IncrementalBar('Finding Requested Packages...', max = 1)
        if package_name == 'git':
            for _ in range(1, 11):
                time.sleep(0.05)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Git...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.05)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install git".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Git! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.045)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.045)
                    testing_bar.next()
                subprocess.run(['git', 'clone', 'https://github.com/zpqrtbnk/test-repo.git'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                for _ in range(60, 101):
                    time.sleep(0.075)
                    testing_bar.next()
                os.system('rm -rf test-repo')
                subprocess.run(['git', '--version'], stdout=subprocess.DEVNULL)
                click.echo('\n')
                click.echo(click.style('Test Passed: Git Version ✅\n', fg='green'))
                click.echo(click.style('Test Passed: Clone Repository ✅\n', fg='green')) 
            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'curl': 
            for _ in range(1, 11):
                time.sleep(0.05)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Curl...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.05)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install git".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Curl! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.075)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.075)
                    testing_bar.next()
                subprocess.run(['curl', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                for _ in range(60, 101):
                    time.sleep(0.1)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: Curl Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'npm':
            for _ in range(1, 11):
                time.sleep(0.05)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing NPM...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.05)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install npm".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed NPM! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.075)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.075)
                    testing_bar.next()
                subprocess.run(['npm', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                for _ in range(60, 101):
                    time.sleep(0.1)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: NPM Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'zsh':
            if package_name == 'npm':
                for _ in range(1, 11):
                    time.sleep(0.05)
                    finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing ZSH...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.05)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install zsh".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed ZSH! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.075)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.075)
                    testing_bar.next()
                subprocess.run(['zsh', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                for _ in range(60, 101):
                    time.sleep(0.1)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: ZSH Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'vim':
            for _ in range(1, 11):
                time.sleep(0.05)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Vim...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.05)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install vim".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Vim! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.075)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.075)
                    testing_bar.next()
                subprocess.run(['vim', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                for _ in range(60, 101):
                    time.sleep(0.1)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: Vim Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'chrome':
            for _ in range(1, 2):
                time.sleep(0.05)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Chrome...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.05)
                    installer_progress.next()
                click.echo(click.style('\n Chrome Will Take 2 to 4 Minutes To Download... \n', fg='yellow'))
                proc = Popen("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb".split())
                proc.wait()
                second = Popen("sudo -S apt-get install ./google-chrome-stable_current_amd64.deb".split(), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                # Popen only accepts byte-arrays so you must encode the string
                _ = second.communicate(password.encode())
                
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Chrome! 🎉 \n'))             
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.045)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.045)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: Chrome Launch ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'opera':
            for _ in range(1, 11):
                time.sleep(0.05)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Opera...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.05)
                    installer_progress.next()
                proc = Popen("sudo -S snap install opera".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Opera! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.075)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.075)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.1)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: Opera Launch ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'googler':
            for _ in range(1, 11):
                time.sleep(0.05)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Googler...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.05)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install googler".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Googler! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.075)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.075)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.1)
                    testing_bar.next()
                subprocess.run(['googler','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Googler Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'code':
            for _ in range(1, 11):
                time.sleep(0.05)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Visual Studio Code...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.05)
                    installer_progress.next()
                proc = Popen("sudo -S snap install --classic code".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Visual Studio Code! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.075)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.075)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.1)
                    testing_bar.next()
                subprocess.run(['code','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Visual Studio Code Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'codeinsider':
            for _ in range(1, 11):
                time.sleep(0.05)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Visual Studio Code Insider...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.05)
                    installer_progress.next()
                proc = Popen("sudo -S snap install --classic code-insiders".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Visual Studio Code Insider! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.075)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.075)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.1)
                    testing_bar.next()
                subprocess.run(['code','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Visual Studio Code Insider Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)

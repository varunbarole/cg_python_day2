


import paramiko

def ssh_ctrl(ip, user, password,cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=ip, username=user, password=password, timeout=tout, compress = True, look_for_keys=False, allow_agent=False)
    except (socket.error, paramiko.AuthenticationException, paramiko.SSHException) as message:
        print("ERROR: SSH connection to " + ip + " failed: " + str(message))
        sys.exit(1)

    stdin, stdout, ssh_stderr = ssh.exec_command(cmd)
    out = stdout.read()
    stdin.flush()
    ssh.close()

ssh_ctrl("12.12.12.12","root","password","ls")

import paramiko
import os

def run_deploy():
    host = os.getenv("SSH_HOST")
    user = os.getenv("SSH_USER")
    key_path = os.path.expanduser(os.getenv("SSH_KEY_PATH"))
    command = os.getenv("DEPLOY_CMD")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username=user, key_filename=key_path)
        stdin, stdout, stderr = ssh.exec_command(command)
        out = stdout.read().decode()
        err = stderr.read().decode()
        return out if out else err
    except Exception as e:
        return f"Ошибка SSH: {str(e)}"
    finally:
        ssh.close()
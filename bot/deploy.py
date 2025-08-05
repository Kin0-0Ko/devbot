import subprocess
import os
def run_deploy():
    script_path = os.getenv("DEPLOY_SCRIPT_PATH", "/home/user/devops/deploy.sh")
    try:
        result = subprocess.run(
            ["/bin/bash", script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=300  
        )
        if result.returncode == 0:
            return result.stdout
        else:
            return f"❌ Ошибка:\n{result.stderr}"
    except subprocess.TimeoutExpired:
        return "⚠️ Скрипт превысил лимит времени"
    except Exception as e:
        return f"⚠️ Ошибка при запуске: {str(e)}"

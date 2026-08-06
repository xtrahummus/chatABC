"""
colab_setup.py
Quick-launch helper to run this Streamlit app inside a Google Colab notebook,
exposed publicly via localtunnel (default) or ngrok.

Usage inside a Colab cell:

    !git clone <your-repo-url> rag-streamlit-app
    %cd rag-streamlit-app
    !pip install -r requirements.txt -q
    !python colab_setup.py

Or, paste the contents of this file directly into a Colab cell.
"""

import os
import subprocess
import time
import urllib.request


def get_public_ip() -> str:
    """Fetches the tunnel password (public IP) required by localtunnel."""
    try:
        ip = urllib.request.urlopen("https://ipv4.icanhazip.com").read().decode("utf-8").strip()
        return ip
    except Exception as exc:  # noqa: BLE001
        print(f"Could not fetch public IP: {exc}")
        return ""


def run_with_localtunnel(port: int = 8501) -> None:
    """Launches Streamlit and exposes it via npx localtunnel."""
    print("Installing localtunnel (requires Node.js, pre-installed on Colab)...")
    subprocess.run(["npm", "install", "-g", "localtunnel"], check=False)

    public_ip = get_public_ip()
    if public_ip:
        print(f"\n🔑 Localtunnel password (paste this on the tunnel page): {public_ip}\n")

    print("Starting Streamlit app in the background...")
    streamlit_proc = subprocess.Popen(
        ["streamlit", "run", "app.py", f"--server.port={port}", "--server.headless=true"]
    )
    time.sleep(6)

    print("Opening localtunnel...")
    subprocess.run(["npx", "localtunnel", "--port", str(port)])

    streamlit_proc.terminate()


def run_with_ngrok(port: int = 8501, ngrok_authtoken: str = "") -> None:
    """Launches Streamlit and exposes it via pyngrok."""
    from pyngrok import ngrok, conf

    if ngrok_authtoken:
        conf.get_default().auth_token = ngrok_authtoken

    print("Starting Streamlit app in the background...")
    streamlit_proc = subprocess.Popen(
        ["streamlit", "run", "app.py", f"--server.port={port}", "--server.headless=true"]
    )
    time.sleep(6)

    public_url = ngrok.connect(port)
    print(f"\n🌐 Your app is live at: {public_url}\n")

    try:
        streamlit_proc.wait()
    except KeyboardInterrupt:
        streamlit_proc.terminate()
        ngrok.disconnect(public_url)


if __name__ == "__main__":
    method = os.environ.get("TUNNEL_METHOD", "localtunnel").lower()

    if method == "ngrok":
        token = os.environ.get("NGROK_AUTHTOKEN", "")
        run_with_ngrok(ngrok_authtoken=token)
    else:
        run_with_localtunnel()
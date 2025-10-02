import requests
import sys

def info_usuario(usuario):
    url = f"https://api.github.com/users/{usuario}"
    r = requests.get(url)
    if r.status_code != 200:
        return {"error": f"HTTP {r.status_code}"}
    d = r.json()
    return {
        "Usuario": d.get("login"),
        "Nombre": d.get("name"),
        "Repos públicos": d.get("public_repos"),
        "Seguidores": d.get("followers"),
        "Siguiendo": d.get("following"),
        "URL avatar": d.get("avatar_url")
    }

if __name__ == "__main__":
    usuario = sys.argv[1] if len(sys.argv) > 1 else "octocat"
    print(info_usuario(usuario))

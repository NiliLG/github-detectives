import requests
import sys

# 🔹 Cambiar aquí el usuario por defecto (para alumnos que no usan terminal)
usuario_default = "octocat"

def info_usuario(usuario):
    url = f"https://api.github.com/users/{usuario}"
    r = requests.get(url)
    if r.status_code != 200:
        return {"error": f"Usuario no encontrado (HTTP {r.status_code})"}
    d = r.json()
    return {
        "Usuario": d.get("login"),
        "Nombre": d.get("name") or "No disponible",
        "Repos públicos": d.get("public_repos"),
        "Seguidores": d.get("followers"),
        "Siguiendo": d.get("following"),
        "URL avatar": d.get("avatar_url")
    }

if __name__ == "__main__":
    # 🔹 Primero revisa si se pasó un argumento por terminal
    usuario = sys.argv[1] if len(sys.argv) > 1 else usuario_default
    datos = info_usuario(usuario)

    print("📊 Información del usuario:")
    for k, v in datos.items():
        print(f"{k}: {v}")

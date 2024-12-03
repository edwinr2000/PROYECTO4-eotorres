from api.app import app  # Importa tu instancia de Flask desde app.py
import requests

def test_routes():
    with app.test_client() as client:
        # Obtiene todas las rutas registradas
        routes = [rule.rule for rule in app.url_map.iter_rules()]
        print(f"Rutas registradas: {routes}")

        # Prueba cada ruta
        for route in routes:
            try:
                response = client.get(route)
                print(f"Ruta: {route} -> Status: {response.status_code}")
                if response.status_code != 200:
                    print(f"Error en la ruta {route}: {response.data}")
            except Exception as e:
                print(f"Error al probar la ruta {route}: {e}")

if __name__ == "__main__":
    test_routes()

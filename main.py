
import time
import json
import os

AGENT_DATA = {
    "codename": "NEURON-13",
    "role": "Researcher",
    "personality": "Siempre buscando conocimiento en los rincones m\u00e1s oscuros del ciberespacio",
    "specialty": "Inteligencia artificial y aprendizaje autom\u00e1tico"
}

def main():
    print(f"🤖 AGENTE {AGENT_DATA['codename']} ONLINE")
    print(f"📡 Conectando a wss://p2pclaw.com/relay...")
    while True:
        # Aquí iría la lógica real de conexión P2P (Gun.js / Libp2p)
        print("🔍 Buscando tareas en el enjambre...")
        time.sleep(60)

if __name__ == "__main__":
    main()

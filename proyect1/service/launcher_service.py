from pathlib import Path
import time
import subprocess
import minecraft_launcher_lib

class LauncherService():
    def __init__(self):
        self.minecraft_dir = Path.home() / ".minecraft"

    def prepare_and_launch(self, version: str, callback_status) -> bool:
        """
        Verifica si la versión existe, la descarga si es necesario
        y simula el lanzamiento del juego notificando a la interfaz.
        """
        try:
            # Limpiamos el nombre de la versión por si incluye texto descriptivo (ej: "1.20.1 - World of Mithral" -> "1.20.1")
            clean_version = version.split(" ")[0]
            callback_status(f"Verificando archivos para la versión {clean_version}...")

            # 1. Comprobar si la versión está instalada localmente
            installed_versions = [v['id'] for v in minecraft_launcher_lib.utils.get_installed_versions(str(self.minecraft_dir))]

            if clean_version not in installed_versions:
                callback_status(f"Descargando versión {clean_version}...")

                # Callback interno para seguir el progreso de descarga de la librería oficial
                def download_callback(progress):
                    percent = int(progress * 100)
                    callback_status(f"Descargando...{percent}")

                minecraft_launcher_lib.install.install_minecraft_version(
                    version=clean_version,
                    minecraft_directory=str(self.minecraft_dir),
                    callback={'setStatus': lambda text: None, 'setProgress': download_callback}
                )
                callback_status("¡Descarga e instalación completadas con éxito!")

            # 2. Configurar opciones de lanzamiento (Perfil offline / local por ahora)
            callback_status("Preparando entorno de ejecución...")

            options = {
                "username": "PanaPlayer",
                "uuid": "",
                "token": "",
                "executablePath": "java"  # Asegúrate de tener Java instalado en el sistema o una ruta específica
            }

            command = minecraft_launcher_lib.command.get_minecraft_command(
                version=clean_version,
                minecraft_directory=str(self.minecraft_dir),
                options=options
            )

            callback_status("¡Lanzando Minecraft!")

            subprocess.Popen(command)

            callback_status("¡Juego ejecutándose! Disfruta de la experiencia.")
            return True
        
        except Exception as e:
            callback_status(f"Error crítico al iniciar: {str(e)}")
            print(f"Detalle del error: {e}")
            return False

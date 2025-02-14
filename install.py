import subprocess
import ctypes
import sys
import os

def run_as_admin():
    """Garante que o script tenha permissões de administrador."""
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("🔹 Solicitando privilégios de administrador...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit(0)

# Chama a função para garantir permissões elevadas
run_as_admin()

# Obtém o diretório onde o script está rodando
BASE_DIR = os.getcwd()  # Pasta onde o script está sendo executado

# Lista de instaladores com caminhos absolutos baseados no diretório do script

#(os.path.join(BASE_DIR, "DriversLeitora", "OMNIKEY3x21_x64AMD_for_R1_2_2_8.exe"), ["/S", "/v", "/qn", "/norestart"]),   
#(os.path.join(BASE_DIR, "DriversLeitora", "SCR3_DriversOnly_V8.41.exe"), ["/S", "/v", "/qn", "/norestart"]),
installers = [
    (os.path.join(BASE_DIR, "DriversLeitora", "gemccid_en-us_64.msi"), ["/quiet", "/norestart"]),
    (os.path.join(BASE_DIR, "DriversLeitora", "OMNIKEY3x21_x64AMD_for_R1_2_2_8.exe"),[]),
    (os.path.join(BASE_DIR, "DriversLeitora", "SCR3_DriversOnly_V8.41.exe"),[]),
    (os.path.join(BASE_DIR, "Cartoes", "AWP_Manager_5.1.8_64_bits.msi"), ["/quiet", "/norestart"]),
    (os.path.join(BASE_DIR, "Cartoes", "certisign10.6-x64-10.6.msi"), ["/quiet", "/norestart"]),
    (os.path.join(BASE_DIR, "Cartoes", "SafeSign_Identity_Client-Standard-3.0.87-general-x64-win-admin-std-vc8.exe"), []),
    (os.path.join(BASE_DIR, "Cartoes", "SafeSignIC30124-x64-win-tu-admin.exe"), []),
]

# Loop para instalar os programas
for installer, args in installers:
    try:
        # Verifica se o arquivo existe
        if not os.path.isfile(installer):
            print(f"❌ Arquivo não encontrado: {installer}")
            continue
        
        print(f"📌 Instalando: {installer}...")

        # MSI usa msiexec
        if installer.endswith(".msi"):
            command = ["msiexec", "/i", installer] + args
        else:
            command = [installer] + args
        
        # Executa o processo
        process = subprocess.run(command, check=True, timeout=300, capture_output=True, text=True, shell=True)

        # Verifica retorno
        if process.returncode == 0:
            print(f"✅ {installer} instalado com sucesso!\n")
        else:
            print(f"⚠️ {installer} pode não ter sido instalado corretamente. Código: {process.returncode}\nSaída: {process.stdout}\nErro: {process.stderr}\n")

    except subprocess.TimeoutExpired:
        print(f"⏳ Tempo limite excedido para {installer}. Ele pode estar esperando interação do usuário.\n")

    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar {installer}. Código: {e.returncode}\nSaída: {e.output}\nErro: {e.stderr}\n")

    except Exception as e:
        print(f"❌ Erro inesperado ao instalar {installer}: {e}\n")

print("🎯 Instalação concluída!")

input("Pressione Enter para sair...")

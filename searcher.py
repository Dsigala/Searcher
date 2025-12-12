#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8




from __future__ import print_function
import sys
import os
import subprocess
import time
import platform

# ==============================================
# AUTO SETUP SYSTEM - HACE TODO AUTOMÁTICAMENTE
# ==============================================
def setup_environment():
    """Configura todo automáticamente: venv, dependencias, etc."""
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 32 + "DORKS EYE AUTO-SETUP" + " " * 27 + "║")
    print("╚" + "═" * 78 + "╝\n")
    
    # Verificar Python
    print("[1/7] 🔍 Checking Python version...")
    try:
        python_version = sys.version_info
        if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
            print(f"[!] Python {python_version.major}.{python_version.minor} is too old!")
            print("[!] Please install Python 3.8 or higher")
            return False
        print(f"[+] Python {python_version.major}.{python_version.minor}.{python_version.micro} ✓")
    except:
        print("[!] Cannot determine Python version!")
        return False
    
    # Determinar sistema operativo
    is_windows = platform.system() == "Windows"
    print(f"[+] Operating System: {platform.system()} {'(Windows)' if is_windows else ''}")
    
    # Verificar si ya estamos en un venv
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    
    if not in_venv:
        print("\n[2/7] 🏗️  Creating virtual environment...")
        venv_dir = "venv"
        
        if os.path.exists(venv_dir):
            print(f"[+] Virtual environment '{venv_dir}' already exists")
        else:
            try:
                print(f"[~] Creating virtual environment in '{venv_dir}'...")
                subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True, capture_output=True)
                print("[+] Virtual environment created successfully ✓")
            except subprocess.CalledProcessError as e:
                print(f"[!] Failed to create virtual environment: {e}")
                print("[!] Trying alternative method...")
                try:
                    import venv
                    venv.create(venv_dir, with_pip=True)
                    print("[+] Virtual environment created with venv module ✓")
                except Exception as e2:
                    print(f"[!] Failed with venv module: {e2}")
                    print("[?] Continue without virtual environment? (Y/N)")
                    if input("> ").strip().lower() != 'y':
                        return False
        
        # En Windows, necesitamos activar el venv de manera especial
        if is_windows and os.path.exists(venv_dir):
            print("\n[3/7] ⚡ Activating virtual environment...")
            
            # Determinar el path del Python en el venv
            if os.path.exists(os.path.join(venv_dir, "Scripts", "python.exe")):
                venv_python = os.path.join(venv_dir, "Scripts", "python.exe")
            elif os.path.exists(os.path.join(venv_dir, "bin", "python")):
                venv_python = os.path.join(venv_dir, "bin", "python")
            else:
                print("[!] Cannot find Python in virtual environment")
                venv_python = sys.executable
            
            # Usar el Python del venv para el resto del script
            print(f"[+] Using Python from: {venv_python}")
            
            # Verificar si podemos usar este Python
            try:
                result = subprocess.run([venv_python, "--version"], capture_output=True, text=True)
                print(f"[+] Virtual environment Python: {result.stdout.strip()}")
                # Cambiar el ejecutable de Python para las instalaciones
                sys.executable = venv_python
            except:
                print("[!] Cannot use venv Python, using system Python")
    
    else:
        print("\n[+] Already in virtual environment ✓")
    
    # Instalar/actualizar pip
    print("\n[4/7] 📦 Updating pip...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
                      check=True, capture_output=True)
        print("[+] pip updated successfully ✓")
    except:
        print("[!] Failed to update pip, continuing anyway...")
    
    # Instalar dependencias
    print("\n[5/7] 📥 Installing dependencies...")
    
    dependencies = [
        "ddgs",
        "googlesearch-python",
        "requests",
        "beautifulsoup4",
        "lxml",
        "colorama"
    ]
    
    all_installed = True
    for dep in dependencies:
        print(f"[~] Installing {dep}...")
        try:
            # Usar --quiet para menos output
            if is_windows:
                subprocess.run([sys.executable, "-m", "pip", "install", dep, "--quiet"], 
                              check=True, capture_output=True)
            else:
                subprocess.run([sys.executable, "-m", "pip", "install", dep], 
                              check=True, capture_output=True)
            print(f"[+] {dep} installed ✓")
        except subprocess.CalledProcessError:
            print(f"[!] Failed to install {dep}")
            all_installed = False
    
    if not all_installed:
        print("\n[!] Some dependencies failed to install automatically")
        print("[?] Try manual installation with: pip install ddgs googlesearch-python requests beautifulsoup4 lxml colorama")
        print("[?] Continue anyway? (Y/N)")
        if input("> ").strip().lower() != 'y':
            return False
    
    print("\n[6/7] 🔄 Verifying installations...")
    
    # Verificar imports críticos
    critical_modules = ["ddgs", "requests", "bs4"]
    missing_modules = []
    
    for module in critical_modules:
        try:
            if module == "bs4":
                __import__("bs4")
            else:
                __import__(module)
            print(f"[+] {module} ✓")
        except ImportError:
            print(f"[!] {module} ✗")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n[!] Missing critical modules: {', '.join(missing_modules)}")
        print("[?] Try installing manually or continue anyway? (Y/N)")
        if input("> ").strip().lower() != 'y':
            return False
    
    print("\n[7/7] ✅ Setup completed successfully!")
    print("\n" + "=" * 80)
    print("[+] Everything is ready to run Dorks Eye!")
    print("[+] Starting main application...")
    print("=" * 80 + "\n")
    
    time.sleep(2)
    return True


# Ejecutar el setup automático
if __name__ == "__main__":
    # Preguntar si ejecutar auto-setup
    print("\n" + "▄" * 80)
    print("█" + " " * 30 + "DORKS EYE v2.1" + " " * 33 + "█")
    print("▀" * 80 + "\n")
    
    print("[?] Do you want to run automatic setup? (creates venv, installs dependencies)")
    print("[?] This will take a few minutes. (Y/N)")
    
    try:
        run_setup = input("> ").strip().lower()
        if run_setup == 'y':
            if not setup_environment():
                print("\n[!] Setup failed. Exiting...")
                sys.exit(1)
        else:
            print("\n[!] Skipping automatic setup...")
            print("[!] Make sure you have all dependencies installed manually")
            print("[!] Required: ddgs, googlesearch-python, requests, beautifulsoup4, lxml, colorama")
            print("\n[?] Continue without setup? (Y/N)")
            if input("> ").strip().lower() != 'y':
                sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n[!] Setup cancelled by user")
        sys.exit(1)

# ==============================================
# IMPORTAR MÓDULOS DESPUÉS DEL SETUP
# ==============================================
print("[~] Loading modules...")

try:
    from ddgs import DDGS
    print("[+] ddgs module loaded ✓")
except ImportError:
    print("[!] ERROR: ddgs module not found!")
    print("[!] Install with: pip install ddgs")
    sys.exit(1)

try:
    from googlesearch import search as google_search
    print("[+] googlesearch module loaded ✓")
except ImportError:
    print("[!] WARNING: googlesearch-python not installed")
    print("[!] Google searches will not work")
    google_search = None

try:
    import requests
    from bs4 import BeautifulSoup
    import urllib.parse
    print("[+] BeautifulSoup4 and requests loaded ✓")
except ImportError as e:
    print(f"[!] ERROR: {e}")
    print("[!] Install missing modules")
    sys.exit(1)

try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    print("[+] colorama loaded ✓")
except ImportError:
    print("[!] WARNING: colorama not installed, colors may not work")
    # Definir colores básicos si colorama no está disponible
    class Fore:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'
        RESET = '\033[0m'

# ==============================================
# CONTINUAR CON EL RESTO DEL SCRIPT
# ==============================================
import threading
import hashlib


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    CGREEN = "\33[92m"
    CYELLOW = "\33[93m"
    CMAGENTA = "\33[95m"
    CCYAN = "\33[96m"
    ENDC = "\033[0m"


banner = ("""
███████╗██╗ ██████╗  █████╗ ██╗      █████╗ 
██╔════╝██║██╔════╝ ██╔══██╗██║     ██╔══██╗
███████╗██║██║  ███╗███████║██║     ███████║
╚════██║██║██║   ██║██╔══██║██║     ██╔══██║
███████║██║╚██████╔╝██║  ██║███████╗██║  ██║
╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                             v2.1 AUTO-SETUP""")


print("\n" + Fore.CYAN + "=" * 80)
print(Fore.YELLOW + "STARTING SIGALA...")
print(Fore.CYAN + "=" * 80 + "\n")

for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.002)

x = ("""
                Author:  CR4CK3N\n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.004)

y = "\n\t\tLet's start looking 𓂀\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.05)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


class SearchEngine:
    def __init__(self):
        self.duckduckgo_cache = {}
        self.results_lock = threading.Lock()
        
    def duckduckgo(self, dork, amount):
        cache_key = hashlib.md5(dork.encode()).hexdigest()
        if cache_key in self.duckduckgo_cache:
            return self.duckduckgo_cache[cache_key]
        
        results = []
        max_retries = 2
        retry_delay = 3
        
        for attempt in range(max_retries):
            try:
                with DDGS() as ddgs:
                    for r in ddgs.text(dork, max_results=amount):
                        if 'href' in r:
                            results.append(r['href'])
                break
            except Exception:
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
        
        self.duckduckgo_cache[cache_key] = results
        return results
    
    def bing(self, dork, amount):
        results = []
        max_retries = 1
        retry_delay = 2
        
        for attempt in range(max_retries):
            try:
                with DDGS() as ddgs:
                    for r in ddgs.text(dork, backend="html", max_results=amount):
                        if 'href' in r:
                            results.append(r['href'])
                break
            except Exception:
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
        return results
    
    def google(self, dork, amount):
        results = []
        if google_search is None:
            return results
        
        max_retries = 1
        retry_delay = 3
        
        for attempt in range(max_retries):
            try:
                count = 0
                for result in google_search(dork, num_results=min(amount, 10)):
                    results.append(result)
                    count += 1
                    if count >= amount:
                        break
                    time.sleep(1.5)
                break
            except Exception:
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
        return results
    
    def brave(self, dork, amount):
        results = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate'
        }
        
        try:
            query = urllib.parse.quote_plus(dork)
            url = f"https://search.brave.com/search?q={query}"
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('http') and 'brave.com' not in href:
                    results.append(href)
                    if len(results) >= amount:
                        break
                        
        except Exception:
            pass
        
        return results[:amount]
    
    def yandex(self, dork, amount):
        results = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        try:
            query = urllib.parse.quote_plus(dork)
            url = f"https://yandex.com/search/?text={query}"
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            patterns = ['a[href^="http"]', 'a.Link', 'a.serp-item__title-link']
            
            for pattern in patterns:
                links = soup.select(pattern)
                for link in links:
                    href = link.get('href')
                    if href and 'yandex' not in href:
                        results.append(href)
                        if len(results) >= amount:
                            break
                if len(results) >= amount:
                    break
                    
        except Exception:
            pass
        
        return results[:amount]


def safe_input(prompt, is_int=False, default=None):
    """Función segura para entrada de datos"""
    while True:
        try:
            value = input(prompt).strip()
            if not value and default is not None:
                return default
            if is_int:
                return int(value)
            return value
        except ValueError:
            if is_int:
                print(Fore.RED + "[!] Please enter a valid number!")
            continue
        except KeyboardInterrupt:
            raise


try:
    print("\n" + "  " + "»" * 78 + "\n")
    print(Fore.CYAN + "[~] Choose Your Search Engine:\n")
    print(Fore.YELLOW + "[1] DuckDuckGo - Fast, reliable for massive dorks")
    print(Fore.YELLOW + "[2] Bing - Fast but sometimes unstable")
    print(Fore.YELLOW + "[3] Google - Slow but good results")
    print(Fore.YELLOW + "[4] Brave Search - Fast, independent")
    print(Fore.YELLOW + "[5] Yandex - Fast, different index")
    print(Fore.YELLOW + "[6] ALL (Not recommended for massive files)")
    
    engine_choice = safe_input(Fore.GREEN + "\n[+] Select Option (1-6): ")
    
    print(Fore.CYAN + "\n[~] Input Mode:")
    print(Fore.YELLOW + "[1] Single Dork (Manual Input)")
    print(Fore.YELLOW + "[2] Multiple Dorks from File (MASSIVE MODE)")
    
    input_mode = safe_input(Fore.GREEN + "\n[+] Select Input Mode (1/2): ")
    
    data = safe_input(Fore.GREEN + "[+] Do You Like To Save The Output In A File? (Y/N) ", default="N")
    l0g = ""

except KeyboardInterrupt:
    print("\n")
    print(Fore.RED + "[!] User Interruption Detected..!")
    time.sleep(0.5)
    print("\n\n\t" + Fore.RED + "[!] I like to See Ya, Hacking " + Fore.RESET + "😃\n\n")
    time.sleep(0.5)
    sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.lower().startswith("y"):
    l0g = safe_input(Fore.CYAN + "[~] Give The File a Name: ", default="results")
    print(Fore.GREEN + f"[+] Results will be saved to: {l0g}.txt")
else:
    print(Fore.YELLOW + "[!] Saving is Skipped...")

print("\n" + "  " + "»" * 78 + "\n")


def count_lines(filename):
    """Contar líneas en archivo de forma eficiente"""
    count = 0
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            for _ in f:
                count += 1
                if count % 1000000 == 0:
                    print(Fore.CYAN + f"[~] Counting... {count:,} lines so far")
    except Exception as e:
        print(Fore.RED + f"[!] Error counting lines: {e}")
        return 0
    return count


def stream_dorks(filename, start=0, batch_size=10000):
    """Stream dorks from file to avoid memory issues"""
    count = 0
    batch = []
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            for _ in range(start):
                next(f, None)
            
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    batch.append(line)
                    count += 1
                    
                    if len(batch) >= batch_size:
                        yield batch
                        batch = []
            
            if batch:
                yield batch
                
    except Exception as e:
        print(Fore.RED + f"[!] Error reading file: {e}")
        if batch:
            yield batch


def process_single_dork():
    """Process a single dork entered manually"""
    dork = safe_input(Fore.CYAN + "\n[+] Enter The Dork Search Query: ")
    amount = safe_input(Fore.CYAN + "[+] Enter The Number Of Websites To Display: ", is_int=True, default=10)
    print("\n")
    return [dork], amount


def process_massive_file():
    """Process massive dorks file"""
    filename = safe_input(Fore.CYAN + "\n[+] Enter the path to your MASSIVE dorks file: ")
    
    if not os.path.exists(filename):
        print(Fore.RED + f"[!] File '{filename}' does not exist!")
        return [], 0
    
    print(Fore.CYAN + "[~] Counting lines in file (this may take a while)...")
    total_lines = count_lines(filename)
    
    if total_lines == 0:
        print(Fore.RED + "[!] File is empty or cannot be read!")
        return [], 0
    
    print(Fore.GREEN + f"[+] File has {total_lines:,} total lines")
    
    print(Fore.CYAN + "\n[~] Processing Range:")
    print(Fore.YELLOW + f"    File has lines: 1 - {total_lines}")
    
    start_line = safe_input(Fore.CYAN + f"[+] Start from line (1-{total_lines}): ", is_int=True, default=1)
    end_line = safe_input(Fore.CYAN + f"[+] End at line ({start_line}-{total_lines}): ", is_int=True, default=total_lines)
    
    if start_line < 1:
        start_line = 1
    if end_line > total_lines:
        end_line = total_lines
    if start_line > end_line:
        start_line, end_line = end_line, start_line
    
    total_to_process = end_line - start_line + 1
    print(Fore.GREEN + f"[+] Will process {total_to_process:,} dorks")
    
    if total_to_process > 100000:
        print(Fore.RED + f"[!] WARNING: Processing {total_to_process:,} dorks will take DAYS!")
        confirm = safe_input(Fore.YELLOW + "[?] Are you REALLY sure? (Y/N): ").lower()
        if confirm != 'y':
            return [], 0
    
    batch_size = safe_input(Fore.CYAN + "[+] Batch size (dorks per batch, 1000-10000): ", is_int=True, default=5000)
    batch_size = max(1000, min(batch_size, 10000))
    
    amount = safe_input(Fore.CYAN + "[+] Results per dork (1-20): ", is_int=True, default=5)
    amount = max(1, min(amount, 20))
    
    print(Fore.GREEN + "\n[+] Configuration:")
    print(Fore.YELLOW + f"    Dorks: {total_to_process:,}")
    print(Fore.YELLOW + f"    Batch size: {batch_size}")
    print(Fore.YELLOW + f"    Results per dork: {amount}")
    print(Fore.YELLOW + f"    Estimated batches: {total_to_process // batch_size + 1}")
    
    confirm = safe_input(Fore.YELLOW + "\n[?] Start massive processing? (Y/N): ").lower()
    if confirm != 'y':
        return [], 0
    
    return {"filename": filename, "start": start_line-1, "end": end_line, 
            "batch_size": batch_size, "total": total_to_process}, amount


def dorks():
    try:
        searcher = SearchEngine()
        
        if input_mode == "1":
            dorks_list, amount = process_single_dork()
            is_streaming = False
        elif input_mode == "2":
            dorks_config, amount = process_massive_file()
            if not dorks_config:
                return
            is_streaming = True
        else:
            print(Fore.RED + "[!] Invalid input mode!")
            return
        
        engines = []
        if engine_choice == "1":
            engines = ["duckduckgo"]
        elif engine_choice == "2":
            engines = ["bing"]
        elif engine_choice == "3":
            engines = ["google"]
        elif engine_choice == "4":
            engines = ["brave"]
        elif engine_choice == "5":
            engines = ["yandex"]
        elif engine_choice == "6":
            print(Fore.RED + "[!] WARNING: Using ALL engines with massive file will be VERY slow!")
            engines = ["duckduckgo", "brave", "yandex"]
        else:
            print(Fore.RED + "[!] Invalid choice, using DuckDuckGo...")
            engines = ["duckduckgo"]
        
        all_results = set()
        processed_total = 0
        
        if not is_streaming:
            for dork in dorks_list:
                for engine_type in engines:
                    try:
                        if engine_type == "duckduckgo":
                            results = searcher.duckduckgo(dork, amount)
                        elif engine_type == "bing":
                            results = searcher.bing(dork, amount)
                        elif engine_type == "google":
                            results = searcher.google(dork, amount)
                        elif engine_type == "brave":
                            results = searcher.brave(dork, amount)
                        elif engine_type == "yandex":
                            results = searcher.yandex(dork, amount)
                        else:
                            results = []
                        
                        for result in results:
                            if result not in all_results:
                                all_results.add(result)
                                print(Fore.GREEN + result)
                                
                                if data.lower().startswith("y"):
                                    logger(result)
                                    
                    except Exception:
                        continue
                
                processed_total += 1
                
        else:
            filename = dorks_config["filename"]
            start_line = dorks_config["start"]
            end_line = dorks_config["end"]
            batch_size = dorks_config["batch_size"]
            total_dorks = dorks_config["total"]
            
            print(Fore.CYAN + f"\n[+] Starting MASSIVE processing...")
            print(Fore.YELLOW + f"[+] Press Ctrl+C to stop at any time\n")
            
            batch_num = 0
            current_position = start_line
            
            for batch in stream_dorks(filename, start_line, batch_size):
                batch_num += 1
                current_position += len(batch)
                
                if current_position > end_line:
                    batch = batch[:end_line - (current_position - len(batch))]
                    if not batch:
                        break
                
                print(Fore.CYAN + f"[~] Processing batch {batch_num}: {len(batch):,} dorks")
                
                for dork in batch:
                    for engine_type in engines:
                        try:
                            if engine_type == "duckduckgo":
                                results = searcher.duckduckgo(dork, amount)
                            elif engine_type == "bing":
                                results = searcher.bing(dork, amount)
                            elif engine_type == "google":
                                results = searcher.google(dork, amount)
                            elif engine_type == "brave":
                                results = searcher.brave(dork, amount)
                            elif engine_type == "yandex":
                                results = searcher.yandex(dork, amount)
                            else:
                                results = []
                            
                            for result in results:
                                if result not in all_results:
                                    all_results.add(result)
                                    print(Fore.GREEN + result)
                                    
                                    if data.lower().startswith("y"):
                                        logger(result)
                                        
                        except Exception:
                            continue
                    
                    processed_total += 1
                    
                    if processed_total % 100 == 0:
                        percent = (processed_total / total_dorks) * 100
                        sys.stderr.write(Fore.CYAN + f"\r[~] Progress: {processed_total:,}/{total_dorks:,} dorks ({percent:.1f}%) | URLs found: {len(all_results):,}")
                        sys.stderr.flush()
                
                time.sleep(0.5)
            
            print(Fore.GREEN + f"\n\n[+] MASSIVE processing completed!")
            print(Fore.GREEN + f"[+] Processed: {processed_total:,} dorks")
            print(Fore.GREEN + f"[+] Unique URLs found: {len(all_results):,}")
        
        if data.lower().startswith("y"):
            print(Fore.GREEN + f"\n[+] Results saved to: {l0g}.txt")
        
        print(f"\n\t\t\t\t" + Fore.CYAN + "Dorks Eye AUTO-SETUP" + Fore.RESET)
        print(f"\t\t" + Fore.RED + "[!] I like to See Ya, Hacking " + Fore.RESET + "😃\n\n")

    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Processing stopped by user")
        print(Fore.YELLOW + f"[!] Processed: {processed_total:,} dorks")
        print(Fore.YELLOW + f"[!] Unique URLs found: {len(all_results):,}")
        if data.lower().startswith("y"):
            print(Fore.YELLOW + f"[!] Partial results saved to: {l0g}.txt")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"[!] Unexpected error: {e}")
        sys.exit(1)


# Ejecutar la función principal
dorks()
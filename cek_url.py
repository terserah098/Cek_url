import time
import sys
import random
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich import box  # Dipindahkan ke atas agar bisa diakses oleh semua fungsi

console = Console()

def play_blinking_error_animation():
    """Menampilkan animasi layar error berkedip (strobe effect) yang dramatis."""
    error_text = "\n" * 5 + "[bold white on red]        ⚠️  FATAL EXCEPTION: SYSTEM CRASH DETECTED  ⚠️        [/bold white on red]\n" * 3
    blank_text = "\n" * 10
    
    for _ in range(3):  # Dikurangi menjadi 3 agar tidak terlalu lama tetapi efek tetap terasa
        console.clear()
        console.print(error_text, justify="center")
        time.sleep(0.15)
        
        console.clear()
        console.print(blank_text)
        time.sleep(0.08)

    console.clear()
    console.print(error_text, justify="center")
    console.print("\n[bold red]🔄 REBOOTING CORE SYSTEM...[/bold red]", justify="center")
    time.sleep(1.2)
    
    console.clear()
    with console.status("[bold green]Mengembalikan modul sistem...", spinner="bouncingBar"):
        time.sleep(1.0)
    
    console.clear()

def show_welcome_screen():
    """Menampilkan banner utama dengan isi panel berada di tengah kotak."""
    ascii_lines = [
        "[bold cyan]      _  _  _   ___   __     _  _   ___   __    __    ___   ___   ___[/bold cyan]",
        "[bold deep_sky_blue1]      |  |  |  |___  |__]    |__|  |___  |__|  |  |  |___  |__/  [__ [/bold deep_sky_blue1]",
        "[bold dodger_blue1]      |__|__|  |___  |__]    |  |  |___  |  |  |__|  |___  |  \\  ___][/bold dodger_blue1]"
    ]
    
    print()
    # Mencetak judul ASCII rata kiri
    for line in ascii_lines:
        console.print(Text.from_markup(line))
        
    # Menambahkan justify="center" agar teks di dalam panel berada di tengah kotak
    content = Text(justify="center")
    content.append("\n🛡️  Alat Defensif Konfigurasi Keamanan Website\n", style="bold white")
    content.append("⚙️  Engine: v2.5 (Stable)  |  🟢 Status: Ready\n", style="dim cyan")
    content.append("─" * 68 + "\n", style="dim dark_slate_gray1")
    
    content.append("🚀 Collaboration Project by:\n", style="dim white")
    content.append("[ ", style="dim white")
    content.append("Ikhsan", style="bold italic spring_green3")
    content.append(" ]", style="dim white")
    content.append(" X ", style="dim white")
    content.append("[ ", style="dim white")
    content.append("Bayu", style="bold italic spring_green3")
    content.append(" ]\n", style="dim white")
    
    # Menampilkan panel di pinggir kiri dengan isi konten rata tengah
    console.print(
        Panel(
            content,
            border_style="bright_magenta",
            box=box.DOUBLE,
            padding=(0, 2),
            expand=False
        )
    )
    print()


def simulate_loading():
    """Membuat animasi loading/spinner yang modern."""
    with Progress(
        SpinnerColumn(spinner_name="dots", style="bold cyan"),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task1 = progress.add_task(description="[yellow] Menginisialisasi sistem...[/yellow]", total=1)
        time.sleep(0.8)
        
        task2 = progress.add_task(description="[cyan] Menghubungkan ke server target...[/cyan]", total=1.2)
        time.sleep(1.2)
        
        task3 = progress.add_task(description="[magenta] Menganalisis respons HTTP header...[/magenta]", total=1)
        time.sleep(0.8)

def check_security_headers(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url

    simulate_loading()
    
    # Header box informasi target
    target_info = Text(justify="center")
    target_info.append("🔍 HASIL ANALISIS TARGET\n", style="bold white")
    target_info.append(url, style="bold underline green")
    
    console.print(Panel(target_info, border_style="blue", box=box.ROUNDED, expand=False), justify="center")
    print()

    important_headers = {
        "Strict-Transport-Security": "Melindungi dari serangan MITM (Memaksa HTTPS).",
        "Content-Security-Policy": "Mencegah serangan Cross-Site Scripting (XSS).",
        "X-Frame-Options": "Melindungi situs dari serangan Clickjacking.",
        "X-Content-Type-Options": "Mencegah browser menebak (sniffing) tipe MIME.",
        "Referrer-Policy": "Mengontrol informasi referrer yang bocor."
    }

    try:
        # Menambahkan User-Agent agar tidak diblokir oleh beberapa web server/Cloudflare
        headers_request = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers_request, timeout=10)
        headers = response.headers
        
        table = Table(
            title="\n📊 [bold white]Status Konfigurasi Keamanan Header[/bold white]", 
            box=box.HEAVY_HEAD, 
            show_lines=True
        )
        table.add_column("Nama Header", style="bold cyan", no_wrap=True, width=30)
        table.add_column("Status", justify="center", width=18)
        table.add_column("Keterangan / Dampak jika Hilang", style="white")

        missing_count = 0
        
        for header, description in important_headers.items():
            if header.lower() in [h.lower() for h in headers.keys()]:
                table.add_row(header, "[bold green]✓ TERPASANG[/bold green]", "[dim green]Header aktif dan melindungi situs.[/dim green]")
            else:
                table.add_row(header, "[bold red]✗ HILANG[/bold red]", f"[bold red]⚠️[/bold red] [light_salmon3]{description}[/light_salmon3]")
                missing_count += 1
                
        console.print(table, justify="center")
        print()
        
        if missing_count == 0:
            success_text = Text("\n🎉 Sempurna! Semua header keamanan dasar telah terkonfigurasi dengan baik.\nSitus ini memiliki pertahanan awal yang solid.", justify="center")
            console.print(Panel(success_text, border_style="green", box=box.ROUNDED, expand=False), justify="center")
        else:
            warn_text = Text(justify="center")
            warn_text.append(f"⚠️  Peringatan: Ditemukan {missing_count} celah konfigurasi header yang belum terpasang.\n", style="bold yellow")
            warn_text.append("Disarankan untuk memperbarui konfigurasi web server (Nginx/Apache/Cloudflare) Anda.", style="dim white")
            console.print(Panel(warn_text, border_style="yellow", box=box.ROUNDED, expand=False), justify="center")

    except requests.exceptions.ConnectionError:
        console.print("[bold red]❌ [Error] Gagal terhubung ke website. Pastikan URL benar atau website sedang aktif.[/bold red]", justify="center")
    except requests.exceptions.Timeout:
        console.print("[bold red]❌ [Error] Waktu permintaan habis (Timeout).[/bold red]", justify="center")
    except Exception as e:
        console.print(f"[bold red]❌ [Error] Terjadi kesalahan: {e}[/bold red]", justify="center")

if __name__ == "__main__":
    # Menjalankan animasi eror kedap-kedip di awal
    play_blinking_error_animation()
    
    # Menampilkan banner utama
    show_welcome_screen()
    
    # Mempercantik form inputan target
    target_url = console.input("[bold yellow]👉 Masukkan URL Website Target (contoh: google.com): [/bold yellow]").strip()
    print()
    
    if target_url:
        check_security_headers(target_url)
    else:
        console.print("[bold red]❌ URL tidak boleh kosong![/bold red]", justify="center")

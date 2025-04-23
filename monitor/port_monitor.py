import psutil
import logging

# Taniqli portlar haqida izohlar
known_ports = {
    80: "HTTP (veb server)",
    443: "HTTPS (SSL veb server)",
    22: "SSH (masofaviy boshqaruv)",
    445: "Windows SMB (xavfli bo'lishi mumkin)",
    5432: "PostgreSQL (ma'lumotlar bazasi)",
    3306: "MySQL (ma'lumotlar bazasi)",
    8080: "HTTP (custom server yoki test)",
    21: "FTP (fayl uzatish protokoli)"
}

# Faqat ruxsat berilgan xavfsiz portlar ro'yxati
safe_ports = [80, 443, 22, 5432]

def check_open_ports():
    conns = psutil.net_connections(kind='inet')
    for conn in conns:
        if conn.status == 'LISTEN':
            ip = conn.laddr.ip
            port = conn.laddr.port
            desc = known_ports.get(port, "Noma'lum yoki custom xizmat")

            if port in safe_ports:
                logging.info(f"✅ Listening port: {ip}:{port} — {desc}")
            else:
                logging.warning(f"⚠️ POTENSIAL XAVF: {ip}:{port} — {desc}")

# Práctica 4 — Taller de Sistemas Operativos
## Creación de una Red Privada Virtual (VPN) en CachyOS

La guía original usa **Ubuntu + PPTP (`pptpd`)**, que hoy es inseguro
(Android incluso marca “VPN no segura”).

Aquí haces lo mismo en **CachyOS** con un servicio más actual:
**WireGuard** + `systemd`.

Equivalencias:

| Práctica antigua (PPTP)              | Moderna (WireGuard en CachyOS)      |
|--------------------------------------|-------------------------------------|
| `sudo apt update`                    | `sudo pacman -Syu`                  |
| `apt-get install pptpd`              | `sudo pacman -S wireguard-tools`    |
| `/etc/pptpd.conf` (`localip/remoteip`)| `/etc/wireguard/wg0.conf`           |
| `/etc/ppp/chap-secrets` (usuario/pass)| claves públicas/privadas            |
| `systemctl start pptpd.service`      | `systemctl enable --now wg-quick@wg0` |
| Cliente Android tipo PPTP            | App **WireGuard** (Play Store)      |

---

## 0) Requisitos

- CachyOS (físico o VirtualBox)
- Red en modo **Adaptador puente** (Bridge) si usas VirtualBox
  (así el celular en la misma Wi‑Fi puede llegar a la IP del servidor)
- Anota la IP del servidor:

```bash
ip -br a
```

Ejemplo: `192.168.1.16` (usa la tuya).

---

## 1) Actualizar e instalar WireGuard

```bash
sudo pacman -Syu
sudo pacman -S wireguard-tools
```

Verifica:

```bash
wg --version
```

---

## 2) Generar claves (servidor + cliente)

```bash
sudo mkdir -p /etc/wireguard
sudo chmod 700 /etc/wireguard
cd /etc/wireguard

# Claves del servidor
sudo sh -c 'umask 077; wg genkey | tee server_private.key | wg pubkey > server_public.key'

# Claves del cliente (celular / otra PC)
sudo sh -c 'umask 077; wg genkey | tee client_private.key | wg pubkey > client_public.key'

# Ver claves (las necesitas para el reporte y para el celular)
sudo cat server_private.key
sudo cat server_public.key
sudo cat client_private.key
sudo cat client_public.key
```

> En PPTP metías usuarios en `chap-secrets`.
> En WireGuard la “autenticación” son estas claves.

---

## 3) Configurar el servidor VPN

Crea `/etc/wireguard/wg0.conf`:

```bash
sudo tee /etc/wireguard/wg0.conf >/dev/null <<'EOF'
[Interface]
# IP interna del servidor VPN (equivalente a localip 10.10.10.1)
Address = 10.10.10.1/24
ListenPort = 51820
PrivateKey = PEGA_AQUI_server_private.key

# NAT para que el cliente salga a Internet por el servidor (opcional pero útil)
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o $(ip -br route show default | awk '{print $3; exit}') -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o $(ip -br route show default | awk '{print $3; exit}') -j MASQUERADE

[Peer]
# Cliente (equivalente a usuario1 en chap-secrets)
PublicKey = PEGA_AQUI_client_public.key
# IP que tendrá el cliente (equivalente a remoteip)
AllowedIPs = 10.10.10.10/32
EOF
```

Reemplaza las dos claves con las reales:

```bash
sudo nano /etc/wireguard/wg0.conf
```

Permisos:

```bash
sudo chmod 600 /etc/wireguard/wg0.conf
```

Habilita reenvío IP (necesario en VPN):

```bash
echo 'net.ipv4.ip_forward=1' | sudo tee /etc/sysctl.d/99-wireguard-forward.conf
sudo sysctl --system
```

Si no tienes `iptables`:

```bash
sudo pacman -S iptables
```

---

## 4) Arrancar el servicio (como en la práctica con systemctl)

```bash
sudo systemctl enable --now wg-quick@wg0
systemctl status wg-quick@wg0
sudo wg show
```

Debe salir `active (running)` y verse la interfaz `wg0`.

Comandos útiles (para capturas del reporte):

```bash
sudo systemctl stop wg-quick@wg0
sudo systemctl start wg-quick@wg0
sudo systemctl restart wg-quick@wg0
systemctl is-enabled wg-quick@wg0
journalctl -u wg-quick@wg0 -n 50
```

Abrir firewall (si lo usas):

```bash
# ufw
sudo ufw allow 51820/udp
sudo ufw allow from 10.10.10.0/24
sudo ufw status

# o firewalld
sudo firewall-cmd --permanent --add-port=51820/udp
sudo firewall-cmd --reload
```

---

## 5) Configurar el cliente (celular) — reemplazo del PPTP en Android

1. Instala la app **WireGuard** (Play Store / F-Droid).
2. Crear túnel → **Crear desde cero** (o importar archivo).
3. Datos del túnel del teléfono:

```ini
[Interface]
PrivateKey = PEGA_AQUI_client_private.key
Address = 10.10.10.10/32
DNS = 1.1.1.1

[Peer]
PublicKey = PEGA_AQUI_server_public.key
Endpoint = 192.168.1.XX:51820
AllowedIPs = 10.10.10.0/24
PersistentKeepalive = 25
```

Cambia `192.168.1.XX` por la IP real de tu CachyOS (`ip -br a`).

4. Activa el túnel.
5. Prueba desde el celular (Termux o otra app de terminal / desde otra PC):

```bash
ping 10.10.10.1
```

En el servidor deberías ver handshake:

```bash
sudo wg show
```

---

## 6) Segundo “usuario” (como usuario1 y usuario2 del PDF)

Genera otro par de claves:

```bash
cd /etc/wireguard
sudo sh -c 'umask 077; wg genkey | tee client2_private.key | wg pubkey > client2_public.key'
```

Agrega otro `[Peer]` en `/etc/wireguard/wg0.conf`:

```ini
[Peer]
PublicKey = PEGA_AQUI_client2_public.key
AllowedIPs = 10.10.10.11/32
```

Recarga:

```bash
sudo systemctl restart wg-quick@wg0
sudo wg show
```

Config del segundo cliente:

```ini
[Interface]
PrivateKey = PEGA_AQUI_client2_private.key
Address = 10.10.10.11/32
DNS = 1.1.1.1

[Peer]
PublicKey = PEGA_AQUI_server_public.key
Endpoint = 192.168.1.XX:51820
AllowedIPs = 10.10.10.0/24
PersistentKeepalive = 25
```

---

## 7) Evidencias para el reporte

Captura / pega:

1. Título: VPN con WireGuard en CachyOS (alternativa moderna a PPTP)
2. `cat /etc/os-release`
3. Instalación: `pacman -Qi wireguard-tools`
4. Archivo `/etc/wireguard/wg0.conf` (oculta claves privadas si lo vas a compartir)
5. `systemctl status wg-quick@wg0`
6. `sudo wg show` con peer conectado
7. Celular conectado (app WireGuard en verde) + `ping 10.10.10.1`
8. Conclusión breve: PPTP está obsoleto; WireGuard es el estándar actual

---

## 8) Si el profesor exige exactamente PPTP

En CachyOS/Arch **`pptpd` ya no es práctica recomendable** (paquete viejo/inseguro).
Puedes mencionarlo en el reporte:

> Se sustituyó PPTP por WireGuard por seguridad y soporte actual en CachyOS.

Si aun así lo intentan forzar, dilo al profesor: Android marca PPTP como **“VPN no segura”**.

---

## 9) Limpieza

```bash
sudo systemctl disable --now wg-quick@wg0
sudo rm -f /etc/wireguard/wg0.conf
# opcional:
# sudo pacman -Rns wireguard-tools
```

# Práctica 4 — Taller de Sistemas Operativos
## CachyOS con servicio moderno: nginx + systemd

Estas son instrucciones para terminal (sin página web de guía).
En vez de Apache (lo típico en guías viejas), usamos **nginx**, que en CachyOS está bien soportado y se administra con **systemd**.

---

## 0) Antes de empezar

Abre una terminal en CachyOS y actualiza el sistema:

```bash
sudo pacman -Syu
```

Anota (para el reporte):
- Distro: `cat /etc/os-release`
- Kernel: `uname -r`
- Usuario: `whoami`

---

## 1) Instalar nginx

```bash
sudo pacman -S nginx
```

Comprueba que el paquete quedó instalado:

```bash
pacman -Qi nginx
nginx -v
```

---

## 2) Arrancar y habilitar el servicio (systemd)

En distros modernas **no** uses `service apache2 start`. Usa `systemctl`:

```bash
# Recargar unidades (por si acaso)
sudo systemctl daemon-reload

# Iniciar ahora
sudo systemctl start nginx

# Habilitar al arranque
sudo systemctl enable nginx

# Ver estado (captura esto para el reporte)
systemctl status nginx
```

Debe aparecer `Active: active (running)`.

Atajo equivalente:

```bash
sudo systemctl enable --now nginx
```

---

## 3) Probar que el servicio responde

```bash
# Desde la misma máquina
curl -I http://127.0.0.1
curl http://127.0.0.1
```

También abre el navegador en:

```text
http://localhost
```

o

```text
http://127.0.0.1
```

Deberías ver la página por defecto de nginx.

Para ver tu IP local (si quieres entrar desde otra PC de la red):

```bash
ip -br a
```

Luego prueba `http://TU_IP` desde otro equipo (si el firewall lo permite).

---

## 4) Publicar tu propio contenido (recomendado para la práctica)

En Arch/CachyOS el DocumentRoot de nginx suele ser:

```text
/usr/share/nginx/html
```

Crea tu página:

```bash
sudo tee /usr/share/nginx/html/index.html >/dev/null <<'EOF'
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Práctica 4 - Taller SO</title>
</head>
<body>
  <h1>Servidor nginx en CachyOS</h1>
  <p>Práctica 4 - Servicio web moderno administrado con systemd.</p>
  <p>Alumno: TU_NOMBRE</p>
</body>
</html>
EOF
```

Recarga nginx sin cortar conexiones:

```bash
sudo systemctl reload nginx
```

Vuelve a abrir `http://localhost`.

---

## 5) Comandos de administración que suelen pedir en la práctica

```bash
# Estado
systemctl status nginx

# Detener
sudo systemctl stop nginx

# Iniciar
sudo systemctl start nginx

# Reiniciar
sudo systemctl restart nginx

# Recargar config (sin bajar el servicio)
sudo systemctl reload nginx

# ¿Está habilitado al arranque?
systemctl is-enabled nginx

# Deshabilitar al arranque
sudo systemctl disable nginx

# Volver a habilitar
sudo systemctl enable nginx
```

Logs del servicio:

```bash
journalctl -u nginx -e
journalctl -u nginx -f
```

(`-f` = seguir en vivo; sal con Ctrl+C)

Probar la configuración de nginx:

```bash
sudo nginx -t
```

---

## 6) (Opcional pero útil) Firewall

Si usas `ufw`:

```bash
sudo pacman -S ufw
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw enable
sudo ufw status
```

Si usas `firewalld`:

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

Si usas nftables a mano, abre el puerto 80/tcp según tu reglaset.

---

## 7) Extra moderno: crear TU PROPIO servicio systemd

Si la práctica pide “crear un servicio” (no solo instalar nginx), haz esto.

### 7.1 Script del servicio

```bash
mkdir -p ~/servicios
cat > ~/servicios/monitor.sh <<'EOF'
#!/bin/bash
while true; do
  echo "$(date '+%F %T') - servicio de práctica activo" >> /tmp/practica4-monitor.log
  sleep 10
done
EOF
chmod +x ~/servicios/monitor.sh
```

### 7.2 Unit file

```bash
sudo tee /etc/systemd/system/practica4-monitor.service >/dev/null <<EOF
[Unit]
Description=Monitor de Practica 4 Taller SO
After=network.target

[Service]
Type=simple
ExecStart=/home/$USER/servicios/monitor.sh
Restart=always
RestartSec=3
User=$USER

[Install]
WantedBy=multi-user.target
EOF
```

### 7.3 Activarlo

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now practica4-monitor
systemctl status practica4-monitor
tail -f /tmp/practica4-monitor.log
```

Para el reporte también captura:

```bash
systemctl cat practica4-monitor
journalctl -u practica4-monitor -n 50
```

---

## 8) Checklist de evidencias (reporte)

Toma capturas o pega salidas de:

1. `cat /etc/os-release` (CachyOS)
2. `nginx -v`
3. `systemctl status nginx` → active (running)
4. `systemctl is-enabled nginx` → enabled
5. Navegador/curl mostrando tu `index.html`
6. `journalctl -u nginx -n 20`
7. (Si hiciste el extra) `systemctl status practica4-monitor` + log en `/tmp`

---

## 9) Limpieza (si el profe lo pide al final)

```bash
sudo systemctl disable --now nginx
# opcional desinstalar:
# sudo pacman -Rns nginx

sudo systemctl disable --now practica4-monitor
sudo rm -f /etc/systemd/system/practica4-monitor.service
sudo systemctl daemon-reload
```

---

## Notas rápidas CachyOS vs guías viejas

| Guía antigua (Debian/Ubuntu) | En CachyOS (Arch) |
|---|---|
| `sudo apt install apache2` | `sudo pacman -S nginx` (o `apache` → servicio `httpd`) |
| `sudo service apache2 start` | `sudo systemctl start nginx` |
| `/var/www/html` | `/usr/share/nginx/html` |
| `apache2` | servicio moderno: `nginx` |

Si tu PDF pide explícitamente Apache, en CachyOS sería:

```bash
sudo pacman -S apache
sudo systemctl enable --now httpd
systemctl status httpd
```

Documento raíz típico de Apache en Arch/CachyOS: `/srv/http`

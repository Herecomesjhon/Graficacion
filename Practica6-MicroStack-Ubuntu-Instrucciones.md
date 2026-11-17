# Práctica 6 — Taller de Sistemas Operativos
## Implementación de nubes privadas (MicroStack / OpenStack)

**Entorno requerido por la guía:** máquina virtual con **Ubuntu**  
(No uses CachyOS para esta: MicroStack/snap OpenStack está pensado para Ubuntu.)

---

## Requisitos de la VM
- Ubuntu 22.04 o 24.04
- Ideal: **4 CPU**, **16 GB RAM**, **40+ GB disco**
- VirtualBox/VMware con virtualización anidada si puedes
- Internet en la VM

---

## Ruta A — Como el PDF (MicroStack clásico)

> Nota: MicroStack beta ya casi no se mantiene, pero es lo que pide tu guía.
> Si falla la instalación, usa la **Ruta B** (moderna) y en el reporte explica el cambio.

### 1) Actualizar
```bash
sudo apt update
sudo apt upgrade -y
```

### 2) Instalar MicroStack
```bash
sudo snap install microstack --beta
```
(Te pedirá contraseña)

### 3) Ver el snap instalado
```bash
snap list microstack
```
Captura: name, version, rev, tracking, publisher, notes.

### 4) Inicializar (nodo de control)
```bash
sudo microstack init --auto --control
```
Tarda varios minutos. Espera a que termine.

### 5) Listar imágenes
```bash
microstack.openstack image list
```
Debe aparecer **cirros** en estado **active**.

### 6) Listar flavors
```bash
microstack.openstack flavor list
```
Verás CPU, RAM, disco, etc.

### 7) Crear instancia `test`
```bash
microstack launch cirros --name test
```
o, según versión:
```bash
microstack launch cirros -n test
```
Guarda la IP / datos SSH que muestre.

### 8) Obtener contraseña del panel
```bash
sudo snap get microstack config.credentials.keystone-password
```

### 9) Entrar al panel web
En el navegador de Ubuntu abre (como en el PDF):

```text
https://10.20.20.1
```
o la IP que te haya indicado la salida.

- **User:** `admin`
- **Password:** la del paso 8

En **Instances** debe aparecer la instancia **test**.

---

## Ruta B — Moderna (si MicroStack falla): Canonical OpenStack / Sunbeam

Equivalente actual al MicroStack del PDF.

### 1) Instalar
```bash
sudo apt update
sudo snap install openstack
```

### 2) Preparar nodo
```bash
sunbeam prepare-node-script --bootstrap | bash -x
newgrp snap_daemon
```

### 3) Bootstrap de la nube
```bash
sunbeam cluster bootstrap --accept-defaults --role control,compute,storage
```
(Tarda bastante)

### 4) Configurar
```bash
sunbeam configure --accept-defaults --openrc demo-openrc
```

### 5) Lanzar instancia
```bash
sunbeam launch ubuntu --name test
```

### 6) Dashboard
```bash
sunbeam dashboard-url
```
Abre la URL, inicia sesión y verifica la instancia.

---

## Capturas para el reporte (checklist)

- [ ] `sudo apt update`
- [ ] Instalación (`snap install ...`)
- [ ] `snap list ...`
- [ ] Inicialización / bootstrap
- [ ] `image list` (cirros u otra imagen activa)
- [ ] `flavor list`
- [ ] Instancia `test` creada
- [ ] Contraseña / acceso al dashboard
- [ ] Pantalla de OpenStack con la instancia visible

---

## Equivalencias PDF → moderno

| PDF (MicroStack) | Moderno (Sunbeam) |
|---|---|
| `snap install microstack --beta` | `snap install openstack` |
| `sudo microstack init --auto --control` | `sunbeam cluster bootstrap ...` |
| `microstack.openstack image list` | `openstack image list` (con openrc) |
| `microstack launch cirros -n test` | `sunbeam launch ubuntu --name test` |
| `https://10.20.20.1` | `sunbeam dashboard-url` |

---

## Conclusión corta (para el reporte)

Se implementó una nube privada basada en OpenStack, permitiendo desplegar imágenes, flavors e instancias virtuales dentro de una infraestructura controlada por la organización. Con ello se comprobó el modelo de nube privada frente a una nube pública, destacando control, administración local de recursos y acceso mediante panel web.

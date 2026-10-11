# Hecho por Cristian Rafael López Rodríguez

import csv
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI(
    title="Sistema Asilo Cabeza de Algodón",
    description="Portal Principal, Autenticación y Módulo de Registro de Pacientes",
    version="1.0.0"
)

expediente_pacientes = []

class PacienteRegistro(BaseModel):
    nombre_completo: str
    edad: int
    psicopatologia: str
    familiar_responsable: str
    telefono: str

@app.get("/", response_class=HTMLResponse)
def pagina_inicio():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Asilo Cabeza de Algodón - Inicio</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: #f4f7f6; color: #333; }
            header { background-color: #2c3e50; color: white; padding: 20px 50px; display: flex; justify-content: space-between; align-items: center; }
            header h1 { margin: 0; font-size: 24px; }
            .btn-header { background-color: #27ae60; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; font-weight: bold; }
            .hero { background: linear-gradient(rgba(44, 62, 80, 0.7), rgba(44, 62, 80, 0.7)), url('https://images.unsplash.com/photo-1576765608535-5f04d1e3f289?auto=format&fit=crop&w=1200&q=80'); background-size: cover; background-position: center; color: white; text-align: center; padding: 80px 20px; }
            .hero h2 { font-size: 38px; margin-bottom: 10px; }
            .hero p { font-size: 18px; max-width: 600px; margin: 0 auto 30px auto; }
            .btn-hero { background-color: #e74c3c; color: white; padding: 15px 30px; border-radius: 6px; text-decoration: none; font-size: 18px; font-weight: bold; transition: background 0.3s; }
            .btn-hero:hover { background-color: #c0392b; }
            .services { padding: 50px 20px; max-width: 1000px; margin: auto; text-align: center; }
            .grid { display: flex; gap: 20px; justify-content: center; margin-top: 30px; flex-wrap: wrap; }
            .card { background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); width: 280px; text-align: left; }
            .card h3 { color: #2c3e50; margin-top: 0; }
            footer { background-color: #1a252f; color: #bdc3c7; text-align: center; padding: 20px; margin-top: 40px; font-size: 14px; }
        </style>
    </head>
    <body>

        <header>
            <h1> Asilo Cabeza de Algodón </h1>
            <a href="/login" class="btn-header">Iniciar Sesión</a>
        </header>

        <section class="hero">
            <h2>Cuidado, Dignidad y Amory para Nuestros Mayores</h2>
            <p>Ofrecemos atención médica especializada, actividades recreativas y la mejor estancia para el bienestar de sus seres queridos.</p>
            <a href="/login" class="btn-hero"> Registrar Nuevo Adulto Mayor</a>
        </section>

        <section class="services">
            <h2>Nuestros Servicios Integrales</h2>
            <div class="grid">
                <div class="card">
                    <h3> Atención Médica</h3>
                    <p>Monitoreo de signos vitales, administración de medicamentos y chequeos geriatrícos permanentes.</p>
                </div>
                <div class="card">
                    <h3> Actividades Recreativas</h3>
                    <p>Talleres cognitivos, terapia ocupacional, música y convivencias diseñadas para el adulto mayor.</p>
                </div>
                <div class="card">
                    <h3> Nutrición Personalizada</h3>
                    <p>Planes alimenticios balanceados adaptados a los requerimientos de cada paciente.</p>
                </div>
            </div>
        </section>

        <footer>
            &copy; 2026 Asilo Cabeza de Algodón - Sistema de Gestión de Pacientes
        </footer>

    </body>
    </html>
    """

@app.get("/login", response_class=HTMLResponse)
def pagina_login():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Iniciar Sesión - Cabeza de Algodón</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f8f9fa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .login-card { background: white; padding: 35px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 350px; text-align: center; }
            .login-card h2 { color: #2c3e50; margin-bottom: 8px; }
            .login-card p { color: #7f8c8d; font-size: 14px; margin-bottom: 25px; }
            .form-group { margin-bottom: 18px; text-align: left; }
            label { display: block; font-weight: 600; color: #34495e; margin-bottom: 6px; font-size: 14px; }
            input { width: 100%; padding: 10px; border: 1.5px solid #bdc3c7; border-radius: 6px; box-sizing: border-box; }
            button { width: 100%; padding: 12px; background-color: #3498db; color: white; border: none; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; margin-top: 10px; }
            button:hover { background-color: #2980b9; }
            .back-link { display: block; margin-top: 20px; color: #7f8c8d; text-decoration: none; font-size: 13px; }
        </style>
    </head>
    <body>

        <div class="login-card">
            <h2>Acceso al Sistema</h2>
            <p>Ingrese sus credenciales para registrar un paciente</p>

            <form action="/login" method="post">
                <div class="form-group">
                    <label>Usuario / Correo</label>
                    <input type="text" name="usuario" required placeholder="admin@asilo.org">
                </div>
                <div class="form-group">
                    <label>Contraseña</label>
                    <input type="password" name="password" required placeholder="••••••••">
                </div>
                <button type="submit">Ingresar al Formulario</button>
            </form>

            <a href="/" class="back-link">← Volver al inicio</a>
        </div>

    </body>
    </html>
    """

@app.post("/login")
def procesar_login():
    return RedirectResponse(url="/registro-despues", status_code=303)

@app.get("/registro-despues", response_class=HTMLResponse)
def vista_registro_despues():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Registro de Pacientes - Asilo Cabeza de Algodón</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f8f9fa; margin: 0; padding: 40px; }
            .container { max-width: 550px; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); margin: auto; }
            .header-bar { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding-bottom: 15px; margin-bottom: 20px; }
            h2 { color: #2c3e50; margin: 0; font-size: 20px; }
            .btn-logout { color: #e74c3c; text-decoration: none; font-size: 14px; font-weight: bold; }
            p.sub { text-align: center; color: #7f8c8d; font-size: 14px; margin-bottom: 25px; }
            .form-group { margin-bottom: 18px; }
            label { display: block; font-weight: 600; color: #34495e; margin-bottom: 6px; font-size: 14px; }
            .req { color: #e74c3c; font-weight: bold; }
            input { width: 100%; padding: 10px; border: 1.5px solid #bdc3c7; border-radius: 6px; box-sizing: border-box; font-size: 14px; }
            input:focus { border-color: #3498db; outline: none; }
            input:required:valid { border-color: #2ecc71; }
            button { width: 100%; padding: 12px; background-color: #27ae60; color: white; border: none; border-radius: 6px; font-weight: bold; font-size: 16px; cursor: pointer; margin-top: 10px; }
            button:hover { background-color: #219150; }
            .btn-download { background-color: #2c3e50; }
            .btn-download:hover { background-color: #1a252f; }
            .alert-toast { display: none; background-color: #d4edda; border-left: 5px solid #28a745; color: #155724; padding: 12px; border-radius: 4px; margin-bottom: 20px; font-size: 14px; }
        </style>
    </head>
    <body>

    <div class="container">
        <div class="header-bar">
            <h2>Registro de Nuevo Paciente</h2>
            <a href="/" class="btn-logout">Cerrar Sesión</a>
        </div>
        
        <p class="sub">Complete los datos obligatorios marcados con (<span class="req">*</span>)</p>
        
        <div id="toast" class="alert-toast">
            <strong>¡Éxito!</strong> Paciente registrado e integrado al expediente general.
        </div>

        <form id="formRegistro">
            <div class="form-group">
                <label>Nombre Completo del Paciente <span class="req">*</span></label>
                <input type="text" id="nom" required placeholder="Ej. Juan Carlos Pérez">
            </div>

            <div class="form-group">
                <label>Edad (Años) <span class="req">*</span></label>
                <input type="number" id="ed" min="60" required placeholder="Ej. 78">
            </div>

            <div class="form-group">
                <label>Diagnóstico / Psicopatología <span class="req">*</span></label>
                <input type="text" id="diag" required placeholder="Ej. Demencia Senil / Hipertensión">
            </div>

            <div class="form-group">
                <label>Familiar Responsable <span class="req">*</span></label>
                <input type="text" id="fam" required placeholder="Ej. Ana Pérez (Hija)">
            </div>

            <div class="form-group">
                <label>Teléfono de Urgencias <span class="req">*</span></label>
                <input type="tel" id="tel" required placeholder="Ej. 5555-4321">
            </div>

            <button type="submit">Guardar en Expediente</button>
        </form>

        <a href="/api/v1/pacientes/descargar-expediente" style="text-decoration: none;">
            <button type="button" class="btn-download" style="margin-top: 15px;">
                Descargar Expediente (CSV)
            </button>
        </a>
    </div>

    <script>
        document.getElementById('formRegistro').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const payload = {
                nombre_completo: document.getElementById('nom').value,
                edad: parseInt(document.getElementById('ed').value),
                psicopatologia: document.getElementById('diag').value,
                familiar_responsable: document.getElementById('fam').value,
                telefono: document.getElementById('tel').value
            };

            const response = await fetch('/api/v1/pacientes/guardar', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            if (response.ok) {
                const toast = document.getElementById('toast');
                toast.style.display = 'block';
                document.getElementById('formRegistro').reset();
                setTimeout(() => { toast.style.display = 'none'; }, 4000);
            }
        });
    </script>
    </body>
    </html>
    """

@app.post("/api/v1/pacientes/guardar")
def guardar_en_expediente(paciente: PacienteRegistro):
    expediente_pacientes.append(paciente.dict())
    print(f"[EXPEDIENTE] Nuevo paciente guardado: {paciente.nombre_completo}")
    return {"status": "éxito", "total_pacientes": len(expediente_pacientes)}

@app.get("/api/v1/pacientes/descargar-expediente")
def descargar_expediente_csv():
    nombre_archivo = "expediente_pacientes.csv"
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre Completo", "Edad", "Psicopatología", "Familiar Responsable", "Teléfono"])
        for p in expediente_pacientes:
            writer.writerow([
                p.get("nombre_completo"),
                p.get("edad"),
                p.get("psicopatologia"),
                p.get("familiar_responsable"),
                p.get("telefono")
            ])
    return FileResponse(path=nombre_archivo, filename="Expediente_Cabeza_De_Algodon.csv", media_type="text/csv")
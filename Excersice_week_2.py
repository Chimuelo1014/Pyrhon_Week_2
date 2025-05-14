import datetime # para trabajar con fechas y horas

# Constantes
PRECIOS_BASE = {
    "nacional": {"destino": "Bogotá → Medellín", "precio": 230_000},
    "internacional": {"destino": "Bogotá → España", "precio": 4_200_000}
}

COSTOS_EQUIPAJE = [
    (20, 50_000),
    (30, 70_000),
    (50, 110_000)
]

MAX_EQUIPAJE_MANO = 13
MAX_EQUIPAJE_PRINCIPAL = 50

# Variables globales
reservas = []
contador_id = 1

# Funciones
def generar_id():
    global contador_id
    id_generado = f"COMP{contador_id:04}"
    contador_id += 1
    return id_generado

def obtener_costo_equipaje(peso):
    for limite, costo in COSTOS_EQUIPAJE:
        if peso <= limite:
            return costo
    return None  # Si supera 50kg

def registrar_reserva():
    print("\n--- Nueva Reserva ---")
    nombre = input("Nombre del pasajero: ").strip()
    tipo_viaje = input("Tipo de viaje (nacional/internacional): ").strip().lower()

    if tipo_viaje not in PRECIOS_BASE:
        print("❌ Tipo de viaje inválido.")
        return

    try:
        peso_principal = float(input("Peso del equipaje principal (kg): "))
        equipaje_mano = input("¿Lleva equipaje de mano? (sí/no): ").strip().lower()
        peso_mano = 0
        if equipaje_mano == "sí":
            peso_mano = float(input("Peso del equipaje de mano (kg): "))
        fecha = input("Fecha del viaje (YYYY-MM-DD): ").strip()
        datetime.datetime.strptime(fecha, "%Y-%m-%d")  # Validar formato
    except ValueError:
        print("❌ Entrada inválida.")
        return

    estado_principal = "Admitido"
    estado_mano = "Sin equipaje"

    costo_base = PRECIOS_BASE[tipo_viaje]["precio"]
    destino = PRECIOS_BASE[tipo_viaje]["destino"]

    costo_equipaje = obtener_costo_equipaje(peso_principal)
    if costo_equipaje is None:
        estado_principal = "No admitido"
        costo_equipaje = 0

    if equipaje_mano == "sí":
        estado_mano = "Admitido" if peso_mano <= MAX_EQUIPAJE_MANO else "Rechazado"

    total = costo_base + costo_equipaje if estado_principal != "No admitido" else costo_base

    reserva = {
        "id": generar_id(),
        "nombre": nombre,
        "destino": destino,
        "tipo": tipo_viaje,
        "fecha": fecha,
        "estado_principal": estado_principal,
        "estado_mano": estado_mano,
        "total": total
    }

    reservas.append(reserva)

    print("\n✅ Reserva registrada exitosamente:")
    print_resumen(reserva)

def print_resumen(reserva):
    print(f"ID de compra: {reserva['id']}")
    print(f"Nombre: {reserva['nombre']}")
    print(f"Destino: {reserva['destino']}")
    print(f"Fecha del viaje: {reserva['fecha']}")
    print(f"Estado equipaje principal: {reserva['estado_principal']}")
    print(f"Estado equipaje de mano: {reserva['estado_mano']}")
    print(f"Costo total del viaje: ${reserva['total']:,}")

# Funciones administrativas
def reporte_admin():
    while True:
        print("\n📊 Reporte Administrativo")
        print("1. Total recaudado en todas las compras")
        print("2. Total recaudado para una fecha específica")
        print("3. Número total de pasajeros")
        print("4. Pasajeros por tipo de viaje")
        print("5. Consultar reserva por ID")
        print("6. Volver")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            total = sum(r["total"] for r in reservas)
            print(f"💰 Total recaudado: ${total:,}")
        elif opcion == "2":
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
            total = sum(r["total"] for r in reservas if r["fecha"] == fecha)
            print(f"💰 Total para {fecha}: ${total:,}")
        elif opcion == "3":
            print(f"👥 Total de pasajeros: {len(reservas)}")
        elif opcion == "4":
            nacionales = sum(1 for r in reservas if r["tipo"] == "nacional")
            internacionales = sum(1 for r in reservas if r["tipo"] == "internacional")
            print(f"✈️ Nacionales: {nacionales}")
            print(f"🌍 Internacionales: {internacionales}")
        elif opcion == "5":
            id_buscar = input("Ingrese ID de compra (ej. COMP0001): ").strip()
            reserva = next((r for r in reservas if r["id"] == id_buscar), None)
            if reserva:
                print_resumen(reserva)
            else:
                print("❌ No se encontró la reserva.")
        elif opcion == "6":
            break
        else:
            print("❌ Opción inválida.")

# Menú principal
def main():
    while True:
        print("\n🚀 Sistema de Gestión de Equipaje Aéreo")
        print("1. Registrar nueva reserva")
        print("2. Reporte administrativo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_reserva()
        elif opcion == "2":
            reporte_admin()
        elif opcion == "3":
            print("👋 Saliendo del sistema.")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()

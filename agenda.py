# practica iv python
# usando lo aprendido hasta ahora:
# hacer un programa con acceso a base de datos
# que sirva como una agenda telefónica.
# debe tener un menu que permita:
# 1 – agregar nuevo contacto
# 2 – listar todos los contactos
# 3 – buscar contactos por nombre o numero de teléfono
# 4 – actualizar un contacto
# 5 – eliminar un contacto
# 6 – salir
# al agregar un nuevo contacto, debe validar que el contacto no exista previamente. si existe debe dar un
# mensaje notificando al usuario.
# al terminar de agregar un contacto debe preguntar si desea agregar otro.


# Agregando soporte para SQLite3 y funciones de sistema operativo
import sqlite3
from os import system, name
from time import sleep


def LimpiarPantalla():
    """
    Funcion para limpiar pantalla
    """
    if (name == "nt"):
        system("cls")
    else:
        system("clear")


# Definicion creacion/conexion a DB y definiendo cursor
Conexion = sqlite3.connect("agenda.db")
Cursor = Conexion.cursor()


# Definicion creacion de la tabla agenda
Cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS agenda(
        codigo integer primary key autoincrement not null,
        nombre text not null,
        apellido text not null,
        telefono text not null,
        email text
    );
    """
)


# Salvando los cambios a la DB
Conexion.commit()


# 1 – agregar nuevo contacto
def AgregarContacto():
    """
    Funcion para agregar contactos a base de datos SQLite3
    """
    AgregarOtroContacto = ""
    Continuar = True
    Conexion = sqlite3.connect("agenda.db")
    Cursor = Conexion.cursor()
    while (Continuar):
        LimpiarPantalla()
        # Capturando datos a agregar
        Nombre = input("Por favor ingrese el nombre del contacto a agregar: ")
        Apellido = input(
            "Por favor ingrese el apellido del contacto a agregar: ")
        Telefono = input(
            "Por favor ingrese el telefono del contacto a agregar: ")
        Email = input("Por favor ingrese el email del contacto a agregar: ")
        Cursor.execute('INSERT INTO agenda(nombre, apellido, telefono, email) VALUES("' +
                       (Nombre)+'", "'+(Apellido)+'", "'+(Telefono)+'", "'+(Email)+'");')
        Conexion.commit()
        print()
        print("Contacto ingresado satisfactoriamente")
        print()

        # Confirmacion para agregar otro usuario y control de errores
        AgregarOtroContacto = input(
            "Desea agregar otro contacto? Presione 'S' para continuar, 'N' para salir: ")
        if (AgregarOtroContacto == "S" or AgregarOtroContacto == "s"):
            Continuar = True
        elif (AgregarOtroContacto == "N" or AgregarOtroContacto == "n"):
            print()
            print("Salida, no mas contactos a agregar")
            print()
            Continuar = False
        else:
            print()
            print("Opcion invalida, por favor intente nuevamente")


# 2 – listar todos los contactos
def ListarTodosLosContactos():
    Conexion = sqlite3.connect("agenda.db")
    Cursor = Conexion.cursor()
    LimpiarPantalla()
    Cursor.execute("SELECT * FROM agenda;")
    TodosLosRegistros = Cursor.fetchall()
    for Registro in TodosLosRegistros:
        print("ID:", Registro[0], "\t", "Nombre:", Registro[1], "\t",
              "Apellido:", Registro[2], "\t", "Telefono:", Registro[3], "\t", "Email:\n", Registro[4])
    print()
    input("Presione cualquier tecla para volver al menu principal: ")
    print()

# 3 – buscar contactos por nombre o numero de teléfono
def BuscarPorNombreOTelefono():
    """
    Funcion para buscar contactos por nombre o numero de telefono
    """
    Conexion = sqlite3.connect("agenda.db")
    Cursor = Conexion.cursor()
    LimpiarPantalla()
    Busqueda = input(
        "Por favor ingrese 'N' para buscar por nombre o 'T' para buscar por telefono: ")
    if (Busqueda == "N" or Busqueda == "n"):
        BuscarNombre = input(
            "Por favor ingrese el nombre del contacto que desea buscar: ")
        Cursor.execute(
            "SELECT * FROM agenda WHERE nombre=?", (BuscarNombre,))
        TodosLosRegistros = Cursor.fetchall()
        for Registro in TodosLosRegistros:
            print("ID:", Registro[0], "\t", "Nombre:", Registro[1], "\t",
                  "Apellido:", Registro[2], "\t", "Telefono:", Registro[3], "\t", "Email:\n", Registro[4])
        print()
        input("Presione cualquier tecla para volver al menu principal: ")
        print()
    elif (Busqueda == "T" or Busqueda == "t"):
        BuscarTelefono = input(
            "Por favor ingrese el telefono del contacto que desea buscar: ")
        Cursor.execute(
            "SELECT * FROM agenda WHERE telefono=?", (BuscarTelefono,))
        TodosLosRegistros = Cursor.fetchall()
        for Registro in TodosLosRegistros:
            print("ID:", Registro[0], "\t", "Nombre:", Registro[1], "\t",
                  "Apellido:", Registro[2], "\t", "Telefono:", Registro[3], "\t", "Email:\n", Registro[4])
        print()
        input("Presione cualquier tecla para volver al menu principal: ")
        print()
    else:
        print()
        print("Opcion invalida, por favor intente nuevamente")


# 4 – actualizar un contacto
def ActualizarUnContacto():
    """
    Funcion para actualizar un contacto
    """
    Conexion = sqlite3.connect("agenda.db")
    Cursor = Conexion.cursor()
    LimpiarPantalla()
    BuscarID = int(input("Por favor introduzca el ID de usuario a editar: "))
    ActualizarNombre = input("Por favor introduzca el nuevo nombre: ")
    ActualizarApellido = input("Por favor introduzca el nuevo apellido: ")
    ActualizarTelefono = input("Por favor introduzca el nuevo telefono: ")
    ActualizarEmail = input("Por favor introduzca el nuevo email: ")
    SQLQuery = """UPDATE agenda
    SET nombre=?, apellido=?, telefono=?, email=?
    WHERE codigo=?
    """
    Valores = (ActualizarNombre, ActualizarApellido,
               ActualizarTelefono, ActualizarEmail, BuscarID)
    Cursor.execute(SQLQuery, Valores)
    print()
    print("Contacto actulizado satisfactoriamente")
    print()
    input("Presione cualquier tecla para volver al menu principal: ")
    print()
    Conexion.commit()


# 5 – eliminar un contacto
def EliminarUnContacto():
    """
    Funcion para eliminar un contacto
    """
    LimpiarPantalla()
    Conexion = sqlite3.connect("agenda.db")
    Cursor = Conexion.cursor()
    print()
    print("Para borrar un usuario es necesario saber el ID del usuario, de no conocer el ID de usuario")
    print("Por favor vuelva al menu principal y elija la opcion '2.- Listar todos los contactos'")
    print("Para ver todos los usuarios y sus IDs.-")
    print()
    BuscarID = input(
        "Por favor introduzca el ID del usuario que desea eliminar: ")
    SeguroEliminar = input(
        "Esta seguro que sea eliminar este usuario, escriba 'S' para Si, 'N' para cancelar: ")
    if (SeguroEliminar == "S" or SeguroEliminar == "s"):
        SQLQuery = """DELETE FROM agenda
        WHERE codigo=?
        """
        Valores = (BuscarID)
        Cursor.execute(SQLQuery, Valores)
        print()
        print("Contacto eliminado satisfactoriamente")
        Conexion.commit()
        print()
        input("Presione cualquier tecla para volver al menu principal: ")
        print()
    elif (SeguroEliminar == "N" or SeguroEliminar == "n"):
        print()
        print("Eliminacion cancelada, no se ha borrado ningun contacto")
        print()
        input("Presione cualquier tecla para volver al menu principal: ")
        print()
    else:
        print("Opcion invalida, por favor intente nuevamente")
        print()
        input("Presione cualquier tecla para volver al menu principal: ")
        print()


# 6 – salir
def Salir():
    """
    Funcion para guardar todos los cambios y cerrar la conexion
    """
    Conexion.commit()
    Conexion.close()
    print()
    print("Hasta luego!")
    print()


# Menu principal
Continuar = True
while (Continuar):
    LimpiarPantalla()
    print("#"*50)
    print()
    print("-------.Bienvenido a tu agenda telefonica .-------")
    print("-------------. Beta version 0.0.1 .---------------")
    print()
    print("1.- Agregar nuevo contacto")
    print("2.- Listar todos los contactos")
    print("3.- Buscar contacto por nombre o numero de telefono")
    print("4.- Actualizar un contacto")
    print("5.- Eliminar un contacto")
    print("6.- Salir")
    print()
    print("#"*50)
    print()
    Opcion = int(input("Ingrese el numero de la opcion deseada: "))

    if (Opcion == 1):
        AgregarContacto()
    elif (Opcion == 2):
        ListarTodosLosContactos()
    elif (Opcion == 3):
        BuscarPorNombreOTelefono()
    elif (Opcion == 4):
        ActualizarUnContacto()
    elif (Opcion == 5):
        EliminarUnContacto()
    elif (Opcion == 6):
        Salir()
        Continuar = False
    else:
        print("Opcion invalida, por favor intente nuevamente")
        print()
        input("Presione cualquier tecla para volver al menu principal: ")
        print()
    
        


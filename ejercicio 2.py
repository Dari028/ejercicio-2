from datetime import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        self.__tipo=""
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
 
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
    def ver_tipo(self):
        return self.__tipo
    
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
   
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    def asignartipo(self,hf):
        self.__tipo=hf
    
class sistemaV:
    def __init__(self):
        self.__dict_felinos = {}
        self.__dict_caninos = {}
    
    def verificarExiste(self,historia):
        for m in self.__dict_caninos:
            if historia == m.verHistoria():
                return True
        for m in self.__dict_felinos:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        j= len(self.__dict_felinos) 
        a=len(self.__dict_caninos) 
        pi=int(a)+int(j)
        return pi
    
    def ingresarMascota(self, mascota, tipo, historia):
        if tipo == 'canino':
            self.__dict_caninos[historia] = mascota
        elif tipo == 'felino':
            self.__dict_felinos[historia] = mascota
   

    def verFechaIngreso(self, historia, mascota):
        if isinstance(mascota, Mascota):
            if mascota.ver_tipo() == 'canino':
                fecha_canino = self.__dict_caninos.get(historia, None)
                if fecha_canino is not None:
                    return mascota.verFecha()
            elif mascota.ver_tipo()== 'felino':
                fecha_felino = self.__dict_felinos.get(historia, None)
                if fecha_felino is not None:
                    return mascota.verFecha()
        return None


    def verMedicamento(self,historia,Mascota):
        if historia in self.__dict_caninos:
            if self.__dict_caninos[historia] == Mascota.verHistoria():
                return Mascota.verLista_Medicamentos()

        # Verificar si la historia está en el diccionario de felinos
        if historia in self.__dict_felinos:
            if self.__dict_felinos[historia] == Mascota.verHistoria():
                return Mascota.verLista_Medicamentos()

        return None


    
    def eliminarMascota(self, historia,Mascota):
       
        for historia in self.__dict_caninos():
            if historia == Mascota.verHistoria():
                del self.__dict_caninos[Mascota.verHistoria]
                return True  

       
        for historia in self.__dict_felinos.items():
            if historia == Mascota.verHistoria():
                del self.__dict_felinos[Mascota.verHistoria]
                return True  

        return False  
    def eliminar_medicamento(self, historia_mascota, nombre_medicamento):
        mascota = self.__dict_caninos.get(historia_mascota, None)
        if mascota is None:
            mascota = self.__dict_felinos.get(historia_mascota, None)
            if mascota is None:
               
                return False

        lista_medicamentos = mascota.verLista_Medicamentos()
        if lista_medicamentos:
            for medicamento in lista_medicamentos:
                if medicamento.verNombre() == nombre_medicamento:
                    lista_medicamentos.remove(medicamento)
                    print(f"Medicamento '{nombre_medicamento}' eliminado correctamente.")
                    return True
            
        else:
            return False
 

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- eliminar medicamento 
                       \n7.  salir
                       \nUsted ingresó la opción:
                       ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            mas= Mascota()
            histori=int(input("Ingrese la historia clínica de la mascota: "))
            historia=str(histori)
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                peso=float(input("Ingrese el peso de la mascota: "))
                while True:
                    fecha_str = input("Por favor, ingresa una fecha en el formato dd/mm/aa: ")
                    try:
                        fechaformat = datetime.strptime(fecha_str, "%d/%m/%y")
                        fecha=fechaformat.strftime("%d/%m/%y")
                        
                        break
                    except ValueError:
                        print("Formato de fecha incorrecto. Por favor, intenta de nuevo.")
        
                
                
                while True:
                    tip=input("ingrese el tipo de animal 1- canino  2-felino ")
                    if tip=="1":
                        tipo="canino"
                        break
                    elif tip=="2":
                        tipo="felino"
                        break
                    else:
                        print("opcion  no valida")
                        continue
                lista_med=[]
                lista_medi=[]
                nm=int(input("Ingrese cantidad de medicamentos: "))
                medi=mas.verLista_Medicamentos()
                for i in range(0,nm):
                    
                    while True:
                        nombre_medicamento = input("Ingrese el nombre del medicamento: ")
                        if nombre_medicamento in lista_medi:  
                            print("Este medicamento ya está en la lista.")
                            
                        else:
                            break
                    
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamento)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                    j=medicamento.verNombre()
                    lista_medi.append(j)
                    print(lista_medi)

                
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignartipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                mas.asignartipo(tipo)
                servicio_hospitalario.ingresarMascota(mas,tipo,historia)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            mas=Mascota()
            qi = int(input("Ingrese la historia clínica de la mascota: "))
            q=str(qi)
            fecha = servicio_hospitalario.verFechaIngreso(q,mas)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            mas=Mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q,mas) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            
            h=int(input("ingresa la historia de la mascota"))
            meddd=input("ingresa el nombre del medicamento")
            sistem=sistemaV()
            j=sistem.eliminar_medicamento(h,meddd)
            print(j)
        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")
            print("ttt")

if __name__=='__main__':
    main()





            

                


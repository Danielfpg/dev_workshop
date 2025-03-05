class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        lista_invertida=[]
        i = len(lista) -1
        while i>=0:
            lista_invertida.append(lista[i])
            i-=1
        
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i]==elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        listaNoDuplicada=[]
        Elementos=[]
    
        for elemento in lista:
            if not any(elemento is x for x in Elementos):
                listaNoDuplicada.append(elemento)
                Elementos.append(elemento)
        return listaNoDuplicada

    def merge_ordenado(self, lista1, lista2):
        i,j=0,0
        lista=[]
        while i < len(lista1) and j < len(lista2):
            if lista1[i]< lista2[j]:
                lista.append(lista1[i])
                i+=1
            else:
                lista.append(lista2[j])
                j+=1

        while i< len(lista1):
            lista.append(lista1[i])
            i+=1

        while j < len(lista2):
            lista.append(lista2[j])
            j += 1

        return lista
    def rotar_lista(self, lista, k):
        if not lista:
            return lista
        
        n=len(lista)
        k= k % n
        
       
        return lista[-k:]+lista[:-k]

    def encuentra_numero_faltante(self, lista):
        n= len(lista)+1
        suma=n*(n+1)//2
        sumaActual=sum(lista)
        return suma-sumaActual
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        
        pila = []  
        def push(elemento):
                pila.append(elemento)

        def pop():
                if not is_empty():
                    return pila.pop()
                return None 
        def peek():
                if not is_empty():
                    return pila[-1]
                return None  

        def is_empty():
                return len(pila) == 0
        
        return {"push": push, "pop": pop, "peek": peek, "is_empty": is_empty}  

    def implementar_cola(self):
        cola = []  

        def enqueue(elemento):
            cola.append(elemento)  

        def dequeue():
            if not is_empty():
                return cola(0)  
            return None  

        def peek():
            if not is_empty():
                return cola[0]  
            return None

        def is_empty():
            return len(cola) == 0 

        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty}
        
    def matriz_transpuesta(self, matriz):
        filas= len(matriz)
        columnas=len(matriz[0] if filas > 0 else 0)

        transpuesta=[[0]* filas for i in range(columnas)]

        for i in range(filas):
            for j in range(columnas):
                transpuesta[j][i]=matriz[i][j]
        return transpuesta
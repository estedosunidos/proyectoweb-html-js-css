class carrocompra:
    
    def __init__(self,request):
        self.request = request
        self.seccion=self.seccion.request
        carro=self.seccion.get("carro")
        if not carro:
            carro=self.seccion["carro"]={}
        #else:
        carro=self.carro
    #Agregar producto al carro
    def agregar(self,producto):
        if( str(producto.id) not in self.carro.keys()):
            self.producto.idcarro[producto.id]={
                "" : producto.id,
                "nombre" : producto.nombre,
                "cantidad" : 1,
                "precio": producto.precio,
                "imagen" : producto.imagen.url
                
            }
        else:
            for key,value in self.carro.items():
                if key ==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carro()
    # Guarda los producto  
    def guardar_carro(self):
        self.seccion["carro"]=self.carro 
        self.seccion.modified=True
     #eliminar los producto en el carro   
    def eliminar(self,producto):
           producto.id=str(producto.id)
           if producto.id==str(producto.id):
               del self.carro[producto.id]
               self.guardar_carro()
     #resta los proctuco en el carro          
    def resta_producto(self,producto):
        for key,value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]+1
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()
    #vacia todo el carro
    def limpiar_carro(self):
        self.seccion["carro"]={}
        self.seccion.modified=True

        
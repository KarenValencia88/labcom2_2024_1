
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
        self, 
        name = 'PROMEDIOS_TIEMPO',
        in_sig =[np.float32],
        out_sig=[np.float32, np.float32, np.float32, np.float32, np.float32]
        )
        self.acum_anterior =0
        self.Ntotales =0
        self.acum_anterior1=0
        self.acum_anterior2=0

        
    def work(self, input_items, output_items): 
        x=input_items[0]        #señal de entrada 
        y0=output_items[0]      #promedio 
        y1=output_items[1]      #media cuadratica 
        y2=output_items[2]      #RMS
        y3=output_items[3]      #potencia promedio 
        y4=output_items[4]      #desviacion estandar 
        
        
        #CALCULANDO EL PROMEDIO O MEDIA 
        N=len(x)
        self.Ntotales=self.Ntotales + N #guarda la longitud del vectro de entrada 
        acumulador= self.acum_anterior + np.cumsum(x) #calcula la suma de los elementos del vector 
        self.acum_anterior=acumulador[N-1] #PARA QUE HACE ESA COPIA ?
        y0[:]=(acumulador/self.Ntotales) #NO SERIA acum_anterior ?
        
        #CALCULANDO LA MEDIA CUADRATICA
        xp=np.multiply(x,x)
        acumulador1=self.acum_anterior1 + np.cumsum(xp)
        self.acum_anterior1=acumulador1[N-1]
        y1[:]=acumulador1/self.Ntotales
        
        #CALCULANDO EL VALOR RMS 
        y2[:]=np.sqrt(y1)
        
        #CALCULANDO LA POTENCIA PROMEDIO 
        y3[:]=np.multiply(y2,y2)
        
        #CALCULANDO LA DESVIACION ESTANDAR 
        xd=np.multiply(x-y0,x-y0)
        acumulador2=self.acum_anterior2 + np.cumsum(xd)
        self.acum_anterior2=acumulador2[N-1]
        y4[:]=np.sqrt(acumulador2/self.Ntotales)
        
        return len(y0)

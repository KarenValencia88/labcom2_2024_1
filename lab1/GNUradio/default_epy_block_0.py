
#BLOQUE ACUMULADOR

import numpy as np 
from gnuradio import gr


class blck(gr.sync_block):
    
    def __init__(self):
        gr.sync_block.__init__(
            self ,
            name = 'ACUMULADOR',  #NOMBRE DEL BLOQUE 
            in_sig=[np.float32],  #TIPO DE DATO DE LAS SALIDAS 
            out_sig=[np.float32]  #TIPO DE DATO DE LAS ENTRADAS
            )
            
    def work(self, input_items, output_items):
        x=input_items[0] #ASIGANCION DE LA ENTRADA
        y=output_items[0] #ASIGANCION DE LA SALIDA 
        
        y0[:]=np.cumsum(X) #SUMA ACUMULADA DE CADA UNO DE LOS ELEMENTOS DE LA ENTRADA 
        
        return len(y0)  #RETORNA EL VALOR DE LA SALIDA
        
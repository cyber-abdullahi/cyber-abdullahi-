# A simple App that fills as empty drum to 25 litres.The drum will be filled at 5 litre increments every 1 second until it fills up.
 
import time

drum = 0 

while drum < 25:  
    start_time = time.time
    print(f"Drum contains {drum} litres")
    drum = drum + 5
    time.sleep(1)
    end_time =time.time()
    print(f"Drum is full. volume: {drum}.\n Time of completion{end_time}")
    

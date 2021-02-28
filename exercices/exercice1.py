def moyenne(liste):
    for i in range (len(liste)):
        if i == 0:
            result = liste[i]
        else:
            result = result + liste [i]
        
    moyene_des_notes = result / len (liste)
    return moyene_des_notes
    

package com.example.equipo_adsi.virtualkey1;

/**
 * Created by Equipo-ADSI on 01/11/2016.
 */
public class Puerta {

    String nombrePuerta;
    String estadoPuerta;
    String codigoPuerta;


    public Puerta() {

    }


    public Puerta(String nombrePuerta, String estadoPuerta, String codigoPuerta) {
        this.nombrePuerta = nombrePuerta;
        this.estadoPuerta = estadoPuerta;
        this.codigoPuerta = codigoPuerta;
    }

    public String getNombrePuerta() {
        return nombrePuerta;
    }

    public void setNombrePuerta(String nombrePuerta) {
        this.nombrePuerta = nombrePuerta;
    }

    public String getEstadoPuerta() {
        return estadoPuerta;
    }

    public void setEstadoPuerta(String estadoPuerta) {
        this.estadoPuerta = estadoPuerta;
    }

    public String getCodigoPuerta() {
        return codigoPuerta;
    }

    public void setCodigoPuerta(String codigoPuerta) {
        this.codigoPuerta = codigoPuerta;
    }
}




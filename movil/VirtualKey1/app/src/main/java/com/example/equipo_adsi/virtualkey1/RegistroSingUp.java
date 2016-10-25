package com.example.equipo_adsi.virtualkey1;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class RegistroSingUp extends AppCompatActivity {

    TextView nombres, apellidos, documento, correo, contraseña, repitacontraseña;
    EditText ingresenombres, ingreseapellidos, ingresedocumento, ingresecorreo, ingresecontraseña, Repitcontraseña;
    Button registrarse;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registro_sing_up);


        nombres = (TextView)findViewById(R.id.nombres);
        apellidos = (TextView)findViewById(R.id.apellidos);
        documento = (TextView)findViewById(R.id.documento);
        correo = (TextView)findViewById(R.id.correo);
        contraseña = (TextView)findViewById(R.id.contraseña);
        repitacontraseña = (TextView)findViewById(R.id.repitacontraseña);

        ingresenombres =(EditText)findViewById(R.id.ingresenombres);
        ingreseapellidos =(EditText)findViewById(R.id.ingreseapellidos);
        ingresedocumento =(EditText)findViewById(R.id.ingresedocumento);
        ingresecorreo =(EditText)findViewById(R.id.ingresecorreo);
        ingresecontraseña =(EditText)findViewById(R.id.ingresecontraseña);
        Repitcontraseña =(EditText)findViewById(R.id.Repitcontraseña);

        registrarse =(Button)findViewById(R.id.registrarse);


    }
}

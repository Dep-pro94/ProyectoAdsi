package com.example.equipo_adsi.virtualkey1;

import android.content.Intent;
import android.media.Image;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class RegistrarPuerta extends AppCompatActivity {

    Button registrarpuerta;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registrar_puerta);

        registrarpuerta = (Button)findViewById(R.id.registrarpuerta);


    }

    public void irDescripcion(View view){
        Intent intent= new Intent(RegistrarPuerta.this, DescripcionPuerta.class);
        startActivity(intent);

    }



}

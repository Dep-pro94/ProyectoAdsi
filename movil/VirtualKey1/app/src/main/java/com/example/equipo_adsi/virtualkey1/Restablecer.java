package com.example.equipo_adsi.virtualkey1;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

public class Restablecer extends AppCompatActivity {

    TextView restablecer , correo;
    ImageView logo;
    EditText ingresecontraseña;
    Button btnenviar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_restablecer);

        restablecer = (TextView)findViewById(R.id.restablecer);
        correo = (TextView)findViewById(R.id.correo);

        logo = (ImageView)findViewById(R.id.imglogo);

        ingresecontraseña =(EditText)findViewById(R.id.ingresecontraseña);


        btnenviar =(Button)findViewById(R.id.btnenviar);

    }
}

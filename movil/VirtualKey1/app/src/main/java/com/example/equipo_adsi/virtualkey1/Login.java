package com.example.equipo_adsi.virtualkey1;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class Login extends AppCompatActivity {


    TextView nombre;
    ImageView imglogo;
    Button login, registrarse;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        nombre = (TextView)findViewById(R.id.nombre);

        imglogo = (ImageView)findViewById(R.id.imglogo);

        registrarse =(Button)findViewById(R.id.registrarse);
        login =(Button)findViewById(R.id.login);
    }

    public void irLogin(View view){
        Intent intent= new Intent(Login.this, LoginSignIn.class);
        startActivity(intent);

    }

    public void irRegistro (View view){
        Intent intent= new Intent(Login.this, RegistroSingUp.class);
        startActivity(intent);

    }
    }
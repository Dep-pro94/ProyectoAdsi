package com.example.equipo_adsi.virtualkey1;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

public class LoginSignIn extends AppCompatActivity {

    TextView nombre, correo, contraseña, olvidastecontraseña;
    ImageView logo;
    EditText ingresecorreo, ingresecontraseña;
    Button ingresar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_sign_in);

        nombre = (TextView)findViewById(R.id.nombre);
        correo = (TextView)findViewById(R.id.correo);
        contraseña = (TextView)findViewById(R.id.contraseña);
        olvidastecontraseña= (TextView)findViewById(R.id.olvidastecontraseña);


        logo =(ImageView) findViewById(R.id.logo);

        ingresecorreo =(EditText)findViewById(R.id.ingresecorreo);
        ingresecontraseña =(EditText)findViewById(R.id.ingresecontraseña);

       ingresar =(Button)findViewById(R.id.ingresar);

        olvidastecontraseña.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent intent= new Intent(LoginSignIn.this, Restablecer.class);
                startActivity(intent);
            }
        });

    }


}

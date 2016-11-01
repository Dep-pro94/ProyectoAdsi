package com.example.equipo_adsi.virtualkey1;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;

import com.example.equipo_adsi.virtualkey1.adapter.AdaptadorRecycler;

import java.util.ArrayList;
import java.util.List;

public class DoorsActivity extends AppCompatActivity {

    RecyclerView recyclerView;
    Puerta puerta;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_doors);

        recyclerView = (RecyclerView) findViewById(R.id.recycler);
        List<Puerta> puertaList = new ArrayList<>();
        if (puertaList.isEmpty()) {
            for (int i = 0; i < 3; i++) {
                puerta = new Puerta("Puerta L");
                puerta = new Puerta("Puerta TBT");
                puerta = new Puerta("Puerta Fabrica");
            }
            puertaList.add(puerta);
        }
        AdaptadorRecycler adaptadorRecycler = new AdaptadorRecycler(puertaList);
        LinearLayoutManager manager = new LinearLayoutManager(getApplicationContext());
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(manager);
        recyclerView.setAdapter(adaptadorRecycler);
    }

}

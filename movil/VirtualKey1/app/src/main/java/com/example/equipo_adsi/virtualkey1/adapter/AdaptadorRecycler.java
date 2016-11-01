package com.example.equipo_adsi.virtualkey1.adapter;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.example.equipo_adsi.virtualkey1.Puerta;
import com.example.equipo_adsi.virtualkey1.R;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Equipo-ADSI on 01/11/2016.
 */
public class AdaptadorRecycler extends RecyclerView.Adapter<AdaptadorRecycler.Holder> {

    List<Puerta> puertaList = new ArrayList<>();

    public AdaptadorRecycler(List<Puerta> puertaList) {
        this.puertaList = puertaList;
    }

    @Override
    public Holder onCreateViewHolder(ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_recycler,parent,false);
        Holder holder = new Holder(v);
        return holder;
    }

    @Override
    public void onBindViewHolder(Holder holder, int position) {
        holder.txtPuerta.setText(puertaList.get(position).getNombrePuerta());

    }

    @Override
    public int getItemCount() {
        return puertaList.size();
    }

    public static class Holder extends RecyclerView.ViewHolder {

        TextView txtPuerta ;

        public Holder(View itemView) {
            super(itemView);

            txtPuerta  = (TextView) itemView.findViewById(R.id.txtPuerta);
        }
    }
}

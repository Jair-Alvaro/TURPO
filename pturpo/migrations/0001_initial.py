# Generated by Django 3.2 on 2023-07-27 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblCategoriaP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'tbl_categoria_p',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblOrganizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=300)),
                ('ruc', models.DecimalField(decimal_places=0, max_digits=20)),
                ('direccion', models.CharField(max_length=300)),
                ('departamento', models.CharField(blank=True, max_length=100, null=True)),
                ('provincia', models.CharField(blank=True, max_length=100, null=True)),
                ('distrito', models.CharField(blank=True, max_length=100, null=True)),
                ('notas', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'tbl_organizacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_personal', models.CharField(max_length=200)),
                ('apell_personal', models.CharField(max_length=200)),
                ('telefono_p', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('cargo_p', models.CharField(max_length=200)),
                ('nom_referencia', models.CharField(blank=True, max_length=200, null=True)),
                ('vinculo', models.CharField(blank=True, max_length=150, null=True)),
                ('telefono_r', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('direccion_p', models.CharField(blank=True, max_length=300, null=True)),
                ('departamento_p', models.CharField(blank=True, max_length=100, null=True)),
                ('provincia_p', models.CharField(blank=True, max_length=100, null=True)),
                ('distrito_p', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tbl_personal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_proyecto', models.CharField(blank=True, max_length=250, null=True)),
                ('prioridad', models.CharField(blank=True, max_length=150, null=True)),
                ('f_registro', models.DateTimeField(blank=True, null=True)),
                ('f_inicio_p', models.DateField(blank=True, null=True)),
                ('f_final_p', models.DateField(blank=True, null=True)),
                ('presupuesto_p_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('num_presupuesto_doc', models.CharField(blank=True, max_length=250, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=300, null=True)),
                ('estado', models.CharField(blank=True, max_length=200, null=True)),
                ('id_categoria', models.ForeignKey(blank=True, db_column='id_categoria', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pturpo.tblcategoriap')),
                ('id_organizacion', models.ForeignKey(blank=True, db_column='id_organizacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pturpo.tblorganizacion')),
            ],
            options={
                'db_table': 'tbl_proyecto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblRelacioncomercial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relacion', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'tbl_relacioncomercial',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblTipoR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_r', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'tbl_tipo_r',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblUnidadM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tbl_unidad_m',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tarea', models.CharField(blank=True, max_length=200, null=True)),
                ('f_inicio_t', models.DateField(blank=True, null=True)),
                ('f_final_t', models.DateField(blank=True, null=True)),
                ('dias', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('presupuesto_t', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('notas', models.CharField(blank=True, max_length=300, null=True)),
                ('estado', models.CharField(blank=True, max_length=200, null=True)),
                ('id_proyecto', models.ForeignKey(blank=True, db_column='id_proyecto', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pturpo.tblproyecto')),
            ],
            options={
                'db_table': 'tbl_tarea',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblRecurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle_nom_p', models.CharField(blank=True, max_length=200, null=True)),
                ('num_factura_idp', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('f_recurso', models.DateField(blank=True, null=True)),
                ('notas', models.CharField(blank=True, max_length=300, null=True)),
                ('id_tarea', models.ForeignKey(blank=True, db_column='id_tarea', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pturpo.tbltarea')),
                ('id_tipo_r', models.ForeignKey(blank=True, db_column='id_tipo_r', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pturpo.tbltipor')),
                ('id_unidad_m', models.ForeignKey(blank=True, db_column='id_unidad_m', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pturpo.tblunidadm')),
            ],
            options={
                'db_table': 'tbl_recurso',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='tblorganizacion',
            name='id_relacion',
            field=models.ForeignKey(blank=True, db_column='id_relacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pturpo.tblrelacioncomercial'),
        ),
        migrations.CreateModel(
            name='TblContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contacto', models.CharField(max_length=200)),
                ('apell_contacto', models.CharField(max_length=200)),
                ('cargo', models.CharField(blank=True, max_length=200, null=True)),
                ('correo', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('celular', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('notas', models.CharField(blank=True, max_length=300, null=True)),
                ('id_relacion', models.ForeignKey(blank=True, db_column='id_relacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pturpo.tblorganizacion')),
            ],
            options={
                'db_table': 'tbl_contacto',
                'managed': True,
            },
        ),
    ]

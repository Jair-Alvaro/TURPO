# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblCategoriaP(models.Model):
    categoria = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_categoria_p'


class TblContacto(models.Model):
    id_relacion = models.ForeignKey('TblOrganizacion', models.DO_NOTHING, db_column='id_relacion', blank=True, null=True)
    nom_contacto = models.CharField(max_length=200)
    apell_contacto = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200, blank=True, null=True)
    correo = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    celular = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    notas = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_contacto'


class TblOrganizacion(models.Model):
    id_relacion = models.ForeignKey('TblRelacioncomercial', models.DO_NOTHING, db_column='id_relacion', blank=True, null=True)
    denominacion = models.CharField(max_length=300)
    ruc = models.DecimalField(max_digits=10, decimal_places=0)
    direccion = models.CharField(max_length=300)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    distrito = models.CharField(max_length=100, blank=True, null=True)
    notas = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_organizacion'


class TblPersonal(models.Model):
    nombre_personal = models.CharField(max_length=200)
    apell_personal = models.CharField(max_length=200)
    telefono_p = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cargo_p = models.CharField(max_length=200)
    nom_referencia = models.CharField(max_length=200, blank=True, null=True)
    vinculo = models.CharField(max_length=150, blank=True, null=True)
    telefono_r = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    direccion_p = models.CharField(max_length=300, blank=True, null=True)
    departamento_p = models.CharField(max_length=100, blank=True, null=True)
    provincia_p = models.CharField(max_length=100, blank=True, null=True)
    distrito_p = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_personal'


class TblProyecto(models.Model):
    id_organizacion = models.ForeignKey(TblOrganizacion, models.DO_NOTHING, db_column='id_organizacion', blank=True, null=True)
    id_categoria = models.ForeignKey(TblCategoriaP, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    nom_proyecto = models.CharField(max_length=250, blank=True, null=True)
    prioridad = models.CharField(max_length=150, blank=True, null=True)
    f_registro = models.DateTimeField(blank=True, null=True)
    f_inicio_p = models.DateField(blank=True, null=True)
    f_final_p = models.DateField(blank=True, null=True)
    presupuesto_p_t = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    num_presupuesto_doc = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    observaciones = models.CharField(max_length=300, blank=True, null=True)
    estado = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_proyecto'


class TblRecurso(models.Model):
    id_tarea = models.ForeignKey('TblTarea', models.DO_NOTHING, db_column='id_tarea', blank=True, null=True)
    id_tipo_r = models.ForeignKey('TblTipoR', models.DO_NOTHING, db_column='id_tipo_r', blank=True, null=True)
    detalle_nom_p = models.CharField(max_length=200, blank=True, null=True)
    num_factura_idp = models.IntegerField(blank=True, null=True) 
    cantidad = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    id_unidad_m = models.ForeignKey('TblUnidadM', models.DO_NOTHING, db_column='id_unidad_m', blank=True, null=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_recurso'


class TblRelacioncomercial(models.Model):
    relacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_relacioncomercial'

    def __str__(self):
        return self.relacion


class TblTarea(models.Model):
    id_proyecto = models.ForeignKey(TblProyecto, models.DO_NOTHING, db_column='id_proyecto', blank=True, null=True)
    nom_tarea = models.CharField(max_length=200, blank=True, null=True)
    f_inicio_t = models.DateField(blank=True, null=True)
    f_final_t = models.DateField(blank=True, null=True)
    dias = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    presupuesto_t = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    notas = models.CharField(max_length=300, blank=True, null=True)
    estado = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_tarea'


class TblTipoR(models.Model):
    tipo_r = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_tipo_r'


class TblUnidadM(models.Model):
    unidad = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_unidad_m'

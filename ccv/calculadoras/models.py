from django.db import models

# Create your models here.
# class Grupo(models.Model):
#     nombre_grupo = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'grupo'
#
#     def __str__(self):
#         return f'Grupo {self.id}: {self.nombre_grupo}'
#
# class Clase(models.Model):
#     nombre_clase = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'clase'
#
#     def __str__(self):
#         return f'Clase {self.id}: {self.nombre_clase}'
#
# class Mision(models.Model):
#     nombre_mision = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'mision'
#
#     def __str__(self):
#         return f'Mision {self.id}: {self.nombre_mision}'

# class Equipo(models.Model):
#     nombre_equipo = models.CharField(max_length=150)
#     grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)
#     clase = models.ForeignKey(Clase, on_delete=models.SET_NULL, null=True)
#     mision = models.ForeignKey(Mision, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'equipo'

class Fuerza(models.Model):
    sigla = models.CharField(max_length=20)
    nombre_fuerza = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'fuerza'

# class FuerzaEquipo(models.Model):
#     fuerza = models.ForeignKey(Fuerza, on_delete=models.CASCADE)
#     equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
#
#     class Meta:
#         managed = False
#         db_table = 'fuerza_equipo'
#
#
# class Responsable(models.Model):
#     nombre_responsable = models.CharField(max_length=150, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'responsable'
#
# class Persona(models.Model):
#     primer_nombre = models.CharField(max_length=256, blank=True, null=True)
#     segundo_nombre = models.CharField(max_length=256, blank=True, null=True)
#     primer_apellido = models.CharField(max_length=256, blank=True, null=True)
#     segun_apellido = models.CharField(max_length=256, blank=True, null=True)
#     cargo = models.CharField(max_length=256, blank=True, null=True)
#     dependencia = models.CharField(max_length=256, blank=True, null=True)
#     telefono = models.CharField(max_length=10, blank=True, null=True)
#     corrreo_electronico = models.CharField(max_length=256, blank=True, null=True)
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#     responsable = models.ForeignKey(Responsable, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'personas'
#
#
# class TipoSoporte(models.Model):
#     nombre_tipo_soporte = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'tipo_soporte'
#
# class TipoCostoDocumentacion(models.Model):
#     nombre_tipo_costo_documentacion = models.CharField(max_length=256)
#
#     class Meta:
#         managed = False
#         db_table = 'tipo_costo_documentacion'
#
# class CategoriaDocumentacion(models.Model):
#     nombre_categoria_documentacion = models.CharField(max_length=256)
#
#     class Meta:
#         managed = False
#         db_table = 'categoria_documentacion'
#
#
# class RelacionDocumentacion(models.Model):
#     anio_documentacion = models.IntegerField(blank=True, null=True)
#     descripcion_soporte = models.CharField(max_length=256, blank=True, null=True)
#     categoriaDocumentacion = models.ForeignKey(CategoriaDocumentacion, on_delete=models.SET_NULL, null=True)
#     tipoCostoDcumentacion = models.ForeignKey(TipoCostoDocumentacion, on_delete=models.SET_NULL, null=True)
#     tipoSoporte = models.ForeignKey(TipoSoporte, on_delete=models.SET_NULL, null=True)
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'relacion_documentacion'
#
#
# class TipoMoneda(models.Model):
#     nombre_moneda = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'tipo_moneda'
#
# class CalendarioEntrega(models.Model):
#     anio_entrega = models.IntegerField()
#     cantidad = models.IntegerField()
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'calendario_entregas'
#
#
# class CalendarioPago(models.Model):
#     anio_pago = models.IntegerField()
#     desembolso = models.FloatField()
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#     tipoMoneda = models.ForeignKey(TipoMoneda, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'calendario_pagos'
#
#
#
#
# class CostoOperacion(models.Model):
#     uso_anual = models.IntegerField()
#     combustible_lubricante = models.FloatField()
#     repuesto = models.FloatField()
#     mantenimiento = models.FloatField()
#     tipoMoneda = models.ForeignKey(TipoMoneda, on_delete=models.SET_NULL, null=True)
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'costo_operacion'
#
# class DetalleCostoSoporte(models.Model):
#     nombre_costo_soporte = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'detalle_costo_soporte'
#
#
# class CostoSoporte(models.Model):
#     valor = models.FloatField(blank=True, null=True)
#     detalleCostoSoporte = models.ForeignKey(DetalleCostoSoporte, on_delete=models.SET_NULL, null=True)
#     tipoMoneda = models.ForeignKey(TipoMoneda, on_delete=models.SET_NULL, null=True)
#     equipo = models.ForeignKey('Equipo', on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'costo_soporte'
#
#
# class PlanAdquisicion(models.Model):
#     cantidad_equipo = models.IntegerField()
#     vida_util = models.IntegerField()
#     costo_unitario = models.FloatField()
#     tipoMoneda = models.ForeignKey('TipoMoneda', on_delete=models.SET_NULL, null=True)
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'plan_adquisicion'
#
# class Metrica(models.Model):
#     nombre_metrica = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'metrica'
#
# class TipoMantenimiento(models.Model):
#     nomre_tipo_mantenimiento = models.CharField(max_length=250, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tipo_mantenimiento'
#
# class MantenimientoMayor(models.Model):
#     desgaste_inicial = models.IntegerField()
#     frecuencia = models.IntegerField()
#     costo_unitario = models.FloatField()
#     actividad = models.CharField(max_length=150)
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#     metrica = models.ForeignKey(Metrica, on_delete=models.SET_NULL, null=True)
#     tipoMantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.SET_NULL, null=True)
#     tipoMoneda = models.ForeignKey(TipoMoneda, on_delete=models.SET_NULL, null=True)
#     calendarioEntrega = models.ForeignKey(CalendarioEntrega, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'mantenimiento_mayor'
#
# class TipoInfraestructura(models.Model):
#     nombre_infraestructura = models.CharField(max_length=250)
#
#     class Meta:
#         managed = False
#         db_table = 'tipo_infraestructura'
#
#
# class InfraestructuraEquipo(models.Model):
#     anio_inicial = models.IntegerField()
#     vida_util_infraestructura = models.IntegerField()
#     costo_adquisicion = models.FloatField()
#     costo_sostenimiento_anual = models.FloatField()
#     descripcion = models.CharField(max_length=150, blank=True, null=True)
#     tipoMoneda = models.ForeignKey(TipoMoneda, on_delete=models.SET_NULL, null=True)
#     tipoInfraestructura = models.ForeignKey(TipoInfraestructura, on_delete=models.SET_NULL, null=True)
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'infraestructura_equipos'
#
# class Concepto(models.Model):
#     nombre_concepto = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'concepto'
#
# class DetalleConcepto(models.Model):
#     nombre_detalle_consulta = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'detalle_concepto'
#
# class ConceptoPersonal(models.Model):
#     tripulacion = models.IntegerField(blank=True, null=True)
#     personal_mantenimiento = models.IntegerField(blank=True, null=True)
#     personal_tierra = models.IntegerField(blank=True, null=True)
#     concepto = models.ForeignKey(Concepto, on_delete=models.SET_NULL, null=True)
#     detalleConcepto = models.ForeignKey(DetalleConcepto, on_delete=models.SET_NULL, null=True)
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'concepto_personal'
#
# class ConceptoPersonalMoneda(models.Model):
#     id_concepto_personal_moneda = models.IntegerField(primary_key=True)
#     tripulacion_moneda = models.FloatField(blank=True, null=True)
#     personal_mantenimiento_moneda = models.FloatField(blank=True, null=True)
#     personal_tierra_moneda = models.FloatField(blank=True, null=True)
#     concepto = models.ForeignKey(Concepto, on_delete=models.SET_NULL, null=True)
#     detalleConcepto = models.ForeignKey(DetalleConcepto, on_delete=models.SET_NULL, null=True)
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#     tipoMoneda = models.ForeignKey(TipoMoneda, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'concepto_personal_moneda'
#
# class AnioBase(models.Model):
#     anio_base = models.IntegerField()
#     equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'anio_base'
#
# class Inflacion(models.Model):
#     anio_inflacion = models.IntegerField()
#     cpicol = models.FloatField()
#     cpiusa = models.FloatField()
#     cpieu = models.FloatField()
#     cpiuk = models.FloatField()
#     cpiyen = models.FloatField()
#
#     class Meta:
#         managed = False
#         db_table = 'inflaciones'
#
# class TasaCambio(models.Model):
#     anio_tasa = models.IntegerField()
#     usdcop = models.FloatField()
#     usdeur = models.FloatField()
#     usdgbp = models.FloatField()
#     usdjpy = models.FloatField()
#     eurcop = models.FloatField()
#     gbpcop = models.FloatField()
#     jpycop = models.FloatField()
#
#     class Meta:
#         managed = False
#         db_table = 'inflaciones'

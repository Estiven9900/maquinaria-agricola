from django.db import models
from django.core.validators import MinValueValidator

class Complemento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('mantenimiento', 'Mantenimiento')
    ])

    def __str__(self):
        return self.nombre

class Maquina(models.Model):
    id_complemento = models.ForeignKey(Complemento, on_delete=models.SET_NULL, null=True)
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    estado_maquina = models.CharField(max_length=20, choices=[
        ('operativa', 'Operativa'),
        ('averiada', 'Averiada'),
        ('mantenimiento', 'Mantenimiento')
    ])
    cilindraje = models.IntegerField(validators=[MinValueValidator(0)])
    modelo = models.CharField(max_length=50)
    serial = models.CharField(max_length=50, unique=True)
    estado_disponible = models.BooleanField(default=True)
    kilometraje = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    tipo_combustible = models.CharField(max_length=20, choices=[
        ('gasolina', 'Gasolina'),
        ('diesel', 'Diesel'),
        ('electrico', 'Eléctrico')
    ])

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.serial})"

class Trabajador(models.Model):
    id_rol = models.CharField(max_length=20, choices=[
        ('operador', 'Operador'),
        ('mecanico', 'Mecánico'),
        ('supervisor', 'Supervisor')
    ])
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Operacion(models.Model):
    id_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    id_maquinaria = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField(null=True, blank=True)
    area = models.CharField(max_length=50)
    consumo = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Operación {self.id} - {self.id_maquinaria}"
# Generated by Django 4.1.1 on 2022-11-04 00:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Contacto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("correo", models.EmailField(max_length=254)),
                (
                    "tipo_consulta",
                    models.IntegerField(
                        choices=[
                            [0, "Consulta"],
                            [1, "Reclamo"],
                            [2, "Sugerencia"],
                            [3, "Felicitaciones"],
                        ]
                    ),
                ),
                ("mensaje", models.TextField()),
                ("avisos", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Ingrediente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("cantidad", models.IntegerField()),
                ("imagen", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Registro",
            fields=[
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("rut", models.IntegerField(primary_key=True, serialize=False)),
                ("nombre_usario", models.CharField(max_length=20)),
                ("comuna", models.CharField(max_length=20)),
                ("telefono", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=20)),
                (
                    "creacion_usr",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
            options={"ordering": ["-rut"],},
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("precio", models.IntegerField()),
                ("descripcion", models.TextField()),
                ("imagen", models.ImageField(null=True, upload_to="producto")),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="app.categoria"
                    ),
                ),
            ],
        ),
    ]

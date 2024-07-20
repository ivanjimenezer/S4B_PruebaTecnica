from django.db import migrations

SQL = """
CREATE PROCEDURE insert_verif_country(
    country_name VARCHAR,
    country_capital VARCHAR,
    country_population INTEGER,
    country_area DOUBLE PRECISION
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM backend_paises_detalle WHERE nombre = country_name AND capital = country_capital
    ) THEN
        INSERT INTO backend_paises_detalle (id, nombre, capital, poblacion, area, is_active)
        VALUES (uuid_generate_v4(), country_name, country_capital, country_population, country_area, TRUE);
    END IF;
END;
$$;
"""

class Migration(migrations.Migration):
    
    dependencies = [
        ('backend', '0003_paises_detalle_is_active'),
    ]

    operations = [migrations.RunSQL(SQL)] 

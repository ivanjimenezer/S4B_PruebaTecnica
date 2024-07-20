
CREATE TABLE backend_paises_detalle (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  nombre varchar(100) NOT NULL,
  capital varchar(100) NOT NULL,
  poblacion integer NOT NULL,
  area double precision NOT NULL,
  is_active boolean DEFAULT true
);

-- ---------------------------------------------------------------------------
\dt  
\d backend_paises_detalle  
-- ---------------------------------------------------------------------------
select * from backend_paises_detalle limit 10;

select * from backend_paises_detalle where is_Active = false;

SELECT * FROM information_schema.columns WHERE table_name = 'backend_paises_detalle';

GRANT ALL PRIVILEGES ON DATABASE countries TO admin;
-- ---------------------------------------------------------------------------
DROP PROCEDURE IF EXISTS insert_verif_country(VARCHAR, VARCHAR, INTEGER, DOUBLE PRECISION);

CREATE PROCEDURE insert_verif_country(
    country_name VARCHAR(100),
    country_capital VARCHAR(100),
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
        VALUES (
            uuid_generate_v4(),  
            country_name,
            country_capital,
            country_population,
            country_area,
            TRUE
        );
    END IF;
END;
$$;

-- ---------------------------------------------------------------------------
SELECT proname, proargtypes, prorettype FROM pg_proc WHERE proname = 'insert_verif_country';
-- ---------------------------------------------------------------------------
TRUNCATE TABLE backend_paises_detalle;

SELECT COUNT(*) FROM backend_paises_detalle;


-- ---------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE delete_random_rows(num_rows INTEGER)
LANGUAGE plpgsql
AS $$
DECLARE
    total_rows INTEGER;
BEGIN
    -- Obtenemos el numero total de filas
    SELECT COUNT(*) INTO total_rows FROM backend_paises_detalle;

    -- Checamos si es posible la eliminación
    IF num_rows > total_rows THEN
        RAISE EXCEPTION 'Cannot delete more rows than the total number of rows in the table';
    ELSE
        -- Procedemos con la eliminación de filas
        EXECUTE format('DELETE FROM backend_paises_detalle WHERE id IN (
                            SELECT id FROM backend_paises_detalle 
                            ORDER BY random() 
                            LIMIT %s)', num_rows);
    END IF;
END;
$$;

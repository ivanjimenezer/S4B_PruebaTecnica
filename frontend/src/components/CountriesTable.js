import './styles.css';
import React from 'react';

const CountriesTable = ({ countries, handleDelete, handleActivate }) => {
    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Capital</th>
                    <th>Poblacion</th>
                    <th>Area Cuadrada</th>
                    <th>Activado</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                {countries.map((country) => (
                    <tr
                        key={country.id}
                        className={!country.is_active ? 'hidden-row' : ''}
                    >
                        <td>{country.nombre}</td>
                        <td>{country.capital}</td>
                        <td>{country.poblacion}</td>
                        <td>{country.area}</td>
                        <td>{country.is_active ? "Activado" : "Oculto"}</td>
                        <td>
                            <button onClick={() => handleDelete(country.id)} className="btn btn-danger mr-2 button-spacing">Ocultar</button>
                            <button onClick={() => handleActivate(country.id)} className="btn btn-success button-spacing">Activar</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default CountriesTable;

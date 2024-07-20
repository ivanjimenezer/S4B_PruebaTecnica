import React, { useState, useEffect } from 'react';
import ApiUtils from '../utils/apiUtils';
import FilterInput from './FilterInput';
import CountriesTable from './CountriesTable';
import RandomDeleteInput from './RandomDeleteInput';
import './styles.css';

const MainComponent = () => {
    const [countries, setCountries] = useState([]);
    const [filter, setFilter] = useState({ name: '', capital: '', population: '' });
    const [sorted, setSorted] = useState(false);
    const [filteredCountries, setFilteredCountries] = useState([]);
    const [totalCountries, setTotalCountries] = useState(0); // Estado para el total de elementos

    useEffect(() => {
        ApiUtils.fetchCountries((data) => {
            setCountries(data);
            setTotalCountries(data.length); // Actualiza el total de elementos
        });
    }, []);

    useEffect(() => {
        const filtered = countries.filter((country) =>
            country.nombre.includes(filter.name) &&
            country.capital.includes(filter.capital) &&
            country.poblacion.toString().includes(filter.population)
        );
        setFilteredCountries(filtered);
    }, [filter, countries]);

    const handleDelete = (id) => {
        ApiUtils.handleDelete(id, () => ApiUtils.fetchCountries((data) => {
            setCountries(data);
            setTotalCountries(data.length);
        }));
    };

    const handleActivate = (id) => {
        ApiUtils.handleActivate(id, () => ApiUtils.fetchCountries((data) => {
            setCountries(data);
            setTotalCountries(data.length);
        }));
    };

    const handleSort = () => {
        const sortedCountries = [...countries].sort((a, b) => a.nombre.localeCompare(b.nombre));
        setCountries(sortedCountries);
        setSorted(true);
    };

    const handleFilterChange = (e) => {
        const { name, value } = e.target;
        setFilter({ ...filter, [name]: value });
    };

    const handleDownloadCSV = () => {
        ApiUtils.handleDownloadCSV(filteredCountries);
    };

    const handleWebScrapping = () => {
        ApiUtils.webScrapping();
        window.location.reload();
    };

    const reloadCountries = () => {
        ApiUtils.fetchCountries((data) => {
            setCountries(data);
            setTotalCountries(data.length);
        });
    };

    return (
        <div className="container mt-4">
            <h1 className="mb-4">Paises Recolectados - {totalCountries} elementos</h1>
            <div className="mb-3">
                <button onClick={handleSort} className="btn btn-primary mr-2 button-spacing">Ordenar Alfabeticamente</button>
                <button onClick={handleDownloadCSV} className="btn btn-secondary button-spacing">Descargar CSV</button>
                <button 
                onClick={handleWebScrapping} 
                className="btn btn-primary mr-2 button-spacing"
                disabled={totalCountries >= 250}
            >
                Hacer WebScrapping
            </button>
            </div>
            <div className="mb-3">
                <FilterInput
                    name="name"
                    placeholder="Filtrar por Nombre"
                    value={filter.name}
                    onChange={handleFilterChange}
                />
                <FilterInput
                    name="capital"
                    placeholder="Filtrar por Capital"
                    value={filter.capital}
                    onChange={handleFilterChange}
                />
                <FilterInput
                    name="population"
                    placeholder="Filtrar por Población"
                    value={filter.population}
                    onChange={handleFilterChange}
                />
            </div>
            <RandomDeleteInput onDeleteComplete={reloadCountries} />
            
            <CountriesTable 
                countries={filteredCountries} 
                handleDelete={handleDelete}
                handleActivate={handleActivate}
            />
        </div>
    );
};

export default MainComponent;

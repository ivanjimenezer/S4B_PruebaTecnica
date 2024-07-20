import axios from 'axios';

const url = "http://127.0.0.1:8000";
 
const deleteRandomRows = async (numRows) => {
    await axios.delete(`${url}/api/del_random/${numRows}`);
};

const webScrapping = async () => {
    await axios.get(`${url}/api/scrap/`);
};

const fetchCountries = async (setCountries) => {
    try {
        const response = await axios.get(`${url}/api/paises/`);
        setCountries(response.data);
    } catch (error) {
        console.error('Error al obtener datos:', error);
    }
};

const handleDelete = async (id, callback) => {
    try {
        await axios.delete(`${url}/api/paises/${id}/`);
        callback();
    } catch (error) {
        console.error('Error al eliminar un pais:', error);
    }
};

const handleActivate = async (id, callback) => {
    try {
        await axios.put(`${url}/api/paises_activate/${id}/`);
        callback();
    } catch (error) {
        console.error('Error al activar un pais:', error);
    }
};

const handleDownloadCSV = async (filteredCountries) => {
    try {
        console.log("handleDown", filteredCountries);
        const activeCountries = filteredCountries.filter(country => country.is_active);
        const response = await axios.post(`${url}/api/getcsv/`, activeCountries, {
            responseType: 'blob',
        });
        const csvBlob = new Blob([response.data], { type: 'text/csv' });
        const csvUrl = URL.createObjectURL(csvBlob);
        const link = document.createElement('a');
        link.href = csvUrl;
        link.setAttribute('download', 'filtered_countries.csv');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(csvUrl);
    } catch (error) {
        console.error('Error al descargar el archivo CSV:', error);
    }
};

export default {
    fetchCountries,
    handleDelete,
    handleActivate,
    handleDownloadCSV,
    deleteRandomRows,
    webScrapping,
};

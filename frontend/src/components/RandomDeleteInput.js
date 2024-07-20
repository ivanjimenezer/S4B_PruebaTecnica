import React, { useState } from 'react';
import ApiUtils from '../utils/apiUtils';

const RandomDeleteInput = ({ onDeleteComplete }) => {
    const [number, setNumber] = useState('');

    const handleChange = (e) => {
        setNumber(e.target.value);
    };

    const handleDelete = async () => {
        try {
            await ApiUtils.deleteRandomRows(number);
            onDeleteComplete();
        } catch (error) {
            console.error('Error al eliminar filas aleatorias:', error);
        }
    };

    return (
        <div className="mb-3">
            <input
                type="number"
                value={number}
                onChange={handleChange}
                placeholder="Número de paises a eliminar para testear el webScrapping"
                className="form-control mr-2"
            />
            <button onClick={handleDelete} className="btn btn-danger mt-2">
                Eliminar Aleatoriamente
            </button>
        </div>
    );
};

export default RandomDeleteInput;

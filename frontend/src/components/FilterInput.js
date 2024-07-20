import React from 'react';

const FilterInput = ({ name, placeholder, value, onChange }) => {
    return (
        <input
            type="text"
            name={name}
            placeholder={placeholder}
            value={value}
            onChange={onChange}
            className="form-control mr-2"
        />
    );
};

export default FilterInput;
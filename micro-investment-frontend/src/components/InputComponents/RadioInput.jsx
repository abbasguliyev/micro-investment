import React from 'react'

function RadioInput({label, id, name, type, value, onChange, onBlur, style, checked}) {
  return (
    <>
        <input
            id={id}
            name={name}
            type="radio"
            value={value}
            onChange={onChange}
            onBlur={onBlur}
            className="mr-2 rounded-md border-0 py-1.5 text-gray-900 shadow-sm placeholder:text-gray-400 sm:text-sm sm:leading-6"
            checked={checked}
        />
        <label htmlFor={id}>{label}</label><br></br>
    </>
  )
}

export default RadioInput
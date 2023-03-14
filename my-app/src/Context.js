import React, { createContext, useState } from "react";

export const ListContext = createContext();

const ListContextProvider = ({ children }) => {
  const [list, setList] = useState([]);

  const addItem = (item) => {
    setList([...list, item]);
  };

  const clearList = () => {
    setList([]);
  };

  return (
    <ListContext.Provider value={{ list, addItem, clearList }}>
      {children}
    </ListContext.Provider>
  );
};

export default ListContextProvider;
